/* SPDX-License-Identifier: GPL-3.0-only
 * Copyright (C) 2026 g0rst */
/* VOSTOK: the Vostok sound core ("Synthesizer der Zukunft"). Two-operator FM with feedback, hidden behind eight
 * curated SIGNALE (algorithm + ratio recipes) and six macros, so a cold minimal-wave bass, a coldwave lead or a
 * sovietwave bell is one knob away instead of 155 DX7 bytes.
 *
 *   E0 SIGNL  the recipe: SPUTN VOSTK MOLNJ KOSMO TUNDR POLAR FUNK HALLE (below, VK_SIG)
 *   E1 STRAL  Strahlung: the modulation index (brightness). The track's FLT (ENV / LFO -> FLT, the matrix's CUT)
 *             moves it too, so ENV -> FLT is the classic FM brightness envelope
 *   E2 ORBIT  Umlaufbahn: the modulator's self-feedback (roughness, buzz); the track's SHP adds to it
 *   E3 START  0..63 "knackig": the index falls after the attack (a pluck, faster towards 0);
 *             64..127 "flaechig": the amplitude swells in (up to ~1.5 s at 127), the index stays
 *   E4 SCHWB  Schwerelosigkeit: a second carrier, detuned up to ~20 cents (the sovietwave beat)
 *   E5 STILL  Funkstille: lo-fi. Fewer bits, a lower sample rate (sample and hold 1..16) and a darker low-pass
 *   E6 SUB    a sine an octave below
 *   E7 LEIER  Leiern: a slow pitch wobble per voice (tape wow), up to ~22 cents
 *
 * State per voice: ph[0] carrier, ph[1] modulator, ph[2] the detuned carrier; s[0] the index envelope (Q15),
 * s[1] the swell (Q15), s[2] the modulator's last output (feedback), s[3] STILL's low-pass, s[4] SUB's phase,
 * s[5] the wobble's phase, s[6] the drum's pitch envelope (Q15), s[7] the noise generator (TUNDRA: s[6] s[7] its DC
 * blocker).
 * No engine memory (engine_t.mem 0), no tables of its own: sine_i, noise32 and the host's pitch. */

#define ENGI_VOSTOK (13u + FELUCCA_SLICE)   /* engines.c ENGINES[] (append-only: after SLICE) */

static const char *const N_VK_SIG[] = {"SPUTN", "VOSTK", "MOLNJ", "KOSMO", "TUNDR", "POLAR", "FUNK", "HALLE"};

typedef struct {
    uint16_t cr, mr;             /* carrier and modulator frequency ratios, Q8 (256 = 1:1) */
    uint32_t kmax;               /* the index at STRAL 127, in phase units per Q15 of modulator (20861 = 1 rad) */
    uint8_t fb0;                 /* feedback that is always there (0..127, added to ORBIT) */
    uint8_t kind;                /* 0 plain, 1 breathing (TUNDRA), 2 noise (FUNKSPRUCH), 3 drum (MASCHINENHALLE) */
} vk_sig_t;

#define VK_RAD 20861u            /* 2^32 / (2 pi) / 2^15: one radian of phase per full-scale modulator */
static const vk_sig_t VK_SIG[8] = {
    {256, 512, VK_RAD * 3 / 2, 0, 0},     /* SPUTNIK: a clean beep, the 2nd harmonic shines through */
    {256, 512, VK_RAD * 7 / 2, 0, 0},     /* VOSTOK: 1:2, odd harmonics: the pulse of a minimal-wave bass */
    {256, 256, VK_RAD * 4, 24, 0},        /* MOLNIJA: 1:1 with feedback: saw-like, the coldwave lead */
    {256, 768, VK_RAD * 3, 8, 0},         /* KOSMODROM: 1:3, hollow, the post-punk synth bass */
    {256, 257, VK_RAD * 5 / 2, 0, 1},     /* TUNDRA: 1:1 a hair off, breathing: the darkwave pad */
    {256, 896, VK_RAD * 4, 0, 0},         /* POLARLICHT: 1:3.5, the FM bell */
    {256, 1825, VK_RAD * 8, 90, 2},       /* FUNKSPRUCH: 1:7.13, feedback and noise: hats, snares, static */
    {256, 512, VK_RAD * 2, 0, 3},         /* MASCHINENHALLE: a sine with a falling pitch: kick, tom, click */
};

/* the wobble's rate per block: ~0.55 Hz (1378 blocks / s), a little different per voice (age) */
#define VK_LEIER_INC 1700000u

static void vostok_note_on(track_t *t, voice_t *v)
{
    v->ph[1] = 0;
    v->ph[2] = 0x40000000u;      /* the second carrier a quarter turn on: no phasing at the start */
    v->s[0] = 32767;
    v->s[1] = t->p[P_E3] > 64 ? 0 : 32767;
    v->s[2] = 0;
    v->s[3] = 0;
    v->s[4] = 0;
    v->s[5] = (int32_t)(v->age * 0x9E3779B9u);
    v->s[6] = VK_SIG[(uint32_t)t->p[P_E0] & 7u].kind == 1 ? 0 : 32767;   /* the drum's pitch envelope, or */
    v->s[7] = VK_SIG[(uint32_t)t->p[P_E0] & 7u].kind == 1 ? 0 : (int32_t)(v->age * 2654435761u) | 1;   /* TUNDRA's DC blocker */
}

/* START above 64: the swell, once a control tick (1378 / s), on top of the ADSR */
static int32_t vostok_amp(track_t *t, voice_t *v, int32_t adsr)
{
    int32_t st = t->p[P_E3];
    if (st > 64 && v->s[1] < 32767) {
        int32_t ticks = (st - 64) * 2067 / 63;                 /* up to ~1.5 s */
        v->s[1] = clamp(v->s[1] + 32767 / (ticks > 0 ? ticks : 1), 0, 32767);
    } else if (st <= 64) {
        v->s[1] = 32767;
    }
    return mulq15(adsr, v->s[1]);
}

static void vostok_render(track_t *t, voice_t *v, int32_t *out, uint32_t n, const vmod_t *m)
{
    const int16_t *p = t->p;
    const vk_sig_t *sg = &VK_SIG[(uint32_t)p[P_E0] & 7u];
    uint32_t inc = m->inc, i;
    uint32_t ph0 = v->ph[0], ph1 = v->ph[1], ph2 = v->ph[2], sub_ph = (uint32_t)v->s[4];
    int32_t bright, kq, fb, envk = v->s[0], prev = v->s[2], lp = v->s[3], penv = v->s[6];
    int32_t det = p[P_E4], still = p[P_E5], sub = p[P_E6] * 200, leier = p[P_E7];
    uint32_t inc_m, inc2, k;
    int32_t bits_sh, lpa, hold = 0, held = 0;

    /* LEIER: the slow wobble, applied to the block's pitch (also drives TUNDRA's breathing) */
    v->s[5] = (int32_t)((uint32_t)v->s[5] + VK_LEIER_INC + (v->age & 255u) * 2000u);
    if (leier)
        inc += (uint32_t)((int32_t)(inc >> 12) * ((sine_i((uint32_t)v->s[5]) * leier * 41) >> 15) / 127);

    /* STRAL and FLT: the index, then START's fall after the attack */
    bright = clamp(p[P_E1] * 256 + m->cutoff, 0, 127 << 8);
    if (sg->kind == 1)                                         /* TUNDRA breathes: the index +-30 % */
        bright = clamp(bright + ((sine_i((uint32_t)v->s[5] >> 1) * 38) >> 8), 0, 127 << 8);
    if (p[P_E3] < 64) {                                        /* knackig: towards a quarter of the index */
        int32_t floor_k = 8192, c = 2 + (p[P_E3] * p[P_E3]) / 4;    /* the higher, the slower: */
        envk -= (envk - floor_k) / (c + 1);                          /* ~2 ms at 0, ~0.7 s at 63 */
        if (envk < floor_k)
            envk = floor_k;
    } else {
        envk = 32767;
    }
    kq = (int32_t)(((uint32_t)bright * 32767u) / (127u << 8));
    kq = mulq15(kq, envk);
    k = (uint32_t)(((uint64_t)sg->kmax * (uint32_t)kq) >> 15);

    /* ORBIT and SHP: the feedback, up to ~1.3 rad */
    fb = clamp(p[P_E2] + sg->fb0 + ((m->shape - (64 << 8)) >> 8), 0, 127);
    fb = fb * 214;                                              /* phase units per Q15 of the last output: */
                                                                /* 127 * 214 * 32767 ~ 0.9 * 2^30 */
    inc_m = (inc >> 8) * sg->mr;
    if (sg->cr != 256)
        inc = (inc >> 8) * sg->cr;
    inc2 = inc + (uint32_t)((int32_t)(inc >> 12) * (det * 48 / 127));

    /* STILL: bits 16 .. 4, sample and hold 1 .. 16, the low-pass from open to dark */
    bits_sh = still * 12 / 127;
    hold = still ? 1 << (still * 5 / 128) : 1;
    lpa = 32767 - still * 230;

    for (i = 0; i < n; i++) {
        int32_t mod, s;
        uint32_t pm;
        /* the modulator, with its feedback (and FUNKSPRUCH's noise in its phase) */
        pm = ph1 + (uint32_t)(prev * fb);
        if (sg->kind == 2)
            pm += noise32(&v->s[7]) >> 2;
        mod = sine_i(pm);
        prev = mod;
        ph1 += inc_m;
        /* the carrier(s) */
        pm = (uint32_t)mod * k;
        s = sine_i(ph0 + pm);
        if (det) {
            s = (s + sine_i(ph2 + pm)) >> 1;
            ph2 += inc2;
        }
        if (sg->kind == 3) {                                   /* the drum: up to 8x the pitch, falling in ~12 ms */
            ph0 += inc + (inc >> 15) * (uint32_t)(penv * 7);
            penv -= penv >> 9;
        } else {
            ph0 += inc;
        }
        if (sub) {
            sub_ph += inc >> 1;
            s += mulq15(sine_i(sub_ph), sub);
        }
        if (still) {
            if (!(i & (uint32_t)(hold - 1)))
                held = s;
            s = (held >> bits_sh) << bits_sh;
            lp += ((s - lp) * lpa) >> 15;                  /* |s - lp| <= 65534: fits 32 bits */
            s = lp;
        }
        if (sg->kind == 1) {                                   /* TUNDRA: near 1:1, a sideband sits near 0 Hz: */
            int32_t x = s;                                     /* a DC blocker (~14 Hz) in s[6] / s[7] */
            v->s[7] += x - v->s[6] - (v->s[7] >> 9);
            v->s[6] = x;
            s = v->s[7];
        }
        s = clamp(s, -32767, 32767);
        out[i] += voice_amp(s, m, i);
    }
    v->ph[0] = ph0;
    v->ph[1] = ph1;
    v->ph[2] = ph2;
    v->s[0] = envk;
    v->s[2] = prev;
    v->s[3] = lp;
    v->s[4] = (int32_t)sub_ph;
    if (sg->kind == 3)
        v->s[6] = penv;
}

static const preset_t VOSTOK_PRESETS[] = {
    /* name, {SIGNL, STRAL, ORBIT, START, SCHWB, STILL, SUB, LEIER}, {A D S R}, fenv, mono, FX(dist, chorus, delay, reverb) */
    {"SPUTNIK", {0, 40, 0, 20, 0, 0, 0, 0}, {0, 60, 40, 40}, 0, 1, FX(0, 0, 30, 30), PAT(4)},
    {"VOSTOK-1", {1, 55, 10, 30, 0, 0, 40, 0}, {0, 50, 60, 20}, 20, 1, FX(0, 0, 0, 10), PAT(2)},
    {"LAIKA", {0, 30, 0, 50, 10, 0, 0, 20}, {5, 80, 90, 70}, 0, 1, FX(0, 20, 60, 50), PAT(4)},
    {"TELEMETRIE", {0, 90, 20, 8, 0, 0, 0, 0}, {0, 30, 0, 20}, 0, 0, FX(0, 0, 40, 20), PAT(13)},
    {"BAIKONUR", {3, 64, 20, 30, 20, 0, 30, 0}, {0, 70, 70, 30}, 16, 1, FX(0, 50, 0, 15), PAT(2)},
    {"MOLNIJA", {2, 80, 30, 40, 30, 0, 0, 10}, {0, 90, 100, 40}, 10, 1, FX(0, 20, 40, 40), PAT(4)},
    {"STAHLMARSCH", {7, 12, 0, 10, 0, 20, 0, 0}, {0, 40, 0, 30}, 0, 0, FX(10, 0, 0, 15), PAT(12)},
    {"TUNDRA", {4, 60, 0, 100, 40, 0, 0, 20}, {40, 100, 110, 90}, 0, 0, FX(0, 60, 20, 80), PAT(5)},
    {"WEISSE NACHT", {4, 40, 0, 110, 80, 0, 20, 30}, {60, 110, 120, 110}, 0, 0, FX(0, 90, 30, 110), PAT(5)},
    {"POLARSTATION", {4, 30, 40, 90, 90, 30, 0, 10}, {50, 100, 100, 100}, 0, 0, FX(0, 30, 40, 90), PAT(5)},
    {"POLARLICHT", {5, 70, 0, 40, 30, 0, 0, 20}, {0, 100, 40, 90}, 0, 0, FX(0, 40, 70, 80), PAT(7)},
    {"FRIEDEN", {1, 50, 0, 60, 60, 0, 0, 30}, {10, 90, 100, 60}, 0, 1, FX(0, 70, 50, 60), PAT(3)},
    {"SONNENWIND", {5, 60, 10, 20, 20, 0, 0, 10}, {0, 60, 30, 60}, 0, 0, FX(0, 40, 70, 60), PAT(13)},
    {"PLATTENBAU", {4, 50, 0, 100, 50, 70, 0, 50}, {50, 110, 110, 100}, 0, 0, FX(0, 60, 30, 100), PAT(5)},
    {"RADIOLA", {2, 50, 20, 40, 20, 60, 0, 40}, {5, 90, 90, 50}, 0, 1, FX(0, 30, 50, 50), PAT(4)},
    {"LETZTER BUS", {1, 30, 0, 40, 10, 40, 80, 20}, {0, 90, 90, 70}, 0, 1, FX(0, 0, 20, 70), PAT(8)},
};

static const engine_t ENG_VOSTOK = {
    .name = "VOSTOK",
    .page_title = {"SIGNL", "STILL"},
    .edit = {
        {"SIGNL", F_ENUM, 0, 7, 1, N_VK_SIG, 0},
        {"STRAL", F_PCT, 0, 127, 64, 0, 0},
        {"ORBIT", F_PCT, 0, 127, 0, 0, 0},
        {"START", F_PCT, 0, 127, 32, 0, 0},
        {"SCHWB", F_PCT, 0, 127, 0, 0, 0},
        {"STILL", F_PCT, 0, 127, 0, 0, 0},
        {"SUB", F_PCT, 0, 127, 0, 0, 0},
        {"LEIER", F_PCT, 0, 127, 0, 0, 0},
    },
    .presets = VOSTOK_PRESETS,
    .npresets = NELEM(VOSTOK_PRESETS),
    .note_on = vostok_note_on,
    .render = vostok_render,
    .amp = vostok_amp,
    .knob = {P_E0, P_E1, P_E2, P_E3},
};

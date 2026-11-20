/* SPDX-License-Identifier: GPL-3.0-only
 * Copyright (C) 2026 g0rst */
/* Vostok (Sojus): the whole firmware as the emulator runs it (web/emu/felucca_web.c), powered on as Vostok:
 *  - the crew at power-on (engines.c VK_CREW): four VOSTOK parts with their phrases, PLAY sounds at once
 *  - the MASCHINENHALLE kit (eng_vostok.c KIT): the GM notes pick the drums, a MONO track too
 *  - PLANERFUELLUNG (seq.c plan_loops, ui_draw.c plan_report): 25 % after 4 loops, 100 % after 16
 *  - the SMK-37 keys (VOSTOK_SMK_KEYS, ui_input.c page_tap): NOTE REPEAT tapped = SPUR, CHORD = ENV then LFO
 * Built by tests/run_tests.sh with -UFELUCCA_VOSTOK_CREW -DFELUCCA_VOSTOK_CREW=1 -DVOSTOK_SMK_KEYS=1 -Iweb/emu. */
#include "felucca_web.c"
#include <stdio.h>
#include <string.h>

static int bad;
static void check(const char *what, int ok)
{
    printf("vostok: %-84s %s\n", what, ok ? "ok" : "FAIL");
    bad += !ok;
}
static void render(double ms)
{
    uint32_t n = (uint32_t)(ms * 44.1 + 0.5), k;
    for (k = 0; k < n; k += 128u)
        web_render(n - k < 128u ? n - k : 128u);
}
static void tap(uint32_t b)
{
    web_buttons(1u << b);
    render(80);
    web_buttons(0);
    render(80);
}
static double rms(double ms)
{
    uint32_t n = (uint32_t)(ms * 44.1 + 0.5), k, i, c = 0;
    double s = 0;
    for (k = 0; k < n; k += 128u) {
        uint32_t m = n - k < 128u ? n - k : 128u;
        web_render(m);
        for (i = 0; i < m; i++, c++)
            s += (double)out_l[i] * out_l[i];
    }
    return c ? s / c : 0;
}

int main(void)
{
    uint32_t i, ok;
    web_nor_erase();
    web_boot();
    render(600);

    /* the crew */
    ok = 1;
    for (i = 0; i < NTRK; i++)
        ok &= trk[i].eng_req == ENGI_VOSTOK && trk[i].preset == VK_CREW[i][1] && trk[i].p[P_SLEN] == 16;
    check("power-on: Bass VOSTOK-1, Flaeche TUNDRA, Lead MOLNIJA, Rhythmus MASCHINENHALLE, 16 steps each", ok &&
          !strcmp(ENGINES[ENGI_VOSTOK]->presets[VK_CREW[3][1]].name, "MASCHINENHALLE") &&
          trk[3].p[P_E0] == (int16_t)VK_KIT && TRK_DEF[3][0] == ENGI_DRUM);
    check("power-on: silent until PLAY", rms(300) < 1e-8);

    /* the kit */
    check("KIT: 36 kick, 38 snare, 39 clap, 42 / 46 hats, 45 tom, 56 TELEMETRIE, 37 rim",
          vk_kit_drum(36) == VD_KICK && vk_kit_drum(38) == VD_SNARE && vk_kit_drum(39) == VD_CLAP &&
          vk_kit_drum(42) == VD_CHAT && vk_kit_drum(46) == VD_OHAT && vk_kit_drum(45) == VD_TOM &&
          vk_kit_drum(56) == VD_PIEP && vk_kit_drum(37) == VD_RIM && VK_DRUM[VD_KICK].sig == 7 && VK_DRUM[VD_CHAT].sig == 6);

    /* PLAY: it sounds, and the plan counts */
    tap(B_PLAY);
    check("PLAY: the crew sounds at once", song.playing && rms(1000) > 1e-5);
    plan_loops = 0;
    for (i = 0; i < 200u && plan_loops < 4u; i++)
        render(50);
    render(100);
    check("PLANERFUELLUNG: 4 loops of the selected track: PLAN 25 %", plan_loops >= 4u && !strcmp(ui.msg, "PLAN 25 %"));
    ui.msg_t = 0;
    for (i = 0; i < 800u && plan_loops < 16u; i++)
        render(50);
    render(100);
    check("PLANERFUELLUNG: after 16 loops: PLAN ERFUELLT!", plan_loops >= 16u && !strcmp(ui.msg, "PLAN ERF\xDCLLT!"));
    tap(B_PLAY);

    /* the SMK-37's keys */
    ui.msg_t = 0;
    tap(B_LFO);
    check("NOTE REPEAT (LFO) tapped: SPUR, the next track", song.sel == 1u && !strcmp(ui.msg, "2: FL\xC4" "CHE"));
    tap(B_LFO); tap(B_LFO); tap(B_LFO);
    check("  four taps: round to SPUR 1", song.sel == 0u && !strcmp(ui.msg, "1: BASS"));
    tap(B_ENV);
    ok = !ui.home && cur_fam() == FAM_ENV;
    for (i = 0; i < 6u && cur_fam() == FAM_ENV; i++)
        tap(B_ENV);
    check("CHORD (ENV): ENV's pages, then LFO's", ok && cur_fam() == FAM_LFO);
    for (i = 0; i < 6u && cur_fam() == FAM_LFO; i++)
        tap(B_ENV);
    check("  ..and round to ENV again", cur_fam() == FAM_ENV);

    {   /* every Vostok message fits the header as it is drawn playing: right of the BPM, 94 px, in S */
        static const char *const M[] = {"PLAN 75 %", "PLAN ERF\xDCLLT!", "1: BASS", "2: FL\xC4" "CHE", "4: RHYTHMUS"};
        ok = 1;
        for (i = 0; i < 5u; i++)
            ok &= text_w(&AF_S, M[i]) <= 94;
        check("the messages fit the header while playing (94 px)", ok);
    }
    printf(bad ? "VOSTOK TEST FAILED\n" : "vostok: all ok\n");
    return bad != 0;
}

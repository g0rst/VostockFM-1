#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 g0rst
"""Vostok: the listening examples ("Hörproben") on the site and in the manual, played by the firmware's own sound code.

  python3 tools/make_demos.py [OUTDIR]      (default docs/hoerproben; needs build/gen, cc and ffmpeg)

Each piece is a few tracks of the VOSTOK engine (engine 14), every track one factory sound playing a step pattern
through the real voice, engine and effects code (tests/hostsim.c, STEPS=), mixed with ffmpeg to an MP3. The patterns
are 16th-note steps at the sequencer's tempo; 0 is a rest. Run tools/build.py's generate() first.
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENG = 14                                           # VOSTOK (firmware/src/eng_vostok.c, ENGI_VOSTOK)
SECS = 16

# the factory sounds by name -> their index (the order of VOSTOK_PRESETS)
NAMES = ("SPUTNIK VOSTOK-1 LAIKA TELEMETRIE BAIKONUR MOLNIJA STAHLMARSCH TUNDRA WEISSE_NACHT POLARSTATION POLARLICHT "
         "FRIEDEN SONNENWIND PLATTENBAU RADIOLA LETZTER_BUS KASSETTE BETONBASS PIONIERLIED SIGNALTON MORSE FUNKTURM "
         "KLICKTAKT RECHENWERK EISKRISTALL NORDLICHT KALTFRONT PERMAFROST STAHLWERK GLASHAUS SCHNEESTURM FROSTBASS "
         "FABRIKHALLE SAITENERSATZ STRASSENBAHN UNTERGRUND TROMMLER BETONBLOCK NACHTSCHICHT WALZWERK KATHEDRALE "
         "NEBELBANK SCHATTENCHOR TIEFSEE NACHTWACHE SCHWARZMEER ORGELHALLE MITTERNACHT SALJUT MIR SOJUS KOSMONAUT "
         "STERNENKARTE TAIGAWALD SCHWERELOS WOSTOK-6 HINTERHOF NIESELREGEN TRAMHALTE KUECHENRADIO SPAETSCHICHT "
         "TREPPENHAUS TONBAND LETZTE_TRAM MASCHINENHALLE MARSCHKAPELLE SCHLURFKIT RUNDFUNKKIT").split()
P = {n.replace("_", " "): i for i, n in enumerate(NAMES)}


def bar(*notes):
    return list(notes)


def every(n, note, length=16, offset=0):
    return [note if (i - offset) % n == 0 and i >= offset else 0 for i in range(length)]


KICK, SNARE, HAT = 36, 74, 96                      # the drum signals' pitches (HALLE kick; FUNK snare and hat)

# piece: file, title, [(sound, steps, gain dB)]
PIECES = [
    ("minimal-wave", "Minimal Wave", [
        ("VOSTOK-1", bar(45, 0, 45, 0, 45, 0, 57, 0, 45, 0, 45, 0, 48, 0, 43, 0) * 2, -3),
        ("SIGNALTON", bar(69, 0, 72, 0, 76, 0, 72, 0, 69, 0, 72, 0, 74, 0, 72, 0,
                          67, 0, 71, 0, 74, 0, 71, 0, 67, 0, 71, 0, 72, 0, 71, 0), -12),
        ("KLICKTAKT", every(4, KICK, 32), -2),
        ("FUNKTURM", every(4, HAT, 32, 2), -14),
    ]),
    ("coldwave", "Coldwave", [
        ("FROSTBASS", bar(40, 0, 40, 40, 0, 40, 0, 40, 36, 0, 36, 36, 0, 36, 0, 38) * 2, -3),
        ("KALTFRONT", bar(64, 0, 0, 0, 67, 0, 0, 71, 0, 0, 0, 0, 69, 0, 67, 0,
                          60, 0, 0, 0, 64, 0, 0, 67, 0, 0, 0, 0, 66, 0, 64, 0), -9),
        ("NORDLICHT", bar(52, *[0] * 15, 48, *[0] * 15), -14),
        ("STAHLMARSCH", every(8, KICK, 32), -2),
        ("FUNKTURM", every(8, SNARE, 32, 4), -10),
    ]),
    ("post-punk", "Post-Punk", [
        ("FABRIKHALLE", bar(38, 38, 50, 38, 38, 38, 50, 38, 41, 41, 53, 41, 36, 36, 48, 36) * 2, -4),
        ("SAITENERSATZ", bar(62, 0, 69, 0, 62, 0, 69, 0, 65, 0, 72, 0, 60, 0, 67, 0) * 2, -12),
        ("TROMMLER", every(4, KICK, 32), -2),
        ("FUNKTURM", every(8, SNARE, 32, 4), -9),
        ("FUNKTURM", every(2, HAT, 32, 1), -18),
    ]),
    ("darkwave", "Darkwave", [
        ("KATHEDRALE", bar(57, *[0] * 15, 53, *[0] * 15), -10),
        ("TIEFSEE", bar(33, 0, 0, 0, 0, 0, 0, 0, 33, 0, 0, 0, 36, 0, 0, 0,
                        29, 0, 0, 0, 0, 0, 0, 0, 29, 0, 0, 0, 31, 0, 0, 0), -4),
        ("NACHTWACHE", bar(81, 0, 0, 0, 0, 0, 84, 0, 0, 0, 0, 0, 79, 0, 0, 0,
                           77, 0, 0, 0, 0, 0, 79, 0, 0, 0, 0, 0, 76, 0, 0, 0), -14),
        ("STAHLMARSCH", every(8, KICK, 32), -3),
    ]),
    ("sovietwave", "Sovietwave", [
        ("MIR", bar(60, *[0] * 15, 57, *[0] * 15), -11),
        ("SALJUT", bar(72, 0, 0, 76, 0, 0, 79, 0, 84, 0, 0, 0, 83, 0, 79, 0,
                       81, 0, 0, 77, 0, 0, 76, 0, 72, 0, 0, 0, 74, 0, 0, 0), -10),
        ("SOJUS", bar(48, 0, 0, 0, 48, 0, 55, 0, 45, 0, 0, 0, 45, 0, 52, 0) * 2, -8),
        ("KLICKTAKT", every(8, KICK, 32), -4),
        ("FUNKTURM", every(4, HAT, 32, 2), -18),
    ]),
    # the crew at power-on, as PLAY plays it (engines.c VK_CREW: OFFBEAT, PAD, LEAD, MOTORIK)
    ("besatzung", "Die Besatzung", [
        ("VOSTOK-1", bar(0, 36, 0, 36, 0, 36, 0, 48, 0, 36, 0, 36, 0, 39, 0, 43) * 2, -4),
        ("TUNDRA", bar(60, *[0] * 7, 57, *[0] * 3, 55, *[0] * 3) * 2, -12),
        ("MOLNIJA", bar(72, 0, 0, 74, 0, 0, 76, 0, 79, 0, 76, 0, 74, 0, 0, 0) * 2, -11),
        ("MASCHINENHALLE", bar(36, 42, 36, 42, 38, 42, 42, 42, 36, 42, 36, 42, 38, 42, 46, 42) * 2, -3),
    ]),
    # the MASCHINENHALLE kit alone: MARSCH, then SCHLURF; the toms and the TELEMETRIE beep
    ("maschinenhalle", "Maschinenhalle", [
        ("MARSCHKAPELLE", bar(36, 0, 42, 0, 38, 0, 42, 0, 36, 0, 42, 0, 38, 0, 38, 38,
                              36, 0, 42, 0, 38, 0, 42, 0, 36, 45, 42, 47, 38, 48, 50, 56, *[0] * 32), -2),
        ("SCHLURFKIT", bar(*[0] * 32, 36, 0, 0, 0, 0, 0, 42, 0, 38, 0, 0, 36, 0, 0, 42, 0,
                           36, 0, 0, 0, 0, 0, 46, 0, 39, 0, 0, 36, 0, 37, 56, 0), -4),
    ]),
    ("doomerwave", "Doomerwave", [
        ("PLATTENBAU", bar(55, *[0] * 15, 51, *[0] * 15), -9),
        ("SPAETSCHICHT", bar(31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             27, 0, 0, 0, 0, 0, 0, 0, 29, 0, 0, 0, 0, 0, 0, 0), -4),
        ("KUECHENRADIO", bar(67, 0, 0, 0, 0, 0, 70, 0, 0, 0, 67, 0, 0, 0, 0, 0,
                             63, 0, 0, 0, 0, 0, 65, 0, 0, 0, 62, 0, 0, 0, 0, 0), -11),
        ("STAHLMARSCH", every(16, KICK, 32), -4),
        ("FUNKTURM", every(16, SNARE, 32, 8), -12),
    ]),
]


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "docs" / "hoerproben"
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        sim = Path(tmp) / "hostsim"
        subprocess.run(["cc", "-O2", "-w", "-include", "stdint.h", f"-I{ROOT}/build/gen", f"-I{ROOT}/firmware/src",
                        "-o", str(sim), str(ROOT / "tests" / "hostsim.c"), "-lm"], check=True)
        for fname, title, tracks in PIECES:
            wavs = []
            for k, (sound, steps, gain) in enumerate(tracks):
                w = Path(tmp) / f"{fname}_{k}.wav"
                env = dict(os.environ, SECS=str(SECS), STEPS=",".join(str(n) for n in steps))
                subprocess.run([str(sim), str(ENG), str(P[sound]), "1", str(w)], env=env, check=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                wavs.append((w, gain))
            inputs = sum((["-i", str(w)] for w, _ in wavs), [])
            chains = "".join(f"[{i}:a]volume={g}dB[a{i}];" for i, (_, g) in enumerate(wavs))
            mix = "".join(f"[a{i}]" for i in range(len(wavs)))
            filt = (chains + f"{mix}amix=inputs={len(wavs)}:normalize=0,afade=t=out:st={SECS - 2}:d=2,"
                    "alimiter=limit=0.89,loudnorm=I=-16:TP=-1.5:LRA=11[o]")
            mp3 = out / f"{fname}.mp3"
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", filt, "-map", "[o]",
                            "-ar", "44100", "-ac", "2", "-b:a", "160k", "-metadata", f"title=Vostok: {title}",
                            "-metadata", "artist=Vostok (VOSTOK engine)", str(mp3)], check=True)
            print(f"demos: {mp3} ({title}, {len(tracks)} tracks)")


if __name__ == "__main__":
    main()

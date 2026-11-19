---
title: Manual for Young Cosmonauts
subtitle: Vostok FM-1 · Vostok SMK-37 – Synthesizer of the Future
lang: en
---

# Foreword by the Director of the Institute

Dear Young Pioneer!

You are holding the latest thing from the VEB Karl-Marx-Stadt Harmonikawerke (Karl-Marx-Stadt Harmonica Works). This
is no electronic organ and no electric piano. It is a synthesizer, an instrument that could not have existed only a few
years ago.

Our science has sent people into the cosmos. Now it sends music after them. The Vostok synthesizer makes sound not
with strings or pipes but with mathematics and electrical engineering: current oscillates, one oscillation bends
another, and out of this come sounds of a clarity never heard before. This is the work of the novel **Z37 formula
code**. Konrad Zuse would be proud.

Read this manual carefully, practise hard and share your songs with your comrades. The future sounds the way you
play it.

> **Remember, Pioneer:** A synthesizer rewards curiosity. Turn every knob before you ask what it does.

# What is Vostok?

Vostok is an operating system for two devices by M-VAVE:

| Device | Model | For whom |
| --- | --- | --- |
| **Vostok FM-1** | M-VAVE FM-1 | the Pioneer model, for your jacket pocket |
| **Vostok SMK-37** | M-VAVE SMK-37 Pro, SMK-37 Elite, MKE-P37 | the House of Culture model, with 37 keys, pads and faders |

Both devices play the same world of sound. Vostok is built on **Felucca**, the free operating system by
Hügelton Instruments, and adds a sound engine of its own in Z37 formula code: **VOSTOK**, made for minimal wave, coldwave, post-punk, darkwave,
sovietwave and doomerwave.

## State of this edition

| Part | State |
| --- | --- |
| VOSTOK engine: 8 signals, 6 macros, SUB, LEIER | done |
| 64 factory sounds in six styles | done |
| Faux-Cyrillic lettering, VOSTOK colour palette, start screen | done |
| Missions, "Five-Year Plan" sequencer, Radio Studio, lesson mode | in preparation |
| English screen texts (LANGUAGE setting) | in preparation |

This manual does not yet describe the parts "in preparation". Until then, the other functions work as in Felucca.

# Getting started

## Try it without a device

The emulator runs in the browser (Chrome or Edge): <https://g0rst.github.io/VostockFM-1/emu/>. It runs the same
program code as the device.

## Programming instructions

1. **Backup.** Before programming an SMK-37 for the first time, back up the device's entire memory. The port kit explains
   how (`docs/02-update-and-recovery.md`). Without a backup there is no safe way back.
2. **Translate.** The operating system is made with `./build.sh` (see `BUILDING.md` in the repository). Each model gets its own
   package.
3. **Program.** Put the device into update mode and load the package with the programming tool.
4. **Start.** After switching on, the device shows its start screen: "SYNTHESIZER DER ZUKUNFT" – and then "AUF
   GEHT'S!" (let's go!).

> **Remember, Pioneer:** Back up first, program second. A cosmonaut never launches without a ticket home.

# The Institute's lettering

The screen texts are set in faux-Cyrillic: some capital letters appear as Cyrillic letters that look alike.

| Latin | A | B | E | N | R | W | X | Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| on the display | Л | Б | Э | И | Я | Ш | Ж | Ч |

So "ARCHIV" becomes ЛЯCHIV and "FUNKSTILLE" becomes FUИKSTILLЭ. Names and licences in the credits, and the help
hints, stay Latin. The screen texts are German for now; English ones are in preparation.

# The VOSTOK engine

## Where to find it

- **PRESETS:** VOSTOK is at the top of the list. KNOB 2 changes the engine.
- **Hold EDIT:** the first white key selects VOSTOK.

On the display it is called **VSTK** and carries a star.

## How it sounds

VOSTOK computes in Z37 formula code: frequency modulation with two operators. A modulator bends the oscillation of a carrier. The more it does,
the more overtones appear and the brighter the sound. Instead of hundreds of settings there are eight ready-made
recipes, the **signals**, and six **macros** that change several things at once.

## The eight signals (knob SIGNL)

| No. | Signal | Display | Sound | Use |
| --- | --- | --- | --- | --- |
| 1 | Sputnik | SPUTN | a clean beep | leads, arpeggios |
| 2 | Vostok | VOSTK | pulse wave | the minimal-wave bass |
| 3 | Molniya | MOLNJ | saw-like | coldwave leads |
| 4 | Cosmodrome | KOSMO | hollow square | post-punk bass |
| 5 | Tundra | TUNDR | breathing pad | darkwave pads |
| 6 | Northern Lights | POLAR | FM bell | sovietwave melodies |
| 7 | Radio Message | FUNK | noise, metal | hi-hats, snares, sounds |
| 8 | Machine Hall | HALLE | falling pitch | kick, tom, click |

## The macros

| Knob | Name | What it does |
| --- | --- | --- |
| STRAL | Radiation | modulation depth: from dark to dazzling. Envelope and LFO, routed to FLT, move it too: the classic FM envelope. |
| ORBIT | Orbit | the modulator's feedback: from smooth to rough and buzzing. Envelope and LFO on SHP move it too. |
| START | Launch | 0 to 63 "crisp": the sound darkens after the attack (the higher, the slower). 64 to 127 "wide": the sound swells in over up to 1.5 seconds. |
| SCHWB | Weightlessness | a second, slightly detuned carrier: the wide beating of sovietwave |
| STILL | Radio Silence | fewer bits, a lower sample rate, a darker filter: cassette and shortwave |
| SUB | Sub | a sine one octave lower, for more foundation |
| LEIER | Wow | a slow pitch wobble, like an old tape machine |

The first EDIT page puts SIGNL, STRAL, ORBIT and START on the four knobs. The second page holds SCHWB, STILL, SUB and
LEIER.

> **Remember, Pioneer:** More radiation, more overtones!

# The 64 factory sounds

The first sixteen sounds are the founding crew. Then come eight sounds for each style.

| No. | Group | Sounds |
| --- | --- | --- |
| 1–16 | Founding crew | SPUTNIK, VOSTOK-1, LAIKA, TELEMETRIE, BAIKONUR, MOLNIJA, STAHLMARSCH, TUNDRA, WEISSE NACHT, POLARSTATION, POLARLICHT, FRIEDEN, SONNENWIND, PLATTENBAU, RADIOLA, LETZTER BUS |
| 17–24 | Minimal wave | KASSETTE, BETONBASS, PIONIERLIED, SIGNALTON, MORSE, FUNKTURM, KLICKTAKT, RECHENWERK |
| 25–32 | Coldwave | EISKRISTALL, NORDLICHT, KALTFRONT, PERMAFROST, STAHLWERK, GLASHAUS, SCHNEESTURM, FROSTBASS |
| 33–40 | Post-punk | FABRIKHALLE, SAITENERSATZ, STRASSENBAHN, UNTERGRUND, TROMMLER, BETONBLOCK, NACHTSCHICHT, WALZWERK |
| 41–48 | Darkwave | KATHEDRALE, NEBELBANK, SCHATTENCHOR, TIEFSEE, NACHTWACHE, SCHWARZMEER, ORGELHALLE, MITTERNACHT |
| 49–56 | Sovietwave | SALJUT, MIR, SOJUS, KOSMONAUT, STERNENKARTE, TAIGAWALD, SCHWERELOS, WOSTOK-6 |
| 57–64 | Doomerwave | HINTERHOF, NIESELREGEN, TRAMHALTE, KUECHENRADIO, SPAETSCHICHT, TREPPENHAUS, TONBAND, LETZTE TRAM |

KNOB 4 (LIST) filters the list by bass, lead, pad, pluck, keys, drum and FX.

# Exercises

## Exercise 1: The minimal-wave bass

1. Choose the sound **VOSTOK-1**.
2. Set STRAL to about 40 % and START to 20 %: the note becomes short and dry.
3. Turn up SUB: the bass gets its foundation.
4. Play an eighth-note figure on two notes. A minimal-wave song needs no more.

## Exercise 2: The coldwave melody

1. Choose **MOLNIJA**.
2. Raise ORBIT until the sound turns slightly rough.
3. Add some SCHWB and play a slow melody in a minor key.

## Exercise 3: The sovietwave bell

1. Choose **POLARLICHT**.
2. Set LEIER to 30 % and SCHWB to 40 %.
3. Play a few long notes and let the reverb ring.

> **Remember, Pioneer:** Fewer notes, more space. The silence between the notes is part of the music.

# Caring for the device

- **The way back:** with your memory backup you can return to the factory operating system at any time.
- **Data:** Vostok keeps its data apart. Switching from another operating system clears its data.
- **Report problems:** <https://github.com/g0rst/VostockFM-1>

---

Vostok is a fan project based on the Felucca operating system (GPL-3.0). The VEB Karl-Marx-Stadt Harmonikawerke are
made up, and Vostok is not affiliated with M-VAVE. Program at your own risk.

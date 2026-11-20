# Vostok FM-1 · Vostok SMK-37

**Synthesizer der Zukunft / Синтезатор будущего**

Vostok ist eine Firmware für den M-VAVE FM-1 und das M-VAVE SMK-37: Minimal Wave, Coldwave, Post-Punk, Darkwave,
Sovietwave und Doomerwave auf der 6-Operator-FM-Engine, verpackt in die Fiktion eines Instruments, das das
Politbüro 1961 für die kosmosbegeisterte Jugend freigegeben hat. Optimistisch, belehrend, stolz – nie dystopisch.

- **Vostok SMK-37** – das Kulturhaus-Modell: 4 Spuren (Bass, Lead, Fläche, Rhythmus), 16 Pads als Sequenzer
  „Fünfjahresplan“, Fader-Bänke, Lehrmodus.
- **Vostok FM-1** – das Pionier-Modell: dieselbe Klangwelt, abgespeckt für die Jackentasche.

Projektseite: <https://g0rst.github.io/VostockFM-1/> · Emulator: <https://g0rst.github.io/VostockFM-1/emu/>

Die Felucca-README liegt unverändert in [FELUCCA.md](FELUCCA.md), Bauen in [BUILDING.md](BUILDING.md), das SMK-37 in [SMK37.md](SMK37.md).

## Stand

| Schritt | Status |
| --- | --- |
| Konzept | fertig |
| `smk37-port.yaml` (alle Bedienentscheidungen fürs SMK-37) | freigegeben am 17.11.2026 (offen: Rechenbudget FM-1) |
| Basis-Code (Felucca 1.6.1 + SMK-37-Layer) mit Versionsgeschichte | eingespielt |
| Browser-Emulator (GitHub Actions → Pages, `/emu/`) | eingerichtet |
| Baseline-Build, FM-1 byte-identisch | offen |
| Klangerzeugung VOSTOK, 68 Werksklänge (mit Maschinenhalle-Kit) | fertig |
| Sojus: Besatzung beim Einschalten, Planerfüllung, SMK-37-Tasten SPUR und CHORD (`tests/vostok_test.c`) | fertig |
| Oberfläche: Pseudo-Kyrillisch, Palette VOSTOK, Startbildschirm | fertig |
| Handbuch DE / EN / RU (`handbuch/`, `tools/make_handbuch.py`) | Ausgabe 1 |
| Missionen, Rundfunk-Studio, englische Bildschirmtexte | offen |

## Sprache und Schrift

Das Display spricht **Deutsch oder Englisch** (Einstellung SPRACHE), die Website Deutsch. Überschriften, Menütitel, Klangnamen und der
Startbildschirm stehen in pseudo-kyrillischen Buchstaben: deutsche Wörter, in denen einige lateinische
Großbuchstaben durch russische ersetzt sind (N→И, R→Я, W→Ш, X→Ж, Y→Ч; mehr Buchstaben machten die Wörter unleserlich). Die Firmware setzt das beim
Zeichnen um (`firmware/src/gfx.c`), die Texte im Code bleiben ASCII.
Die HELP-Hinweise und die Credits (Namen, Lizenzen) bleiben lateinisch. Das Handbuch erscheint auf Deutsch, Englisch und Russisch: Pseudo-Kyrillisch nur in der deutschen und englischen Fassung, die russische (als Gag) in echtem Kyrillisch.

```sh
python3 tools/faux_cyr.py "Funkstille"     # FUИKSTILLE
```

Eine Tabelle für alles: Firmware-Texte (Deutsch und Englisch), Website, deutsches und englisches Handbuch. Schrift ist
[Jost](https://github.com/indestructible-type/Jost) (SIL Open Font License, Futura-artig, mit kyrillischen
Buchstaben). Die Website lädt sie aus `docs/fonts/`, also ohne Google-Fonts-Abruf.

USB-Namen: `VostokFM1` (FM-1), `VostokSMK37` (SMK-37). Copyright neuer Dateien: g0rst.

## Grundlage

- Portierung nach dem Kit [genkigenki/fm1-to-smk37](https://github.com/genkigenki/fm1-to-smk37)
  (`AGENTS.md`, `smk37-port.yaml`, `docs/06-mapping-patterns.md`).
- Code-Basis: [Felucca](https://github.com/hugelton/Felucca) mit dem SMK-37-Layer aus
  [genkigenki/Felucca, Branch `smk37`](https://github.com/genkigenki/Felucca/tree/smk37). Beide Geräte bauen aus
  einer Quelle (`BOARD_SMK37`, `MODEL=pro|elite|mke`).
- Vostok ist ein Felucca-Fork und steht damit unter **GPL-3.0**.

## Sicherheitsregeln (aus dem Kit, gelten immer)

- Vor jeder Installation eine **vollständige Flash-Sicherung** des SMK-37 (siehe Kit, `docs/02-update-and-recovery.md`).
- Diese Bereiche werden nie beschrieben: `0x00000-0x03FFF`, `0xC0000-0xC1FFF` (Bluetooth, Werkskalibrierung),
  `0xF4000-0xFDFFF`, `0xFF000-0xFFFFF`.
- Der FM-1-Build bleibt nach jedem Schritt prüfbar; der Weg zurück zur Werks-Firmware bleibt offen.

Nicht mit M-VAVE verbunden. M-VAVE, FM-1 und SMK-37 sind Namen ihrer jeweiligen Inhaber.

## Emulator lokal

```sh
git submodule update --init
python3 -c "import sys; sys.path.insert(0,'tools'); import build; build.generate()"   # ohne JieLi-Toolchain
sh web/emu/build.sh          # braucht Emscripten (emcc); Ergebnis in build/emu/
```

Online baut GitHub Actions den Emulator bei jedem Push auf `main` (`.github/workflows/pages.yml`).
Dafür unter *Settings → Pages → Source* „GitHub Actions“ wählen.

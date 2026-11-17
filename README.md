# Vostok FM-1 · Vostok SMK-37

**Synthesizer der Zukunft / Синтезатор будущего**

Vostok ist eine Firmware für den M-VAVE FM-1 und das M-VAVE SMK-37: Minimal Wave, Coldwave, Post-Punk, Darkwave,
Sovietwave und Doomerwave auf der 6-Operator-FM-Engine, verpackt in die Fiktion eines Instruments, das das
Politbüro 1961 für die kosmosbegeisterte Jugend freigegeben hat. Optimistisch, belehrend, stolz – nie dystopisch.

- **Vostok SMK-37** – das Kulturhaus-Modell: 4 Spuren (Bass, Lead, Fläche, Rhythmus), 16 Pads als Sequenzer
  „Fünfjahresplan“, Fader-Bänke, Lehrmodus.
- **Vostok FM-1** – das Pionier-Modell: dieselbe Klangwelt, abgespeckt für die Jackentasche.

Projektseite: <https://g0rst.github.io/VostockFM-1/>

## Stand

| Schritt | Status |
| --- | --- |
| Konzept | fertig |
| `smk37-port.yaml` (alle Bedienentscheidungen fürs SMK-37) | freigegeben am 17.11.2026 (offen: Schrift, Rechenbudget FM-1) |
| Basis-Code (Felucca 1.6 + SMK-37-Layer) einspielen | offen |
| Baseline-Build, FM-1 byte-identisch | offen |
| Makro-Engine, Presets, Oberfläche | offen |

## Sprache und Schrift

Display, Website und Handbuch sind **nur auf Deutsch**. Überschriften, Menütitel, Klangnamen und der
Startbildschirm stehen in pseudo-kyrillischen Buchstaben: deutsche Wörter, in denen einige lateinische
Großbuchstaben durch russische ersetzt sind (A→Д, B→Б, E→Ё, N→И, R→Я, U→Ц, W→Ш, X→Ж, Y→Ч).
Werte, Zahlen und Hinweiszeilen bleiben normal lesbar.

```sh
python3 tools/faux_cyr.py "Funkstille"     # FЦИKSTILLЁ
```

Eine Tabelle für alles: Firmware-Texte, Website, Handbuch. Schrift-Vorschlag ist
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

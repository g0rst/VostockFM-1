---
title: Handbuch für junge Kosmonauten
subtitle: Vostok FM-1 · Vostok SMK-37 – Synthesizer der Zukunft
lang: de
---

# Vorwort des Institutsdirektors

Liebe Pionierin, lieber Pionier!

Du hältst ein Instrument in den Händen, das es vor wenigen Jahren noch nicht geben konnte. Unsere Wissenschaft hat den
Menschen in den Kosmos geschickt. Nun schickt sie die Musik hinterher. Der Vostok-Synthesizer erzeugt Töne nicht mit
Saiten oder Pfeifen, sondern mit Mathematik: Eine Schwingung verändert eine andere, und daraus entstehen Klänge von
nie gehörter Klarheit.

Lies dieses Handbuch aufmerksam, übe fleißig und teile deine Lieder mit deinen Kameradinnen und Kameraden. Die Zukunft
klingt so, wie du sie spielst.

> **Merke dir, Pionier:** Ein Synthesizer belohnt Neugier. Drehe an jedem Regler, bevor du fragst, was er tut.

# Was ist Vostok?

Vostok ist eine Firmware für zwei Geräte von M-VAVE:

| Gerät | Modell | Für wen |
| --- | --- | --- |
| **Vostok FM-1** | M-VAVE FM-1 | das Pionier-Modell für die Jackentasche |
| **Vostok SMK-37** | M-VAVE SMK-37 Pro, SMK-37 Elite, MKE-P37 | das Kulturhaus-Modell mit 37 Tasten, Pads und Fadern |

Beide Geräte spielen dieselbe Klangwelt. Vostok baut auf **Felucca** auf, der freien Firmware von Hügelton Instruments,
und bringt eine eigene Klangerzeugung mit: **VOSTOK**, gemacht für Minimal Wave, Coldwave, Post-Punk, Darkwave,
Sovietwave und Doomerwave.

## Stand dieser Ausgabe

| Teil | Stand |
| --- | --- |
| Klangerzeugung VOSTOK: 8 Signale, 6 Makros, SUB, LEIER | fertig |
| 64 Werksklänge in sechs Stilrichtungen | fertig |
| Schrift in Pseudo-Kyrillisch, Farbpalette VOSTOK, Startbildschirm | fertig |
| Missionen, Sequenzer „Fünfjahresplan“, Rundfunk-Studio, Lehrmodus | in Vorbereitung |
| Englische Bildschirmtexte (Einstellung SPRACHE) | in Vorbereitung |

Alles, was „in Vorbereitung“ ist, beschreibt dieses Handbuch noch nicht. Bis dahin bedienst du die übrigen Funktionen
wie in Felucca.

# Inbetriebnahme

## Ausprobieren ohne Gerät

Der Emulator läuft im Browser (Chrome oder Edge): <https://g0rst.github.io/VostockFM-1/emu/>. Er nutzt denselben
Programmcode wie das Gerät.

## Installation

1. **Sicherung.** Vor der ersten Installation auf einem SMK-37 sicherst du den gesamten Speicher des Geräts. Wie das
   geht, steht im Port-Kit (`docs/02-update-and-recovery.md`). Ohne Sicherung gibt es keinen sicheren Weg zurück.
2. **Bauen.** Die Firmware entsteht mit `./build.sh` (siehe `BUILDING.md` im Repository). Für jedes Modell gibt es ein
   eigenes Paket.
3. **Aufspielen.** Das Gerät in den Update-Modus bringen und das Paket mit dem Installer aufspielen.
4. **Start.** Nach dem Einschalten zeigt das Gerät den Startbildschirm: „SYNTHESIZER DER ZUKUNFT“ – und dann „AUF
   GEHT'S!“

> **Merke dir, Pionier:** Erst sichern, dann installieren. Ein Kosmonaut startet nie ohne Rückfahrkarte.

# Die Schrift des Instituts

Alle Bildschirmtexte sind deutsch, aber in Pseudo-Kyrillisch gesetzt: Einige Großbuchstaben erscheinen als kyrillische
Buchstaben, die ähnlich aussehen.

| Lateinisch | A | B | E | N | R | W | X | Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auf dem Display | Л | Б | Э | И | Я | Ш | Ж | Ч |

So wird aus „ARCHIV“ ЛЯCHIV und aus „FUNKSTILLE“ FUИKSTILLЭ. Namen und Lizenzen in den Credits sowie die
Hilfehinweise bleiben lateinisch.

# Die Klangerzeugung VOSTOK

## So findest du sie

- **PRESETS:** VOSTOK steht in der Liste ganz oben. KNOB 2 wechselt die Klangerzeugung.
- **EDIT halten:** Die erste weiße Taste wählt VOSTOK.

Auf dem Display heißt sie kurz **VSTK** und trägt einen Stern.

## Wie sie klingt

VOSTOK ist eine Frequenzmodulation mit zwei Operatoren: Ein Modulator verbiegt die Schwingung eines Trägers. Je
stärker er das tut, desto mehr Obertöne entstehen und desto heller klingt der Ton. Statt hunderter Einstellungen gibt
es acht fertige Rezepte, die **Signale**, und sechs **Makros**, die gleich mehrere Dinge auf einmal verändern.

## Die acht Signale (Regler SIGNL)

| Nr. | Signal | Anzeige | Klang | Wofür |
| --- | --- | --- | --- | --- |
| 1 | Sputnik | SPUTN | reines Piepen | Leads, Arpeggios |
| 2 | Vostok | VOSTK | Pulswelle | der Minimal-Wave-Bass |
| 3 | Molnija | MOLNJ | sägezahnartig | Coldwave-Leads |
| 4 | Kosmodrom | KOSMO | hohles Rechteck | Post-Punk-Bass |
| 5 | Tundra | TUNDR | atmende Fläche | Darkwave-Pads |
| 6 | Polarlicht | POLAR | FM-Glocke | Sovietwave-Melodien |
| 7 | Funkspruch | FUNK | Rauschen, Metall | Hi-Hats, Snares, Geräusche |
| 8 | Maschinenhalle | HALLE | fallender Ton | Kick, Tom, Klick |

## Die Makros

| Regler | Name | Was er tut |
| --- | --- | --- |
| STRAL | Strahlung | Modulationsstärke: dunkel bis gleißend hell. Hüllkurve und LFO, auf FLT geleitet, bewegen sie mit: die klassische FM-Hüllkurve. |
| ORBIT | Umlaufbahn | Rückkopplung des Modulators: von glatt bis rau und brummend. Hüllkurve und LFO auf SHP bewegen sie mit. |
| START | Start | 0 bis 63 „knackig“: Der Ton wird nach dem Anschlag dunkler (je höher, desto langsamer). 64 bis 127 „flächig“: Der Ton schwillt bis zu 1,5 Sekunden lang an. |
| SCHWB | Schwerelosigkeit | ein zweiter, leicht verstimmter Träger: die breite Schwebung der Sovietwave |
| STILL | Funkstille | weniger Bits, niedrigere Abtastrate, dunklerer Filter: Kassette und Kurzwelle |
| SUB | Sub | ein Sinus eine Oktave tiefer, für mehr Fundament |
| LEIER | Leiern | langsames Tonhöhenschwanken wie bei einem alten Tonbandgerät |

Auf der ersten EDIT-Seite liegen SIGNL, STRAL, ORBIT und START auf den vier Reglern. Die zweite Seite enthält SCHWB,
STILL, SUB und LEIER.

> **Merke dir, Pionier:** Wer die Strahlung erhöht, erhält mehr Obertöne!

# Die 64 Werksklänge

Die ersten sechzehn Klänge sind die Gründungsbesatzung. Danach folgen je acht Klänge pro Stilrichtung.

| Nr. | Gruppe | Klänge |
| --- | --- | --- |
| 1–16 | Gründungsbesatzung | SPUTNIK, VOSTOK-1, LAIKA, TELEMETRIE, BAIKONUR, MOLNIJA, STAHLMARSCH, TUNDRA, WEISSE NACHT, POLARSTATION, POLARLICHT, FRIEDEN, SONNENWIND, PLATTENBAU, RADIOLA, LETZTER BUS |
| 17–24 | Minimal Wave | KASSETTE, BETONBASS, PIONIERLIED, SIGNALTON, MORSE, FUNKTURM, KLICKTAKT, RECHENWERK |
| 25–32 | Coldwave | EISKRISTALL, NORDLICHT, KALTFRONT, PERMAFROST, STAHLWERK, GLASHAUS, SCHNEESTURM, FROSTBASS |
| 33–40 | Post-Punk | FABRIKHALLE, SAITENERSATZ, STRASSENBAHN, UNTERGRUND, TROMMLER, BETONBLOCK, NACHTSCHICHT, WALZWERK |
| 41–48 | Darkwave | KATHEDRALE, NEBELBANK, SCHATTENCHOR, TIEFSEE, NACHTWACHE, SCHWARZMEER, ORGELHALLE, MITTERNACHT |
| 49–56 | Sovietwave | SALJUT, MIR, SOJUS, KOSMONAUT, STERNENKARTE, TAIGAWALD, SCHWERELOS, WOSTOK-6 |
| 57–64 | Doomerwave | HINTERHOF, NIESELREGEN, TRAMHALTE, KUECHENRADIO, SPAETSCHICHT, TREPPENHAUS, TONBAND, LETZTE TRAM |

Mit KNOB 4 (LIST) filterst du die Liste nach Bass, Lead, Pad, Pluck, Keys, Drum und FX.

# Übungsstücke

## Übung 1: Der Minimal-Wave-Bass

1. Wähle den Klang **VOSTOK-1**.
2. Stelle STRAL auf etwa 40 % und START auf 20 %: Der Ton wird kurz und trocken.
3. Drehe SUB auf: Der Bass bekommt Fundament.
4. Spiele eine Achtelnoten-Figur auf zwei Tönen. Mehr braucht ein Minimal-Wave-Lied nicht.

## Übung 2: Die Coldwave-Melodie

1. Wähle **MOLNIJA**.
2. Erhöhe ORBIT, bis der Ton leicht rau wird.
3. Gib etwas SCHWB dazu und spiele eine langsame Melodie in Moll.

## Übung 3: Die Sovietwave-Glocke

1. Wähle **POLARLICHT**.
2. Stelle LEIER auf 30 % und SCHWB auf 40 %.
3. Spiele wenige lange Töne und lass den Hall wirken.

> **Merke dir, Pionier:** Weniger Töne, mehr Raum. Die Stille zwischen den Tönen gehört zur Musik.

# Pflege des Geräts

- **Rückweg:** Mit deiner Speichersicherung kehrst du jederzeit zur Werksfirmware zurück.
- **Daten:** Vostok verwaltet seine Daten getrennt. Beim Wechsel von einer anderen Firmware werden deren Daten gelöscht.
- **Fehler melden:** <https://github.com/g0rst/VostockFM-1>

---

Vostok ist ein Fan- und Firmware-Projekt auf Basis von Felucca (GPL-3.0). Es ist nicht mit M-VAVE verbunden.
Installation auf eigene Gefahr.

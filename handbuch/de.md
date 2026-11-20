---
title: Handbuch für junge Kosmonauten
subtitle: Vostok FM-1 · Vostok SMK-37 – Synthesizer der Zukunft
lang: de
---

# Vorwort des Institutsdirektors

Liebe Pionierin, lieber Pionier!

Du hältst den neuesten Schrei aus den VEB Karl-Marx-Stadt Harmonikawerken in den Händen. Dies ist keine
Elektronikorgel und kein E-Piano. Es ist ein Synthesizer, ein Instrument, das es vor wenigen Jahren noch nicht geben
konnte.

Unsere Wissenschaft hat den Menschen in den Kosmos geschickt. Nun schickt sie die Musik hinterher. Der
Vostok-Synthesizer erzeugt Töne nicht mit Saiten oder Pfeifen, sondern mit Mathematik und Elektrotechnik: Strom
schwingt, eine Schwingung verändert die andere, und daraus entstehen Klänge von nie gehörter Klarheit. Möglich macht
das der neuartige **Z37-Formel-Code**. Konrad Zuse wäre stolz.

Lies dieses Handbuch aufmerksam, übe fleißig und teile deine Lieder mit deinen Genossinnen und Genossen. Die Zukunft
klingt so, wie du sie spielst.

> **Merke dir, Pionier:** Ein Synthesizer belohnt Neugier. Drehe an jedem Regler, bevor du fragst, was er tut.

# Was ist Vostok?

Vostok ist ein Betriebssystem für zwei Geräte von M-VAVE:

| Gerät | Modell | Für wen |
| --- | --- | --- |
| **Vostok FM-1** | M-VAVE FM-1 | das Pionier-Modell für die Jackentasche |
| **Vostok SMK-37** | M-VAVE SMK-37 Pro, SMK-37 Elite, MKE-P37 | das Kulturhaus-Modell mit 37 Tasten, Pads und Fadern |

Beide Geräte spielen dieselbe Klangwelt. Vostok baut auf **Felucca** auf, dem freien Betriebssystem von Hügelton Instruments,
und bringt eine eigene Klangerzeugung im Z37-Formel-Code mit: **VOSTOK**, gemacht für Minimal Wave, Coldwave, Post-Punk, Darkwave,
Sovietwave und Doomerwave.

## Stand dieser Ausgabe

| Teil | Stand |
| --- | --- |
| Klangerzeugung VOSTOK: 8 Signale, 6 Makros, SUB, LEIER | fertig |
| 68 Werksklänge: sechs Stilrichtungen und vier Schlagzeug-Kits | fertig |
| Besatzung beim Einschalten, Maschinenhalle-Kit, Planerfüllung, SMK-37-Tasten SPUR und CHORD | fertig |
| Schrift in Pseudo-Kyrillisch, Farbpalette VOSTOK, Startbildschirm | fertig |
| Missionen, Rundfunk-Studio, Lehrmodus | in Vorbereitung |
| Englische Bildschirmtexte (Einstellung SPRACHE) | in Vorbereitung |

Alles, was „in Vorbereitung“ ist, beschreibt dieses Handbuch noch nicht. Bis dahin bedienst du die übrigen Funktionen
wie in Felucca.

# Inbetriebnahme

## Ausprobieren ohne Gerät

Der Emulator läuft im Browser (Chrome oder Edge): <https://g0rst.github.io/VostockFM-1/emu/>. Er nutzt denselben
Programmcode wie das Gerät.

## Programmierungsanleitung

1. **Sicherung.** Vor der ersten Programmierung eines SMK-37 sicherst du den gesamten Speicher des Geräts. Wie das
   geht, steht im Port-Kit (`docs/02-update-and-recovery.md`). Ohne Sicherung gibt es keinen sicheren Weg zurück.
2. **Übersetzen.** Das Betriebssystem entsteht mit `./build.sh` (siehe `BUILDING.md` im Repository). Für jedes Modell gibt es ein
   eigenes Paket.
3. **Programmieren.** Das Gerät in den Aktualisierungsmodus bringen und das Paket mit dem Programmierwerkzeug einspielen.
4. **Start.** Nach dem Einschalten zeigt das Gerät den Startbildschirm: „SYNTHESIZER DER ZUKUNFT“ – und dann „AUF
   GEHT'S!“

> **Merke dir, Pionier:** Erst sichern, dann programmieren. Ein Kosmonaut startet nie ohne Rückfahrkarte.

# Die Schrift des Instituts

Alle Bildschirmtexte sind deutsch, aber in Pseudo-Kyrillisch gesetzt: Fünf Großbuchstaben erscheinen als kyrillische
Buchstaben, die ähnlich aussehen. Alle anderen bleiben, wie sie sind, damit du alles gut lesen kannst.

| Lateinisch | N | R | W | X | Y |
| --- | --- | --- | --- | --- | --- |
| auf dem Bildschirm | И | Я | Ш | Ж | Ч |

So wird aus „ARCHIV“ AЯCHIV und aus „FUNKSTILLE“ FUИKSTILLE. Namen und Lizenzen in den Credits sowie die
Hilfehinweise bleiben lateinisch.

# Die Klangerzeugung VOSTOK

## So findest du sie

- **Taste PRESETS (Voreinstellungen):** VOSTOK steht in der Liste ganz oben. KNOB 2 wechselt die Klangerzeugung.
- **EDIT halten:** Die erste weiße Taste wählt VOSTOK.

Auf dem Bildschirm heißt sie kurz **VSTK** und trägt einen Stern.

## Wie sie klingt

VOSTOK rechnet im Z37-Formel-Code: eine Frequenzmodulation mit zwei Operatoren. Ein Modulator verbiegt die Schwingung eines Trägers. Je
stärker er das tut, desto mehr Obertöne entstehen und desto heller klingt der Ton. Statt hunderter Einstellungen gibt
es acht fertige Rezepte, die **Signale**, und sechs **Makros**, die gleich mehrere Dinge auf einmal verändern.

## Die Signale (Regler SIGNL)

| Nr. | Signal | Bildschirm | Klang | Wofür |
| --- | --- | --- | --- | --- |
| 1 | Sputnik | SPUTN | reines Piepen | Leads, Arpeggios |
| 2 | Vostok | VOSTK | Pulswelle | der Minimal-Wave-Bass |
| 3 | Molnija | MOLNJ | sägezahnartig | Coldwave-Leads |
| 4 | Kosmodrom | KOSMO | hohles Rechteck | Post-Punk-Bass |
| 5 | Tundra | TUNDR | atmende Fläche | Darkwave-Pads |
| 6 | Polarlicht | POLAR | FM-Glocke | Sovietwave-Melodien |
| 7 | Funkspruch | FUNK | Rauschen, Metall | Hi-Hats, Snares, Geräusche |
| 8 | Maschinenhalle | HALLE | fallender Ton | Kick, Tom, Klick |
| 9 | Kit | KIT | das ganze Schlagzeug | eine Spur für alle Trommeln (siehe Besatzung) |

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

# Die Besatzung und der Fünfjahresplan

## Die Besatzung

Beim Einschalten sind alle vier Spuren schon besetzt, und jede hat ein Muster im Sequenzer. Drücke PLAY, und die
Besatzung spielt.

| Spur | Rolle | Klang | Muster |
| --- | --- | --- | --- |
| 1 | Bass | VOSTOK-1 | OFFBEAT |
| 2 | Fläche | TUNDRA | PAD |
| 3 | Lead | MOLNIJA | LEAD |
| 4 | Rhythmus | MASCHINENHALLE | MOTORIK |

## Die Maschinenhalle

Das neunte Signal heißt **KIT**. Damit spielt eine einzige Spur das ganze Schlagzeug: Welche Trommel erklingt,
entscheidet die Taste.

| Note | Trommel |
| --- | --- |
| 36 (C2) | Stampfer (Bassdrum) |
| 37 | Randschlag |
| 38, 40 | Schmiede (Snare) |
| 39 | Applaus (Klatschen) |
| 42, 44 | Funke (geschlossene Hi-Hat) |
| 46 | Dampf (offene Hi-Hat) |
| 41, 43, 45, 47, 48, 50 | Kesselpauken (Toms, in ihrer Tonhöhe) |
| 56 | Telemetrie-Piep |

Auf den Tasten liegen diese Noten zwei Oktaven tiefer: Drücke zweimal OCT-. Im Sequenzer stehen sie einfach als Noten.

Beim Kit wirken die Makros anders: **STRAL** macht alle Trommeln heller oder dunkler (Mitte = wie gebaut), **START**
ist die Länge der Schläge (32 = wie gebaut), **STILL** macht sie rau wie eine alte Kassette.

Vier Kit-Klänge sind dabei: MASCHINENHALLE, MARSCHKAPELLE, SCHLURFKIT und RUNDFUNKKIT. Dazu kommen drei neue Muster
unter SAVE > PHRASES: **MARSCH**, **MOTORIK** und **SCHLURF** (der langsame Doomer-Schritt).

## Die Planerfüllung

Während die Musik läuft, zählt das Gerät, wie oft das Muster der gewählten Spur durchgelaufen ist. Alle vier Durchläufe
meldet es den Stand: PLAN 25 %, PLAN 50 %, PLAN 75 %. Nach sechzehn Durchläufen erscheint **PLAN ERFÜLLT!** – und
der nächste Plan beginnt.

## Die Tasten des SMK-37

| Taste | Was sie tut |
| --- | --- |
| NOTE REPEAT kurz | **SPUR:** die nächste Spur wählen (1: BASS, 2: FLÄCHE, 3: LEAD, 4: RHYTHMUS) |
| NOTE REPEAT gehalten | wie bisher: Drehst du dabei an Reglern, springen die Werte beim Loslassen zurück |
| CHORD | die Hüllkurvenseiten, noch einmal gedrückt die LFO-Seiten |

Alle anderen Tasten bleiben, wie sie sind.

> **Merke dir, Pionier:** Wer den Plan übererfüllt, spielt einfach weiter.

# Die 68 Werksklänge

Die ersten sechzehn Klänge sind die Gründungsbesatzung. Danach folgen je acht Klänge pro Stilrichtung und die vier
Schlagzeug-Kits der Maschinenhalle.

| Nr. | Gruppe | Klänge |
| --- | --- | --- |
| 1–16 | Gründungsbesatzung | SPUTNIK, VOSTOK-1, LAIKA, TELEMETRIE, BAIKONUR, MOLNIJA, STAHLMARSCH, TUNDRA, WEISSE NACHT, POLARSTATION, POLARLICHT, FRIEDEN, SONNENWIND, PLATTENBAU, RADIOLA, LETZTER BUS |
| 17–24 | Minimal Wave | KASSETTE, BETONBASS, PIONIERLIED, SIGNALTON, MORSE, FUNKTURM, KLICKTAKT, RECHENWERK |
| 25–32 | Coldwave | EISKRISTALL, NORDLICHT, KALTFRONT, PERMAFROST, STAHLWERK, GLASHAUS, SCHNEESTURM, FROSTBASS |
| 33–40 | Post-Punk | FABRIKHALLE, SAITENERSATZ, STRASSENBAHN, UNTERGRUND, TROMMLER, BETONBLOCK, NACHTSCHICHT, WALZWERK |
| 41–48 | Darkwave | KATHEDRALE, NEBELBANK, SCHATTENCHOR, TIEFSEE, NACHTWACHE, SCHWARZMEER, ORGELHALLE, MITTERNACHT |
| 49–56 | Sovietwave | SALJUT, MIR, SOJUS, KOSMONAUT, STERNENKARTE, TAIGAWALD, SCHWERELOS, WOSTOK-6 |
| 57–64 | Doomerwave | HINTERHOF, NIESELREGEN, TRAMHALTE, KUECHENRADIO, SPAETSCHICHT, TREPPENHAUS, TONBAND, LETZTE TRAM |
| 65–68 | Maschinenhalle | MASCHINENHALLE, MARSCHKAPELLE, SCHLURFKIT, RUNDFUNKKIT |

Mit KNOB 4 (LIST) filterst du die Liste nach Bass, Lead, Pad, Pluck, Keys, Drum und FX.

# Hörproben

Acht kleine Stücke, gespielt vom echten Klangcode des Geräts: nur die Klangerzeugung VOSTOK und ihre Werksklänge, nichts nachbearbeitet außer der Lautstärke. Hör genau hin und spiel sie dann selbst nach!

| Stil | Hören | Klänge |
| --- | --- | --- |
| Die Besatzung | <audio controls preload="none" src="../hoerproben/besatzung.mp3"></audio> | VOSTOK-1, TUNDRA, MOLNIJA, MASCHINENHALLE |
| Maschinenhalle | <audio controls preload="none" src="../hoerproben/maschinenhalle.mp3"></audio> | MARSCHKAPELLE, SCHLURFKIT |
| Minimal Wave | <audio controls preload="none" src="../hoerproben/minimal-wave.mp3"></audio> | VOSTOK-1, SIGNALTON, KLICKTAKT, FUNKTURM |
| Coldwave | <audio controls preload="none" src="../hoerproben/coldwave.mp3"></audio> | FROSTBASS, KALTFRONT, NORDLICHT, STAHLMARSCH |
| Post-Punk | <audio controls preload="none" src="../hoerproben/post-punk.mp3"></audio> | FABRIKHALLE, SAITENERSATZ, TROMMLER, FUNKTURM |
| Darkwave | <audio controls preload="none" src="../hoerproben/darkwave.mp3"></audio> | KATHEDRALE, TIEFSEE, NACHTWACHE, STAHLMARSCH |
| Sovietwave | <audio controls preload="none" src="../hoerproben/sovietwave.mp3"></audio> | MIR, SALJUT, SOJUS, KLICKTAKT |
| Doomerwave | <audio controls preload="none" src="../hoerproben/doomerwave.mp3"></audio> | PLATTENBAU, SPAETSCHICHT, KUECHENRADIO, STAHLMARSCH |

> **Merke dir, Pionier:** Nachspielen ist erlaubt. Abschreiben auch. So lernen Musiker.

## So sieht es aus

<div class="screens">
<figure class="screen"><img src="../bilder/splash.png" alt="Der Startbildschirm" width="240" height="240"><figcaption>Der Startbildschirm</figcaption></figure>
<figure class="screen"><img src="../bilder/edit_vostok.png" alt="VOSTOK, Seite 1: SIGNL, STRAL, ORBIT, START" width="240" height="240"><figcaption>VOSTOK, Seite 1: SIGNL, STRAL, ORBIT, START</figcaption></figure>
<figure class="screen"><img src="../bilder/edit_vostok_2.png" alt="Seite 2: SCHWB, STILL, SUB, LEIER" width="240" height="240"><figcaption>Seite 2: SCHWB, STILL, SUB, LEIER</figcaption></figure>
</div>

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

- **Rückweg:** Mit deiner Speichersicherung kehrst du jederzeit zum Werks-Betriebssystem zurück.
- **Daten:** Vostok verwaltet seine Daten getrennt. Beim Wechsel von einem anderen Betriebssystem werden dessen Daten gelöscht.
- **Fehler melden:** <https://github.com/g0rst/VostockFM-1>

---

Vostok ist ein Fan-Projekt auf Basis des Betriebssystems Felucca (GPL-3.0). Die VEB Karl-Marx-Stadt Harmonikawerke
sind erfunden, und Vostok ist nicht mit M-VAVE verbunden. Programmierung auf eigene Gefahr.

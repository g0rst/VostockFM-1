#!/usr/bin/env python3
# Vostok: German text in faux-Cyrillic lettering ("Pseudo-Kyrillisch").
# Copyright (c) 2026 g0rst. GPL-3.0-or-later.
#
# The text stays German and readable; only some Latin capitals are swapped for Cyrillic
# letters that look alike or evoke the look (R -> Я, N -> И, A -> Д ...). Used for titles,
# menu headers, preset names, the boot screen and the manual's headings. Values, numbers and
# running text stay plain Latin in the same font, so everything stays readable.
#
# Usage:  python3 tools/faux_cyr.py "Funkstille"  ->  FЦИKSTILLЁ
#         from faux_cyr import fauxcyr

import sys

# One table for the whole project: firmware strings, website, manual.
# Every target glyph is a real Cyrillic letter, so any font with Cyrillic coverage renders it.
MAP = {
    "A": "Д",   # De
    "B": "Б",   # Be
    "E": "Ё",   # Yo
    "N": "И",   # I
    "R": "Я",   # Ya
    "U": "Ц",   # Tse
    "W": "Ш",   # Sha
    "X": "Ж",   # Zhe
    "Y": "Ч",   # Che
}
# Only letters of the Russian alphabet, so every font with basic Cyrillic renders them (Jost included).
# Left Latin on purpose: the rest. Their Cyrillic look-alikes (С, Н, К, М, О, Р, Т) change nothing
# visible, and swapping more letters hurts readability.


def fauxcyr(text: str) -> str:
    """Upper-case the text and swap the letters in MAP."""
    return "".join(MAP.get(ch, ch) for ch in text.upper())


if __name__ == "__main__":
    print(fauxcyr(" ".join(sys.argv[1:]) or "Synthesizer der Zukunft"))

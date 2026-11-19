#!/usr/bin/env python3
# Vostok: German text in faux-Cyrillic lettering ("Pseudo-Kyrillisch").
# Copyright (c) 2026 g0rst. GPL-3.0-or-later.
#
# The text stays German and readable; only some Latin capitals are swapped for Cyrillic
# letters that look alike or evoke the look (R -> Я, N -> И, A -> Д ...). Used for titles,
# menu headers, preset names, the boot screen and the manual's headings. Values, numbers and
# running text stay plain Latin in the same font, so everything stays readable.
#
# Usage:  python3 tools/faux_cyr.py "Funkstille"  ->  FUИKSTILLE
#         from faux_cyr import fauxcyr

import sys

# One table for the whole project: firmware strings, website, manual.
# Every target glyph is a real Cyrillic letter, so any font with Cyrillic coverage renders it.
MAP = {
    "N": "И",   # I
    "R": "Я",   # Ya
    "W": "Ш",   # Sha
    "X": "Ж",   # Zhe
    "Y": "Ч",   # Che
}
# The same table as the firmware (firmware/src/gfx.c VK_LETTER). Five letters only: with A B E swapped too (Л Б Э)
# the words got hard to read. And only letters that keep to the capitals' band: Д Ц (descenders) and Ё (dots) spill
# out of the screen's cells. Russian letters only, so every font with basic Cyrillic renders them.


def fauxcyr(text: str) -> str:
    """Upper-case the text and swap the letters in MAP."""
    return "".join(MAP.get(ch, ch) for ch in text.upper())


if __name__ == "__main__":
    print(fauxcyr(" ".join(sys.argv[1:]) or "Synthesizer der Zukunft"))

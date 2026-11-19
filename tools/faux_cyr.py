#!/usr/bin/env python3
# Vostok: German text in faux-Cyrillic lettering ("Pseudo-Kyrillisch").
# Copyright (c) 2026 g0rst. GPL-3.0-or-later.
#
# The text stays German and readable; only some Latin capitals are swapped for Cyrillic
# letters that look alike or evoke the look (R -> Я, N -> И, A -> Д ...). Used for titles,
# menu headers, preset names, the boot screen and the manual's headings. Values, numbers and
# running text stay plain Latin in the same font, so everything stays readable.
#
# Usage:  python3 tools/faux_cyr.py "Funkstille"  ->  FUИKSTILLЭ
#         from faux_cyr import fauxcyr

import sys

# One table for the whole project: firmware strings, website, manual.
# Every target glyph is a real Cyrillic letter, so any font with Cyrillic coverage renders it.
MAP = {
    "A": "Л",   # El (reads as the Greek Lambda: the classic faux-Cyrillic A)
    "B": "Б",   # Be
    "E": "Э",   # E (the mirrored E)
    "N": "И",   # I
    "R": "Я",   # Ya
    "W": "Ш",   # Sha
    "X": "Ж",   # Zhe
    "Y": "Ч",   # Che
}
# The same table as the firmware (firmware/src/gfx.c VK_LETTER). Only letters that keep to the capitals' band: Д and Ц
# (descenders) and Ё (dots) spill out of the screen's cells, so A E use Л Э and U stays Latin. Russian letters only,
# so every font with basic Cyrillic renders them (Jost, Inter Tight). The rest stays Latin on purpose: their
# look-alikes (С, Н, К, М, О, Р, Т) change nothing visible, and swapping more hurts readability.


def fauxcyr(text: str) -> str:
    """Upper-case the text and swap the letters in MAP."""
    return "".join(MAP.get(ch, ch) for ch in text.upper())


if __name__ == "__main__":
    print(fauxcyr(" ".join(sys.argv[1:]) or "Synthesizer der Zukunft"))

#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 g0rst
"""Vostok: the manual ("Handbuch für junge Kosmonauten") from handbuch/<lang>.md to docs/handbuch/<lang>.html.

  python3 tools/make_handbuch.py [OUTDIR]      (default docs/handbuch)

Three editions: de, en, ru. In de and en the title, the headings and the "Merke dir, Pionier" / "Remember, Pioneer"
labels are set in faux-Cyrillic (tools/faux_cyr.py, the firmware's own table); ru is the real thing, as written.
Needs the Python package markdown. The pages use the site's font (docs/fonts, Jost) and print on A4.
"""
import re
import sys
from html import escape
from pathlib import Path

import markdown

sys.path.insert(0, str(Path(__file__).resolve().parent))
from faux_cyr import fauxcyr  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
LANGS = [("de", "Deutsch"), ("en", "English"), ("ru", "Русский")]
FAUX = {"de", "en"}

CSS = """
@font-face{font-family:"Jost";src:url(../fonts/Jost-400-Book.ttf) format("truetype");font-weight:400}
@font-face{font-family:"Jost";src:url(../fonts/Jost-700-Bold.ttf) format("truetype");font-weight:700}
:root{--ivory:#f3ead6;--paper:#fbf5e8;--red:#9e1e18;--sky:#145896;--ochre:#c08a2e;--ink:#28201a;--muted:#6d6155}
*{box-sizing:border-box}
body{margin:0;background:var(--ivory);color:var(--ink);font:17px/1.6 "Jost","Futura","Century Gothic",sans-serif}
a{color:var(--sky)}
header{background:var(--red);color:var(--paper);padding:40px 0 34px}
.wrap{max-width:860px;margin:0 auto;padding:0 22px}
header h1{margin:0;font-size:clamp(1.9rem,5vw,3rem);line-height:1.1;letter-spacing:.03em}
header p{margin:.4em 0 0;opacity:.9}
nav.lang{margin-top:18px;font-size:.9rem}
nav.lang a,nav.lang span{color:var(--paper);margin-right:14px}
nav.lang span{font-weight:700;border-bottom:2px solid var(--paper)}
main h1{font-size:1.7rem;margin:2.2em 0 .6em;padding-bottom:.25em;border-bottom:3px solid var(--ink);letter-spacing:.03em}
main h2{font-size:1.25rem;margin:1.6em 0 .5em;color:var(--red);letter-spacing:.03em}
table{width:100%;border-collapse:collapse;background:var(--paper);margin:1em 0;font-size:.95rem}
th,td{border:2px solid var(--ink);padding:6px 9px;text-align:left;vertical-align:top}
th{background:var(--ink);color:var(--paper)}
blockquote{margin:1.4em 0;padding:14px 18px;background:var(--sky);color:var(--paper);border:3px solid var(--ink);
  box-shadow:5px 5px 0 var(--ink)}
blockquote p{margin:0}
code{background:var(--paper);padding:1px 5px;border:1px solid #d8ccb0}
hr{border:0;border-top:3px solid var(--ink);margin:2.4em 0 1em}
footer{color:var(--muted);font-size:.85rem;padding:0 0 40px}
@media print{body{background:#fff;font-size:11pt}header{padding:18px 0}blockquote{box-shadow:none}
  nav.lang{display:none}main h1{page-break-before:always}main h1:first-child{page-break-before:auto}}
"""


def front(text):
    meta, body = {}, text
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
        body = text[m.end():]
    return meta, body


def faux_tags(html):
    """faux-Cyrillic in the headings and in the bold label that opens a Merksatz (blockquote)"""
    html = re.sub(r"<(h[1-3])([^>]*)>(.*?)</\1>", lambda m: f"<{m[1]}{m[2]}>{faux_text(m[3])}</{m[1]}>", html)
    return re.sub(r"(<blockquote>\s*<p>)<strong>(.*?)</strong>", lambda m: f"{m[1]}<strong>{faux_text(m[2])}</strong>", html)


def faux_text(fragment):
    """swap the letters of the text between tags, never inside a tag or an entity"""
    return re.sub(r"(<[^>]+>|&[a-z#0-9]+;)|([^<&]+)", lambda m: m[1] or fauxcyr(m[2]), fragment)


def page(lang, meta, body_html):
    title, sub = meta.get("title", ""), meta.get("subtitle", "")
    t = fauxcyr(title) if lang in FAUX else title
    nav = " ".join(f"<span>{n}</span>" if c == lang else f'<a href="{c}.html">{n}</a>' for c, n in LANGS)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} – Vostok</title>
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap">
<h1>{escape(t)}</h1>
<p>{escape(sub)}</p>
<nav class="lang">{nav} <a href="../">Vostok</a></nav>
</div></header>
<main class="wrap">
{body_html}
</main>
<footer class="wrap">Vostok · GPL-3.0 · <a href="https://github.com/g0rst/VostockFM-1">github.com/g0rst/VostockFM-1</a></footer>
</body>
</html>
"""


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "docs" / "handbuch"
    out.mkdir(parents=True, exist_ok=True)
    for lang, _ in LANGS:
        meta, body = front((ROOT / "handbuch" / f"{lang}.md").read_text(encoding="utf-8"))
        html = markdown.markdown(body, extensions=["tables"])
        html = re.sub(r"(?<![\"'>])(https?://[^\s<]+[^\s<.,;:)])", r'<a href="\1">\1</a>', html) \
            if "<a href" not in html else html
        if lang in FAUX:
            html = faux_tags(html)
        (out / f"{lang}.html").write_text(page(lang, meta, html), encoding="utf-8")
        print(f"handbuch: {out / (lang + '.html')}")
    (out / "index.html").write_text('<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=de.html">'
                                    '<a href="de.html">Handbuch</a>', encoding="utf-8")


if __name__ == "__main__":
    main()

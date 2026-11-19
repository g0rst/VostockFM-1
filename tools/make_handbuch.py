#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 g0rst
"""Vostok: the manual ("Handbuch für junge Kosmonauten") from handbuch/<lang>.md to docs/handbuch/<lang>.html.

  python3 tools/make_handbuch.py [OUTDIR]      (default docs/handbuch)

Three editions: de, en, ru. In de and en the title, the headings and the "Merke dir, Pionier" / "Remember, Pioneer"
labels are set in faux-Cyrillic (tools/faux_cyr.py, the firmware's own table); ru is the real thing, as written.
Needs the Python package markdown. The pages use docs/fonts (Neucha, Pangolin, PT Serif; OFL) and print on A4.
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

# the look: a booklet for young pioneers, around 1962, kept in a drawer for seventy years. Yellowed paper with foxing,
# two-colour print (red, blue) a little off register, hand-lettered headings (Neucha), the text in an old book face
# (PT Serif), the Merksaetze in a child's hand (Pangolin), a rocket on the cover. All OFL, in docs/fonts.
NOISE = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 .35 0 0 0 0 .25 0 0 0 0 .1 0 0 0 .22 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23n)'/></svg>")
CSS = """
@font-face{font-family:"Neucha";src:url(../fonts/Neucha.ttf) format("truetype")}
@font-face{font-family:"Pangolin";src:url(../fonts/Pangolin-Regular.ttf) format("truetype")}
@font-face{font-family:"PT Serif";src:url(../fonts/PT_Serif-Web-Regular.ttf) format("truetype");font-weight:400}
@font-face{font-family:"PT Serif";src:url(../fonts/PT_Serif-Web-Bold.ttf) format("truetype");font-weight:700}
@font-face{font-family:"PT Serif";src:url(../fonts/PT_Serif-Web-Italic.ttf) format("truetype");font-style:italic}
:root{--paper:#ecdcb4;--paper2:#e3cf9f;--red:#c3362b;--blue:#2f5f9e;--ink:#3a2a1c;--muted:#7a6448;--sun:#f2c14e}
*{box-sizing:border-box}
html{background:#5b4632}
body{margin:0;color:var(--ink);font:18px/1.62 "PT Serif",Georgia,serif;
  background:#5b4632 radial-gradient(circle at 50% 0,#6d553c,#4a3826 70%)}
.sheet{max-width:880px;margin:28px auto;position:relative;overflow:hidden;
  background:url("NOISE"),radial-gradient(ellipse at 18% 12%,rgba(150,95,30,.18) 0 3%,transparent 9%),
    radial-gradient(ellipse at 84% 38%,rgba(150,95,30,.14) 0 2%,transparent 7%),
    radial-gradient(ellipse at 30% 78%,rgba(150,95,30,.16) 0 2.5%,transparent 8%),
    radial-gradient(ellipse at 70% 92%,rgba(150,95,30,.12) 0 2%,transparent 6%),
    linear-gradient(var(--paper),var(--paper2));
  box-shadow:0 18px 40px rgba(0,0,0,.45),inset 0 0 90px rgba(120,80,30,.35);border-radius:3px 6px 4px 7px}
a{color:var(--blue)}
.wrap{padding:0 56px}
.cover{position:relative;padding:44px 56px 30px;border-bottom:4px double var(--ink);
  background:radial-gradient(rgba(195,54,43,.16) 1.4px,transparent 1.6px) 0 0/9px 9px}
.cover .maker{font:15px/1.3 "Neucha",cursive;letter-spacing:.12em;color:var(--blue);text-transform:uppercase}
.cover h1{font:400 clamp(2.6rem,7vw,4.4rem)/1 "Neucha",cursive;color:var(--red);margin:.25em 0 .1em;max-width:70%;
  text-shadow:3px 2px 0 rgba(47,95,158,.55);transform:rotate(-1.5deg)}
.cover .sub{font:italic 1.05rem "PT Serif",serif;max-width:62%}
.cover .rocket{position:absolute;right:46px;top:30px;width:190px;transform:rotate(14deg)}
.badges{display:flex;gap:12px;flex-wrap:wrap;margin-top:22px;align-items:center}
.badge{font:17px "Neucha",cursive;border:2px solid var(--ink);border-radius:999px;padding:2px 14px;background:var(--sun);
  transform:rotate(-2deg)}
.badge.price{background:var(--paper);border-style:dashed;transform:rotate(3deg)}
nav.lang{margin-top:18px;font:17px "Neucha",cursive}
nav.lang a,nav.lang span{margin-right:16px;color:var(--blue)}
nav.lang span{color:var(--red);border-bottom:2px wavy var(--red);text-decoration:underline wavy var(--red)}
main{counter-reset:ch;padding-top:6px}
main h1{counter-increment:ch;font:400 2.1rem/1.15 "Neucha",cursive;color:var(--ink);margin:2.1em 0 .55em;
  display:flex;align-items:center;gap:14px;text-shadow:2px 1px 0 rgba(195,54,43,.35)}
main h1::before{content:counter(ch);flex:none;width:52px;height:52px;border-radius:50%;background:var(--red);
  color:var(--paper);display:grid;place-items:center;font:2rem "Neucha",cursive;box-shadow:3px 3px 0 var(--blue);
  transform:rotate(-6deg)}
main h1::after{content:"";flex:1;height:0;border-top:3px dotted var(--ink);margin-left:6px;opacity:.6}
main h2{font:400 1.45rem "Neucha",cursive;color:var(--blue);margin:1.5em 0 .4em;
  text-decoration:underline wavy rgba(195,54,43,.6);text-underline-offset:6px}
main h2::before{content:"\\2605  ";color:var(--red)}
p{margin:.7em 0}
table{width:100%;border-collapse:separate;border-spacing:0;margin:1.1em 0;font-size:.93rem;
  border:2px solid var(--ink);border-radius:10px;overflow:hidden;background:rgba(255,248,226,.55)}
th,td{padding:7px 10px;text-align:left;vertical-align:top;border-bottom:1px solid rgba(58,42,28,.35)}
td+td,th+th{border-left:1px dashed rgba(58,42,28,.35)}
tr:last-child td{border-bottom:0}
th{background:var(--blue);color:var(--paper);font:400 1.05rem "Neucha",cursive;letter-spacing:.04em}
tr:nth-child(even) td{background:rgba(195,54,43,.06)}
blockquote{position:relative;margin:1.7em 18px;padding:16px 20px 16px 64px;background:#f8eccb;
  border:2.5px dashed var(--red);border-radius:16px;font:1.08rem/1.5 "Pangolin",cursive;transform:rotate(-1deg);
  box-shadow:4px 5px 0 rgba(47,95,158,.35)}
blockquote::before{content:"\\2605";position:absolute;left:16px;top:50%;margin-top:-22px;width:38px;height:38px;
  border-radius:50%;background:var(--sun);border:2px solid var(--ink);display:grid;place-items:center;
  color:var(--red);font:24px/1 sans-serif;transform:rotate(-12deg)}
blockquote p{margin:0}
blockquote strong{color:var(--red);font-weight:400;font-family:"Neucha",cursive;font-size:1.15rem}
ol{counter-reset:st;list-style:none;padding-left:0}
ol>li{counter-increment:st;position:relative;padding-left:46px;margin:.55em 0}
ol>li::before{content:counter(st);position:absolute;left:0;top:-1px;width:32px;height:32px;border-radius:50%;
  border:2px solid var(--blue);color:var(--blue);display:grid;place-items:center;font:1.2rem "Neucha",cursive;
  background:#f8eccb}
ul{padding-left:1.3em}
ul>li::marker{content:"\\2605  ";color:var(--red)}
code{font:.85em ui-monospace,monospace;background:rgba(255,248,226,.8);padding:1px 5px;border:1px solid rgba(58,42,28,.3);
  border-radius:4px}
hr{border:0;height:30px;margin:2.4em 0 .6em;background:center/auto 28px no-repeat
  url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 220 28'><path d='M10 20 Q110 -6 210 20' fill='none' stroke='%232f5f9e' stroke-width='2' stroke-dasharray='5 5'/><circle cx='110' cy='8' r='6' fill='%23c3362b'/><path d='M104 4 L92 0 M116 4 L128 0 M106 13 L96 20 M114 13 L124 20' stroke='%233a2a1c' stroke-width='1.6'/></svg>")}
audio{width:100%;min-width:180px;height:36px}
.screens{display:flex;flex-wrap:wrap;gap:22px;margin:1em 0}
figure.screen{margin:0;padding:10px 10px 6px;background:#f8eccb;border:2px solid var(--ink);border-radius:8px;
  box-shadow:4px 4px 0 rgba(47,95,158,.35);transform:rotate(-1.2deg)}
figure.screen:nth-child(2){transform:rotate(1deg)}
figure.screen img{display:block;width:220px;height:auto;image-rendering:pixelated;border:1px solid rgba(58,42,28,.4)}
figure.screen figcaption{font:15px "Pangolin",cursive;max-width:220px;margin-top:4px}
.colophon{font:15px/1.45 "PT Serif",serif;color:var(--muted);padding:6px 56px 40px}
.colophon .stamp{display:inline-block;margin-top:10px;font:16px "Neucha",cursive;color:var(--red);border:2px solid var(--red);
  padding:2px 10px;border-radius:6px;transform:rotate(-4deg);opacity:.8}
@media (max-width:640px){.wrap,.cover,.colophon{padding-left:20px;padding-right:20px}.cover h1,.cover .sub{max-width:100%}
  .cover .rocket{position:static;width:110px;float:right;margin:0 0 6px 8px}}
@media print{html,body{background:#fff}.sheet{box-shadow:none;margin:0;max-width:none}nav.lang{display:none}
  main h1{page-break-before:always}}
""".replace("NOISE", NOISE)

ROCKET = """<svg class="rocket" viewBox="0 0 120 200" aria-hidden="true">
<g stroke="#3a2a1c" stroke-width="3" stroke-linejoin="round">
<path d="M60 8 C84 38 88 92 84 140 L36 140 C32 92 36 38 60 8Z" fill="#f8eccb"/>
<path d="M60 8 C70 20 76 34 79 50 L41 50 C44 34 50 20 60 8Z" fill="#c3362b"/>
<circle cx="60" cy="80" r="13" fill="#2f5f9e"/><circle cx="60" cy="80" r="6" fill="#f8eccb" stroke-width="2"/>
<path d="M36 112 L14 152 L38 144Z M84 112 L106 152 L82 144Z" fill="#c3362b"/>
<path d="M46 140 L60 192 L74 140Z" fill="#f2c14e"/><path d="M53 140 L60 168 L67 140Z" fill="#c3362b" stroke-width="2"/>
</g><g fill="#2f5f9e"><circle cx="12" cy="40" r="3"/><circle cx="104" cy="22" r="2.5"/><circle cx="110" cy="96" r="3"/>
<circle cx="8" cy="110" r="2"/></g></svg>"""

COVER = {   # the maker (made up), the edition and the price of the booklet
    "de": ("VEB Karl-Marx-Stadt Harmonikawerke", "Ausgabe 1", "Preis 85 Pfennig", "Für Jungpioniere ab 8 Jahren",
           "Geprüft und für gut befunden", "Alle Firmen, Werke und Preise in diesem Heft sind erfunden."),
    "en": ("VEB Karl-Marx-Stadt Harmonikawerke", "Edition 1", "Price 85 pfennigs", "For young pioneers aged 8 and up",
           "Tested and found good", "All firms, works and prices in this booklet are made up."),
    "ru": ("ВЭБ «Карл-Маркс-Штадт Гармоникаверке»", "Выпуск 1", "Цена 85 пфеннигов", "Для октябрят и пионеров от 8 лет",
           "Проверено. Одобрено", "Все предприятия, заводы и цены в этой брошюре выдуманы."),
}


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
    maker, ed, price, age, stamp, note = COVER[lang]
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
<div class="sheet">
<header class="cover">
{ROCKET}
<div class="maker">{escape(maker)}</div>
<h1>{escape(t)}</h1>
<p class="sub">{escape(sub)}</p>
<div class="badges"><span class="badge">{escape(age)}</span><span class="badge price">{escape(ed)} · {escape(price)}</span></div>
<nav class="lang">{nav} <a href="../">Vostok</a></nav>
</header>
<main class="wrap">
{body_html}
</main>
<footer class="colophon">{escape(note)} Vostok · GPL-3.0 ·
<a href="https://github.com/g0rst/VostockFM-1">github.com/g0rst/VostockFM-1</a><br><span class="stamp">{escape(stamp)}</span></footer>
</div>
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

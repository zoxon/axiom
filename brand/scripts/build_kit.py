#!/usr/bin/env python3
"""Slate kit for the two Axiom marks (L1, N4): ink, white, black, favicon, tile. Standard library only."""
import re
from pathlib import Path

D = Path(__file__).parent
INK, PALE, GROUND = '#0f172a', '#f1f5f9', '#0f172a'   # slate-900, slate-100, slate-900
MARKS = {'l1': 'concept-l1-delta-crossbar.svg', 'n4': 'concept-n4-geometric-delta-cap.svg'}


def body(name):
  return re.search(r'<svg[^>]*>(.*)</svg>', (D / name).read_text(), re.S).group(1)


def wrap(inner, size='0 0 256 256'):
  return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{size}">{inner}</svg>\n'


for key, src in MARKS.items():
  out = D / 'kit' / key
  out.mkdir(parents=True, exist_ok=True)
  b = re.sub(r'<title>.*?</title>', '', body(src))
  paint = lambda c: b.replace('#000', c)
  (out / 'symbol-ink.svg').write_text(wrap(f'<title>Axiom</title>{paint(INK)}'))
  (out / 'symbol-white.svg').write_text(wrap(f'<title>Axiom</title>{paint("#ffffff")}'))
  (out / 'symbol-black.svg').write_text(wrap(f'<title>Axiom</title>{paint("#000000")}'))
  # Favicon: transparent, dark ink on light tabs and pale ink on dark tabs.
  # The rules use #fav so they do not leak into a page that inlines the file.
  fav = (f'<style>#fav path{{fill:{INK}}}@media (prefers-color-scheme:dark){{#fav path{{fill:{PALE}}}}}</style>'
         f'<title>Axiom</title>{b}')
  (out / 'favicon.svg').write_text(wrap(fav).replace('<svg ', '<svg id="fav" ', 1))
  (out / 'symbol-pale.svg').write_text(wrap(f'<title>Axiom</title>{paint(PALE)}'))
  # App icon: a full square, no rounded corners (the platform rounds it), pale mark at 62 percent.
  tile = (f'<title>Axiom</title><rect width="256" height="256" fill="{GROUND}"/>'
          f'<g transform="translate(48.6 48.6) scale(.62)">{paint(PALE)}</g>')
  (out / 'app-icon.svg').write_text(wrap(tile))
  print('kit', key)

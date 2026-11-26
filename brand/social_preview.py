#!/usr/bin/env python3
"""Build the GitHub social preview: social-preview.svg and social-preview.png (1280 x 640). Standard library only.

Usage: python3 social_preview.py [--name claude-box] [--tagline1 "..."] [--tagline2 "..."]

The SVG is the source. The PNG is rendered with headless Chrome or Chromium, so that the text uses the system font.
GitHub wants a PNG, JPG or GIF under 1 MB, 1280 x 640 px. Upload it by hand: Settings, General, Social preview.
Keep text and the mark inside the central 80% of the image: other sites crop the edges.
"""
import argparse
import re
import shutil
import subprocess
from html import escape
from pathlib import Path

HERE = Path(__file__).parent
FONTS = '-apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif'
GROUND, NAME, TAGLINE, ACCENT = '#0f172a', '#f1f5f9', '#94a3b8', '#94a3b8'   # slate-900, slate-100, slate-400 (palette.css)
CHROME = ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', 'google-chrome', 'chromium', 'chromium-browser']


def main() -> None:
  parser = argparse.ArgumentParser()
  parser.add_argument('--name', default='Axiom')
  parser.add_argument('--tagline1', default='Portable design tokens and rules')
  parser.add_argument('--tagline2', default='for design systems and agents.')
  parser.add_argument('--mark', default=str(HERE / 'svg' / 'symbol-pale.svg'))
  a = parser.parse_args()

  mark = Path(a.mark).read_text(encoding='utf-8')
  if '<!DOCTYPE' in mark or '<!ENTITY' in mark or '<script' in mark.lower():
    raise SystemExit('Unsafe SVG')
  inner = re.sub(r'<title>.*?</title>', '', re.search(r'<svg\b[^>]*>(.*)</svg>', mark, flags=re.S).group(1), flags=re.S)

  size = 280                                  # the mark, in px
  left, top = 110, (640 - size) // 2          # inside the central 80%: x from 128 would be the strict edge
  text_x = left + size + 70
  svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640" width="1280" height="640" role="img">'
    f'<title>{escape(a.name)}: {escape(a.tagline1)} {escape(a.tagline2)}</title>'
    f'<rect width="1280" height="640" fill="{GROUND}"/>'
    f'<g transform="translate({left} {top}) scale({size / 256:.5f})">{inner}</g>'
    f'<text x="{text_x}" y="300" font-family="{FONTS}" font-size="104" font-weight="700" fill="{NAME}">{escape(a.name)}</text>'
    f'<rect x="{text_x}" y="334" width="112" height="12" rx="6" fill="{ACCENT}"/>'
    f'<text x="{text_x}" y="412" font-family="{FONTS}" font-size="40" fill="{TAGLINE}">{escape(a.tagline1)}</text>'
    f'<text x="{text_x}" y="466" font-family="{FONTS}" font-size="40" fill="{TAGLINE}">{escape(a.tagline2)}</text>'
    '</svg>\n')
  out_svg, out_png = HERE / 'social-preview.svg', HERE / 'social-preview.png'
  out_svg.write_text(svg, encoding='utf-8')
  print('wrote', out_svg.name)

  chrome = next((c for c in CHROME if Path(c).exists() or shutil.which(c)), None)
  if not chrome:
    print('Chrome or Chromium not found: render social-preview.svg to a 1280 x 640 PNG yourself.')
    return
  subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1280,640',
                  f'--screenshot={out_png}', f'file://{out_svg}'], check=True, capture_output=True)
  print('wrote', out_png.name, f'({out_png.stat().st_size // 1024} KB)')


if __name__ == '__main__':
  main()

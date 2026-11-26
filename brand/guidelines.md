# Axiom logo guidelines

The logo is a geometric delta. It has one thick stroke, one thin stroke and a triangle window.
The delta stands for the Greek letter, and for the sign of a definition that needs no proof.

## Colours

All colours come from `src/tokens/palette.css`. Use the token, not a copy of the hex value.

| Use | Ground | Mark colour | Token |
|---|---|---|---|
| Default | Light | `#0f172a` | `--color-slate-900` |
| Default | Dark | `#f1f5f9` | `--color-slate-100` |
| App icon, avatar | `#0f172a` tile | `#f1f5f9` | `--color-slate-900`, `--color-slate-100` |
| One colour, print | White | `#000000` | none |
| One colour, on a photo | Any | `#ffffff` | `--color-white` |

Contrast: slate-900 on white is 17.9:1. slate-100 on slate-900 is 16.3:1. Both pass 3:1 with a wide margin.

## Files

| File | Use |
|---|---|
| `svg/symbol-ink.svg` | Light grounds. |
| `svg/symbol-pale.svg` | Dark grounds. |
| `svg/symbol-white.svg`, `svg/symbol-black.svg` | One colour on photos, print. |
| `svg/favicon.svg`, `favicon.ico` | Browser tab. Transparent. The SVG follows the browser theme. |
| `svg/app-icon.svg` | Full square tile. The platform rounds the corners. |
| `svg/app-icon-rounded.svg` | Tile with rounded corners, for the README header. |
| `png/avatar-512.png` | GitHub avatar. |

## Size and clear space

- Smallest size: 16 px. Below 16 px, use the favicon file as it is.
- Clear space: keep free space of one quarter of the mark width on every side.
- The favicon has no tile. The app icon always has the tile.

## Do not

- Do not rotate, mirror or slant the mark. The mark has no meaning when turned.
- Do not round the corners of the mark. Sharp corners are part of the shape.
- Do not change the stroke widths. The thin stroke needs 18 units, the thick stroke needs 38 units.
- Do not add a gradient, a shadow or an outline.
- Do not use a mark colour that is not in the table above.
- Do not put the name in a font and call it a wordmark. The logo has no wordmark.

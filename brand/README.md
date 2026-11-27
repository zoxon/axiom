# Axiom brand

The logo of Axiom: a geometric delta. An axiom is a statement that needs no proof, and the delta is the sign of a definition.
Use `guidelines.md` for the rules. Use this file to find the files and to understand the choices.

## What is here

| Path | What it is |
|---|---|
| `svg/` | The logo files: ink, pale, white, black, favicon, app icon. |
| `png/` | PNG exports: avatar 512, transparent symbol in 16 to 1024 px. |
| `favicon.ico` | Transparent icon with 16, 32 and 48 px. |
| `readme-header-light.svg`, `readme-header-dark.svg` | The README header, one file for each GitHub theme. |
| `social-preview.png`, `social-preview.svg` | The GitHub social preview, 1280 x 640 px. The SVG is the source. Upload the PNG by hand. |
| `social_preview.py` | Builds the social preview. It needs Python 3 and Chrome. |
| `guidelines.md` | Usage rules. |
| `preview.html` | The logo in real contexts. Open it in a browser. |

## Quick use

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="brand/readme-header-dark.svg">
  <img src="brand/readme-header-light.svg" width="520" alt="Axiom: portable design tokens and rules">
</picture>
```

GitHub removes style attributes from README HTML, so the header is an image. An SVG image keeps its own styles.

## Social preview and avatar

GitHub does not read these from git. Upload them by hand: Settings, General, Social preview (`social-preview.png`). Upload `png/avatar-512.png` as the avatar of the account or organization.

## Update (2026-11-27): line weight

A check of the line weight against the other zoxon logos showed that the lines of the delta were too thin (11 percent of the mark box, against about 20 percent for the others).
The thin branch and the floor are 28 units now (they were 18 and 20). The thick stroke is the same (38). The construction and the silhouette are the same.
All files are rebuilt with the new path. `scripts/build_concepts_11.py` holds the values.

## Decisions (2026-11-26)

**Chosen:** N4, a geometric delta with a flat stroke end, in slate (`slate-900` and `slate-100` from the project palette).

**Why this mark:** it keeps the silhouette of a triangle, the most stable shape. It is the Greek capital delta, and the delta over an equals sign means "equal by definition".
It reads at 16 px better than the letter versions.

**Not chosen, and why:**

| Concept | Reason |
|---|---|
| Unit on a base, cornerstone, three points | Too general. Blocks, a pedestal or the "therefore" sign. |
| Square A | Reads as a house. |
| Keystone | The meaning is the top of the arch, not the base. It looks like a horseshoe at 16 px. |
| Right angle (set square) | Clean, but it is the icon of rulers and drawing tools. |
| Compass A | The compass is a common idea, and the needle is a hair at 16 px. |
| Delta over an equals sign | Close to the maths sign, but the two lines merge at 16 px. |
| L1, delta with a crossbar | Reads as the letter A. The thin crossbar is weak at 16 px. Kept as the letter version. |
| Handwritten forms | They lose the stable silhouette. A hook and a bowl read as other signs. |
| Colours blue, green, amber | Blue is the most common colour in the category. Green and amber mean success and warning in the tokens. |

## Open checks

- Search for similar marks before public use. The delta and the letter A are common in logos.
- "Axiom" is a common name. Check the trademark separately.
- The mark has no small-size cut. Check the favicon at 16 px in a real browser tab, light and dark.
- The mirror and 180-degree reading is a plain arrow shape, with no meaning. The mark must not be turned.
- Not tested: colour-blind view, the white version on photos, print.
- The meaning "equal by definition" is from memory. Check it against a source before you write it in public text.

## Rebuild

The scripts are in the `design` plugin (`design-logo`, `design-web-assets`) and in `scripts/build_concepts_11.py` (the mark) and `scripts/build_kit.py` (the kit).

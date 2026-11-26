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

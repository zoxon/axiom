# Architecture Rules — Design Tokens System

## 1. Three-layer model

The system has exactly three layers. Each layer has a strict role.

### 1.1 Palette Layer
- Contains raw color values only
- Token names: `--color-{name}` or `--color-{name}-{variant}`
- Never referenced in UI code directly
- Only referenced by the semantic layer
- Located in the token source, commonly `src/tokens/palette.css`

### 1.2 Semantic Layer (primary system)
- Defines UI meaning and behavior
- Token names: `--{category}-{role}[-{state}]`
- UI code must only use semantic tokens, never palette tokens
- Located in the token source, commonly `src/tokens/colors.css`

Semantic categories:
- `fill` → surfaces, backgrounds, interactive fills
- `text` → all typography colors
- `border` → stroke system
- `elevation` → shadow system

### 1.3 Component Layer (optional, not in files)
- Aliases of semantic tokens only
- Contains no logic, no new values, no palette references
- Lives inside individual component files — not in the global token files
- Must only reference semantic tokens

---

## 2. Theme variants

Theme switching is optional and is not part of the design-system contract. A product can use `data-theme`, media queries, scoped CSS, build-time themes, or no theme switching at all.

If theme variants exist, they override semantic tokens. Layout primitives (spacing, typography, radius, z-index) are theme-agnostic.

### 2.1 File structure
- `tokens.css` — package entrypoint
- `src/tokens/index.css` — canonical token entrypoint
- `src/tokens/palette.css` — raw palette values
- `src/tokens/colors.css` — semantic color tokens and optional theme variants
- `src/tokens/typography.css`, `spacing.css`, `radius.css`, `shadows.css`, `z-index.css` — theme-agnostic tokens unless the project explicitly chooses otherwise

### 2.2 Theme completeness rule
Only applies when a project defines theme variants. Every semantic token overridden in one variant should be intentionally handled in the other variants.

Tokens normally exempt from theme overrides:
- `--font-*` (font families)
- `--font-size-*`
- `--line-height-*`
- `--space-*`
- `--border-radius-*`
- `--z-index-*`
- `--breakpoint-*`
- `--transition-*`
- `--header-height*`

### 2.3 Valid theme mechanisms
All of these are acceptable because the mechanism is product-owned:

```css
[data-theme='dark'] {
  --fill-background: var(--color-slate-900);
}

@media (prefers-color-scheme: dark) {
  :root {
    --fill-background: var(--color-slate-900);
  }
}
```

---

## 3. Interaction model

The system has two distinct interaction patterns. They must not be mixed without explicit justification.

### 3.1 Text-based interactions
Used for: links, inline actions, metadata actions, anchor text.
Token: `--text-interactive` and its states.

### 3.2 Fill-based interactions
Used for: buttons, toggles, controls, interactive surface backgrounds.
Token: `--fill-interactive` and its states.

---

## 4. State system

All interactive states must be explicit. Computed or implicit states are not allowed.

Required states for interactive tokens:
| State | Description |
|-------|-------------|
| `default` | base token (no suffix) |
| `hover` | cursor over element |
| `active` / `pressed` | element is being activated |
| `focus` | keyboard/programmatic focus |
| `disabled` | element is non-interactive |

State completeness rule: if any non-default state exists for a token, all states in the set must exist.

---

## 5. Surface model

Exactly three surface levels. No more without architectural review.

| Token | Usage |
|-------|-------|
| `--fill-background` | App canvas, page background |
| `--fill-surface` | Cards, containers, panels |
| `--fill-elevated` | Modals, overlays, popovers |
| `--fill-overlay` | Backdrop overlays (semi-transparent) |

---

## 6. System colors

System colors are strictly semantic — functional feedback only.

| Color | Allowed usage |
|-------|---------------|
| `success` | Success states, confirmation feedback |
| `warning` | Warnings, caution states |
| `danger` | Errors, destructive actions, failure states |
| `info` | Informational states |

Forbidden: decorative usage, brand accents, UI styling without semantic meaning.

---

## 7. Typography system

Typography is role-based, not value-based. Direct px/rem values in UI code are forbidden.

### 7.1 Font roles
- `--font-primary` → body text, default content
- `--font-secondary` → headings, emphasis (must not be used for body content)
- `--font-mono` → code, monospace content

### 7.2 Font size roles (current system — 10 roles)
| Token | Approx size | Usage |
|-------|-------------|-------|
| `--font-size-caption` | 12px | Metadata, hints, timestamps |
| `--font-size-body` | 14px | Default content |
| `--font-size-body-lg` | 16px | Emphasized body |
| `--font-size-label` | 18px | Logo label, aside headings, small titles |
| `--font-size-title` | 20px | Section-level headings |
| `--font-size-subheading` | 22px | Card titles, lead body |
| `--font-size-heading` | 24px | Page-level headings |
| `--font-size-content-heading` | 28px | Article h1 |
| `--font-size-display` | 32px | Hero/marketing text |
| `--font-size-hero` | 48px | Hero h1 on desktop |

New size roles are allowed when they have clear semantic meaning and a distinct UI role not covered by existing tokens. Never add numeric sizes (`--font-size-13`, `--font-size-22px`) — only semantic roles with names that describe their purpose.

### 7.3 Line height roles
- `--line-height-tight` (1.2) → headings, display text
- `--line-height-normal` (1.5) → body content
- `--line-height-relaxed` (1.7) → captions, metadata

### 7.4 Typography pairing matrix

| Role | Font | Size | Line height |
|------|------|------|-------------|
| Caption | primary | caption | relaxed |
| Body | primary | body | normal |
| Body Large | primary | body-lg | normal |
| Label | secondary | label | tight |
| Title | secondary | title | tight |
| Subheading | secondary | subheading | tight |
| Heading | secondary | heading | tight |
| Content Heading | secondary | content-heading | tight |
| Display | secondary | display | tight |
| Hero | secondary | hero | tight |

Typography is theme-agnostic. Theme variants may affect color and contrast, but should not change font size, line height, or font family.

---

## 8. Spacing system

Compact scale with fractional values for fine control. The scale is defined in the token source.

Valid spacing values are the tokens defined in `--space-*`. New values require architectural justification — no ad-hoc numeric additions.

Naming: `--space-{n}` where n is a numeric suffix matching the scale (e.g., `--space-4` = 1rem).

---

## 9. Design decision rules

### When adding tokens
- Reuse existing semantic tokens wherever possible
- Prefer extension over creation
- Preserve naming consistency with existing tokens
- Check for value/intent duplication before creating

### When removing tokens
- Always grep for usages first
- Provide a migration path (replacement token or explicit removal with reason)
- Update documentation

### Never do
- Use `--color-*` palette tokens directly in UI files
- Create two tokens with overlapping semantic meaning
- Break role-based structure (e.g., `--text-size-13`, `--blue-button-bg`)
- Add raw hex values to semantic layer without palette equivalent
- If theme variants exist, leave semantic overrides inconsistent across variants

---

## 10. Compatibility requirements

Every new token must satisfy all four checks:

1. **Semantic clarity** — the name alone communicates what it means in the UI
2. **Layer correctness** — palette in palette, semantic in semantic
3. **No duplication** — no existing token serves the same purpose
4. **Theme-agnostic behavior** — layout tokens do not vary by theme

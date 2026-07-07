# Token Conventions

## Naming pattern

```css
--{category}-{role}[-{state}]
```

Every token name must be readable without seeing its value. The name is the contract.

---

## Categories

| Category | Layer | Usage | Example |
|----------|-------|-------|---------|
| `color` | Palette | Raw color values only | `--color-blue`, `--color-gray-500` |
| `fill` | Semantic | Backgrounds, surfaces, interactive fills | `--fill-background`, `--fill-interactive` |
| `text` | Semantic | Typography colors | `--text-primary`, `--text-muted` |
| `border` | Semantic | Stroke colors | `--border-base`, `--border-interactive` |
| `elevation` | Semantic | Shadow values | `--elevation-1`, `--elevation-4` |
| `font` | Layout | Font family roles | `--font-primary`, `--font-mono` |
| `font-size` | Layout | Typography scale | `--font-size-body`, `--font-size-heading` |
| `line-height` | Layout | Line height scale | `--line-height-tight`, `--line-height-normal` |
| `space` | Layout | Spacing scale | `--space-4`, `--space-12` |
| `border-radius` | Layout | Radius scale | `--border-radius-sm`, `--border-radius-full` |
| `z-index` | Layout | Stacking order | `--z-index-modal`, `--z-index-dropdown` |
| `breakpoint` | Layout | Responsive breakpoints | `--breakpoint-md`, `--breakpoint-xl` |
| `transition` | Layout | Animation easing | `--transition-default` |

---

## State suffixes

Appended to interactive tokens. All states in the set must exist if any one of them exists.

| Suffix | When | Example |
|--------|------|---------|
| *(none)* | Default state | `--fill-interactive` |
| `-hover` | Cursor over element | `--fill-interactive-hover` |
| `-active` or `-pressed` | Being activated | `--fill-interactive-active` |
| `-focus` | Keyboard/programmatic focus | `--fill-interactive-focus` |
| `-disabled` | Non-interactive | `--fill-interactive-disabled` |

---

## Palette naming patterns

```css
--color-{name}              /* single value: --color-white, --color-black */
--color-{name}-{variant}    /* dark/light variant: --color-blue-dark */
--color-{name}-{step}       /* scale step: --color-gray-100, --color-gray-900 */
```

Scale steps follow conventional increments: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900.

---

## Semantic naming patterns

### Surfaces (3 levels max)
```css
--fill-background   /* page canvas */
--fill-surface      /* cards, containers */
--fill-elevated     /* modals, overlays */
--fill-overlay      /* semi-transparent backdrop */
```

### Text roles
```css
--text-primary      /* main content */
--text-secondary    /* supporting content */
--text-muted        /* de-emphasized content */
--text-disabled     /* non-interactive */
--text-interactive  /* links, inline actions */
--text-{state}      /* system: success, warning, danger, info */
```

### Border roles
```css
--border-base         /* default strokes */
--border-strong       /* emphasized strokes */
--border-interactive  /* focused/active borders */
--border-{state}      /* system: success, warning, danger */
```

### System colors pattern
```css
--{category}-success  /* confirmation, positive feedback */
--{category}-warning  /* caution, non-critical issue */
--{category}-danger   /* error, destructive, critical */
--{category}-info     /* informational, neutral notice */
```
Where `{category}` is `fill`, `text`, or `border`.

---

## Typography naming patterns

Font roles (semantic, not family names):
```css
--font-primary    /* body text, default content */
--font-secondary  /* headings, emphasis */
--font-mono       /* code, monospace */
```

Font size roles (semantic, not values):
```css
--font-size-caption   /* smallest: hints, timestamps, metadata */
--font-size-body      /* default content text */
--font-size-body-lg   /* emphasized body */
--font-size-title     /* section headings */
--font-size-heading   /* page headings */
--font-size-display   /* hero, marketing */
```

New roles can be added when a UI need arises that isn't covered by existing roles. Never use numeric sizes (`--font-size-13`) — only semantic names.

Line height roles:
```css
--line-height-tight    /* headings, display */
--line-height-normal   /* body text */
--line-height-relaxed  /* captions, metadata */
```

---

## Layout naming patterns

### Spacing
```css
--space-{n}   /* where n is a numeric scale value */
/* e.g.: --space-1 (0.25rem), --space-4 (1rem), --space-8 (2rem) */
```

Common scale steps: 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 64.

### Radius
```css
--border-radius-sm    /* small: inputs, tags */
--border-radius-md    /* medium: buttons, cards */
--border-radius-lg    /* large: modals, panels */
--border-radius-full  /* pill/circle */
```

### Z-index
```css
/* Numeric levels for compositing within a layer */
--z-index-0 through --z-index-5

/* Named levels for specific UI roles */
--z-index-dropdown   /* 1000+ */
--z-index-sticky
--z-index-fixed
--z-index-backdrop
--z-index-modal
--z-index-tooltip
--z-index-max        /* 9999, emergency escape hatch */
```

---

## Anti-patterns

| Anti-pattern | Why wrong | Correct |
|-------------|-----------|---------|
| `--blue-button-bg` | Role + element mixed, not semantic | `--fill-interactive` |
| `--font-size-13` | Numeric, not semantic | `--font-size-caption` |
| `--color-blue` in a component | Palette in UI | `--fill-interactive` or `--text-interactive` |
| `--button-primary-hover-bg` | Too specific, breaks abstraction | `--fill-interactive-hover` |
| `--space-7.5` | Fractional ad-hoc value | Use nearest scale step |
| Two tokens, same value, same meaning | Duplication | Merge to one token |
| `--text-gray` | Describes value, not meaning | `--text-muted` or `--text-secondary` |

---

## Common issues to check during audit

1. **Raw values in semantic layer** — `--text-primary: #1d1d1f` instead of `--text-primary: var(--color-gray-900)`. Flag as warning: works but breaks the palette→semantic mapping, making bulk color changes harder.

2. **Incomplete state sets** — `--fill-interactive-hover` exists but `--fill-interactive-focus` or `--fill-interactive-disabled` is missing. Flag as warning: breaks state consistency.

3. **Theme asymmetry** — token defined in light theme but absent from dark (or vice versa). Flag as violation: causes visual bugs in the missing theme.

4. **Orphaned documentation** — token documented but not in files, or in files but not documented. Flag as warning: causes confusion when extending the system.

5. **System colors used decoratively** — `--text-success` used for a green accent unrelated to a success state. Flag as violation: breaks semantic contract.

6. **Layer leakage** — `--color-blue` used directly in a component file. Flag as violation: bypasses the semantic layer entirely.

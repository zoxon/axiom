---
name: design-tokens
description: Design token system engineer for CSS custom properties. ALWAYS use this skill when user mentions any of: design tokens, tokens, color tokens, semantic tokens, extend tokens, refactor tokens, typography tokens, spacing tokens, wants to modify token files, asks about CSS variables in a design context, or asks whether a token exists or can be used. Use this skill proactively — if the user is working with any UI styling and mentions colors, typography, spacing, surfaces, or interactive states, offer to use this skill. Don't wait for explicit design-system keywords.
---

# Design Tokens System Engineer

You are a Design Tokens System Engineer. Your job is to analyze, extend, refactor, and create design token systems while strictly preserving the semantic contract between UI intent and visual representation.

## File discovery

Before any action, locate the project's token files. Common patterns:

- `tokens.css`, `design-tokens.css`, `variables.css`, `_tokens.scss`
- `tokens.json`, `tokens.js`, `design-tokens.json`
- Directories: `tokens/`, `design-system/`, `theme/`, `styles/tokens/`
- Also look for optional theme files or selectors: `themes.css`, `theme.css`, `dark.css`, `[data-theme]`, `prefers-color-scheme`
- And documentation: `design-tokens.md`, `tokens.md`, `TOKENS.md`

If files aren't obvious, ask: "Where are your design tokens defined?" before proceeding.

For full architecture rules, read `references/architecture-rules.md`.
For naming conventions, read `references/token-conventions.md`.

---

## Axiom package mode

If the project uses `@zoxon/axiom`, treat Axiom as the source of rules and optional token defaults.

First determine how it is used:
- Package consumer: imports `@zoxon/axiom/tokens.css` or `@zoxon/axiom/src/tokens/*`.
- Local source: has `packages/axiom/` in the repository.
- Rule-only: copied `skills/design-tokens/` or references Axiom docs but owns its own tokens.

Then determine the target scope:
- Existing project/site: edit that project's own token files and usages, e.g. root `src/tokens/`.
- Axiom package: edit `packages/axiom/src/tokens/` and package docs/examples.
- Mixed monorepo: do not assume `packages/axiom/` is the target; follow the user's requested scope.

Rules:
- For package consumers, do not edit files inside `node_modules/@zoxon/axiom`; create local overrides after the Axiom import.
- For local source, edit canonical files in `packages/axiom/src/tokens/`; keep `tokens.css` as the entrypoint.
- For existing project/site work in a repo that also contains `packages/axiom/`, use the project token files as the target unless the user explicitly asks to change Axiom itself.
- For rule-only projects, apply the architecture rules to the project's own token files.
- Theme switching is product-owned. If themes exist, override semantic tokens only.
- When overriding a stateful token family, show the complete family in the proposal. Do not show partial examples that omit required states.

---

## Language

Respond in the language the user writes in. If the user's message is in Russian, reply in Russian. If in English, reply in English. Apply this to all reports, questions, and confirmations. Code, token names, and CSS values are always in English regardless of language.

---

## Command routing

Determine user intent and follow the matching workflow:

| Command | User says | Action |
|---------|-----------|--------|
| `analyze` | "check tokens", "audit", "what's wrong", "analyze tokens" | Audit → report → recommendations |
| `extend` | "add token", "need X", "extend", "I need a style for Y" | Clarify → validate → apply |
| `refactor` | "rename", "restructure", "remove token", "refactor" | Impact map → confirm → apply |
| `create` | "create system", "new project", "from scratch", "create from scratch" | Interview → plan → implement |

---

## ANALYZE

Perform a systematic audit and produce a structured report.

**Steps:**

1. Locate and read token file(s) and documentation (if present)
2. Run audit against rules in `references/architecture-rules.md`:
   - **Violations** (must fix):
     - Semantic tokens (`--fill-*`, `--text-*`, `--border-*`) referencing palette tokens from another semantic token
     - Layer leakage: palette token used directly in component or UI file
     - Naming violations: tokens not following `--{category}-{role}[-{state}]` pattern
     - Theme incompleteness: if theme variants exist, semantic token overridden in one variant but missing from another
   - **Warnings** (should fix):
     - Semantic tokens using raw values (hex, rgb) without a palette equivalent — reduces maintainability but doesn't break behavior
     - State gaps: interactive token has `hover` but missing `focus` or `disabled`
     - Redundancy: two tokens with identical or overlapping semantic meaning
     - Documentation drift: token in file but not in docs, or documented but absent from file

**Output format:**

```
## Audit Report — Design Tokens

### Violations (must fix)
- `--token-name`: [rule broken] → [how to fix]

### Warnings (should fix)
- `--token-name`: [issue] → [suggested fix]

### Documentation drift
- In file but undocumented: [list]
- Documented but missing from file: [list]

### Recommendations
- [specific, actionable suggestion with example]
```

If no issues found in a category, write "None."

---

## EXTEND

Add one or more tokens to the system.

**Steps:**

1. Ask clarifying questions before touching any file:
   - What semantic meaning does this token represent? (what UI element or state needs it)
   - Is it theme-sensitive? (does the project have theme variants that need different values)
   - Does it need interactive states (hover, focus, active, disabled)?
   - Which layer: palette (new color) or semantic (new meaning for existing color)?

2. Check for conflicts — read current tokens and look for:
   - Existing token with same meaning
   - Naming collision
   - Value duplication (same value already assigned to another semantic token)

3. Propose the change with full context:
   ```css
   /* add to [section name] in [filename] */
   --text-info: var(--color-blue);  /* informational inline text */
   ```
   If theme-sensitive, show the change for each theme too.
   If stateful, show the complete state family: default, hover, active/pressed, focus, disabled.

4. Wait for confirmation. Apply on "go" / "confirm" / "yes" or equivalent in the user's language.

5. Output mapping impact analysis (see Output Format section).

---

## REFACTOR

Rename, restructure, or remove tokens across the system.

**Steps:**

1. Understand the full scope: what changes, why, and what the target state looks like.

2. Run grep to find all usages before making any change:
   ```bash
   grep -rn "--token-name" src/ --include="*.css" --include="*.scss" --include="*.ts" --include="*.vue" --include="*.astro" --include="*.jsx" --include="*.tsx"
   ```
   Adapt file extensions to the project's stack.

3. Build the impact map and show it explicitly:
   ```
   ## Refactor Plan

   ### Token changes
   - `--old-name` → `--new-name` (reason: ...)
   - `--removed-token` REMOVED → migrate to `--replacement`

   ### Files affected
   - tokens.css — definition
   - theme selector/file — optional semantic overrides
   - src/components/Button.vue:12 — usage
   - src/components/Link.tsx:8 — usage
   ```

4. Wait for explicit confirmation before writing any file. If the user wants corrections, update the plan and ask again.

5. Apply all changes atomically: token definitions → theme overrides → all usages. Never leave the system in a partial state.

6. Output final mapping impact analysis.

---

## CREATE

Generate a complete token system from scratch for a new project.

**Steps:**

1. Interview — ask all questions before writing anything:
   - What is the project type and brand personality?
   - Primary and accent colors? (hex values or "suggest based on brand")
   - Theme variants required? (none, dark mode, brand themes, system media query, etc.)
   - Typography: system fonts or custom? Any preferences?
   - Scale scope: minimal (colors + type only) or full (spacing, radius, z-index, breakpoints)?
   - Any existing design decisions to preserve?
   - What format? (CSS custom properties, SCSS variables, JSON, JS object)
   - Theme mechanism, if any? (`data-theme`, media query, scoped CSS, build-time themes, etc.)

2. Generate a written plan — show structure before writing anything:
   ```
   ## Token System Plan

   Format: CSS custom properties
   Palette: [N] grays + [N] accent colors + system colors
   Semantic: surfaces (3), text (5), borders (3), interactive (5 states), system (success/warning/danger/info)
   Typography: 3 font roles, [N] size roles, 3 line-height roles
   Layout: spacing scale, radius (3), z-index levels, breakpoints
   Themes: [none or variants] via [mechanism]
   ```

3. Wait for confirmation or corrections. Adjust plan if needed.

4. Generate complete file(s) following the plan.

5. Output mapping impact analysis for the full new system.

---

## Architecture rules (critical, inline)

Full rules in `references/architecture-rules.md`. These are the invariants:

**Layer contract**
- Palette (`--color-*`) → raw values only, never referenced directly in UI
- Semantic (`--fill-*`, `--text-*`, `--border-*`, `--elevation-*`) → UI always uses these
- Theme variants are optional. If present, overrides change semantic tokens only, never palette or layout tokens.

**Naming pattern**
`--{category}-{role}[-{state}]`

Valid categories: `fill`, `text`, `border`, `elevation`, `font`, `font-size`, `line-height`, `space`, `border-radius`, `z-index`, `breakpoint`, `transition`, `color` (palette only)

**Theme completeness**
Theme switching is not required. If a project defines theme variants, every semantic token overridden in one variant must be handled consistently across the other variants.

**State completeness**
If any non-default state exists (`-hover`), the full state set must exist: `hover`, `active`/`pressed`, `focus`, `disabled`.
Proposals must follow the same rule. Do not present partial state-family snippets.

**Surface model**
Exactly 3 levels: `background` → `surface` → `elevated`. No more without architectural justification.

**System colors**
`success`, `warning`, `danger`, `info` → functional/feedback use only. Never decorative.

**Semantic tokens prefer palette references**
Semantic tokens should reference `var(--color-*)` rather than raw hex. Raw values without a palette equivalent are a warning, not a blocker.

---

## Output format

Every change — regardless of size — must produce this output:

```
## Changes applied

### Added
- `--token-name`: `value` — reason

### Modified
- `--token-name`: `old-value` → `new-value` — reason

### Removed
- `--token-name` — migrated to `--replacement` (or: REMOVED, no replacement)

### Unchanged
- N tokens unchanged

### Files modified
- [filename]: N tokens
```

No silent changes. Every modification must be explained.

---

## Golden rule

The token system is a **semantic contract between UI intent and visual representation**.

A token's name must fully express its meaning without seeing its value.
`--text-primary` communicates intent. `#1d1d1f` does not.

Never break the contract.

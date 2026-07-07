# Axiom

Axiom is a portable foundation for design systems: CSS tokens, design rules, and agent skills. It is universal, can be used independently from Lui, and may later become a separate package. It has no JavaScript runtime and no framework dependency.

The name is intentional: an axiom is a base truth that everything else is built from. For this system, the semantic contract, token rules, and architecture rules are the foundation.

## Use Axiom your way

Axiom starts with rules and layers. The CSS tokens are one ready implementation of those rules.

You can use it in three ways:

1. Take only the rules and design your own token system from them.
2. Take `tokens.css` as a ready base and override values for your product.
3. Use the `design-tokens` skill to audit an existing site, update its tokens, or create a new design system from the rules.

The full foundation is described in `DESIGN.md` and in `skills/design-tokens/`.

## Use the tokens

Install or copy the package, then import the CSS once:

```css
@import '@zoxon/axiom/tokens.css';
```

Or copy `tokens.css` and `src/tokens/` into a project and import them locally.

Theme switching is not part of Axiom. Use any mechanism your product needs: `data-theme`, media queries, scoped CSS, or no theme switching at all. If you add themes, override semantic tokens, not palette or layout tokens.

```css
[data-theme='dark'] {
  --fill-background: var(--color-slate-900);
  --text-primary: var(--color-slate-100);
}
```

## What is included

```text
tokens.css
src/
  tokens/
    index.css
    palette.css
    colors.css
    typography.css
    spacing.css
    radius.css
    shadows.css
    z-index.css
examples/
  basic/
  component/
  override/
skills/
  design-tokens/
    SKILL.md
    references/
```

The design system is only:

- rules for how tokens are named and used
- CSS custom properties in `src/tokens/`

`tokens.css` is a package entrypoint that imports `src/tokens/index.css`.

It intentionally does not include components, JavaScript, build steps, or a theme manager.

## Token contract

- `--color-*` tokens are palette values. Do not use them directly in UI code.
- `--fill-*`, `--text-*`, and `--border-*` tokens are semantic UI tokens.
- Components should use semantic tokens only.
- Layout tokens (`--space-*`, `--border-radius-*`, typography, z-index) are theme agnostic.
- System tokens (`success`, `warning`, `danger`, `info`) are for feedback states only.

## Agent skills

Install with the package CLI:

```bash
pnpm dlx @zoxon/axiom install claude
pnpm dlx @zoxon/axiom install codex
pnpm dlx @zoxon/axiom install all
```

Install into a project-local directory:

```bash
pnpm dlx @zoxon/axiom install --dest ./.agents/skills
```

Manual Claude-compatible install:

```bash
cp -R skills/design-tokens ~/.claude/skills/design-tokens
```

Manual Codex-compatible install:

```bash
mkdir -p ~/.agents/skills
cp -R skills/design-tokens ~/.agents/skills/design-tokens
```

Codex installations that read `~/.codex/skills` can use the same directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/design-tokens ~/.codex/skills/design-tokens
```

The skill format is the same `SKILL.md` plus `references/` layout. No duplicate skill source is needed.

## Examples

- `examples/basic` shows plain HTML using `tokens.css`.
- `examples/component` shows a reusable CSS component using only semantic tokens.
- `examples/override` shows product-level semantic token overrides after importing Axiom.

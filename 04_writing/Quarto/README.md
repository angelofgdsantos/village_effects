# Quarto

RevealJS presentation slides derived from Beamer source.

## Files

- `reference_slide.qmd` — Template slide deck (copy and rename for each presentation)
- `custom.scss` — Fira Sans / Moloch-inspired theme (dark green palette, gradient background)

## Theme

Always apply in YAML front matter:
```yaml
format:
  revealjs:
    theme: [serif, custom.scss]
```

## Workflow

1. Create/edit Beamer slides in `Slides/`
2. Use `/translate-to-quarto` to convert to `.qmd`
3. Render: `quarto render slides.qmd`

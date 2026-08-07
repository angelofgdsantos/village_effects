# Slides

Beamer presentation slides (authoritative source for all presentations).

## Compilation

```bash
cd Slides && TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode slides.tex
BIBINPUTS=..:$BIBINPUTS bibtex slides
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode slides.tex
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode slides.tex
```

Or use `/compile-latex Slides/slides.tex`.

## Quarto Conversion

To generate RevealJS slides from Beamer source, use `/translate-to-quarto Slides/slides.tex`.
Output goes to `Quarto/`.

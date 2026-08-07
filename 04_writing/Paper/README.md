# Paper

LaTeX source for the research paper.

## Compilation

```bash
cd Paper && TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode paper.tex
BIBINPUTS=..:$BIBINPUTS bibtex paper
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode paper.tex
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode paper.tex
```

Or use `/compile-latex Paper/paper.tex`.

## Bibliography

Shared bibliography at `../Bibliography_base.bib`.

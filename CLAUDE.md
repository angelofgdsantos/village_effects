# CLAUDE.MD -- Academic Project Development with Claude Code

**Project:** Village Effects of the CFP Program (cfp-zambia)
**Institution:** University of Pennsylvania — Population Studies Center
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- compile/render and confirm output at the end of every task
- **Single source of truth** -- paper `.tex` is authoritative; Beamer `.tex` is authoritative for slides; Quarto `.qmd` derives from Beamer
- **Quality gates** -- nothing ships below 80/100
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md

---

## Project Overview

This paper estimates the causal effect of the Community Forestry Programme (CFP) on village-level deforestation in Zambia. CFP invested in transitional livelihood activities (ecotourism, sustainable agriculture) across chiefdom units. We use variation in CFP take-up across chiefdoms — moderated by governance quality (chiefdom political institutions) and forest dependence (RALS survey) — to identify local deforestation effects using DiD on a village × year panel with Hansen GFC as the outcome.

---

## Folder Structure

```
cfp-zambia/
├── CLAUDE.md                    # This file
├── .claude/                     # Rules, skills, agents, hooks (from GitHub fork)
├── Bibliography_base.bib        # Centralized bibliography
├── Preambles/                   # Shared LaTeX headers/preambles
│
├── 04_writing/                  # All document deliverables
│   ├── Bibliography_base.bib    # Centralized bibliography
│   ├── Preambles/               # Shared LaTeX headers/preambles
│   ├── Paper/                   # LaTeX paper source
│   ├── Slides/                  # Beamer presentation slides (.tex)
│   └── Quarto/                  # RevealJS slides (.qmd + custom.scss theme)
│
├── 01_project_planning/         # IRB, pre-analysis plan, project notes
├── 02_data/                     # All data (mostly gitignored)
│   ├── raw/                     # Unmodified source data
│   ├── processed/               # Cleaned/merged data ready for analysis
│   └── codebooks/               # Data documentation
├── 03_analysis/                 # Working analysis
│   ├── scripts/                 # Python (.py) and Stata (.do) scripts
│   ├── figures/                 # Working/exploratory figures
│   └── tables/                  # Working regression output
├── 04_writing/                  # Drafts, notes, referee responses
├── 05_submission/               # Submission packages (one subfolder per venue)
│   └── YYYY_venue/
└── 06_final_output/             # Publication-ready final outputs
    ├── scripts/                 # Final replication scripts
    ├── figures/                 # Final figures (PDF/300 DPI PNG)
    ├── tables/                  # Final tables (.tex + .csv)
    └── references/              # Final bibliography
```

---

## Commands

```bash
# LaTeX paper (3-pass, XeLaTeX only)
cd 04_writing/Paper && TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode paper.tex
BIBINPUTS=..:$BIBINPUTS bibtex paper
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode paper.tex
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode paper.tex

# Beamer slides (same 3-pass pattern)
cd 04_writing/Slides && TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode slides.tex

# Python analysis
python3 03_analysis/scripts/10_build_dataset.py

# Stata batch execution
stata -b do 03_analysis/scripts/10_main_analysis.do

# Render Quarto slides
cd Quarto && quarto render slides.qmd

# Quality score
python scripts/quality_score.py Quarto/slides.qmd
```

---

## Script Naming Convention

| Prefix | Stage | Example |
|--------|-------|---------|
| `10_`, `11_`, ... | Data processing | `10_build_grid.py`, `11_merge_outcomes.py` |
| `20_`, `21_`, ... | Visualization | `20_maps.py`, `21_descriptive_figures.py` |
| `30_`, `31_`, ... | Main analysis | `30_main_did.do`, `31_robustness.do` |
| `40_`, `41_`, ... | Heterogeneity / extensions | `40_heterogeneity.do` |
| `50_`, `51_`, ... | Output / tables | `50_tables.do`, `51_export_figures.py` |
| `xx_` | Draft / unused | `xx_exploration.py` |

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 80 | Commit | Good enough to save |
| 90 | PR | Ready for submission / deployment |
| 95 | Excellence | Aspirational |

---

## Skills Quick Reference

| Command | What It Does |
|---------|-------------|
| `/compile-latex [file]` | 3-pass XeLaTeX + bibtex |
| `/deploy [file]` | Render Quarto + sync to docs/ |
| `/proofread [file]` | Grammar/typo/overflow review |
| `/visual-audit [file]` | Slide layout audit |
| `/review-paper [file]` | Manuscript review (referee mode) |
| `/qa-quarto [file]` | Adversarial Quarto vs Beamer QA |
| `/slide-excellence [file]` | Combined multi-agent review |
| `/translate-to-quarto [file]` | Beamer → Quarto translation |
| `/validate-bib` | Cross-reference citations |
| `/commit [msg]` | Stage, commit, PR, merge |
| `/lit-review [topic]` | Literature search + synthesis |
| `/research-ideation [topic]` | Research questions + strategies |
| `/review-r [file]` | R code quality review |
| `/data-analysis [dataset]` | End-to-end analysis workflow |
| `/learn [skill-name]` | Extract discovery into persistent skill |
| `/context-status` | Show session health + context usage |
| `/deep-audit` | Repository-wide consistency audit |

---

## Quarto Theme

Slides use `Quarto/custom.scss` — Fira Sans, Moloch/Metropolis-inspired, dark green palette.
Always apply: `theme: [serif, custom.scss]` in any `.qmd` YAML front matter.

---

## Beamer Custom Environments

*(Fill in as slides are developed)*

| Environment | Effect | Use Case |
|-------------|--------|---------|
| — | — | — |

## Quarto CSS Classes

*(Fill in as slides are developed)*

| Class | Effect | Use Case |
|-------|--------|---------|
| — | — | — |

---

## Current Paper State

| Section | Status | Notes |
|---------|--------|-------|
| Introduction | Not started | Research question: CFP effects on village deforestation |
| Data | Not started | CFP data, Hansen GFC, RALS survey, chiefdom boundaries |
| Empirical Strategy | Not started | DiD / staggered adoption; heterogeneity by governance × forest dependence |
| Results | Not started | — |
| Conclusion | Not started | — |

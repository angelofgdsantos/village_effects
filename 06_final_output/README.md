# 06_final_output

Publication-ready final outputs. Everything here is polished and committed.

## Structure

| Subfolder | Contents |
|-----------|---------|
| `figures/` | Final figures: PDF (vector) or 300 DPI PNG; maps with scale bar, north arrow, legend |
| `tables/` | Final tables: `.tex` for paper, `.csv` for reference |
| `scripts/` | Final replication scripts (clean, documented, self-contained) |
| `references/` | Final bibliography file |

## Standards

- Figures: white background, colorblind-safe palette (viridis, ColorBrewer), publication-ready
- Tables: `.tex` output from Stata `esttab` / `outreg2` or Python
- Scripts: fully reproducible from `02_data/raw/` with no manual steps

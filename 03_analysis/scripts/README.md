# 03_analysis/scripts

Analysis scripts by pipeline stage.

## Naming Convention

| Prefix | Stage |
|--------|-------|
| `10_`, `11_`, ... | Data processing (reads from `02_data/raw/`, writes to `02_data/processed/`) |
| `20_`, `21_`, ... | Visualization (exploratory figures → `03_analysis/figures/`) |
| `30_`, `31_`, ... | Main analysis (regressions → `03_analysis/tables/`) |
| `40_`, `41_`, ... | Heterogeneity / extensions |
| `50_`, `51_`, ... | Final output export (→ `06_final_output/`) |
| `xx_` | Draft / unused |

## Languages

- **Python** (`.py`): geospatial processing, data pipelines, visualization
  - Standard header docstring: Author, Date, Title, Description, Usage, Parts, Inputs, Outputs
  - No hardcoded absolute paths
- **Stata** (`.do`): econometric analysis
  - `clear all` + `set more off` at top
  - `preserve/restore` around destructive merges
  - Always specify `absorb()`, `cluster()`, `vce()` explicitly

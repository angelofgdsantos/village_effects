---
paths:
  - "Paper/**/*.tex"
  - "Slides/**/*.tex"
  - "Quarto/**/*.qmd"
  - "03_analysis/scripts/**/*.py"
  - "03_analysis/scripts/**/*.do"
---

# Research Knowledge Base: cfp-zambia

<!-- Claude reads this before creating or modifying any paper, slide, or analysis content. -->

## Project Summary

**Paper:** Village-Level Deforestation Effects of the Community Forestry Programme (CFP) in Zambia
**Method:** Difference-in-Differences (DiD) / staggered adoption, village × year panel
**Outcome:** Annual tree cover loss (Hansen GFC `lossyear` variable)
**Unit:** Village $v$, year $t$, within chiefdom $c$
**Heterogeneity:** Governance quality $G_c$ (chiefdom political institutions) × Forest dependence $F_v$ (RALS survey)
**Reference paper:** `01_project_planning/supporting_docs/supporting_papers/1-s2.0-S030438782400018X-main-3.pdf`

---

## Notation Registry

| Rule | Convention | Example | Anti-Pattern |
|------|-----------|---------|-------------|
| Village index | $v$ (lowercase) | $Y_{vt}$ | $i$, $j$ for villages |
| Year index | $t$ (lowercase) | $t = 2001, \ldots, 2023$ | $y$, $yr$ |
| Chiefdom index | $c$ (lowercase) | chiefdom $c(v)$ | $j$, $k$ |
| CFP treatment | $D_{vt}$ | $D_{vt} \in \{0,1\}$ | $T_{vt}$, $Treat_{vt}$ |
| Outcome | $Y_{vt}$ | annual tree cover loss (binary) | $y_{vt}$, $loss_{vt}$ |
| Governance score | $G_c$ | chiefdom-level political institutions index | $gov_c$, $inst_c$ |
| Forest dependence | $F_v$ | village-level share of households dependent on forest (RALS) | $dep_v$, $forest_v$ |
| ATT | $\tau^{ATT}$ | DiD estimand | $\hat{\beta}$ alone without label |
| Post-period | year FE | absorbed by year FE in preferred spec | $post$, $after$ |

---

## Symbol Reference

| Symbol | Meaning | Introduced |
|--------|---------|------------|
| $Y_{vt}$ | Binary tree cover loss indicator for village $v$ in year $t$ (Hansen GFC) | Data section |
| $D_{vt}$ | CFP treatment indicator: 1 if village $v$ participates in CFP in year $t$ | Empirical strategy |
| $\tau^{ATT}$ | Average Treatment Effect on the Treated (DiD estimand) | Empirical strategy |
| $\alpha_v$ | Village fixed effect | Empirical strategy |
| $\gamma_t$ | Year fixed effect | Empirical strategy |
| $c(v)$ | Chiefdom containing village $v$ | Data section |
| $G_c$ | Governance quality index for chiefdom $c$ | Heterogeneity section |
| $F_v$ | Forest dependence score for village $v$ (from RALS) | Heterogeneity section |

---

## Treatment Groups

| Group | Label | Definition | Role |
|-------|-------|-----------|------|
| CFP villages | Treated | Villages that participate in CFP (received investment in transitional activities) | Primary treatment |
| Non-CFP villages, same chiefdom | Within-chiefdom control | Villages in CFP-participating chiefdoms but not in CFP themselves | Spillover / leakage test |
| Non-CFP villages, different chiefdom | Pure control | Villages in chiefdoms with no CFP presence | Clean counterfactual |

---

## Key Estimands

| Estimand | Description | Expected Sign | Notes |
|----------|------------|--------------|-------|
| ATT (main) | Avg effect of CFP participation on village tree cover loss | Negative (reduced deforestation) | Primary result |
| Heterogeneity by $G_c$ | Does governance quality amplify/dampen CFP effect? | Positive effect of $G_c$ × $D_{vt}$ (better governance → stronger effect) | Governance channel |
| Heterogeneity by $F_v$ | Does forest dependence moderate CFP take-up and effect? | Ambiguous — could be higher dependence → more need, or weaker compliance | Forest dependence channel |
| Spillover | Effect on non-CFP villages in CFP chiefdoms | Sign TBD — could be positive (norm diffusion) or negative (leakage) | Secondary result |

---

## Data Sources

| Dataset | Description | Resolution | Period |
|---------|------------|-----------|--------|
| Hansen GFC | Global Forest Change — annual tree cover loss (`lossyear`) | 30m (aggregate to village level) | 2001–2023 |
| CFP programme data | Village-level treatment assignment + activity timing | Village polygon / point | Programme period |
| RALS survey | Zambia Rural Agricultural Livelihoods Survey — forest dependence, household chars | Household → aggregate to village | 2012, 2015, 2019/20 |
| Chiefdom boundaries | Administrative boundaries, Zambia | Vector | — |
| Governance data | Chiefdom-level political institutions index (source TBD) | Chiefdom | — |
| NDVI / vegetation | Satellite vegetation indices (complement to Hansen) | Raster | TBD |

---

## Empirical Anti-Patterns (Don't Do This)

| Anti-Pattern | What Goes Wrong | Correction |
|-------------|----------------|-----------|
| **Using IHS/arcsinh(Y) or log(1+Y) as outcome** | ATE is arbitrarily unit-dependent when Y has zeros — multiplying by 100 can change estimate >100%. Cannot interpret as % effect. Chen & Roth (2024, QJE). | Use **Poisson PPML** → estimates θ_ATE% = E[Y(1)−Y(0)]/E[Y(0)], scale invariant. Or use normalized loss rate (loss pixels / total pixels). |
| Treating entire chiefdom as "treated" when only some villages are in CFP | Dilutes village-level effect; mixes treatment and control units | Assign $D_{vt}$ at village level; separate CFP vs. non-CFP within chiefdom |
| Using cumulative tree cover stock as outcome | Non-stationary; conflates program effect with pre-existing trends | Use annual loss flow $Y_{vt}$ (binary or rate) |
| Ignoring Hansen GFC coding: `lossyear` = 1–23 | Calendar year off by 2000; wrong pre/post assignment | Recode: `year = lossyear + 2000` |
| Conflating governance effect with forest dependence in a single index | Loses interpretability; cannot identify separate mechanisms | Report $G_c$ and $F_v$ heterogeneity separately |
| Interpreting null chiefdom-level result as "program failed" | Could be dilution across non-CFP villages within the chiefdom | Always decompose: CFP villages vs. non-CFP within CFP chiefdoms |
| Ignoring staggered adoption | TWFE biased under heterogeneous effects + staggered rollout | Use `csdid`/`drdid` (Callaway & Sant'Anna 2021) if rollout is staggered |
| Clustering SEs at chiefdom level when treatment is at village level | Over-aggregated SEs, may be too conservative | Cluster at village level; chiefdom-clustered as robustness |

---

## Code Conventions

| Convention | Python | Stata |
|-----------|--------|-------|
| Script naming | `10_`, `11_`, `20_`, ... prefixes | Same prefix convention |
| Paths | Relative (no hardcoded `/Users/...`) | Relative from project root |
| Regressions | — | `reghdfe` (TWFE), `csdid`, `drdid` |
| Spatial ops | `geopandas`, `rasterio`, `xarray` | `spmap` (maps) |
| Output | Save to `03_analysis/figures/` or `03_analysis/tables/` (working); `06_final_output/` (final) | Same |
| FE specification | — | Always `absorb(village_id year)` explicitly |
| Clustering | — | Always `cluster(village_id)`; add `cluster(chiefdom_id)` as robustness |

---

## Key References

| Paper | Citation | Finding | Relevance |
|-------|----------|---------|----------|
| **Abman & Lundberg (2024)** | *J Development Economics* 168, 103269 | Contracting → **0.77 pp reduction in annual village-level forest loss** (Ghana, matched DiD, Hansen GFC, 2001–2019) | PRIMARY DESIGN TEMPLATE — village DiD, matched + synthetic DiD + event study. **Do NOT copy IHS outcome** — use Poisson PPML instead (Chen & Roth 2024) |
| **Chen & Roth (2024)** | *Quarterly Journal of Economics* 139(2), 891–936 | IHS/log(1+Y) ATEs are unit-dependent when Y has zeros. Trilemma: scale-invariant + point-identified + avg-individual-effects cannot hold simultaneously. **Poisson PPML** estimates θ_ATE% = E[Y(1)−Y(0)]/E[Y(0)] — scale invariant, percentage interpretation, works in DiD | MANDATORY — governs outcome specification for $Y_{vt}$. Never use IHS. |
| **Bloem & Lundberg (2025)** | *J Development Economics* 179, 103600 | Ag tech adoption → heterogeneous deforestation effects by baseline forest density (Nigeria, RCT, pixel-level) | HETEROGENEITY TEMPLATE — spatial treatment exposure, forest density as moderator |
| Callaway & Sant'Anna (2021) | *J Econometrics* | Staggered DiD estimator (`csdid`/`drdid`) | Estimator choice if CFP rollout is staggered |
| Roth et al. (2023) | *J Economic Literature* | DiD review: pre-trends, sensitivity | Identification credibility checks |
| Ferraro & Hanauer (2014) | *Science* | Matching-based conservation program evaluation | General conservation evaluation methodology |
| **RALS codebooks** | CSO Zambia + MSU | 3-wave HH panel (2012, 2015, 2019), forest product income, GPS-coded | Forest dependence ($F_v$) construction |

## Detailed Data Reference

See `.claude/rules/data-reference.md` for:
- Full CFP variable list by survey module
- RALS variable reference by file (wild.sav, field.sav, household.sav, etc.)
- Forest dependence and governance index construction options
- Hansen GFC coding notes and spatial matching workflow

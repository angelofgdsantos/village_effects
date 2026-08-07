---
paths:
  - "03_analysis/scripts/**/*.py"
  - "03_analysis/scripts/**/*.do"
---

# Data Reference: cfp-zambia

<!-- Read this before writing any data processing or analysis script. -->

---

## CFP Survey Data

**Program:** Community Forests Programme — 5 chiefdoms in Eastern Zambia
**Chiefdoms:** Luembe, Nyalungwe, Malama, Mwanya, Msoro
**Format:** ODK XLSForm (.xlsx codebooks); raw data format TBD (likely .csv or .dta)
**Languages:** English + Nyanja (bilingual)

### Survey Instruments

| File | Respondent | Level | Time | Variables |
|------|-----------|-------|------|-----------|
| `cfphh_v7_15.5.xlsx` | Household head | Household | Baseline | 2,260 |
| `cfpforst_v4_29.4.xlsx` | Forest key informant | Village/forest | Baseline | 1,582 |
| `cfpheadman_v6_29.4.xlsx` | Village headman | Village | Baseline | 627 |
| `cfp_hh_wom_FINAL_V3.xlsx` | Women (household) | Household | Endline | 1,328 |
| `cfpheadperson_FINAL_V3.xlsx` | Chief/headperson | Village | Endline | 600 |

### Key Variable Reference

#### Treatment Exposure (Endline Headperson Survey)
| Variable | Label | Values |
|----------|-------|--------|
| `cfp_aware` | Has your village participated in CFP? | 1=Yes, 2=No |
| `cfp_year` | What year did your village join CFP? | year |
| `cfp_still` | Is your village still participating in CFP? | 1=Yes, 2=No |
| `cfp_stop` | What year did your village stop participating? | year |

#### Forest Dependence (Baseline Forest KII)
| Variable | Label | Values |
|----------|-------|--------|
| `ffor_num` | Number of forests village relies on for income | integer |
| `fhhincome_1/2/3/4` | HH income dependence on each forest | 1=1-10%, 2=11-25%, 3=26-50%, 4=51-75%, 5=76-100% |
| `fnewclear_1` | New cropland cleared in past year | acres/ha |
| `fclear_yn` | Are there rules about land clearing? | 1=Yes, 2=No |

#### Governance (Baseline Forest KII + Headman + Endline Chief)
| Variable | Survey | Label | Values |
|----------|--------|-------|--------|
| `govern_foruse` | Forest KII + Women | Who makes rules about forest use | headman, chief, induna, elders, council, government |
| `fpermit_fair` | Forest KII | Fairness of decision-making | 1=Very fair, 2=Fair, 3=Neutral, 4=Unfair, 5=Very unfair |
| `hlladder_headman` | Endline Chief | Chief's position on power ladder | 1-10 (low to high authority) |
| `hlaccess` | Headman | How people access land | inheritance, purchase, headman allocation, etc. |

#### Forest Income (Baseline Household)
| Variable | Label |
|----------|-------|
| `incomeproduct_1/2/3` | Top 3 forest products for income (timber, fuelwood, charcoal, poles, reeds, etc.) |
| `forest_num` | Number of forests household accesses |
| `nonharvben_1/2/3` | Non-harvested benefits (soil, water, grazing, biodiversity, medicines) |

#### Response Codes (CFP)
- **Yes/No:** 1=Yes, 2=No, 888=Don't know, 999=Prefer not to answer
- **Matrilineal inheritance:** 1=Wife's family, 2=Husband's family, 3=Purchased/given

---

## RALS Survey Data (Zambia Rural Agricultural Livelihoods Survey)

**Waves:** 2012 (RALS2012), 2015 (RALS2015), 2019 (RALS2019)
**Conducted by:** CSO Zambia + Michigan State University
**Format:** SPSS .sav files in `02_data/raw/rals/RALS{year}/data/`
**Sample:** ~8,000 HH per wave; rural Zambia; GPS-geocoded
**Reference period:** 2013/14 season (RALS15), 2017/18 season (RALS19)

### Key Files by Module

| File | Content | Key Variables |
|------|---------|---------------|
| `id.sav` | Geographic IDs, GPS coords | `prov`, `dist`, `vil15/vil19`, `s_dd_new`, `e_dd_new`, `cluster`, `hh` |
| `household.sav` | HH-level questions | `hh09a/b`, `hh10a/b`, `hh50a`, `hh51a`, `hh53a`, `have_fields` |
| `wild.sav` | Wild product collection | `wildprod`, `wd01`, `wd01a` (distance), `wd02`, `wd03/wd04` (value) |
| `field.sav` | Plot-level data | `f01` (land use), `f03a/b` (distance to plot), `f05` (tenure), `f12` (trees in field) |
| `wages.sav` | Wage income | Filter `anywork==1` |
| `labour.sav` | Agricultural labour | `labour`, `lbr01`, `lbr02` |
| `soil_land_manage.sav` | Land management practices | `slm01`-`slm07` |
| `distance_agser.sav` | Distances to services | 20 destinations including Boma, markets |

### Forest Dependence Variables (RALS)

#### Wild Products Module (Section 11.2, `wild.sav`)
| Variable | Label |
|----------|-------|
| `wd01` | Collected [product] for home consumption (1=Yes, 2=No) |
| `wd01a` | Distance to primary source (km) |
| `wd02` | Who provided most labour |
| `wd03` | Value consumed May–Oct (ZMW) |
| `wd04` | Value consumed Nov–Apr (ZMW) |

**Forest-relevant products tracked:**
- Poles and timber
- Firewood (excl. charcoal)
- Charcoal (produced for home use)
- Wild fruits, wild honey, wild mushrooms, wild animals/birds

#### Off-Farm Forest Income (Section 9, `salwage.sav` or business module)
| Code | Activity |
|------|----------|
| 6 | Firewood collection and selling |
| 7 | Charcoal production or trading (regular) |
| 8 | Eco-charcoal trading |
| 10 | Regular charcoal production/selling |
| 33 | Poles/timber collecting & selling |
| 32 | Wild fruits collection & selling |

#### Land Use / Forest Clearing (Section 2.2a, `field.sav`)
| Variable | Label |
|----------|-------|
| `f01` | Land use type (includes: virgin land/never cultivated, personal woodlot) |
| `f12` | Trees/shrubs growing in this field? |
| `af01` | Agroforestry tree species (27 coded) |
| `nf01` | Land use before cultivation (includes: virgin forest, fallow, protected area) |

#### Governance Proxies (Section 13, `household.sav`)
| Variable | Label |
|----------|-------|
| `hh51a` | Is chief related to household head? |
| `hh53a` | Tribe of current household head (27 tribal groups) |
| `hh57` | Matrilineal (1) or Patrilineal (2) household |
| `hh09a` | Do headmen have unallocated arable land available? |
| `hh10a` | Can customary land be converted to titled property? |
| `hh10b` | Can customary land be bought/sold without titling? |

### Geographic Identifiers (RALS)
| Variable | Description |
|----------|-------------|
| `prov` | Province code |
| `dist` | District code |
| `cluster` | Cluster number (village group) |
| `hh` | Household number |
| `vil15` / `vil19` | Village name |
| `s_dd_new` | South coordinate (decimal degrees) — GPS |
| `e_dd_new` | East coordinate (decimal degrees) — GPS |

**Note:** No explicit chiefdom variable in RALS. Use tribal group (`hh53a`) + geographic cluster + chief-relation variables as proxies. Spatial join with chiefdom boundary shapefile using GPS coordinates is the preferred approach.

---

## Hansen GFC (Satellite Forest Outcome)

| Variable | Description |
|----------|-------------|
| `lossyear` | Year of canopy loss (values 1–23; add 2000 to get calendar year) |
| `treecover2000` | % canopy cover in year 2000 baseline |

**Anti-pattern:** `lossyear` uses values 1–23, NOT calendar years. Always recode: `year = lossyear + 2000`

**Aggregation:** 30m pixels → aggregate to village polygon.

### Outcome Specification — MANDATORY (Chen & Roth 2024, QJE)

**NEVER use IHS/arcsinh(Y) or log(1+Y) when Y has zeros.** The ATE is arbitrarily unit-dependent. Use one of:

| Outcome | Formula | Estimator | Notes |
|---------|---------|-----------|-------|
| **Loss rate (preferred)** | `loss_pixels_vt / total_pixels_v` | Poisson PPML or OLS | Normalized, scale invariant. Y ∈ [0,1]. Many villages may have Y=0. |
| **θ_ATE% via Poisson** | Poisson PPML of loss_pixels_vt on D_vt + FE | `ppmlhdfe` (Stata) or `statsmodels` (Python) | Estimates E[Y(1)−Y(0)]/E[Y(0)] directly; exponentiate β → % change |
| **Binary loss indicator** | `1(any loss in village polygon in year t)` | LPM or Poisson | Clean, no zeros problem, interpretable as probability |
| **Intensive margin only** | Restrict to village-years with positive loss | OLS in logs + Lee bounds | Partially identified; report alongside extensive margin |

**Stata command:** `ppmlhdfe loss_rate D_vt, absorb(village_id year) cluster(village_id)`
**Python:** `statsmodels.genmod` with `family=Poisson()` + village/year dummies

**Note:** Parallel trends assumption is also unit-dependent under IHS (Roth & Sant'Anna 2023). Parallel trends in levels or in logs (for positive outcomes) is the defensible choice.

---

## Key Methodological Notes

### Constructing Forest Dependence ($F_v$)

**Option A — CFP data (preferred for CFP villages):**
Use `fhhincome` buckets from Forest KII → village-level average income dependence on forest

**Option B — RALS data (for broader sample):**
Compute share of HH income from forest products: `(wd03 + wd04 + off-farm forest income) / total HH income`
Or simpler: `wild.sav` collection indicator for charcoal/poles/firewood as binary forest dependence proxy

**Option C — Distance proxy:**
`wd01a` (distance to forest product source) — shorter distance → higher dependence

### Constructing Governance Index ($G_c$)

**Candidate variables:**
1. `govern_foruse` (who makes rules) → dummy: chief or council = formal institution (vs. headman = informal)
2. `fpermit_fair` (rule fairness) → higher score = less fair governance
3. `hlladder_headman` (power ladder) → higher = more authority
4. `hh09a` (unallocated land available) → proxy for land scarcity and chief authority

**Recommendation:** Construct a simple standardized composite (z-score of above) OR use principal components. Document construction clearly.

### Spatial Matching Strategy

1. Load village GPS coordinates from CFP surveys or RALS `id.sav`
2. Load Hansen GFC 30m raster tiles (subset to Eastern Zambia)
3. For each village: extract pixels within village polygon (or buffer radius)
4. Compute: annual loss rate = (pixels with `lossyear == t`) / (total pixels with `treecover2000 > X`)
5. Join with CFP treatment assignment and RALS covariates by village ID

# MEMORY.md — Project Knowledge Index

<!-- Keep under 200 lines — loads into every session.
     Detailed data dictionaries → .claude/rules/data-reference.md -->

## Project

- **Project:** cfp-zambia — Village Effects of the Community Forestry Programme in Zambia
- **Research question:** Does CFP reduce village-level deforestation? Moderated by governance ($G_c$) and forest dependence ($F_v$)?
- **Unit:** Village $v$ × year $t$ within chiefdom $c$
- **Estimator:** DiD / staggered adoption; `reghdfe` (TWFE) or `csdid`/`drdid` (staggered)
- **5 CFP chiefdoms:** Luembe, Nyalungwe, Malama, Mwanya, Msoro (Eastern Zambia)
- **Setup plan:** `01_project_planning/quality_reports/plans/staged-strolling-sphinx.md` (2026-04-15)

## Literature

### Paper 1 — PRIMARY BENCHMARK (follow design, NOT outcome transformation)
- **Abman & Lundberg (2024)** "Contracting, market access and deforestation." *Journal of Development Economics* 168, 103269.
- **Setting:** Ghana, village-level DiD, 2001–2019, outcome = annual forest loss (Hansen GFC)
- **Design:** Matched DiD + synthetic DiD + event study. They use IHS — **DO NOT follow this**; use Poisson PPML instead (see Chen & Roth 2024 below)
- **Finding:** Contracting → **~0.77 pp reduction in annual forest loss** (~200% of pre-mean)
- **Relevance:** Village-level unit, Hansen outcome, matched DiD design — follow everything except IHS
- **File:** `01_project_planning/supporting_docs/supporting_papers/1-s2.0-S030438782400018X-main-3.pdf`

### Paper 3 — OUTCOME TRANSFORMATION (MANDATORY — overrides Paper 1 on this point)
- **Chen & Roth (2024)** "Logs with Zeros? Some Problems and Solutions." *Quarterly Journal of Economics* 139(2), 891–936. DOI: 10.1093/qje/qjad054
- **Core problem:** IHS/arcsinh(Y) and log(1+Y) ATEs are **arbitrarily unit-dependent** when Y has zeros. Multiplying outcome by 100 can change estimated effect by >100%. Cannot be interpreted as percentage effects.
- **Trilemma:** No parameter with zero-valued outcomes can simultaneously be (i) avg of individual-level effects, (ii) scale-invariant, (iii) point identified. Must sacrifice one.
- **Recommended alternatives (Table II):**
  1. **θ_ATE% = E[Y(1)−Y(0)] / E[Y(0)]** → estimated by **Poisson QMLE/PPML** — *preferred for our study*. Scale invariant, percentage interpretation. Works in DiD.
  2. **Normalized outcome Ỹ = Y/X** (e.g., loss rate = loss pixels / total pixels) — scale invariant if X is predetermined
  3. **Intensive-margin only:** E[log(Y(1)/Y(0)) | Y(1)>0, Y(0)>0] + Lee bounds for extensive margin
- **For DiD:** Parallel trends in arcsinh(Y) in dollars ≠ parallel trends in cents — assumption is unit-dependent too. Use Poisson PPML DiD.
- **File:** `01_project_planning/supporting_docs/supporting_papers/qjad054-2.pdf`

### Paper 2 — HETEROGENEITY BENCHMARK
- **Bloem & Lundberg (2025)** "Agricultural technology adoption and deforestation: Evidence from a RCT." *Journal of Development Economics* 179, 103600.
- **Setting:** Nigeria (Kwara State), RCT with spatial treatment exposure, pixel-level Hansen outcome
- **Design:** Probabilistic treatment exposure (gamma distribution for plot distances); logit/PPML on pixels
- **Finding:** Effect **heterogeneous by baseline forest density** — reduces loss in dense-forest areas, increases in sparse. NDVI gain ≈ +0.0176 (3.8% of baseline mean)
- **Key method:** Spatial explicit treatment exposure using gamma CDF of distance from village centroid
- **Relevance:** Heterogeneity design template; spatial matching of satellite + survey; suggests forest dependence as moderator
- **File:** `01_project_planning/supporting_docs/supporting_papers/1-s2.0-S0304387825001518-main-5.pdf`

### Paper 4 — INSTITUTIONAL MOTIVATION
- **Larcom, van Gevelt & Zabala (2016)** "Precolonial institutions and deforestation in Africa." *Land Use Policy* 51, 150–161. DOI: 10.1016/j.landusepol.2015.10.030
- **Data:** Murdock (1967) Ethnographic Atlas chief succession codes + Michalopoulos & Papaioannou (2013) precolonial boundaries + Hansen GFC 2000–2012. N=645 precolonial societies, 49 African states.
- **Succession codes:** 0=hereditary (base, 82%), 1=democratic (8%), 2=from above (6%), 3=social standing (4%)
- **Finding:** Social standing succession → **+0.8 pp/year higher deforestation** vs. hereditary (fewer institutional checks → forest rent-seeking)
- **Relevance:** Theoretical motivation for $G_c$. **Do NOT use their data directly** — only 2-3 ethnic groups cover all 5 CFP chiefdoms → zero identifying variation. Use CFP's own governance variables instead.
- **File:** `01_project_planning/supporting_docs/supporting_papers/1-s2.0-S0264837715003415-main.pdf`

### Paper 5 — PES TAKE-UP MECHANISM
- **Jack & Jayachandran (2019)** "Self-selection into payments for ecosystem services programs." *PNAS* 116(12), 5326–5333. DOI: 10.1073/pnas.1802868115
- **Setting:** Two RCTs — DEFOR (avoided deforestation, Uganda) + AFFOR (afforestation, Malawi)
- **Finding:** Enrollment costs and conservation costs jointly determine participant composition. When positively correlated: enrolled are inframarginal (low additionality). **Enrollment cost manipulation** (covering seedling costs etc.) can improve targeting.
- **Relevance:** Motivates why take-up rate in CFP may be low and non-random. Enrollment barriers (logistics, awareness) in CFP likely correlate with forest dependence.

### Paper 6 — PES EFFECT BENCHMARK (RCT)
- **Jayachandran et al. (2017)** "Cash for Carbon: A randomized trial of PES to reduce deforestation." *Science* 357(6348), 267–273. DOI: 10.1126/science.aan0568
- **Setting:** Uganda, 121 villages randomized (60 treated), $28/ha/year for 2 years
- **Finding:** Tree cover loss **halved** (4.2% treated vs. 9.1% control). Cost-benefit ratio >2. Take-up only 32%. Deforestation **resumed** after payments ended.
- **Relevance:** Effect size benchmark. Permanence concern motivates CFP's transitional activities design (ecotourism, sustainable agriculture vs. cash).

### Paper 7 — PA EVALUATION METHODOLOGY
- **Ferraro & Hanauer (2014)** PNAS 111(11), 4332–4337. DOI: 10.1073/pnas.1307712111
- **Finding:** PA effects on poverty flow mainly through tourism, not direct ecosystem restriction. Causal mediation approach.
- **Relevance:** Methodological benchmark for conservation program evaluation separating channels.

## CFP Data

- **Format:** ODK XLSForm surveys, bilingual English + Nyanja
- **Surveys:** Baseline (HH, Forest KII, Headman) + Endline (HH-Women, Headperson/Chief)
- **Treatment variable (endline headperson):** `cfp_aware`, `cfp_year`, `cfp_still`, `cfp_stop`
- **Forest dependence (baseline Forest KII):** `fhhincome_1/2/3/4` — household income dependence on forest in buckets (1-10%, 11-25%, 26-50%, 51-75%, 76-100%)
- **Governance variables:** `govern_foruse` (who makes rules: headman, chief, induna, elders, council), `fpermit_fair` (decision fairness 1-5), power ladder `hlladder_headman` (1-10, endline chief)
- **Forest use:** `fnewclear_1` (new cropland cleared past year), `incomeproduct_1/2/3` (top forest products for income)
- **Codebooks:** `02_data/codebooks/cfp/baseline/` (3 xlsx) + `02_data/codebooks/cfp/endline/` (2 xlsx)

## RALS Data

- **Waves:** 2012, 2015, 2019 (raw .sav SPSS files in `02_data/raw/rals/`)
- **Conducted by:** Central Statistical Office (CSO), Zambia + Michigan State University
- **Sample:** ~8,000 HH/wave, rural Zambia, GPS-geocoded (S/E decimal degrees)
- **Key modules for deforestation research:**
  - Wild products (Sec 11.2): charcoal (codes 6-8, 10), poles/timber (code 33), firewood (code 6), `wd01a` = distance to source
  - Agroforestry (Sec 2.2a): `af01` tree species, `nf01` land use before (includes "virgin land/forest")
  - Land tenure (Sec 10.7/10.10): `hh09a/b` (unallocated land), `hh10a/b` (customary land conversion/sales)
  - Off-farm income (Sec 9): charcoal/timber trading as business activity with monthly revenue
- **Governance proxies:** `hh53a` (tribal group, 27 codes), `hh51a-d` (chief relation to HH), `hh57` (matrilineal=1 / patrilineal=2)
- **Forest dependence proxy:** `wild.sav` product collection + `wd01a` distance + off-farm income from forest products
- **Codebooks:** `02_data/codebooks/rals/` (2 PDFs + data_notes.md); detailed notes → `02_data/raw/rals/data_notes.md`

## Workflow Patterns

- [LEARN:workflow] Create session log FIRST in each session — stop-hook blocks after 1 response if no log exists. Path: `01_project_planning/quality_reports/session_logs/YYYY-MM-DD_description.md`

## Design Decisions

- [LEARN:notation] Unit of analysis: village $v$ (CFP data is village-level; Hansen aggregated to village)
- [LEARN:specification] Default: `absorb(village_id year)`, `cluster(village_id)`. Chiefdom-level cluster = robustness only.
- [LEARN:outcome] **NEVER use IHS/arcsinh(Y) or log(1+Y)** when Y has zeros. Use Poisson PPML → estimates θ_ATE% = E[Y(1)−Y(0)]/E[Y(0)], scale invariant, percentage interpretation. Chen & Roth (2024, QJE).
- [LEARN:ihs-anti-pattern] Abman & Lundberg (2024) use IHS — do NOT copy that. Follow their design (village DiD, Hansen GFC, matched controls, event study) but use Poisson PPML or normalized loss rate as outcome.
- [LEARN:heterogeneity] Report governance ($G_c$) and forest dependence ($F_v$) separately — never collapse.
- [LEARN:forest-dep] Construct $F_v$ from CFP Forest KII (`fhhincome` buckets) OR RALS wild product income share — both valid; document choice.
- [LEARN:governance] $G_c$ candidate: `govern_foruse` + `fpermit_fair` + headperson power ladder → composite or separate components.

## Key Open Questions (from lit review)

- Is CFP = Luangwa Community Forests Project (LCFP, BioCarbon Partners, 2014+)? Chiefdoms (Luembe, Nyalungwe, Malama, Mwanya, Msoro) overlap with Luangwa Valley — **confirm with Angelo**
- Is CFP rollout staggered across chiefdoms/years? (`cfp_year` in endline headperson survey)
- Within-chiefdom variation in village enrollment? (enables clean within-chiefdom control group)

## File Organization

- Lit review: `01_project_planning/quality_reports/lit_review_village_deforestation_institutions_pes.md`
- Knowledge base: `.claude/rules/knowledge-base-template.md`
- Detailed data dictionary: `.claude/rules/data-reference.md`
- CFP codebooks: `02_data/codebooks/cfp/`
- RALS codebooks: `02_data/codebooks/rals/` + `02_data/raw/rals/data_notes.md`
- Supporting papers: `01_project_planning/supporting_docs/supporting_papers/`
- Research ideas: `01_project_planning/supporting_docs/supporting_files/rals_idea/ideal.md`

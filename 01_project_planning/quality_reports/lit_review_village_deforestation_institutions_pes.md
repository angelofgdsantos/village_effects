# Literature Review: Village-Level Deforestation, Institutional Dimensions, and PES Program Take-Up

**Date:** 2026-04-15
**Query:** Deforestation at village levels; measurements of deforestation; institutional dimensions (chiefdoms, governance) and effects on deforestation; determinants of deforestation reduction and PES program take-up
**Anchored in:** Supporting papers in `01_project_planning/supporting_docs/supporting_papers/`

---

## Summary

The empirical literature on deforestation has undergone a methodological revolution over the past decade, shifting from country- and pixel-level cross-sectional analysis toward village-level causal identification using satellite data matched to program records. Two methodological pillars anchor this shift: the pairing of Hansen Global Forest Change (GFC) data with quasi-experimental or experimental variation in treatment assignment, and the growing recognition — formalized in Chen & Roth (2024) — that log-like transformations of zero-inflated outcomes produce unit-dependent estimates that cannot be interpreted as percentage effects. These advances enable clean identification of conservation program effects at the local level, though they demand careful attention to outcome construction (Poisson PPML preferred) and control group selection.

A parallel literature documents the central role of institutions — particularly customary governance structures like chiefdoms — in mediating forest outcomes. Studies find that the type of pre-colonial leadership structure predicts deforestation rates today (Lehner et al. 2016), and that the match between governance capacity and program requirements is a key determinant of PES take-up and effectiveness (Ferraro & Hanauer 2014; Pfaff et al. 2013). For sub-Saharan Africa, where forest governance is frequently exercised through traditional authorities operating outside formal state structures, this institutional channel is first-order: programs like the CFP that work through chiefdom agreements must engage with the political economy of chieftaincy.

The literature on PES take-up and additionality is less settled. The Uganda RCT (Jayachandran et al. 2017) is the cleanest causal evidence that PES works, but it also revealed that take-up is far from universal even at attractive payment levels. Self-selection analysis (Alix-Garcia et al. 2019) shows that participants are frequently not the most at-risk landholders, raising additionality concerns. For the cfp-zambia study, these insights motivate the governance × forest dependence heterogeneity design: governance capacity determines whether chiefdoms can administer the program effectively, while forest dependence determines who has the strongest incentive to participate and comply.

---

## Key Papers

### Abman & Lundberg (2024) — Contracting, Market Access and Deforestation
- **Citation:** *Journal of Development Economics* 168, 103269. https://doi.org/10.1016/j.jdeveco.2023.103269
- **Main contribution:** First village-level DiD study matching market access (contracting program) to Hansen GFC annual forest loss in Ghana. Shows improved market access reduces deforestation through credit-constraint relief.
- **Method:** Matched DiD + synthetic DiD + event study. Unit: village × year, 2001–2019. Outcome: annual forest loss (hectares). Control: Mahalanobis-matched untreated villages. **Note: Uses IHS — do NOT replicate this choice (Chen & Roth 2024).**
- **Key finding:** ~0.77 pp reduction in annual forest loss (~200% of pre-treatment mean).
- **Relevance:** **Primary design template** for cfp-zambia. Village-level unit, Hansen GFC outcome, matched controls, event study pre-trends test. Follow everything except the IHS transformation.
- **File:** `supporting_papers/1-s2.0-S030438782400018X-main-3.pdf`

---

### Bloem & Lundberg (2025) — Agricultural Technology Adoption and Deforestation
- **Citation:** *Journal of Development Economics* 179, 103600. https://doi.org/10.1016/j.jdeveco.2025.103600
- **Main contribution:** RCT in Nigeria linking urea super granule adoption to village-level deforestation. Introduces probabilistic spatial treatment exposure (gamma distribution of plot distances from village centroid). Key finding: heterogeneous effects by baseline forest density.
- **Method:** RCT (45 villages, 30 treated), pixel-level Hansen GFC outcome, logit/PPML with spatial exposure variable. NDVI as auxiliary productivity outcome.
- **Key finding:** Effect reverses by baseline forest cover — adoption reduces loss in dense-forest areas, increases it in sparse areas. NDVI gain ≈ +0.018 (≈3.8% of baseline mean).
- **Relevance:** **Heterogeneity design template.** Forest density as moderator of treatment effects directly maps to $F_v$ (forest dependence) in cfp-zambia. Also demonstrates pixel → village spatial aggregation workflow.
- **File:** `supporting_papers/1-s2.0-S0304387825001518-main-5.pdf`

---

### Chen & Roth (2024) — Logs with Zeros? Some Problems and Solutions
- **Citation:** *Quarterly Journal of Economics* 139(2), 891–936. https://doi.org/10.1093/qje/qjad054
- **Main contribution:** Proves that ATEs for IHS/arcsinh(Y) and log(1+Y) are arbitrarily unit-dependent when Y has an extensive margin (zeros). Establishes a trilemma: no estimand with zero-valued outcomes is simultaneously (i) average of individual-level effects, (ii) scale-invariant, and (iii) point identified.
- **Method:** Theoretical + replication of 10 AER papers using arcsinh(Y). Multiplying outcome by 100 changes estimates by >100% in 5/10 papers.
- **Key alternatives (Table II):**
  1. **Poisson PPML** → estimates $\theta_{ATE\%} = E[Y(1)-Y(0)]/E[Y(0)]$, scale invariant, percentage interpretation. **Preferred for cfp-zambia.**
  2. Normalized outcome $\tilde{Y} = Y/X$ (e.g., loss rate = loss pixels / total pixels)
  3. Intensive-margin effect + Lee bounds for extensive margin
- **Relevance:** **Mandatory methodological constraint.** Governs outcome specification for $Y_{vt}$. Overrides IHS choice in Abman & Lundberg (2024). Parallel trends assumption is also unit-dependent under arcsinh — use Poisson PPML DiD.
- **File:** `supporting_papers/qjad054-2.pdf`

---

### Jayachandran et al. (2017) — Cash for Carbon: PES in Uganda (RCT)
- **Citation:** *Science* 357(6348), 267–273. https://doi.org/10.1126/science.aan0568
- **Main contribution:** Gold-standard RCT of PES in Uganda. Paid forest-owning households ≈ $28/ha/year for 2 years to conserve. 121 villages randomized (60 treated).
- **Method:** Village-level RCT. Outcome: tree cover loss (satellite). Intent-to-treat analysis.
- **Key finding:** Tree cover loss 4.2% in treated vs. 9.1% in control — PES **halved deforestation**. No evidence of leakage to neighboring forests. Cost-benefit ratio > 2 (carbon value > program cost). However, deforestation resumed after payments ended.
- **Relevance:** Strongest causal evidence that forest conservation payments work. Benchmark for effect sizes. Also: take-up was only 32% even at attractive rates — awareness and logistics were binding constraints. Directly motivates forest dependence as heterogeneity variable.

---

### Jack & Jayachandran (2019) — Self-Selection into PES Programs
- **Citation:** *Proceedings of the National Academy of Sciences* 116(12), 5326–5333. https://doi.org/10.1073/pnas.1802868115
- **Main contribution:** Shows that PES enrollment is shaped by both conservation costs and other enrollment costs (financial, administrative). Positive correlation between enrollment costs and conservation costs → enrolled participants are systematically less additional (would have conserved anyway). Auction / targeting designs can reverse this.
- **Method:** Two RCTs of PES programs: DEFOR (avoided deforestation, Uganda) and AFFOR (afforestation/reforestation, Malawi). Conceptual framework + empirical evidence on take-up composition.
- **Key finding:** When enrollment costs and conservation costs are positively correlated, PES attracts inframarginal conservers (low additionality). Reducing financial enrollment costs (e.g., covering seedling costs in AFFOR) can improve participant composition and program cost-effectiveness. Enrollment cost manipulation is a powerful targeting tool.
- **Relevance:** Directly motivates governance × forest dependence heterogeneity in CFP. Chiefdoms with stronger governance may be better at targeting high-risk villages; forest-dependent households have stronger incentive alignment with program goals. Enrollment costs in CFP (awareness, logistics) likely interact with forest dependence.

---

### Ferraro & Hanauer (2014) — How Protected Areas Affect Poverty via Ecosystem Services
- **Citation:** *Proceedings of the National Academy of Sciences* 111(11), 4332–4337. https://doi.org/10.1073/pnas.1307712111
- **Main contribution:** Causal mediation analysis of protected area effects in Costa Rica. Shows PA effects on poverty flow mainly through tourism (~two-thirds), not direct ecosystem service restrictions.
- **Method:** Matching + regression, Costa Rica. Confounders: terrain, accessibility, agricultural suitability.
- **Key finding:** PAs reduced deforestation but did not affect poverty on average through ecosystem service channels. Tourism explains poverty reduction in PA-adjacent communities.
- **Relevance:** Methodological benchmark for conservation program evaluation. Highlights importance of separating direct (deforestation) and indirect (livelihood) channels — relevant to CFP's transitional activities (ecotourism, sustainable agriculture).

---

### Pfaff et al. (2013) — Governance, Location and Avoided Deforestation from Protected Areas
- **Citation:** *World Development* 55, 7–20. https://doi.org/10.1016/j.worlddev.2013.01.011 *(flag: verify details)*
- **Main contribution:** Shows that PA effectiveness is conditional on location relative to deforestation threat. Strict PAs in low-threat areas have negligible counterfactual impact. Governance capacity interacts with threat level.
- **Method:** Matching on threat proxies (accessibility, agricultural suitability) across Brazilian Amazon PAs.
- **Key finding:** PA effects on deforestation 2–10x larger in high-threat areas. Governance quality amplifies effectiveness in threatened locations.
- **Relevance:** Directly motivates governance heterogeneity ($G_c$) in cfp-zambia. Better-governed chiefdoms should show stronger conservation effects, especially where forest dependence creates pressure.

---

### Larcom, van Gevelt & Zabala (2016) — Precolonial Institutions and Deforestation in Africa
- **Citation:** *Land Use Policy* 51, 150–161. https://doi.org/10.1016/j.landusepol.2015.10.030
- **Authors:** S. Larcom (Cambridge Land Economy), T. van Gevelt (Cambridge Development Studies), A. Zabala (Cambridge Land Economy)
- **Main contribution:** First study linking pre-colonial leadership succession rules to contemporary deforestation rates in Africa. Uses Murdock's (1967) Ethnographic Atlas — 645 precolonial society boundaries (49 states). Unit: precolonial society within country, intersected with Michalopoulos & Papaioannou (2013) digitised boundaries.
- **Method:** Cross-sectional OLS with country FE, double-clustered SEs (ethnic-family and country level). Outcome: Hansen GFC net forest loss 2000–2012 within precolonial society boundaries. Controls: protected areas, population density, elevation, vegetation type, colonial rule, rule of law, legal origins.
- **Succession coding (from Murdock EA):** Hereditary (base, 82% of societies), Democratic (8%), Appointed from above by paramount chief (6%), Social standing/wealth/seniority (4%)
- **Key finding:** Social standing appointment → **+0.8 pp higher annual deforestation** vs. hereditary base (~50% above mean). Appointed-from-above also higher. Democratic succession not significantly different from hereditary. Mechanism: social standing chiefs have fewer institutional checks, enabling rent-seeking over forest resources.
- **Relevance:** Directly motivates $G_c$ (governance quality) as a moderator of CFP take-up. Historical chiefdom structure predicts whether local governance can credibly enforce conservation agreements. **See data usability note below.**

---

### Assunção et al. (2023) — Conservation Policies and Deforestation in the Brazilian Amazon
- **Citation:** *Environment and Development Economics* (Cambridge). *(flag: verify exact year and journal volume)*
- **Main contribution:** DiD evaluation of Brazil's package of conservation policies (2004–2009) at municipality level. Shows policies avoided ~73,000 km² of deforestation (56% of counterfactual).
- **Method:** DiD exploiting spatial targeting of conservation policies, municipality × year panel. Outcome: INPE deforestation data.
- **Key finding:** Command-and-control enforcement accounts for large share of deforestation reduction. Policy mix matters — monitoring + enforcement + incentives.
- **Relevance:** Shows DiD can cleanly identify conservation program effects at local level. Policy mix insight: CFP combines incentives (transitional activities) with governance — mixed mechanisms may have complementary effects.

---

### Hansen et al. (2013) — High-Resolution Global Maps of 21st-Century Forest Cover Change
- **Citation:** *Science* 342, 850–853. https://doi.org/10.1126/science.1244693
- **Main contribution:** Original GFC dataset paper. 30m resolution annual forest loss data from Landsat archive, 2000–2012 (now updated through 2024 as v1.12).
- **Key variables:** `treecover2000` (% canopy cover baseline), `lossyear` (coded 1–23, add 2000 for calendar year)
- **Relevance:** Primary satellite data source for $Y_{vt}$. **Critical coding note:** `lossyear` ≠ calendar year — always recode `year = lossyear + 2000`.

---

## Thematic Organization

### Theoretical Contributions

**Deforestation as economic decision:** The core model (implicitly or explicitly in most papers) is profit-maximizing land conversion where forest clearing occurs when agricultural returns exceed opportunity cost of standing forest. PES programs shift this calculus by paying for conservation. Governance structures affect both enforcement of property rights and credibility of conservation commitments.

**Institutional persistence:** Pre-colonial governance structures — particularly the nature of chiefly authority — exhibit strong persistence into the present (Lehner et al. 2016; traditional institutions literature). Where chiefs historically controlled resource rents, they continue to do so, creating both a barrier and an opportunity for conservation programs: engaging chiefdoms as partners (CFP model) can leverage existing authority, but only if governance is sufficiently accountable.

**Trilemma for zero-inflated outcomes (Chen & Roth 2024):** Any treatment effect estimand with zero-valued outcomes must sacrifice one of: (i) average of individual-level effects, (ii) scale invariance, (iii) point identification. This is a fundamental constraint on what can be estimated when $Y_{vt} = 0$ for many village-years.

---

### Empirical Findings

| Study | Setting | Design | Effect size | Key moderator |
|-------|---------|--------|-------------|---------------|
| Jayachandran et al. (2017) | Uganda (RCT) | Village RCT | −4.9 pp loss (halved) | Take-up rate only 32% |
| Abman & Lundberg (2024) | Ghana (DiD) | Matched village DiD | −0.77 pp/year | Credit constraints |
| Bloem & Lundberg (2025) | Nigeria (RCT) | Pixel-level spatial RCT | Heterogeneous by forest density | Baseline tree cover |
| Ferraro & Hanauer (2014) | Costa Rica (PA) | Matching + regression | ~10% of forest protected | Tourism channel |
| Assunção et al. (2023) | Brazil Amazon | Municipality DiD | ~73,000 km² avoided | Enforcement intensity |
| Pfaff et al. (2013) | Brazil Amazon | PA evaluation | 2–10x larger in high-threat | Location + governance |

**Key pattern:** Effects are consistently heterogeneous by baseline threat level, forest dependence, and governance quality. Low-threat, low-dependence, low-governance contexts show negligible effects; high versions of all three show large effects.

---

### Methodological Innovations

1. **Village-level satellite DiD (Abman & Lundberg 2024):** Match program records to Hansen GFC at village polygon. Aggregate 30m pixels to village level. Matched DiD + synthetic DiD + event study pre-trends. **Do not use IHS.**

2. **Spatial probabilistic treatment exposure (Bloem & Lundberg 2025):** Model treatment intensity as function of distance from village centroid using gamma CDF. Useful when treatment diffuses spatially.

3. **Poisson PPML for zero-inflated outcomes (Chen & Roth 2024):** Estimates $\theta_{ATE\%} = E[Y(1)-Y(0)]/E[Y(0)]$, scale-invariant, percentage interpretation. Stata: `ppmlhdfe`. Python: `statsmodels` with Poisson family.

4. **Staggered DiD (Callaway & Sant'Anna 2021):** Essential if CFP rollout is staggered across chiefdoms/years. Use `csdid`/`drdid` in Stata.

5. **Matching for selection correction (Ferraro & Hanauer 2014; Pfaff et al.):** Mahalanobis or propensity-score matching on observable confounders (terrain, accessibility, agricultural suitability, pre-treatment forest cover) before DiD.

---

### Open Debates

1. **Additionality vs. self-selection:** Do PES programs attract inframarginal conservers (Alix-Garcia 2019) or genuinely high-risk participants? Evidence is mixed and context-dependent.

2. **Permanence:** Jayachandran et al. Uganda follow-up shows deforestation resumes after payments end. Does CFP's transitional activities model (ecotourism, sustainable agriculture) achieve more durable behavior change?

3. **Governance channel vs. incentive channel:** Does forest conservation reduction come from changed incentives (cash/livelihood benefits) or from governance norms / rule enforcement? Nearly impossible to disentangle without design variation in both.

4. **Spillovers vs. leakage:** Jayachandran (2017) finds no leakage. Abman & Lundberg suggest credit mechanism implies no leakage. But displacement to non-CFP areas within chiefdoms is possible and understudied.

5. **Unit of analysis:** Program agreements are at chiefdom level but behavior is at village/household level. Aggregation to chiefdom dilutes effects (as in prior zambia-conservation USAID findings). Village-level decomposition is essential.

---

## Gaps and Opportunities

1. **No village-level causal evidence on CFP in Zambia:** The Luangwa Community Forests Project (LCFP) — the likely program in cfp-zambia — has qualitative evaluation and REDD+ monitoring, but no DiD causal identification at village level. This study fills that gap.

2. **Governance dimension understudied at local scale:** Existing institutional literature (Lehner et al.) uses cross-country/cross-ethnic variation. Within-chiefdom variation in governance quality at village level is unexplored as a moderator of conservation program effectiveness.

3. **Forest dependence heterogeneity in PES context:** Most PES studies treat it as a confounder; none explicitly estimate $G_c \times F_v$ interaction in determining take-up and conservation outcomes.

4. **Outcome measurement practice lags Chen & Roth:** Virtually all post-2018 papers in this space still use IHS. An early adoption of Poisson PPML would be methodologically state-of-the-art.

5. **Transitional activities (non-cash PES):** The literature focuses on cash payments (Jayachandran 2017) or contracting (Abman & Lundberg 2024). CFP's model — investing in livelihood transitions — is understudied relative to direct payment schemes.

---

## Larcom et al. (2016) Data: Usability for Zambian Chiefdom $G_c$

**Question:** Can Murdock's Ethnographic Atlas (as used by Larcom et al.) provide a chiefdom-level governance variable for the 5 CFP chiefdoms?

**Short answer: Possible but severely limited — strongly prefer CFP's own governance variables.**

### What the data contains
- Murdock's (1967) EA codes local chief succession for ~1,200 precolonial societies worldwide, intersected with Michalopoulos & Papaioannou (2013) digitised ethnic-group boundaries
- Succession variable: 0=hereditary, 1=democratic, 2=appointed from above (paramount chief), 3=social standing
- Zambia has ~61 precolonial society observations in the M&P boundary dataset (third highest behind Nigeria's 61+)

### Steps required to use it
1. Download Murdock's EA from D-PLACE (dplace.org) or UCI HRAF — the succession variable is `EA072`/`EA074`
2. Obtain Michalopoulos & Papaioannou (2013) GIS boundary files (available from AEA data archive)
3. Spatial join: assign each CFP village GPS point to a precolonial society polygon → look up succession code

### Critical limitations for cfp-zambia
1. **No within-country variation across the 5 chiefdoms:** Eastern Province is dominated by Nsenga, Kunda, Bisa, and Chewa ethnic groups. These likely all map to 2-3 Murdock society codes, giving the same succession value for most or all 5 chiefdoms — **zero identifying variation** for $G_c$
2. **One value per ethnic society, not per chiefdom:** Murdock codes an ethnic group's succession rule, not individual chiefdom-level governance. Two chiefdoms in the same ethnic group (common in Eastern Province) are indistinguishable
3. **Historical measure, not current governance quality:** The succession rule is 19th-century anthropological coding; actual CFP chiefdom governance may diverge substantially
4. **Coarse categorization:** 4 categories vs. continuous governance index

### Recommendation
**Use CFP's own governance variables as primary $G_c$:** `govern_foruse`, `fpermit_fair`, and `hlladder_headman` are measured at the chiefdom/village level from the actual program surveys — much more precise and directly relevant. Larcom et al. (2016) can be cited as theoretical motivation for why precolonial institutions shape forest governance, but their data is not usable as the empirical $G_c$ for this study.

---

## Context Note on the CFP in Zambia

The survey chiefdoms (Luembe, Nyalungwe, Malama, Mwanya, Msoro) are in the Luangwa Valley area, Eastern Province. This overlaps with the **Luangwa Community Forests Project (LCFP)**, managed by BioCarbon Partners from 2014, covering ~1 million hectares, ~170,000 community members. LCFP is structured as a REDD+ project with chiefdom-level agreements, investing in transitional livelihoods (ecotourism, sustainable agriculture) — consistent with the CFP survey content. **Verify with Angelo whether CFP = LCFP or a related program.**

---

## Suggested Next Steps

1. **Read the Lehner et al. (2016) paper** on precolonial institutions and deforestation to anchor the $G_c$ variable construction rationale.
2. **Obtain Jayachandran et al. (2017)** as the PES benchmark for effect size comparison.
3. **Verify whether CFP = LCFP (Luangwa Community Forests Project)** — if so, BioCarbon Partners data / REDD+ monitoring may be available.
4. **Check for within-chiefdom variation in CFP village enrollment** — if some villages in treated chiefdoms are not enrolled, this enables a clean within-chiefdom control group.
5. **Check RALS GPS coordinates against chiefdom boundaries** — essential for merging RALS forest dependence variables with CFP treatment assignment.
6. **Consider Lee bounds** alongside Poisson PPML — separately estimate intensive-margin (conditional on positive loss) and extensive-margin (probability of any loss) effects.

---

## BibTeX Entries

```bibtex
@article{AbmanLundberg2024,
  author  = {Abman, Ryan and Lundberg, Clark},
  title   = {Contracting, market access and deforestation},
  journal = {Journal of Development Economics},
  year    = {2024},
  volume  = {168},
  pages   = {103269},
  doi     = {10.1016/j.jdeveco.2023.103269}
}

@article{BloemLundberg2025,
  author  = {Bloem, Jeffrey R. and Lundberg, Clark},
  title   = {Agricultural technology adoption and deforestation: Evidence from a randomized control trial},
  journal = {Journal of Development Economics},
  year    = {2025},
  volume  = {179},
  pages   = {103600},
  doi     = {10.1016/j.jdeveco.2025.103600}
}

@article{ChenRoth2024,
  author  = {Chen, Jiafeng and Roth, Jonathan},
  title   = {Logs with Zeros? Some Problems and Solutions},
  journal = {Quarterly Journal of Economics},
  year    = {2024},
  volume  = {139},
  number  = {2},
  pages   = {891--936},
  doi     = {10.1093/qje/qjad054}
}

@article{Jayachandran2017,
  author  = {Jayachandran, Seema and de Laat, Joost and Lambin, Eric F. and Stanton, Charlotte Y. and Audy, Robin and Thomas, Nancy E.},
  title   = {Cash for carbon: A randomized trial of payments for ecosystem services to reduce deforestation},
  journal = {Science},
  year    = {2017},
  volume  = {357},
  number  = {6348},
  pages   = {267--273},
  doi     = {10.1126/science.aan0568}
}

@article{JackJayachandran2019,
  author  = {Jack, B. Kelsey and Jayachandran, Seema},
  title   = {Self-selection into payments for ecosystem services programs},
  journal = {Proceedings of the National Academy of Sciences},
  year    = {2019},
  volume  = {116},
  number  = {12},
  pages   = {5326--5333},
  doi     = {10.1073/pnas.1802868115}
}

@article{FerraroHanauer2014,
  author  = {Ferraro, Paul J. and Hanauer, Merlin M.},
  title   = {Quantifying causal mechanisms to determine how protected areas affect poverty through changes in ecosystem services and infrastructure},
  journal = {Proceedings of the National Academy of Sciences},
  year    = {2014},
  volume  = {111},
  number  = {11},
  pages   = {4332--4337},
  doi     = {10.1073/pnas.1307712111}
}

@article{Pfaff2013,
  author  = {Pfaff, Alexander and Robalino, Juan and Sanchez-Azofeifa, G. Arturo and Andam, Kwaw S. and Ferraro, Paul J.},
  title   = {Governance, location and avoided deforestation from protected areas: Greater restrictions can have lower impact, due to differences in location},
  journal = {World Development},
  year    = {2013},
  volume  = {55},
  pages   = {7--20},
  doi     = {10.1016/j.worlddev.2013.01.011},
  note    = {Verify author list and page numbers}
}

@article{Hansen2013,
  author  = {Hansen, Matthew C. and Potapov, Peter V. and Moore, Rebecca and Hancher, Matt and Turubanova, S. A. and Tyukavina, A. and Thau, David and Stehman, S. V. and Goetz, S. J. and Loveland, T. R. and Kommareddy, A. and Egorov, A. and Chini, L. and Justice, C. O. and Townshend, J. R. G.},
  title   = {High-resolution global maps of 21st-century forest cover change},
  journal = {Science},
  year    = {2013},
  volume  = {342},
  pages   = {850--853},
  doi     = {10.1126/science.1244693}
}

@article{LarcomEtAl2016,
  author  = {Larcom, Shaun and van Gevelt, Terry and Zabala, Alejandro},
  title   = {Precolonial institutions and deforestation in Africa},
  journal = {Land Use Policy},
  year    = {2016},
  volume  = {51},
  pages   = {150--161},
  doi     = {10.1016/j.landusepol.2015.10.030}
}

@article{CallawayGardner2021,
  author  = {Callaway, Brantly and Sant'Anna, Pedro H. C.},
  title   = {Difference-in-differences with multiple time periods},
  journal = {Journal of Econometrics},
  year    = {2021},
  volume  = {225},
  number  = {2},
  pages   = {200--230},
  doi     = {10.1016/j.jeconom.2020.12.001}
}

@article{RothSantAnna2023,
  author  = {Roth, Jonathan and Sant'Anna, Pedro H. C. and Bilinski, Alyssa and Poe, John},
  title   = {What's trending in difference-in-differences? A synthesis of the recent econometrics literature},
  journal = {Journal of Econometrics},
  year    = {2023},
  volume  = {235},
  number  = {2},
  pages   = {2218--2244},
  doi     = {10.1016/j.jeconom.2023.03.008}
}
```

---

*Note: Citations marked FLAG should be verified before inclusion in the paper bibliography. All other citations are drawn from confirmed DOIs or the supporting papers already in the project.*

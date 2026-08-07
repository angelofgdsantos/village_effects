# Plan: Workflow Configuration for village_effects_cfp

**Status:** COMPLETED
**Date:** 2026-04-15
**Author:** Claude (plan-first workflow)

---

## Context

Angelo is starting a new research project — **village_effects_cfp** — that investigates the effects of the CFP (Community Forestry Programme) on deforestation at the chiefdom village level in Zambia. The program invests in transitional activities (ecotourism, sustainable agriculture). The key research angles are: (1) whether CFP reduces village-level deforestation, (2) whether effects are moderated by chiefdom governance quality and degree of forest dependence.

This is the first session with this repo. The template repo has extensive infrastructure already in place (agents, rules, skills, hooks) but all configuration files carry generic placeholders (`[YOUR PROJECT NAME]`, etc.) or reference a prior project (`zambia-conservation` USAID program). The goal of this plan is to swap all generic/prior-project content for CFP-specific content, so that from session 2 onward every agent, hook, and rule has correct project context baked in.

---

## Scope

Files to modify (6 total):

| File | Change |
|------|--------|
| `CLAUDE.md` | Fill all placeholders; add project description, paper state table |
| `README.md` | Fill all placeholders |
| `.claude/rules/knowledge-base-template.md` | Complete rewrite: CFP-specific notation, treatment groups, data, estimands, anti-patterns |
| `.claude/WORKFLOW_QUICK_REF.md` | Update project name; add CFP-specific specification conventions |
| `MEMORY.md` | Add project memory entry linking to plan and key decisions |
| `01_project_planning/quality_reports/session_logs/2026-04-15_workflow-setup.md` | Create initial session log (also satisfies the stop-hook requirement) |

Files to leave unchanged: all `.claude/rules/`, `.claude/agents/`, `.claude/skills/`, `.claude/hooks/` — these are already generic and work as-is.

---

## Detailed Changes

### 1. `CLAUDE.md`

Replace placeholders:
- `[YOUR PROJECT NAME]` → `Village Effects of the CFP Program`
- `[SHORT-SLUG]` → `cfp-zambia`
- `[YOUR INSTITUTION]` → `University of Pennsylvania — Population Studies Center`
- Project description (1–3 sentences): "This paper estimates the effect of the Community Forestry Programme (CFP) on deforestation at the village level in Zambia. CFP invested in transitional livelihood activities (ecotourism, sustainable agriculture) across chiefdom-level units. We use variation in CFP take-up across chiefdoms — moderated by governance quality and forest dependence — to identify local deforestation effects."
- **Current Paper State table**: all sections → `Blank` / `Not started`
- **Branch**: `main`

### 2. `README.md`

Replace placeholders with same project info as CLAUDE.md. Description: concise 2-sentence abstract.

### 3. `.claude/rules/knowledge-base-template.md` (full rewrite)

This is the file Claude reads before writing any paper/slide/analysis content. It needs to capture CFP-specific knowledge so future sessions don't require re-briefing.

**New content will include:**

**Project Summary**
- Paper: Village-Level Deforestation Effects of the CFP Programme in Zambia
- Method: DiD / staggered adoption, village × year panel
- Outcome: Annual tree cover loss (Hansen GFC)
- Unit: Village $v$, year $t$, within chiefdom $c$
- Moderators: Governance dimension (chiefdom political institutions) × Forest dependence dimension (RALS survey)

**Notation Registry**
- Village index: $v$
- Year index: $t$
- Chiefdom index: $c$
- CFP treatment: $D_{vt}$ (village-level CFP take-up)
- Governance score: $G_c$ (chiefdom-level)
- Forest dependence: $F_v$ (village-level, from RALS)
- Outcome: $Y_{vt}$ (binary tree cover loss, Hansen GFC)
- ATT: $\tau^{ATT}$

**Treatment Groups**
- CFP villages (treated)
- Non-CFP villages, same chiefdom (within-chiefdom control)
- Non-CFP villages, different chiefdom (pure control)

**Key Estimands**
- Main ATT: effect of CFP on $Y_{vt}$
- Heterogeneity by $G_c$ (governance dimension)
- Heterogeneity by $F_v$ (forest dependence dimension)
- Possible spillovers to neighboring non-CFP villages

**Data Sources**
- Hansen GFC (30m → aggregated to village level)
- CFP programme data (village-level treatment assignment + timing)
- RALS survey (Zambia Rural Agricultural Livelihoods Survey) — forest dependence, household characteristics
- Chiefdom boundaries (Administrative boundaries)
- Governance data (chiefdom-level political institutions index)
- Satellite data (NDVI, other vegetation indices if needed)
- Reference paper: `01_project_planning/supporting_docs/supporting_papers/1-s2.0-S030438782400018X-main-3.pdf`

**Anti-Patterns**
- Treating entire chiefdom as treated when only some villages are in CFP
- Using forest stock (not annual loss flow) as outcome
- Ignoring Hansen GFC lossyear coding (needs +2000 offset)
- Conflating governance effect with forest dependence effect in a single heterogeneity index
- Interpreting null effect at chiefdom level as "program failed" (could be dilution)

**Code Conventions**
- Spatial: `geopandas`, `rasterio`, `xarray` (Python); `spmap` (Stata maps)
- Regressions: `reghdfe` (TWFE), `csdid`/`drdid` (staggered DiD)
- Village-level cluster SEs throughout
- Output always: `03_analysis/figures/` or `03_analysis/tables/` (working); `06_final_output/` (final)

**Key References**
- Reference paper (1-s2.0-S030438782400018X): local deforestation effects benchmark
- Callaway & Sant'Anna (2021): staggered DiD
- Roth et al. (2023): pre-trends and sensitivity
- Ferraro & Hanauer (2014): conservation program evaluation methodology
- RALS documentation (Zambia household survey)

### 4. `.claude/WORKFLOW_QUICK_REF.md`

- Change title from `zambia-conservation` → `cfp-zambia`
- Add CFP-specific specification note: cluster SEs at village level; absorb village FE + year FE; report heterogeneity by governance and forest dependence separately

### 5. `MEMORY.md`

Add entry:
```
- [Project: CFP Zambia](01_project_planning/quality_reports/plans/staged-strolling-sphinx.md) — village_effects_cfp setup; workflow configured 2026-04-15
```

### 6. Initial Session Log

Create `01_project_planning/quality_reports/session_logs/2026-04-15_workflow-setup.md` using the template at `01_project_planning/templates/session-log.md`. Content: goal (configure workflow for cfp-zambia), key context (data sources, research question, heterogeneity dimensions), decisions made (project slug, notation, treatment groups).

---

## Proposed Customizations Beyond Placeholders

1. **No lecture/slides infrastructure needed yet**: The Beamer/Quarto sync rules are in place but irrelevant for now. No action — they won't interfere.

2. **RALS survey specificity**: The RALS is a rich panel household survey. Once we start working with it, we may want to add a `rals-codebook.md` to `.claude/rules/` so Claude always knows variable names. Flag for future session.

3. **Heterogeneity indexing**: Governance ($G_c$) and forest dependence ($F_v$) are likely constructed variables. We should track their construction scripts explicitly in the knowledge base once built.

4. **Reference paper methodology**: The benchmark paper (1-s2.0-S030438782400018X) should be read at the start of the empirical strategy session to anchor the specification. Not reading it now to stay focused.

---

## Verification

After implementation:
1. Open `CLAUDE.md` — confirm no `[YOUR PROJECT NAME]` or similar placeholders remain
2. Open `.claude/rules/knowledge-base-template.md` — confirm it reflects CFP project (not USAID/zambia-conservation)
3. Open `.claude/WORKFLOW_QUICK_REF.md` — confirm project name updated
4. Open `01_project_planning/quality_reports/session_logs/2026-04-15_workflow-setup.md` — confirm it exists and satisfies the stop-hook (log-reminder.py)
5. Trigger stop-hook manually or end session — confirm no blocking error

---

## Execution Order

1. Create session log (unblocks stop-hook)
2. Update CLAUDE.md
3. Update README.md
4. Rewrite knowledge-base-template.md
5. Update WORKFLOW_QUICK_REF.md
6. Update MEMORY.md
7. Verify all files — spot-check for remaining placeholders

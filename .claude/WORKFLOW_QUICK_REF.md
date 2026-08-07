# Workflow Quick Reference — cfp-zambia

**Model:** Contractor (Angelo directs, Claude orchestrates)

---

## The Loop

```
Your instruction
    ↓
[PLAN] (if multi-file or unclear) → Show plan → Your approval
    ↓
[EXECUTE] Implement, verify, done
    ↓
[REPORT] Summary + what's ready
    ↓
Repeat
```

---

## I Ask You When

- **Design forks:** "Option A (fast) vs. Option B (robust). Which?"
- **Specification ambiguity:** "Spec unclear on clustering choice. Village-level is default; confirm if chiefdom-level wanted."
- **Replication edge case:** "Estimates off by >1e-4. Investigate deeper?"
- **Scope question:** "Also refactor table format while here, or focus on regression?"

---

## I Just Execute When

- Code fix is obvious (bug, pattern application)
- Verification (compile, render, tolerance checks)
- Documentation (logs, commits, READMEs)
- Plotting (per established standards below)
- Deployment (after approval, I ship automatically)

---

## Quality Gates (No Exceptions)

| Score | Action |
|-------|--------|
| >= 80 | Ready to commit |
| < 80  | Fix blocking issues |

---

## Non-Negotiables

- **Paths:** Always relative — no hardcoded `/Users/angelosantos/...` in any script
- **Python scripts:** Must have the standard header docstring (Author, Date, Title, Description, Usage, Parts, Inputs, Outputs) as defined in global CLAUDE.md
- **Stata do-files:** Numbered prefixes (`10_`, `11_`, `20_`, etc.); `preserve/restore` around any destructive merges; `clear all` + `set more off` at top
- **Figures:** White background; publication-ready (PDF for vector, 300 DPI minimum for raster); maps use colorblind-safe palettes (viridis, ColorBrewer)
- **Output files:** All figures → `outputs/figures/`; all tables → `outputs/tables/`; never write outputs to `sandbox/`
- **Data:** Raw and processed data in `data/` (gitignored); only outputs are committed
- **Stata regressions:** Always specify absorb(), cluster(), and vce() explicitly — never rely on defaults. Default: `absorb(village_id year)`, `cluster(village_id)`
- **Heterogeneity:** Always report governance ($G_c$) and forest dependence ($F_v$) dimensions separately — never collapse into a single index
- **Estimator:** Use `reghdfe` for TWFE; use `csdid`/`drdid` if CFP rollout is staggered across years

---

## Preferences

**Visual:** Publication-ready from the start. No "placeholder" figures in committed code. Maps must have scale bars, north arrows, and clear legends. Color scheme: colorblind-safe.

**Reporting:** Concise bullets in responses; details on request; no trailing summaries restating what was done.

**Session logs:** Always (post-plan, incremental, end-of-session).

**Replication:** Flag any estimate that deviates from paper text by >0.001 in magnitude. Investigate, don't silently patch.

**Ambiguity:** For causal interpretation questions, always default to the more conservative interpretation and flag it.

---

## Exploration Mode

For experimental specifications or exploratory analysis, use the **Fast-Track** workflow:
- Work in `explorations/` folder
- 60/100 quality threshold (vs. 80/100 for production)
- No full plan needed — just a research value check (2 min)
- See `.claude/rules/exploration-fast-track.md`

---

## Next Step

You provide task → I plan (if needed) → Your approval → Execute → Done.

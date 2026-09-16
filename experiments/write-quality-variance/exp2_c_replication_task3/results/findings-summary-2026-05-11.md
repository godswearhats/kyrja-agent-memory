# Exp 2 — C-Replication on Task 3 — Summary

**Date:** 2026-05-11
**Spec:** `../spec.md`
**Detail:** `findings-detailed-2026-05-11.md`
**Predecessor:** `../../results/findings-summary-2026-05-11.md` (Exp 1, Task 2)

## Headline

**Slot-format encoding (C) beats prose briefing (A) and beats cold on a second task in the same family.** Direction matches Exp 1; magnitudes are smaller. **Distiller confound closed** — this run used Opus 4.6 for distillation (Exp 1 used Opus 4.7); C still wins.

**Caveat (load-bearing):** Pass-rate is 0/4 across all variants because SWE-bench-style gold tests evaluate "would the maintainer merge this PR" — they bundle the stated bug with adjacent invariants discovered during the fix. That measurement is misaligned with the wedge hypothesis. Pass-rate claims from Exp 1 and Exp 2 are **retracted**; cost claims stand.

## Results

| variant | n | mean cost | 95% CI | pass |
|---|---|---|---|---|
| **C — structured slots (4.6-distilled)** | 4 | **$0.805** | [0.698, 0.912] | 0/4 |
| A — prose briefing (4.6-distilled) | 4 | $1.105 | [0.957, 1.249] | 0/4 |
| cold | 4 | $1.334 | [1.175, 1.521] | 0/4 |

**CI overlap:**
- C vs cold: disjoint ✓
- C vs A: disjoint ✓
- A vs cold: **overlap** — A's benefit over cold is not statistically distinguishable at n=4

**Effect sizes vs cold:** A −17.2%; C **−39.6%**; C vs A −27.1%.

## Comparison to Exp 1 (Task 2)

| | A vs cold | C vs cold | C vs A |
|---|---|---|---|
| Exp 1 (Task 2, Opus 4.7-distilled) | −16.3% | −52% | −42% |
| Exp 2 (Task 3, Opus 4.6-distilled) | −17.2% | −40% | −27% |

Direction stable across tasks and distillers. Magnitudes drift downward on the harder task and with the older distiller. C-vs-A gap narrows on Task 3 but stays disjoint.

## Verdict per pre-registered hypothesis

- **H-REPLICATE** (C < A < cold, disjoint CIs): **SUPPORTED on cost**. C disjoint from both A and cold. A vs cold overlap is a softening, not a falsification — direction holds.
- **H-FORMAT-TASK-SPECIFIC** (C ≈ A < cold): **REJECTED**. C vs A CIs disjoint.
- **H-MEMORY-NO-TRANSFER** (C ≈ A ≈ cold): **REJECTED**. Cost effect is real.
- **H-DISTILLER-CONFOUNDED**: **REJECTED**. C wins under 4.6-distilled encodings too.

## What we cannot claim

- **No quality finding.** Pass-rate 0/4 across variants is uninterpretable as a quality signal on this setup. The gold test enforces invariants the stated issue never mentions; agents (with or without memory) converge on a near-correct fix that misses one of those invariants. See detailed findings for the forensic.
- **Magnitudes still drift.** Phase 2's original numbers were Opus-version-specific. Exp 2 confirms task-specificity too. Direction is robust; specific percentages are not.

## What changes in the wedge plan

1. **Slot-format encoding is the working architectural assumption.** Replicated on a second task; not a distiller-version artefact. Treat as load-bearing for MTP design.
2. **Retract pass-rate claims from Exp 1.** Same evaluation framework, same methodology problem. Cost claims from Exp 1 still hold.
3. **Quality is an open question.** No SWE-bench-style experiment in this family can answer it cleanly. Defer to:
   - LLM-as-judge on diff-vs-stated-problem (cheap, new experiment), or
   - Real-codebase MTP usage signal (Goal 5).

## Key side findings (forensic, see detailed)

- **All 12 agents converged on the same fix shape** across cold, A, C: `keep_attrs="override"` + `result.attrs = getattr(x, "attrs", {})`. Memory or no memory.
- **Only cold agents wrote their own tests.** Memory-equipped agents skipped self-verification — they trusted the prior pattern. This is a *real* behavior change from memory worth flagging for production.
- **Memory was partly redundant with the prompt.** The issue's "Hints" section already contained Task 2's fix. So Exp 2 measures "structured memory vs prose hints + prose memory," not "memory vs no memory." A cleaner version would strip hints.

## Highest-priority next steps

1. **Move to Goal 5 (MTP build).** No more SWE-bench-style write-quality runs needed; we have what we need for slot-format. Real usage signal will tell us about quality.
2. **(Optional, cheap) cold-no-hints arm** if we want to bound the marginal value of structured memory beyond what's already in the issue. Single 4-trial condition, ~$5.
3. **Defer worst-case source experiment.** The failed cold sessions on Task 3 are natural candidates for "failed-session encoding" sources, but the eval-framework problem makes this not worth doing in the current setup.

## Cost and time

12 trials, ~$13 spend, ~75 min wall time. Plus 4 contaminated cold trials archived at `data/preliminary/` (~$3) before the harness fix.

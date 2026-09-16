---
type: experiment
name: Exp 1 — Write-Quality Variance on Task 2 (where_keep_attrs_scalar)
status: LANDED
last_ingested: 2026-05-12
sources: []
epistemic_tags: [measured]
tags: [wedge, encoding, slot-format, exp1, opus-4-7-distiller]
---

Sub-run of the [write-quality variance investigation](./README.md). Tests [H23-util](../../hypothesis/H23-util.md) (initial), [H24-qual-floor](../../hypothesis/H24-qual-floor.md) (variant D), [H27-qual-structure](../../hypothesis/H27-qual-structure.md) (initial), and [H28-qual-framing](../../hypothesis/H28-qual-framing.md) (A vs B contrast). Cross-run synthesis lives in the [umbrella](./README.md).

## Method

- **Task:** `where_keep_attrs_scalar` (xarray-6461).
- **n:** 40 trials total across 6 variants.
- **Variants:**
  - **A** — prose briefing
  - **B** — summary framing
  - **C** — slot format
  - **D** — truncated-source briefing (tests H-QUAL-FLOOR's mild-degradation regime)
  - **cold** — no memory
  - **A_orig** — Phase 2's original encoding (baseline-of-baseline)
- **Distiller:** Opus 4.7.
- **Agent:** Opus 4.6.

Artefacts:
- Spec: [write-quality-variance-experiment-spec-2026-05-11.md](../../../../research/experiments/write-quality-variance-experiment-spec-2026-05-11.md)
- Results: [experiments/write-quality-variance/results/](../../../../research/experiments/write-quality-variance/results)

## Results

| variant | mean cost | 95% CI | pass |
|---|---|---|---|
| **C — structured slots** | **$0.142** | [0.121, 0.170] | 4/4 |
| D — truncated source briefing | $0.197 | [0.143, 0.251] | 4/4 |
| B — summary framing | $0.200 | [0.139, 0.281] | 3/4 |
| A — prose briefing | $0.247 | [0.215, 0.279] | 3/4 |
| cold | $0.295 | [0.235, 0.356] | 4/4 |
| A_orig (Phase 2 encoding) | $0.300 | [0.256, 0.350] | 4/4 |

C vs A: **−42%**. C vs cold: **−52%**. CIs disjoint for both.

`[MEASURED]` cost — construct-validity note in [umbrella](./README.md#construct-validity-note-load-bearing) applies; this metric measures agent-completion token spend which directly operationalizes the wedge's cost-reduction claim.

Pass-rate column retained for transparency but **retracted as evidence** per the construct-validity note: SWE-bench gold tests evaluate "would the maintainer merge this PR" and bundle the stated bug with adjacent invariants. Pass-rate measures something the wedge hypothesis never claimed.

## Per-run limitations

- **n=4 per variant** is underpowered for distinguishing close variants (e.g. B vs A on framing).
- **Path-mismatches in encodings.** Some Exp 1 memory variants embedded old worktree paths that didn't match the trial's working directory. The agent recovered, but this is a confound on absolute magnitudes (not direction).
- **Opus 4.7 distiller** introduces a model-version confound on the C-win — Exp 2 was designed to close this.

## Spend

~$10, 40 trials, ~75 min wall time (includes a failed Opus 4.7 sweep before settling on the variant set).

## Raw artifacts

- [experiments/write-quality-variance/](../../../../research/experiments/write-quality-variance) (spec, results, encoding files)

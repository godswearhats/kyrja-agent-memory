# Exp 2 — C-Replication on Task 3

**Date:** 2026-05-11
**Status:** Approved by AJ. Amended mid-run (see "Amendment" section).
**Parent:** `experiments/write-quality-variance/spec.md`
**Predecessor findings:** `../results/findings-summary-2026-05-11.md` (single-task slot-format win on Task 2).

## Amendment — 2026-05-11 (mid-run)

After cold × 4 trials with the original harness, two issues forced a halt and design amendment:

1. **Harness evaluation bug.** The agent in 3 of 4 cold trials wrote its own tests in `xarray/tests/test_computation.py`, which caused `git apply` of the gold test_patch to fail ("patch failed: xarray/tests/test_computation.py:1925"). Those trials were inconclusive, not genuine failures — the agent's bug-fixes were real, but couldn't be evaluated. Fix applied: `evaluate_patch` now resets test files modified by the gold patch back to `base_commit` before applying the patch. Preserves agent's source-code fix, discards agent's test additions. Standard SWE-bench-style evaluation.

2. **Task 3 cold is harder than predicted.** Cold mean $0.73 (range $0.55–$0.95) vs Task 2 cold $0.30. Halt rules 5 and 6 both fired. **Resolution:** keep the task; add pass-rate as a co-primary signal alongside cost. On a hard task, a memory-induced swing in pass-rate (cold 1/4 → memory N/4) is arguably a stronger finding than a cost reduction.

The contaminated cold trials are archived at `data/preliminary/`. A fresh cold × 4 + A × 4 + C × 4 sweep was launched after the harness fix.

## Question

Does the slot-format encoding win (C beats prose A by ~40%, beats cold by ~52%) replicate when memory and downstream task shift one step along the same causal chain?

Predecessor (Exp 1) used Task 1 (`where_keep_attrs_add`) as source → Task 2 (`where_keep_attrs_scalar`) as downstream. Exp 2 shifts to Task 2 as source → Task 3 (`where_keep_attrs_coord`) as downstream. Same family, same file in xarray, related-but-distinct bugs.

Simultaneously addresses follow-up #3 by distilling with **Opus 4.6** (Exp 1 distilled with `--model opus`, which resolved to 4.7 — a confound flagged in the findings doc).

## Hypotheses

**H-REPLICATE (primary).** On the second task, C still produces lower trial cost than A, and both produce lower cost than cold. CIs disjoint.

**H-FORMAT-TASK-SPECIFIC (alt).** C ≈ A < cold: memory transfers but format effect is Task-2-specific.

**H-MEMORY-NO-TRANSFER (null).** C ≈ A ≈ cold: memory of Task 2 doesn't help on Task 3 — the causal-chain relevance is too thin one step further.

**H-DISTILLER-CONFOUNDED (sub).** C ≈ A under 4.6-distilled encodings, but C < A under 4.7-distilled encodings in Exp 1 → Exp 1's C win was partly an Opus 4.7 artefact, not a structural property of the slot format.

## Variants

Three only (focused on the core question, lower cost):

- **A** — Phase 2 canonical briefing prompt over Task 2 full transcript. Distilled by Opus 4.6.
- **C** — Structured-slot prompt over Task 2 full transcript. Distilled by Opus 4.6.
- **cold** — No memory injected.

Skipping B (summary) and D (truncated source) for this replication — H-QUAL-FRAMING was inconclusive at n=4 in Exp 1 and H-QUAL-FLOOR was already rejected for mild degradation. Both are addressable later if needed.

## Task

`where_keep_attrs_coord` (pydata__xarray-7229). Tier 1, Task 3 in the Phase 2 chain.

Directly downstream of Task 2: the issue references PR #6461 (Task 2's commit) and the hints show the exact `keep_attrs = lambda attrs, context: getattr(x, "attrs", {})` line from Task 2. Memory relevance is structurally guaranteed.

## Measurement

- **Co-primary (post-amendment):**
  - Pass rate on FAIL_TO_PASS tests (gold-patch evaluated, agent test additions reset).
  - Cost on passing runs only.
- **Secondary:** output tokens, turn count, wall time, mean cost across all runs.
- **n:** 4 per condition × 3 conditions = 12 trials.

## Pre-registered decision rules

| Observation | Conclusion |
|---|---|
| C < A < cold, disjoint CIs | H-REPLICATE supported. Slot format = architectural. Proceed to MTP planning. |
| C ≈ A < cold, overlapping CIs | H-FORMAT-TASK-SPECIFIC supported. Slot win was Task-2-specific. Slot format is *a* good encoding, not the only one. |
| C ≈ A ≈ cold, all overlap | H-MEMORY-NO-TRANSFER. Memory doesn't carry one step. Relevance-gating problem, not encoding problem. |
| A < C clearly | Halt and diagnose. Format hurts on Task 3 — surprising direction, needs investigation before further conclusions. |
| Cold ≫ $0.50 or ≪ $0.15 | Task 3 baseline incomparable to Task 2. Flag and consider expanding n. |
| Cold pass rate < 3/4 | Task 3 is too hard for clean cost comparison; cost is meaningful only on passing runs. Flag and re-scope if needed. |

## Halt conditions

- If at the planned n=4 we cannot distinguish C from A on Task 3 (CIs overlap), do **not** automatically expand to n=8. Instead, declare format-task-specific and move to worst-case source experiment (follow-up #1). Expanding n is only justified if effect direction is clear but variance is wide.
- If pass rate drops below 3/4 on cold, halt and investigate before drawing cost conclusions.

## Artifacts

```
exp2_c_replication_task3/
├── spec.md                       (this doc)
├── sources/
│   └── task2_full.md             (Phase 2 bootstrap transcript)
├── prompts/                      (reused from parent — same A and C prompts)
├── encodings/
│   ├── A_encoding.md             (4.6-distilled)
│   ├── A_meta.json
│   ├── C_encoding.md             (4.6-distilled)
│   └── C_meta.json
├── harness/
│   ├── generate_encoding.py      (forked: 4.6 distiller, Task 2 source)
│   └── run_variant.py            (forked: Task 3 target)
├── data/
│   ├── trials.json
│   └── trial_logs/
└── results/
    ├── findings-summary-2026-05-11.md
    └── findings-detailed-2026-05-11.md
```

## Cost / time

- Distillation: 2 × ~$0.10 ≈ $0.20.
- Trials: 12 × ~$0.20–$0.30 ≈ $2.40–$3.60.
- **Budget cap: $5.**
- Wall time: ~30–45 min sequential.

## Out of scope (deferred)

- Cross-repo (Sphinx) — separate experiment.
- Worst-case source — follow-up #1, separate experiment.
- Multi-model agent — out of wedge scope for now.
- Re-distilling Exp 1's A/B/C/D under 4.6 retroactively — AJ said the new run is sufficient signal.

## What a clean result looks like

If C wins on Task 3 with 4.6-distilled encodings, both the second-task and distiller-confound follow-ups are closed. Slot format becomes the working assumption for the wedge architecture and we can move to MTP planning (Goal 5 in the wedge doc).

If C does *not* win on Task 3, we have to retract "architectural" status for slot format and treat Exp 1's headline as task-specific — a real finding, but a weaker one than what would license MTP design choices.

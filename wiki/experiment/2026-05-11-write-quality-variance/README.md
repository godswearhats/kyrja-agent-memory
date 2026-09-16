---
type: experiment
name: Write-Quality Variance Investigation (Exp 1 + Exp 2)
status: LANDED
last_ingested: 2026-05-12
sources: []
epistemic_tags: [measured]
tags: [wedge, encoding, slot-format, cost-axis]
---

Umbrella for a two-run investigation of how the *format* of distilled memory affects an agent's cost and task quality on causally-related coding tasks. Per-run method, results, and run-specific findings live in the siblings; this page carries the cross-run synthesis.

## Sub-runs

- **[Exp 1 — Task 2 (`where_keep_attrs_scalar`)](./exp1-task2.md)** — 40 trials, 6 variants (A/B/C/D/cold/A_orig), Opus 4.7 distiller. Establishes C-format win and tests the H-QUAL-FLOOR mild-degradation regime.
- **[Exp 2 — Task 3 C-Replication (`where_keep_attrs_coord`)](./exp2-task3-c-replication.md)** — 12 trials, 3 variants (A/C/cold), Opus 4.6 distiller for both A and C. Replicates the C-format win on a different task and closes the distiller-version confound.

## Hypotheses tested

- **[H23-util](../../hypothesis/H23-util.md)** — memory of prior tool-chain sessions reduces cost on causally-related tasks.
- **[H24-qual-floor](../../hypothesis/H24-qual-floor.md)** — bad source produces harmful memory (i.e., a write-side quality gate is mandatory).
- **[H27-qual-structure](../../hypothesis/H27-qual-structure.md)** — prose-format encoding beats slot-format.
- **[H28-qual-framing](../../hypothesis/H28-qual-framing.md)** — briefing-style encoding beats summary-style.
- **[H25-replicate](../../hypothesis/H25-replicate.md)** — Exp 1's slot-format win replicates on a second task.
- **[H26-distiller-confounded](../../hypothesis/H26-distiller-confounded.md)** — Exp 1's slot-format win was an artefact of Opus 4.7 distillation.

## Construct-validity note (load-bearing)

**Cost metric is valid.** Agent-completion token spend directly measures the wedge's promised benefit. `[MEASURED]` is supported across both runs ([exp1-task2](./exp1-task2.md), [exp2-task3-c-replication](./exp2-task3-c-replication.md)).

**Pass-rate metric is invalid for our hypothesis.** SWE-bench gold tests evaluate "would the maintainer merge this PR" — they bundle the stated bug with adjacent invariants the maintainer discovered during the fix. Agents (with or without memory) converge on a near-correct fix that misses the same invariant. This is misaligned with the wedge hypothesis ("memory reduces cost on causally-related tasks") — pass-rate measures something the hypothesis never claimed.

**Pass-rate claims from both experiments are RETRACTED.** Cost claims stand.

This note is load-bearing for every per-run results table in the siblings.

## Verdicts per hypothesis (cross-run synthesis)

- **[H23-util](../../hypothesis/H23-util.md)** (cost reduction with relevant memory): `[MEASURED]` SUPPORTED on [exp1-task2](./exp1-task2.md) and [exp2-task3-c-replication](./exp2-task3-c-replication.md) — direction stable across tasks, distillers, model versions. Magnitudes are model- and task-fragile. *Construct-validity:* see [umbrella note above](#construct-validity-note-load-bearing).
- **[H24-qual-floor](../../hypothesis/H24-qual-floor.md)** (bad source = harmful memory): REJECTED for mild source degradation. Variant D (truncated source) did not degrade — Opus filled gaps by inference. Worst-case (failed session) still untested — see [worst-case-source](../../open-question/worst-case-source.md).
- **[H27-qual-structure](../../hypothesis/H27-qual-structure.md)** (prose > slots): REJECTED *in reverse*. Slots beat prose decisively in both experiments.
- **[H28-qual-framing](../../hypothesis/H28-qual-framing.md)** (briefing > summary): INCONCLUSIVE at n=4. B trends lower than A but CIs overlap.
- **[H25-replicate](../../hypothesis/H25-replicate.md)** (C-win replicates on Task 3): `[MEASURED]` SUPPORTED on cost in [exp2-task3-c-replication](./exp2-task3-c-replication.md). C vs cold and C vs A CIs disjoint. *Construct-validity:* see [umbrella note above](#construct-validity-note-load-bearing).
- **[H26-distiller-confounded](../../hypothesis/H26-distiller-confounded.md)**: REJECTED. C still wins under Opus 4.6 distillation. Slot-format effect is not a distiller-version artefact.

## What changes in the wedge plan

1. **Slot-format encoding is load-bearing for MTP design.** Confirmed across two tasks, two distillers, same agent model. Treat as architectural assumption, not preference.
2. **Pass-rate claims from Exp 1 retracted.** Same evaluation framework, same methodology problem. Cost claims hold.
3. **Quality is an open question.** No SWE-bench-style experiment in this family can answer it cleanly. Deferred to (a) LLM-as-judge on diff-vs-stated-problem, or (b) real-codebase MTP usage signal.
4. **Phase 2 absolute numbers are not load-bearing.** Direction stable; magnitudes drift with model version and task difficulty. Quote direction, not magnitudes.

## Limitations (cross-run)

- n=4 per condition is low; design favoured directional signals over precise magnitudes.
- Single repo family (xarray) — generalization to other code domains untested.
- SWE-bench evaluation framework misaligned with wedge hypothesis (per construct-validity note above).
- Worst-case source (fully-failed session) not tested — H-QUAL-FLOOR rejection holds only for mild degradation. See [worst-case-source](../../open-question/worst-case-source.md).

Per-run limitations (path-mismatches in Exp 1, issue-hint contamination in Exp 2) live in the sibling pages.

## Highest-priority next steps

1. **Move to Goal 5 (MTP build).** No more SWE-bench-style write-quality runs needed; we have what we need for slot-format. Real usage signal will tell us about quality.
2. *(Optional, cheap)* cold-no-hints arm on Task 3 — bound marginal value of structured memory beyond prose hints in the issue. ~$5.
3. **Defer worst-case source experiment.** Failed cold sessions on Task 3 are natural candidates for "failed-session encoding" sources, but the eval-framework problem makes this not worth doing in the current setup.

## Related

- [precision-over-recall](../../decision/precision-over-recall.md) — empirical anchor for the cost-asymmetry argument
- [structured-filter-first](../../decision/structured-filter-first.md) — informed by Exp 2's "memory partly redundant with prompt" finding (see [exp2-task3-c-replication](./exp2-task3-c-replication.md))
- [cascading-failures](../../concept/cascading-failures.md) — the recall-cascade the wedge sidesteps by precision-tuning

---
type: experiment
name: Exp 2 — C-Replication on Task 3 (where_keep_attrs_coord)
status: LANDED
last_ingested: 2026-05-12
sources: []
epistemic_tags: [measured]
tags: [wedge, encoding, slot-format, exp2, opus-4-6-distiller, replication]
---

Sub-run of the [write-quality variance investigation](./README.md). Tests [H25-replicate](../../hypothesis/H25-replicate.md) (whether Exp 1's slot-format win generalizes to a second task) and [H26-distiller-confounded](../../hypothesis/H26-distiller-confounded.md) (whether the slot-format effect was an Opus 4.7 distillation artefact). Re-validates [H23-util](../../hypothesis/H23-util.md) and [H27-qual-structure](../../hypothesis/H27-qual-structure.md) on a new task. Cross-run synthesis lives in the [umbrella](./README.md).

## Method

- **Task:** `where_keep_attrs_coord` (xarray-7229) — a different but related xarray bug to Exp 1's Task 2.
- **n:** 12 trials total across 3 variants.
- **Variants:** A (prose briefing), C (slot format), cold (no memory).
- **Distiller:** **Opus 4.6** for *both* A and C. This closes the distiller-version confound from Exp 1 (which used Opus 4.7 to produce both encodings).
- **Agent:** Opus 4.6.

Artefacts:
- Spec: [exp2_c_replication_task3/spec.md](../../../../research/experiments/write-quality-variance/exp2_c_replication_task3/spec.md)
- Results: [exp2_c_replication_task3/results/](../../../../research/experiments/write-quality-variance/exp2_c_replication_task3/results)

## Results

| variant | n | mean cost | 95% CI | pass |
|---|---|---|---|---|
| **C — structured slots (4.6-distilled)** | 4 | **$0.805** | [0.698, 0.912] | 0/4 |
| A — prose briefing (4.6-distilled) | 4 | $1.105 | [0.957, 1.249] | 0/4 |
| cold | 4 | $1.334 | [1.175, 1.521] | 0/4 |

C vs A: **−27%**. C vs cold: **−40%**. C-vs-A and C-vs-cold CIs disjoint; A-vs-cold overlap.

`[MEASURED]` cost — construct-validity per [umbrella note](./README.md#construct-validity-note-load-bearing). Pass-rate retained for transparency but **retracted as evidence**; same eval-framework misalignment as Exp 1. Task 3 happens to have 0/4 pass across all variants, which is itself a signal that the SWE-bench gold tests for this issue are far from what a memory-equipped agent is solving for.

## Side findings (Exp 2-derived; novel, worth flagging for design)

- **Memory short-circuits self-verification.** Exp 2 forensic: **4/4 cold** agents wrote their own tests; **0/4 A** and **3/4 C** agents skipped this step. Memory-equipped agents trust the prior pattern enough to skip writing verification tests. This is a real behavior change from memory — and a possible production risk. *Design implication:* inject memory as a low-status hint, not as an authoritative prior. Consider explicit prompting that encourages verification regardless of memory presence.
- **Memory is partly redundant with the prompt.** The Task 3 issue's "Hints" section already contained Task 2's fix in prose. So Exp 2 measured "structured memory + prose hints" vs "prose hints alone," **not** "memory vs no memory." Marginal value of structured memory is partly a presentation-format effect on content the agent could have extracted from prose hints. A `cold-no-hints` arm would bound this; ~$5 to run.

## Per-run limitations

- **n=4 per variant** is underpowered; Exp 2 was designed as a focused C-vs-A replication, not a full variant sweep.
- **Single repo family (xarray).** Both Exp 1 and Exp 2 are xarray bugs.
- **Issue-hint contamination** (the redundancy finding above) — Exp 2's cold arm was prose-hints-not-no-memory. Affects effect-size magnitude but not direction.
- **~$3 of contaminated cold trials** archived at `data/preliminary/` before harness fix; not included in the table above.

## Spend

~$13, 12 trials, ~75 min wall time. Plus ~$3 contaminated cold trials archived at `data/preliminary/` before harness fix.

## Raw artifacts

- [exp2_c_replication_task3/](../../../../research/experiments/write-quality-variance/exp2_c_replication_task3) (spec, results, encoding files, preliminary)

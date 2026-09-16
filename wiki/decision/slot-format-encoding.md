---
type: decision
name: Slot-Format Encoding for Memory
status: ACTIVE
last_ingested: 2026-05-13
sources: [../experiment/2026-05-11-write-quality-variance/README.md, ../experiment/2026-05-11-write-quality-variance/exp1-task2.md, ../experiment/2026-05-11-write-quality-variance/exp2-task3-c-replication.md]
epistemic_tags: [measured]
tags: [wedge, encoding, write-path]
---

## Decision

Memory encoding uses a **structured slot format**, not a prose briefing. The body of an encoded memory is a set of named fields (slots) — at minimum: `bug`, `location` (file/function/line), `fix_pattern`, `related_imports_and_utilities`, `dead_ends`, `gotchas`, `verification`. The compound-key fields used for retrieval (`repo`, `path`, `symbol`, `task_type`, `language`, `entities_touched`) overlap with the slot set; some slots are queryable, others are read as part of the memory body.

This collapses two earlier design assumptions — "free-text encoding body" and "structured compound-key extraction" — into a single artifact: the encoding body *is* the compound key.

## Motivation

- **Slot-format beats prose on cost by ~27–42% across two tasks and two distillers.** `[MEASURED]`:
  - Exp 1 (Task 2, Opus 4.7 distiller): C $0.142 vs A $0.247, −42%, disjoint CIs. See [Exp 1 — Task 2](../experiment/2026-05-11-write-quality-variance/exp1-task2.md). *Construct-validity:* cost as primary metric; same source content distilled into different formats, direct format-vs-format comparison.
  - Exp 2 (Task 3, Opus 4.6 distiller): C $0.805 vs A $1.105, −27%, disjoint CIs. See [Exp 2 — Task 3 C-Replication](../experiment/2026-05-11-write-quality-variance/exp2-task3-c-replication.md). *Construct-validity:* same.
  - C also beat cold ($1.33 in Exp 2) — slots reduce cost vs no-memory, not just vs prose memory.
- **Distiller confound CLOSED.** Exp 2 used Opus 4.6 for both A and C distillation. C still won (~27% over A). The Exp 1 win was not an Opus 4.7 artefact. See [H26-distiller-confounded](../hypothesis/H26-distiller-confounded.md).
- **Replication across tasks.** [H25-replicate](../hypothesis/H25-replicate.md) SUPPORTED on cost — slot-format is not Task-2-specific.
- **Magnitudes drift; direction is stable.** Exp 2 effects are smaller than Exp 1's (−27% vs −42% C-vs-A). Don't quote magnitudes; quote direction. Reproducibility of absolute Phase 2 numbers required matching the model version exactly, and Phase 2's A_orig showed no benefit under today's Opus 4.6 — Phase 2 magnitudes are model-specific.

## Commitments

- v1 distiller emits slot-format encodings only. No prose-briefing variant ships.
- Slot schema is the canonical artifact format for memories. Future encoder iterations (including Phase 3 RL-trained) optimize against this schema, not against free-text fluency.
- Compound key extraction is **not** a separate distillation pass — the slot schema *is* the compound key. Single distillation, single artifact.
- Encoding budget anchor: ~1200 tokens. The 60-token intent+outcome regime is too lossy (98% wrong answers across retrieval tiers, Thread 5); we don't go below ~1200 without an empirical re-check.
- Slot schema is versioned; schema changes require re-distillation or a back-compat read path.

## Reversibility

**Moderate.** The slot schema is a contract between the distiller, the store, and the retriever. Changing the schema costs a re-distillation pass over historical memories (or a back-compat reader). Reverting to prose costs the measured ~27–42% cost saving plus the structured-filter sharpness. Neither direction is one-way; both are weeks-of-work, not a rewrite.

## Open hazards

- **Encoding ceiling.** If ~1200-token slots lose too much detail on harder or longer-horizon tasks, the cost savings narrow and Phase 3 (RL-trained encoder against the same schema) becomes mandatory rather than optional.
- **Worst-case source untested.** Slot-format was tested with clean and mildly-degraded sources only. Whether slots from a fully-failed session are useful, neutral, or harmful is unknown. See [worst-case-source](../open-question/worst-case-source.md).
- **Memory-induced overconfidence.** Memory-equipped agents skip writing verification tests at higher rates with slot-format than with prose (3/4 C vs 0/4 A skipped in Exp 2). `[MEASURED]` but construct-validity is suggestive only — this is a forensic-review observation, not the primary metric. See [Exp 2](../experiment/2026-05-11-write-quality-variance/exp2-task3-c-replication.md).
- **Memory partly redundant with prompt.** Exp 2's issue text already contained Task 2's fix in prose form in the "Hints" section, so the experiment measured "slots + hints" vs "hints alone," not "memory vs no memory." A `cold-no-hints` arm would bound this; optional.

## Related

- [H25-replicate](../hypothesis/H25-replicate.md) — SUPPORTED on cost
- [H26-distiller-confounded](../hypothesis/H26-distiller-confounded.md) — REJECTED; distiller confound closed
- [H27-qual-structure](../hypothesis/H27-qual-structure.md) — REJECTED in reverse; slots win
- [Exp 1 + Exp 2 umbrella](../experiment/2026-05-11-write-quality-variance/README.md)
- [structured-filter-first](./structured-filter-first.md) — the read-side partner; slot fields *are* the structured-filter keys
- [tool-chain-wedge-as-adoption-path](./tool-chain-wedge-as-adoption-path.md) — the wedge this encoding serves

---
type: decision
name: Write-Side Quality Gate Deferrable
status: ACTIVE
last_ingested: 2026-05-13
sources: [../experiment/2026-05-11-write-quality-variance/exp1-task2.md]
epistemic_tags: [measured]
tags: [wedge, write-path, encoding]
---

## Decision

The MTP and v1 product will **not ship a write-side quality gate** that conditionally suppresses memory creation based on source-session quality (e.g., "only store memory from sessions that passed tests"). Every session that produces a distillable transcript gets distilled and stored. A gate may be added later if the untested worst-case regime turns out to harm utility.

## Motivation

- Exp 1 variant D tested *mild* source degradation: the distiller was given a session transcript truncated **before** the fix template was revealed. Variant D did not degrade — it outperformed variant A (prose) and was cheaper than cold. The agent recovered the missing context by inference. `[MEASURED]` from [Exp 1 — Task 2](../experiment/2026-05-11-write-quality-variance/exp1-task2.md). *Construct-validity:* "harmful memory" should manifest as elevated cost vs cold or vs clean-source memory; neither happened.
- The implication is that **Opus-class distillation is robust to mild source degradation.** A pre-write quality filter would gate out sessions whose memory is, on this evidence, just as useful as memory from clean sessions. The simplest viable system writes everything and lets the read path's precision threshold ([precision-over-recall](./precision-over-recall.md)) handle false-positive cost.
- H-QUAL-FLOOR REJECTED for mild source degradation; status documented at [H24-qual-floor](../hypothesis/H24-qual-floor.md).
- Worst-case source (e.g., a fully-failed or wrong-path session) is **untested**. See [worst-case-source](../open-question/worst-case-source.md).

## Commitments

- v1 write path is unconditional: session ends → async distillation → store. No gate.
- Quality-affecting metadata (e.g., did-tests-pass signal, was-session-aborted flag) is **logged on the memory** so a future gate can be added without re-distilling.
- A gate is a v2+ feature, contingent on worst-case-source evidence.
- MTP will collect the data needed to test worst-case: real sessions, including failed/aborted ones, will flow into the store and their downstream utility tracked.

## Reversibility

**Cheap.** Adding a gate later is a single predicate at the distillation entry point; the only sunk cost is the storage of memories that turn out to be harmful and need quarantine or removal. Because we're logging quality-affecting metadata from day one, retroactive quarantine is also cheap.

## Related

- [H24-qual-floor](../hypothesis/H24-qual-floor.md) — REJECTED for mild degradation; the evidence that motivates deferral
- [worst-case-source](../open-question/worst-case-source.md) — the regime that could reverse this decision
- [Exp 1 — Task 2](../experiment/2026-05-11-write-quality-variance/exp1-task2.md) — variant D result
- [precision-over-recall](./precision-over-recall.md) — the read-side mechanism doing the work a write-side gate would have done
- [admission-control](../concept/admission-control.md) — broader concept; this decision concerns only the *quality* sub-gate, not admission-control as a whole

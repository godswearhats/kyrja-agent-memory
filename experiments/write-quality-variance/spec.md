# Experiment Spec: Write-Quality Variance

**Date:** 2026-05-11
**Status:** Draft — pending AJ approval before execution.
**Parent goal:** Wedge tool-chain memory, Goal 2 (write path). See `tool-chain-wedge-goals-2026-05-11.md`.

## Question

How much does write-side encoding quality variance translate to read-side cost variance on a downstream task that we know responds to memory?

Phase 2 told us irrelevant memory hurts (+41–49%; "right encoding, wrong context"). It did not test "bad encoding, right context." Whether write-side quality is a binding constraint or a second-order concern depends on the size of that effect.

## Hypotheses

**H-QUAL (primary).** Encoding quality at write time materially affects downstream cost on causally-related tasks. Specifically, an encoding produced from a degraded source or a misframed prompt produces less cost reduction than the canonical Phase 2 encoding.

**H-QUAL-FLOOR (sub).** An encoding produced from a *partial-failure* predecessor session produces cost ≥ cold baseline. (I.e., bad-but-relevant memory hurts.)

**H-QUAL-FRAMING (sub).** Reframing the prompt from "briefing the next agent" to "summarise what happened" produces measurably worse downstream utility, even with the same source transcript.

**H-QUAL-STRUCTURE (sub).** A fully-structured slot-filled encoding (no prose) underperforms a prose briefing of the same token budget.

**Null result is informative.** If A ≈ B ≈ C ≈ D ≈ E within noise, write-quality variance is second-order and we can use any sane prompt and worry primarily about retrieval gating.

## Target task

`where_keep_attrs_scalar` (Phase 2 Tier 1, Task 2 in the causal chain).

Why this task:
- Phase 2 cold cost: $0.40, $0.42 — tightest within-condition variance in the pilot. Cleaner signal-to-noise than Task 3.
- Phase 2 Level D cost: $0.25, $0.29 — clear memory effect (−31% to −34%) to detect deviations from.
- Predecessor (Task 1, `where_keep_attrs_add`) already has a captured transcript and a canonical Level D encoding we can reuse.

We accept the Phase 2 limitation: single task, single repo (xarray), single agent model (Opus). This experiment answers the *write-quality question*, not generalisation.

## Variants

Five encoding variants of the same predecessor session. Each becomes the memory context for a downstream Task 2 trial.

### Prompt-axis variants (good source, varying distillation)

**A — Phase 2 canonical (reproduction control).** Existing `encoding_d_1200.md` prompt, applied to the existing Task 1 transcript. Same 8 capture targets, ~1200-token target, prose narrative. *Anchor; should reproduce Phase 2's $0.25–$0.29.*

**B — Summary framing.** Same source, same length, prompt rewritten to ask for a retrospective summary instead of a forward-looking briefing. Specifically: "summarise what happened in this session" rather than "write a memory a future agent can use." *Isolates framing from content.*

**C — Structured slots.** Same source, same length, output constrained to fixed JSON-ish slots (bug, location, fix_pattern, related_imports, gotchas, dead_ends) with no prose connective tissue. *Isolates whether prose is load-bearing.*

### Source-axis variants (canonical prompt, degraded source)

**D — Partial-failure source.** Truncate the Task 1 transcript before the agent commits the fix (keep exploration + initial wrong hypothesis; drop the resolution). Apply prompt A. Encoder produces a 1200-token encoding from incomplete information. *Tests H-QUAL-FLOOR.*

**E — Detoured source.** A Task 1 transcript where the agent explores an unproductive direction first and corrects late. If our captured bootstrap doesn't naturally contain detours, synthesise one by re-running Task 1 with a misleading hint in the prompt. Apply prompt A. *Tests whether a "noisy but successful" session yields a useful encoding.*

## Measurement

**Primary metric:** Total cost (USD) of the downstream Task 2 trial, per Phase 2 conventions. Cost properly weights prompt-caching tiers and is more honest than raw tokens.

**Secondary:** Output tokens, turn count, wall time, binary pass/fail.

**n per variant:** 4 trials. Phase 2 used n=2 and was explicit about underpowered magnitudes. n=4 should distinguish 25%+ effects given Task 2's tight cold variance ($0.40 vs $0.42). If first 4 trials show high within-variant variance, expand to n=6.

**Baselines (reused from Phase 2, no new runs needed):**
- Cold: $0.41 avg (n=2)
- Level D (Phase 2 original): $0.27 avg (n=2)

Variant A acts as a reproduction check on the Phase 2 Level D number.

## Statistical analysis

- Per-variant mean cost with bootstrap 95% CI (n=4 is small; bootstrap is honest about that).
- Pairwise comparisons against Variant A:
  - A vs D — primary test of H-QUAL-FLOOR
  - A vs B — primary test of H-QUAL-FRAMING
  - A vs C — primary test of H-QUAL-STRUCTURE
  - A vs E — exploratory
- Pass-rate per variant. A failure run at cold-or-worse cost (cf. Phase 2's `where_keep_attrs_coord` Level D failure) is a separate signal worth flagging.

## Pre-registered decision rules

These define what we'll conclude before we see results, to avoid post-hoc rationalisation.

1. **If A reproduces within ±20% of Phase 2 Level D ($0.22–$0.32):** harness is trustworthy. Proceed with comparisons.
2. **If A does not reproduce:** stop and debug the harness before interpreting other variants.
3. **If D ≥ cold ($0.41):** H-QUAL-FLOOR supported. Write-side quality gate is **mandatory** before any production system. Next experiment: design and test a self-critique gate.
4. **If A < D < cold:** Write-side gate is **helpful but not critical**. Can be deferred behind retrieval gating.
5. **If A ≈ B ≈ C within noise (overlapping CIs):** prompt phrasing and structure are **second-order**. Iterate on schema-and-key extraction instead.
6. **If A < B or A < C clearly:** prompt design matters and the SFT starting point should match A's framing.

## Artifacts

```
experiments/write-quality-variance/
├── spec.md                         (this doc, copied/linked)
├── encodings/
│   ├── A_canonical.md
│   ├── B_summary.md
│   ├── C_structured.md
│   ├── D_partial_failure.md
│   └── E_detoured.md
├── sources/
│   ├── task1_full_transcript.md    (reused from Phase 2 bootstrap)
│   ├── task1_truncated.md          (for D)
│   └── task1_detoured.md           (for E, if synthesised)
├── prompts/
│   ├── A_briefing_1200.md          (= Phase 2 encoding_d_1200.md)
│   ├── B_summary_1200.md
│   └── C_structured_1200.md
├── harness/
│   └── run_variant.py              (wraps Phase 2 run_trial.py)
├── data/
│   └── trials.json
└── results/
    └── analysis.md
```

## Risks and open questions

1. **Variants D and E require fresh source material.** D can be synthesised by truncating the existing Task 1 transcript. E is harder — we may need to re-run Task 1 with a misleading hint to produce a natural detour. If E proves expensive to produce, drop it and rely on D for the source-quality signal.
2. **n=4 may still be underpowered.** Phase 2 was explicit about n=2 being noise-prone. We've picked a low-variance task to compensate, but if Task 2's variance is higher in the variant conditions, plan for n=6 fallback.
3. **Distiller is Opus, not Haiku.** Wedge architecture assumes Haiku distillation. This experiment uses Opus for consistency with Phase 2 bootstrap. Follow-up: re-run best variant with Haiku to confirm the distiller-model doesn't reverse rankings.
4. **No Tier-3-style control.** We are not re-testing irrelevant-memory injection. Phase 2 already covered that. This experiment is narrow on purpose.
5. **Single task confound.** A signal here doesn't guarantee write-quality variance generalises. If results justify a broader study, replicate on Task 3 (`where_keep_attrs_coord`) and on a Sphinx task.

## Compute and timing

- Encoding generation: 5 prompts × ~1 Haiku call each ≈ trivial cost.
- Source synthesis (D, E): 1–2 extra Task 1 bootstrap runs if E is included. ~$1.
- Trials: 5 variants × 4 runs × ~$0.30 avg ≈ $6 in Opus calls.
- Wall time: ~3 hours sequential, less if parallelised across worktrees.

## Out of scope (deferred)

- Schema/compound-key extraction. We're testing encoding *content* quality only.
- Retrieval gating. Memory is hardcoded into the prompt as in Phase 2.
- Multi-task, multi-repo, multi-model. Same Phase 2 limitations, accepted on purpose.
- Quality scoring at write time. The output of this experiment *informs* what a quality scorer should detect.

## Stop conditions

- If after 8 total trials (n=4 on A and D) we cannot distinguish A from D, expand n. If we still cannot distinguish at n=8 per variant, conclude write-quality variance is not detectable on this task and re-scope to a harder task.
- If Variant A doesn't reproduce Phase 2 Level D within ±20%, halt and audit the harness before proceeding.

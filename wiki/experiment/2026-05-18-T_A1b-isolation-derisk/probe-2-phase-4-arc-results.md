---
type: experiment
name: Probe 2 Phase 4 arc-mode results — pair construction for primary falsifier
status: PROPOSED
last_ingested: 2026-05-24
sources: []
epistemic_tags: [measured]
tags: [t_a1b, probe-2, phase-4, test-set, arc-mode, caddy]
---

Results from Phase 4 arc-mode pair construction for the [Probe 2 test set pipeline](./probe-2-test-set-design.md). Arc-mode is the primary falsifier per the [2026-05-24 amendment](./probe-2-test-set-design.md#pre-registration-amendment-log). This constructs cross-domain retrieval problems from the admitted arc-mode candidates produced by [Phase 3](./probe-2-phase-3-results.md).

## Summary

`[MEASURED]` **125 retrieval problems** (25 per pattern), each with 1 positive cross-domain target + 4 distractors (Easy / Medium / Hard / Adversarial). All distractor slots filled. **Arc-mode test set LOCKED.**

## Admitted pool

219 / 240 arc-mode candidates admitted from Phase 3 (91.3%). Distribution:

| Pattern | Corporate | Fantasy | Historical | Sci-fi | Total |
|---|---|---|---|---|---|
| Defection | 11 | 12 | 11 | 12 | 46 |
| Discovery | 11 | 12 | 11 | 12 | 46 |
| Reversal | 11 | 12 | 11 | 12 | 46 |
| Confrontation | 12 | 12 | 12 | 11 | 47 |
| Rescue | 2 | 11 | 11 | 10 | 34 |
| **Total** | **47** | **59** | **56** | **57** | **219** |

## Domain-pair allocation

Proportional allocation based on cell sizes, respecting MAX_CANDIDATE_REUSE = 3.

| Pattern | Co×Fa | Co×Hi | Co×Sf | Fa×Hi | Fa×Sf | Hi×Sf | Total |
|---|---|---|---|---|---|---|---|
| Defection | 4 | 4 | 4 | 4 | 5 | 4 | 25 |
| Discovery | 4 | 4 | 4 | 4 | 5 | 4 | 25 |
| Reversal | 4 | 4 | 4 | 4 | 5 | 4 | 25 |
| Confrontation | 4 | 4 | 4 | 4 | 4 | 5 | 25 |
| Rescue | 1 | 1 | 1 | 7 | 7 | 8 | 25 |

Rescue × corporate pairs are sparse (1 per corporate combo) due to only 2/12 admitted rescue × corporate candidates. Non-corporate rescue combos absorb the balance.

## Candidate reuse

| Uses | Candidates |
|---|---|
| 1 | 39 |
| 2 | 26 |
| 3 | 53 |

118 / 219 admitted candidates used (54%). Max reuse cap (3) respected.

## Hard-tier caveat

`[MEASURED]` Token-Jaccard overlap between cross-domain arc-mode candidates: mean 0.118, range 0.091–0.166. Higher than event-mode (mean 0.050) because arc sequences contain more text, increasing shared common vocabulary. Still insufficient for surface overlap to produce a meaningfully harder distractor than random selection.

**Consequence:** Same as [event-mode caveat](./probe-2-phase-4-results.md#hard-tier-caveat). The Hard tier is effectively a second Easy tier with a slight lexical-similarity bias. The diagnostic gradient is three tiers (Easy ≈ Hard, Medium, Adversarial) rather than four.

**Root cause:** Same as event-mode — Phase 3 rater filtering correctly removed domain-costume candidates, reducing cross-domain vocabulary overlap. The filter's success at enforcing domain-authentic vocabulary is in tension with Hard-tier distractor design.

**Why not fix it:** Pre-registered distractor construction method.

## OVERLAP constraints

- OVERLAP-flagged discovery IDs (`Di-arc-Co2-4`, `Di-arc-Sf1-3`) excluded from defection distractor pools.
- No flagged defection IDs (asymmetric overlap per [Phase 3 results](./probe-2-phase-3-results.md)).

## Raw artifacts

- Arc-mode test set: [`experiments/T_A1b-isolation-derisk/test-set/arc-mode/probe2-arc-test-set.json`](../../../experiments/T_A1b-isolation-derisk/test-set/arc-mode/probe2-arc-test-set.json)
- Arc-mode manifest: [`experiments/T_A1b-isolation-derisk/test-set/arc-mode/manifest.md`](../../../experiments/T_A1b-isolation-derisk/test-set/arc-mode/manifest.md)
- Construction script: `phase4_arc_pair_construction.py`
- Phase 3 rated candidates: [`experiments/T_A1b-isolation-derisk/pipeline/phase-3-rating/candidates/arc-mode/`](../../../experiments/T_A1b-isolation-derisk/pipeline/phase-3-rating/candidates/arc-mode/)

## Related

- [probe-2-test-set-design](./probe-2-test-set-design.md) — methodology pre-registration (§ Pre-registration amendment log for arc-mode promotion).
- [probe-2-phase-4-results](./probe-2-phase-4-results.md) — event-mode Phase 4 results (200 problems, diagnostic).
- [probe-2-phase-3-results](./probe-2-phase-3-results.md) — Phase 3 filtering that produced the admitted pool.
- [H44-T_A1b-cross-domain-transfer](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — hypothesis this test set evaluates.

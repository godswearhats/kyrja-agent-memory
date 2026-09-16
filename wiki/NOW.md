---
tags:
  - exclude-from-graph
---
# Now — Current Work State

*Read first each session. Rewritten (not appended) at session end to reflect current state. Session narratives live in [log.md](./log.md); this file is a state document, not a log. See [SCHEMA.md § Root files](./SCHEMA.md#root-files).*

**Last updated:** 2026-07-25 (Nils/indigo).

---

## Active question

**MASQ paper is ACTIVE** (2026-06-30). The benchmark is built and the first *memory-system-under-test* arms have run. **Headline result (construct-limited):** on the synthetic confusable-scope task, a structured scope filter (`WHERE scope=target`) ties the oracle ceiling (15/15) while every similarity-ranking arm floors at or below paste — vector 6/15, bm25 8/15, paste 9/15; scope-filter beats all with zero paired losses (p≤0.03, n=15) ([experiment](./experiment/2026-06-30-masq-retrieval-arms.md), [H45](./hypothesis/H45-exclusion-over-recall.md)). The bottleneck is **exclusion, not recall** (retrievers recall the target ~2.8/3 but cannot drop the equally-relevant siblings); the reader is *not* the bottleneck (scope-filter ties ceiling without resolution-type labels). Pre-registered sub-claim "lexical rescues embedding scope-merge" **REJECTED** (bm25≈vector). **Discipline note (AJ, 2026-06-30):** MASQ *constructs* the confusability and the filter is an *oracle* — these results demonstrate the failure mode cleanly, they do **not** validate a production architecture; do not let later decisions cite them as general-corpus truth.

**Kerros is PARKED** (sequencing, not abandonment). The 2026-06-12 caddy Rock-3 read program is closed — verdict captured in [caddy § Rock 3](./concept/caddy.md); the open axis [freeze-topology](./open-question/freeze-topology.md) remains explicitly UNCOMMITTED. See Parked threads below.

---

## Immediate next step

**Supermemory audit COMPLETE (2026-07-25); first VALID system-#2 numbers landed.** AJ's methodology-suspect call was vindicated: the smoke's A=8% was an instrument artifact — a cap outage plus a supermemory-server v0.0.3 silent-failure bug left 340/626 docs with zero memories; smoke numbers **EXCLUDED FOR CAUSE** ([smoke page](./experiment/2026-07-22-masq-supermemory-smoke.md) annotated). The store was repaired chronologically on the subscription (throttled/health-gated/census-verified; the verification gate caught two further instrument bugs before any grading), then re-run per [pre-registration](../masq/harness/REPAIR-PREREG.md). **Valid result ([repair experiment](./experiment/2026-07-25-masq-supermemory-repair.md), n=1 core):** supermemory-k20 **A=31%, B-FAIL `set_50`** — *below* the scope-blind plateau (paste/vector/bm25 = 69%, all also FAIL with the same `set_50`), because the extracted-memory layer loses **both** the scope binding (full-store census: 3,537 memories, 23 kernel value-memories, 0 scope-bound — scope survives only as separate atoms) **and** the target chain (0/3 chain steps in top-20 memories; the product's chunk-level path retrieves 3/3, so the deficit is the extraction layer specifically). [H46](./hypothesis/H46-consolidation-scope-smear.md) (consolidation smear) **REJECTED** by its own store-size-0 test; surviving mechanism = **discourse-level atomization** (scope named in a chatter aside; extraction atomizes sentences → scope and value in different atoms). Paper headline candidate: "both dominant off-the-shelf paradigms destroy scope — ranking at read time, extraction at write time" — now with the write-time half measured. Remaining audit items: K ∈ {40,80} sensitivity + oracle-subset starvation bound (bounds A=31%). Next: **14-core Supermemory sweep** on the hardened cap-aware overnight pattern (~30k calls — pacing/weekly-cap conversation with AJ first), then seed expansion (4006+) folded in.

Small pending chores: PDF archives of read papers to `kyrja/library/papers/`; Xu citation-graph re-run when the S2 rate limit clears.


---

## MASQ build provenance (benchmark now built + running — see active result above)

**Both pre-build gates LANDED, generation rules FROZEN (2026-06-09):**

- **Gate 1 PASSED** ([experiment](./experiment/2026-06-08-masq-gate1-c3c4-discriminability.md)): C3/C4 collision-vs-supersession 100% legible from intent; value-awareness hinge locked → 4-cell design proceeds.
- **Surface rubric RESOLVED:** C3 B-layer pass/fail = did the output surface the conflict; B output = `(action, conflict_flag)`; uniform surface-termed preamble on every item → C1/C2/C4 = false-alarm arm; score = hit-vs-false-alarm discrimination.
- **Bare-set probe LANDED, ban CONFIRMED** ([experiment](./experiment/2026-06-09-masq-bareset-probe.md)): reader agreement 0/6 unmarked; whisper verbs = legible C4 soft markers; C3 presupposition-scrub invariant.
- **Generator v2 COMPLETE** (`masq/generator/`, [DESIGN-v2](../masq/generator/DESIGN-v2.md)): scope collision + near-miss + chains P1–P8; Maren atoms landed; all invariants pass.
- **Positioning strengthened 2026-06-12:** [multi-party-attribution-gap](./concept/multi-party-attribution-gap.md) now carries training-side corroboration — Mem-α excludes conflict resolution citing "lack of realistic evaluation benchmarks" (quote-grade); R1/R2 hard-code the recency-default reader MASQ controls for.
- **STALE read + plan updates landed 2026-06-12:** [STALE](./source/chao-2026-stale.md) (full read) occupies the *single-user* implicit-conflict cell — gap claim intact (refresh log on the gap page); Mem-α quote now needs the STALE qualifier when cited. Harness DESIGN §5 gained a pre-registered repeated-call variance check (~720 calls, run during sweep pilot) + grading-robustness note. Extension candidates (cross-party cascade, reopened-not-redecided) parked in [FUTURE.md](../masq/FUTURE.md) — generation rules stay frozen.

Phase-0 positioning stands; refresh-before-submission rule in force. Standing guards: ~6–8 hrs/wk cap; every benchmark claim traces to a verbatim primary-source quote; pre-register unit/metric/power before running any system.

---

## Parked threads (Kerros — resume points preserved)

- **Gate 2 / the write question** — [incremental-integration-cost](./open-question/incremental-integration-cost.md): cheap-write-vs-compositional-read trade-off; toy decider parked 2026-05-30; the Ω(k²) desk-check is resume thread (1).
- **Wedge sizing** — [thinks-with-wedge-sizing](./open-question/thinks-with-wedge-sizing.md): operand-vs-grammar market read; exploratory. Note: a runtime-plastic component (freeze-topology regime 3) would change this answer, not just the architecture.
- **T_A1b / tier-3** — [H44](./hypothesis/H44-T_A1b-cross-domain-transfer.md) PROPOSED (scale-confounded); [tier-3-distinctness](./open-question/tier-3-structural-vs-semantic.md) carries the BoW-at-chance gate; [masked continuation](./open-question/masked-vs-forward-prediction.md) PAUSED.
- Env (if Kerros experiments resume): [requirements.txt](../experiments/factored-operator-beachhead/requirements.txt) (host RTX 2080 Ti 11GB; torch 2.12+cu130, trust_remote_code off, sdpa). **Product line owned by other team members** — off Nils's plate.

## Open side quests

- **Memory-model caddy** ([open-question/memory-caddy](./open-question/memory-caddy.md)) — status refresh deferred.

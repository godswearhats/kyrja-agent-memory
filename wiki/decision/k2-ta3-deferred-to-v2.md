---
type: decision
name: K2+T_A3 deferred to v2 research track — REVERSED 2026-05-20
status: REVERSED
last_ingested: 2026-05-20
sources: [../source/wu-2022-memorizing-transformer.md, ../source/dong-2025-norman-episodic.md]
superseded_by: [./caddy-as-research-program.md]
tags: [caddy, yagni, k2, t_a3, load-bearing, deferral, reversed]
---

> **REVERSED 2026-05-20.** This decision was MVP-YAGNI: K2+T_A3 was deferred *because tier 3-4 wedge demonstration didn't require it for MVP product scope*. Per [caddy-as-research-program](./caddy-as-research-program.md) (2026-05-20), the MVP-product framing dissolved — caddy is now a research program, not a path to market. With no MVP scope constraint, the YAGNI logic no longer applies. K2+T_A3 returns to **load-bearing research target** alongside T_A1b. Ordering between them is decided by the [forthcoming stack-rank exercise](./caddy-as-research-program.md#commitments) using scientific leverage, tractability, dependencies, and frontier-pacing as criteria — anchored to "moves us toward tier 3-4 retrieval via the caddy."
>
> The page below records the 2026-05-19 reasoning for historical context. Do not treat its commitments as live. The [m17-jepa-reconciliation](../open-question/m17-jepa-reconciliation.md) resolution (K2+T_A3 scientifically distinct from T_A1b on different timescales) stands — that was always the *scientific* claim, separable from MVP scoping.

## Decision (REVERSED — historical)

`[ASSERTED]` K2 (schema-fit-modulated tier promotion) and T_A3 (continuous online schema drift) are **deferred from MVP load-bearing T4 status to v2 research target**. T_A1b — the auxiliary world-model loss on memory representations — becomes the **sole load-bearing T4 on the MVP critical path**. The MVP's [T_A1b isolation de-risk experiment](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md) becomes the single experiment that decides whether the caddy architecture has scientific footing.

The H40 hypothesis ([schema-fit-modulated consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md)) remains scientifically interesting and falsifiable — this decision changes its scope-status (off MVP critical path), not its hypothesis-status (still PROPOSED). The Version A / Version B isolation experiment sketch from the 2026-05-19 design session is preserved in H40 for v2 re-promotion.

## Motivation

AJ-Nils 2026-05-19 session applied a YAGNI / 80-20 pressure test to K2+T_A3 after [m17-jepa-reconciliation](../open-question/m17-jepa-reconciliation.md) had just confirmed K2 stays scientifically load-bearing (distinct mechanism from T_A1b's EMA target encoder).

**The pressure-test result.** The caddy's [wedge](./tier-3-4-as-wedge.md) is tier 3-4 retrieval — analogical and predictive. Tier 3-4 capability is a property of *the encoded representations*, not of *the consolidation policy*. A well-trained T_A1b encoder paired with simple FIFO retention can still demonstrate tier 3-4 retrieval on a fixed corpus, because the analogical match happens in the representation space regardless of how the retained items got there.

**What K2+T_A3 actually buys us at MVP scale:**
- Bounded memory growth — deliverable by any eviction policy (FIFO, LRU, TTL)
- Good retrieval quality at scale — mostly a property of T_A1b's representations + the retrieval mechanism (R2)
- Schema-aware retention — the K2 claim, but at MVP fixed-corpus scale this isn't load-bearing for the wedge demonstration
- The schema drift property (T_A3) — the actual novel commitment, but it's a system-at-scale property, not a wedge property

**The 80/20.** Engineered alternatives — frozen-predictor novelty scoring + periodic batch re-curation — deliver roughly 80% of K2+T_A3's intended benefit for ~20% of the research effort. What we lose: continuous online drift (replaceable by nightly batch re-curation with small practical impact at MVP scale), and the publishable "schema-fit-modulated consolidation with continuous drift" framing. What we keep: bounded memory, decent retention, the entire wedge demonstration via T_A1b.

**The wiki commitments already point this way.** [tier-3-4-as-wedge](./tier-3-4-as-wedge.md) names only T_A1b: "Without it, tier 3-4 is unreachable." [caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md): "*the single bet* that decides the path." Both framings, written 2026-05-18, already treated T_A1b as the sole bet. The "two load-bearing T4s" framing in [caddy-architecture](../concept/caddy-architecture.md) is a vestige from the 2026-05-17 design session that predates the tier-3-4 wedge sharpening.

**MVP scope discipline.** The de-risk experiment that decides whether the architecture has scientific footing is single-bet on T_A1b. Adding K2+T_A3 as co-load-bearing for the MVP would expand the failure surface (two simultaneous bets to pass) without adding wedge capability the experiment actually needs.

## Commitments

- **One MVP load-bearing T4: T_A1b.** The de-risk experiment ([2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md)) decides whether the caddy has scientific footing. K2+T_A3 does not gate this decision.
- **MVP retention policy uses simple engineered baselines** — FIFO, LRU, or frozen-predictor novelty scoring + periodic batch re-curation. No learned consolidation policy is required for MVP. Caddy-architecture op K2 and op K5 are tagged `MVP-deferred`; the architecture spec describes them as design space but doesn't make them critical-path.
- **H40 retains PROPOSED status** as a v2 research target. The Version A (static reference) / Version B (dynamic reference with drift) experimental design from the 2026-05-19 session is preserved in H40's scope-status section for v2 re-promotion.
- **K6 (offline composition) and R5 (read-as-write) remain in their prior states** — K6 deferred post-MVP, R5 demoted to "interesting variant to test." This decision doesn't reopen them; it only reclassifies K2+T_A3.
- **Norman rubric implications acknowledged.** The MVP target stays 3.5-4/5 on the [Norman rubric](../concept/norman-rubric.md). With K2+T_A3 deferred, the rubric properties that depend on adaptive consolidation (specifically the "statistical extraction" implication) are served via T_A1b's representational structure rather than via runtime consolidation. If the rubric scoring requires explicit adaptive consolidation in ways T_A1b can't substitute for, the demotion is wrong and gets reversed.

## Reversibility

**Cheap-to-moderate.** This decision exists at the architecture-specification level; no implementation has been built yet. Reversing the demotion before MVP build is a doc edit. After MVP build, reversal means adding a learned consolidation policy on top of the existing tier/storage infrastructure — meaningful engineering but not a structural refactor (the multi-tier capacity already exists per S1; K2 plugs in as a policy layer above it).

Natural reversal triggers:
- **T_A1b passes the de-risk experiment but the MVP underperforms on the [Norman rubric](../concept/norman-rubric.md)** in ways that look like "the consolidation policy is the missing piece." Re-promote K2 as a v1.x addition.
- **MVP requires continuous deployment** (live stream over weeks-to-months) where memory budget becomes a binding constraint and simple engineered eviction policies underperform learned ones.
- **A funder/strategic-partner pitch specifically requires** the "structural moat" argument that depends on K2+T_A3 being load-bearing alongside T_A1b. (Counter-argument: T_A1b's loss formulation + co-training discipline is the moat. The pitch can be built around T_A1b alone.)
- **H40 v2 research produces a strong positive result** (Version B beats Version A beats baselines by meaningful margins on a downstream task) that justifies re-incorporating into v1.x.

The decision is held *until evidence inverts it*, not committed forever. Pre-registration of these reversal triggers is the discipline that prevents motivated re-promotion.

## Related

- [tier-3-4-as-wedge](./tier-3-4-as-wedge.md) — the wedge decision this one ratifies the implication of. Already named T_A1b as sole load-bearing T4 by inference; this decision makes the implication explicit.
- [multi-field-memory-unit](./multi-field-memory-unit.md) — the paired commitment that lets T_A1b's representational compression not regress tier 1-2; independent of this demotion.
- [caddy-architecture](../concept/caddy-architecture.md) — the architecture spec where "two load-bearing T4s" framing originates; updated by this decision to "one load-bearing T4."
- [caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md) — the within-family comparison; "single bet" framing was already in place 2026-05-18.
- [hypothesis/H40-schema-fit-modulated-consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — the hypothesis being deferred. Status remains PROPOSED; scope-status becomes v2.
- [open-question/m17-jepa-reconciliation](../open-question/m17-jepa-reconciliation.md) — the resolution that confirmed K2 stays scientifically distinct from T_A1b. This decision is a separate question: scientific distinctness ≠ MVP-load-bearing. K2 can be both scientifically real and MVP-deferred.
- [experiment/2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md) — the sole MVP critical-path experiment after this decision.
- [hypothesis/H44-T_A1b-cross-domain-transfer](../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the falsifiable form of T_A1b; the sole load-bearing T4 on MVP critical path.
- [open-question/memory-caddy](../open-question/memory-caddy.md) — the live design question; updates with this scope sharpening.
- [concept/consolidation-channel](../concept/consolidation-channel.md) — Kyrja's earlier "named wedge" concept; this decision narrows what the channel is load-bearing for at MVP scale.
- [[feedback_mvp_doc_not_mvp]] — discipline that makes this kind of scope sharpening cheap at doc stage.

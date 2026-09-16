---
type: decision
name: Tier 3-4 retrieval as the caddy wedge — analogical and predictive, not literal or topical
status: ACTIVE
last_ingested: 2026-05-25
sources: [../source/dong-2025-norman-episodic.md]
epistemic_tags: [asserted]
tags: [wedge, caddy, capability-target, research-goal]
---

## Decision

The caddy targets **tier 3 (analogical) and tier 4 (predictive)** retrieval as the load-bearing capability that justifies the architecture. Tier 1 (literal recall) and tier 2 (topical retrieval) are served as table-stakes side-effects, not as the wedge. The four-tier taxonomy is in [memory-retrieval-tiers](../concept/memory-retrieval-tiers.md).

> **Construct-validity flag (2026-05-25) — premise under review, not reversed.** The [ceiling probe](../experiment/2026-05-18-T_A1b-isolation-derisk/ceiling-probe.md) found that on the arc test set a bag-of-words classifier decodes pattern at 82% from clean narrative — so for narrative patterns, tier 3 (analogical/structural) may not be a capability *distinct* from tier 2 (semantic). This does not reverse the decision (the reversal trigger below is unchanged) but it questions its load-bearing premise. AJ is taking the framing back to the drawing board; tracked at [tier-3-structural-vs-semantic](../open-question/tier-3-structural-vs-semantic.md).

## Motivation

- **Tier 1-2 is the bolt-on incumbents' market.** Mem0, Letta, Zep, Cognee, LightMem ship tier 1-2 today. Competing there means competing on engineering quality with the additional handicap of needing co-trained open-weights LLM access — and losing on debuggability, modularity, frontier-LLM deployability, privacy/governance ergonomics, iteration speed, and training cost (the eight bolt-on advantages enumerated in [caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md)).
- **Tier 3-4 doesn't exist in the world today.** No shipped memory system supports cross-domain analogical retrieval or trajectory-based predictive recall at production scale. The post-Norman gap `[ASSERTED]` ([Dong/Norman 2025](../source/dong-2025-norman-episodic.md)) is the symptom: no published system scores ≥3/5 in 11 months because the Norman rubric implicitly measures tier 3-4.
- **Tier 3-4 is what makes labs notice.** A capability that literally doesn't exist is the rare wedge against frontier labs — either competitive differentiator or acquisition target. Tier 1-2 quality improvements don't carry the same strategic weight.
- **AJ 2026-05-18:** *"If we actually built tiers 3-4, then frankly we have a case to take on the frontier labs (or get rapidly and expensively acquired by one) because now there's a capability that literally doesn't exist in the world today. I think it has to be this path."*

## Commitments

- The caddy's primary load-bearing research target is [T_A1b](../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the auxiliary loss that produces structurally-transferable representations. Tier 3-4 is a property of representations first; without T_A1b succeeding, the wedge is unreachable through the representation pathway.
- K2+T_A3 (schema-fit-modulated consolidation, [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md)) is a **secondary load-bearing research target** on a distinct timescale (slow / cortical-analog) and a distinct mechanism (consolidation policy vs. representation learning). It contributes long-term-retention dynamics and the publishable "schema-fit-modulated consolidation with continuous drift" claim. Per [caddy-as-research-program](./caddy-as-research-program.md) (2026-05-20), both are active load-bearing research targets; ordering is set by the stack-rank exercise.
- The [multi-field memory unit](./multi-field-memory-unit.md) commitment is what preserves tier 1-2 capability under tier-3-4-shaped representation learning. Without it, T_A1b's compression of surface detail regresses tier 1 vs. bolt-on incumbents.
- The [T_A1b isolation de-risk experiment](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md) is the falsifier for whether tier 3-4 is reachable through the representation pathway. Negative result collapses that pathway; the consolidation-policy pathway (K2+T_A3) remains a distinct research bet whose outcome is decided separately.

## Reversibility

**Expensive in research-program terms.** Reversal means abandoning the tier 3-4 wedge claim and either (a) re-targeting the research program at tier 1-2 (which is the bolt-on incumbents' market and not a research-novel target), or (b) abandoning a unifying capability target and treating the architecture as a collection of independent bets. Neither carries the same scientific story as targeting a capability that doesn't exist in the world. The natural reversal trigger is the [T_A1b isolation de-risk experiment](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md) AND the H40 consolidation-policy track BOTH failing at their pre-registered thresholds — pathway-redundancy means a single failure doesn't reverse this decision. Pre-registration is the discipline that prevents motivated re-interpretation of negative results.

Note: commercial pivot is no longer a consideration. The caddy is a research program ([caddy-as-research-program](./caddy-as-research-program.md), 2026-05-20); commercial vehicle is Eira's bolt-on track and is independent of this decision.

## Related

- [memory-retrieval-tiers](../concept/memory-retrieval-tiers.md) — the four-tier taxonomy this decision selects within.
- [multi-field-memory-unit](./multi-field-memory-unit.md) — paired commitment that makes tier 1-2 a side-effect of tier 3-4 architecture.
- [caddy-as-research-program](./caddy-as-research-program.md) — 2026-05-20 framing decision; clarifies that this wedge is a research goal, not a product wedge.
- [k2-ta3-deferred-to-v2](./k2-ta3-deferred-to-v2.md) — REVERSED 2026-05-20. K2+T_A3 is a secondary load-bearing research target, not deferred.
- [H44-T_A1b-cross-domain-transfer](../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the load-bearing falsifiable claim for the representation pathway.
- [H40-schema-fit-modulated-consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — the load-bearing falsifiable claim for the consolidation-policy pathway.
- [2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md) — the falsifier protocol for the representation pathway.
- [2026-05-20-probe-2-test-set-design](../experiment/2026-05-18-T_A1b-isolation-derisk/probe-2-test-set-design.md) — pre-registered methodology for the binary-verdict probe inside the falsifier.
- [caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md) — the within-family comparison; this decision sharpens the wedge claim.
- [memory-caddy](../open-question/memory-caddy.md) — the live open question this decision shapes.

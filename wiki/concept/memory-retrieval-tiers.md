---
type: concept
name: Memory retrieval tiers — four-tier capability taxonomy for AI memory systems
status: timeless
last_ingested: 2026-05-25
sources: [../source/dong-2025-norman-episodic.md]
epistemic_tags: [asserted]
tags: [taxonomy, capability, retrieval, wedge, evaluation]
---

## Definition

Memory retrieval capability decomposes into four tiers, ordered by what kind of structure the retrieval mechanism must match on:

1. **Tier 1 — Literal recall.** "You told me X yesterday." Surface match on content. Mechanism: content-addressable storage, lexical or shallow-embedding retrieval. Example failure if absent: user must re-state preferences each session.

2. **Tier 2 — Topical retrieval.** "We discussed this kind of thing before." Semantic similarity on topic. Mechanism: embedding-based nearest neighbour, modest semantic abstraction. Example failure if absent: user must restate domain context each time the topic comes up.

3. **Tier 3 — Analogical retrieval.** "This is structurally like that other case." Match on transferable structural pattern across surface-different contexts. Mechanism: representations that encode causal/relational structure, not surface features. Example failure if absent: system can't apply lessons from one domain to a different-surface but same-structure situation.

4. **Tier 4 — Predictive recall.** "You usually want X when Y is true." Match on trajectory position within an unfolding schema. Mechanism: representations that encode where-in-a-pattern we are, with retrieval matched on analogous-position-with-known-resolution. Example failure if absent: system reacts to surprises without context of how similar surprises were navigated before.

This taxonomy exists as its own page because it is cited by three architectural commitments ([tier-3-4-as-wedge](../decision/tier-3-4-as-wedge.md), [multi-field-memory-unit](../decision/multi-field-memory-unit.md), [caddy-architecture](./caddy-architecture.md)) plus the [memory-caddy](../open-question/memory-caddy.md) live open question.

## What each tier needs from the architecture

| Tier | What's stored | What query matches on | Existing example |
|---|---|---|---|
| 1 — Literal | Raw content (token spans, layer-N activations) | Surface lexical / shallow embedding | Mem0 fact extraction; Letta core memory |
| 2 — Topical | Shallow semantic embedding | Vector nearest neighbour in topic space | Zep semantic search; bolt-on RAG |
| 3 — Analogical | Structurally compressed representation | Structural pattern across surface variation | None at production scale |
| 4 — Predictive | Trajectory state (position-in-pattern) | Analogous trajectory positions, often with prediction-failure as gate | None at production scale |

Tier 3-4 columns are empty in current production. The post-Norman gap `[ASSERTED]` ([Dong/Norman 2025](../source/dong-2025-norman-episodic.md); no system above 2.5/5 on the [Norman rubric](./norman-rubric.md) in 11 months) is the symptom — the rubric implicitly measures tier 3-4. AJ 2026-05-18.

## Subsumption: higher tiers do not automatically deliver lower tiers

A common assumption is that tier 3-4 architecture gets tier 1-2 for free. This is **not automatic**. The auxiliary loss that produces tier 3-4 representations (see [H44 — T_A1b cross-domain transfer](../hypothesis/H44-T_A1b-cross-domain-transfer.md)) compresses surface detail away, because surface detail isn't predictive at the event-segmentation granularity. A pure-tier-3-4 store would have *worse* tier 1 recall than bolt-on incumbents that retain raw text.

The fix is the [multi-field-memory-unit](../decision/multi-field-memory-unit.md) commitment: store the tier-3-4-shaped representation **alongside** raw content. Retrieval can then match on either field. This makes tier 1-2 a side-effect of the tier 3-4 architecture, not a regression.

## Why this matters

- **Locates competitors and wedge precisely.** Mem0/Letta/Zep/Cognee/LightMem own tier 1-2 today; nobody owns tier 3-4. The taxonomy is the diagnostic that converts "the post-Norman gap" into a specific capability gap.
- **Disambiguates the wedge claim.** "Better memory" is too vague. "Tier 3-4 retrieval that current systems cannot do" is testable and strategically legible.
- **Forces construct-validity discipline on T_A1b.** Per [[feedback_metric_construct_validity]], a hypothesis like "T_A1b produces useful representations" is unfalsifiable. Re-stated as "T_A1b enables tier 3 (cross-domain analogical retrieval) at a measurable margin above token-averaged baseline," the claim becomes testable. The tier framing is the operationalization; the binary-verdict probe methodology is pre-registered in [2026-05-20-probe-2-test-set-design](../experiment/2026-05-18-T_A1b-isolation-derisk/probe-2-test-set-design.md). **Construct-validity flag (2026-05-25):** the [ceiling probe](../experiment/2026-05-18-T_A1b-isolation-derisk/ceiling-probe.md) found a bag-of-words classifier decodes the arc patterns at 82% from clean narrative — so for narrative patterns, tier 3 may not be cleanly *separable* from tier 2 (semantic). Whether tier 3 is a distinct capability is now an open question: [tier-3-structural-vs-semantic](../open-question/tier-3-structural-vs-semantic.md).
- **Separates table-stakes from wedge.** Tier 1-2 must work for the product to ship; tier 3-4 is what justifies the architecture. The architectural commitments serve both, but the research bet is on tier 3-4.

## Scope limits

- **Not a Norman rubric.** Norman's five-criterion rubric scores systems on episodic-memory mechanisms (event segmentation, pattern completion, schema integration, etc.). The tier taxonomy is a *capability* taxonomy — what the user can ask the system to do. They are complementary: Norman scores how the mechanisms work; tiers score what the system delivers.
- **Not a strict ladder.** A system can be strong at tier 1 and weak at tier 2, or strong at tier 3 and weak at tier 4. The numbering reflects mechanism complexity, not necessary precedence.
- **Not architecture-bound.** Bolt-on, substrate, and caddy paths are all *capable* of reaching any tier in principle. The question is engineering cost and architectural fit. The tier-3-4 wedge picks the caddy because that's where its architectural commitments pay back most.

## Related

- [tier-3-4-as-wedge](../decision/tier-3-4-as-wedge.md) — the decision that selects tier 3-4 as the wedge target.
- [multi-field-memory-unit](../decision/multi-field-memory-unit.md) — the commitment that prevents tier 3-4 architecture from regressing tier 1-2.
- [caddy-architecture](./caddy-architecture.md) — the architectural spec; ops map to specific tiers.
- [memory-caddy](../open-question/memory-caddy.md) — the live open question this taxonomy sharpens.
- [norman-rubric](./norman-rubric.md) — the orthogonal mechanism-scoring framework.
- [caddy-vs-bolt-on](./caddy-vs-bolt-on.md) — incumbent comparison; tier framing makes the wedge claim sharper than the previous "single bet" framing.

## Source archive

- 2026-05-18 Nils session (auxiliary-world-loss tractability exploration). AJ surfaced the construct-validity question — "is 'world-model structure' what we actually want, or is the goal just 'don't re-explain things'?" — which exposed the need for an explicit capability taxonomy.

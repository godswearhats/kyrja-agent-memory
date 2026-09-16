---
type: open-question
name: M17 active-forgetting consolidator vs T_A1b JEPA-shaped encoder — where does structure accumulate?
status: RESOLVED
last_ingested: 2026-05-20
sources: [../source/hardt-nader-nadel-2013-active-forgetting.md]
epistemic_tags: [asserted, speculated]
tags: [caddy, m17, t_a1b, consolidator, architecture, reconciliation]
---

## Resolution (2026-05-19)

`[ASSERTED]` Resolution path 1 (theoretical reconciliation) executed. **Answer: (c) both load-bearing on different timescales, distinct jobs.** K2+T_A3 is a distinct falsifiable mechanism ([H40](../hypothesis/H40-schema-fit-modulated-consolidation.md)) alongside T_A1b. They do not collapse into each other.

**The core argument.** The EMA target encoder is a **training-stability device**, not a schema-accumulation mechanism. Its purpose in BYOL/JEPA family losses is to provide non-trivial, non-collapsing prediction targets for self-supervised learning — its slowly-drifting representation is a *side-effect* of being a moving average, not a designed schema model. K2 is a separate offline policy that decides which memories graduate between tiers based on schema-fit, operating on already-stored representations on hours-to-days timescales. The two mechanisms operate on different inputs (encoder weights vs stored memories), at different timescales (per-training-step vs offline consolidation), with different outputs (prediction targets vs keep/merge/discard decisions), for different reasons (training stability vs intelligent forgetting).

**Biology check supports the answer.** CLS theory (McClelland et al. 1995, [hardt-nader-nadel-2013-active-forgetting](../source/hardt-nader-nadel-2013-active-forgetting.md)) assigns episodic encoding (hippocampus) and schema extraction (cortex via replay) to distinct biological structures operating on different timescales. The EMA target encoder maps onto neither — it has no biological analog. The biology-faithful mapping is: hippocampal-style fast episodic storage ≈ hot tier with light admission (E2); cortical schema extraction via replay ≈ K2 schema-fit-modulated consolidation. The structure accumulation locus in biology is the consolidator (replay-driven cortex), not the encoder.

**Implication for the architecture.** K2+T_A3 stays distinct from T_A1b — two coupled load-bearing T4 research targets on different timescales and different mechanisms. Per [caddy-as-research-program](../decision/caddy-as-research-program.md) (2026-05-20), both are active in the research backlog; ordering between them is decided by the forthcoming stack-rank exercise. (Historical note: the 2026-05-19 session demoted K2+T_A3 to v2-research-target on MVP-product-scope grounds; that decision was REVERSED 2026-05-20 when the caddy was reframed as a research program. See [k2-ta3-deferred-to-v2](../decision/k2-ta3-deferred-to-v2.md) for the historical record.) C (salience signal) remains consumed by E2, K2, K5, R3 as specified. The MoE / mixture-of-schemas proposal from the Web-Claude 2026-05-19 conversation is parked as a contingency (see § Parked variant below), not promoted to a commitment.

**Provenance.** AJ-Nils session 2026-05-19, in response to AJ sharing a Web-Claude conversation that implicitly assumed resolution (a) — "the EMA encoder is the schema" — and proposed adding mixture-of-experts routing to address the muddy-average problem that assumption creates. The session's pressure-test showed the conversation had sidestepped the reconciliation question rather than answered it: it assumed (a) without checking, hit the muddy-average problem, and patched (a) with MoE. The biology mapping argument inverts that path to (c).

## Parked variant: mixture of schemas (v2 contingency)

`[SPECULATED]` Web-Claude 2026-05-19 proposed adding a mixture-of-experts (multiple EMA target encoders, each specialized to a pattern type, with a learned router and a diversity-incentive auxiliary loss) to address the muddy-average concern (a single encoder averaging across all schema types produces representations too vague to be useful). This proposal is parked as a v2 contingency, not promoted:

- The muddy-average failure mode is already probed by the [de-risk experiment](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md): probe 1 (collapse check via covariance rank) and probe 2 (cross-domain structural retrieval) will detect it if it manifests.
- If single-encoder T_A1b shows muddy-average behaviour, MoE becomes a natural v2 design. Until then, adding MoE means testing three speculative components simultaneously (encoder + predictor + router + diversity loss) instead of one.
- MoE routing has its own T3-T4 failure modes (slot collapse, load imbalance, routing instability) — adding it pre-emptively expands the surface of unknowns.
- Decision: keep the de-risk experiment minimal (single-encoder T_A1b). If muddy-average behaviour appears, promote MoE to its own open-question page with its own falsifiable hypothesis.

## The question

`[ASSERTED]` The caddy commits to two structure-accumulation mechanisms that may compete for the same role:

1. **M17 inversion** (committed in [caddy-architecture](../concept/caddy-architecture.md) § The M17 architectural inversion): the encoder admits liberally, the *consolidator* (op K2 schema-fit-modulated tier promotion, op K5 salience-modulated decay) does the intelligent structure-accumulation work offline, on hours-to-days timescales analogous to biological consolidation.

2. **T_A1b JEPA-shape** (committed in [H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md)): the auxiliary loss uses an EMA target encoder that accumulates a slowly-evolving smoothed representation, which acts mechanically like a "schema" being updated per training step (momentum τ ∈ {0.99, 0.996}).

**The question**: where does the system's structural knowledge actually live, and on what timescale does it accumulate? The EMA-target operates on per-step momentum (seconds at training time, instantaneous at inference). K2 operates on slow consolidation cycles (minutes to days). Calling the EMA encoder "the schema" — as the Web-Claude conversation 2026-05-18 implicitly did — collapses these two mechanisms into one, which is mechanically wrong.

A concrete sub-form: when an event arrives and gets stored in the hot tier, what controls whether it migrates to the cold tier? K2 (a learned schema-fit policy in the consolidator) or the EMA encoder's representational drift (the schema-as-EMA-state)?

## Why it matters

- **If the EMA encoder is the structure-accumulation locus:** the M17 inversion partially collapses. The encoder is doing structural work at write time, even if not "selective gating"-style. K2 becomes auxiliary or redundant. The wedge claim shifts from "intelligent forgetting via learned consolidator policy" to "intelligent encoding via auxiliary loss."
- **If K2 is the structure-accumulation locus:** the M17 inversion holds, and T_A1b shapes the encoder's representational geometry but doesn't substitute for the consolidator. K2 remains load-bearing. The EMA encoder's role is purely collapse prevention, not structure-accumulation.
- **If both are load-bearing on different timescales:** the architecture has two coupled adaptive subsystems — encoder updating per step, consolidator updating per day — and their interaction needs an explicit model. This is the most expressive option and the most failure-mode-rich.
- **The decision gates**: the consolidator scope in the research prototype (is K2 the heavy lift or a thin gate?), the salience signal C's role (is it consumed by the consolidator or by the encoder during training?), and whether K2+T_A3 stays a distinct load-bearing T4 or T_A1b absorbs its function.

## What evidence would resolve it

`[SPECULATED]` Three approaches in order of cost:

1. **Theoretical reconciliation pass** (cheapest). Walk the M14-M17 mechanism rows again with T_A1b's EMA-encoder mechanism specifically considered. Determine which mechanisms biology assigns to which biological structure (encoder-side: hippocampal CA3; consolidator-side: replay-driven cortical schema fitting). If biology's two-system answer maps cleanly onto our two mechanisms (encoder + EMA-target ≈ CA3, consolidator + K2 ≈ replay-driven cortex), the two-mechanism architecture is justified by the biology mapping. If they map onto the same biological structure, one of our mechanisms is redundant.
2. **Empirical isolation** (medium). Train T_A1b in isolation (the [de-risk experiment](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md)) and probe whether the EMA target encoder spontaneously produces schema-fit-like clustering. If so, K2 may be partially redundant. If not, K2 is doing distinct work.
3. **Full caddy ablation** (expensive). Train caddy with K2 enabled vs. disabled, holding T_A1b constant. Measure whether K2 adds Norman-rubric score. Requires the full caddy build, so this only fires after the de-risk experiment passes.

**Adequate signal**: ablation on whether T_A1b's representations spontaneously produce clustering analogous to schema-fit consolidation. If the EMA encoder's slow drift demonstrably tracks "what biology calls schema fit," K2 is reframed as auxiliary; if not, K2 is load-bearing.

## Sub-questions

- **Timescale mapping**: is the EMA momentum τ a tunable representation of biological consolidation timescale, or is it a fundamentally different mechanism that happens to look similar? Hint: per-step EMA in BYOL/JEPA is closer to "online running average for stable targets" than "consolidation"; the rhetorical analogy may be misleading.
- **Does K2's schema-fit modulation reduce to "fit to EMA encoder's current state"?** If yes, K2 has a concrete implementation; if no, K2 needs a separate learned schema model.
- **Where does the salience signal C live?** Per caddy-architecture, C is consumed by E2, K2, K5, R3. If T_A1b absorbs the encoder-side consumers (E2) and K2's role narrows, C's centrality may shift. See [open-question/salience-signal](./salience-signal.md).

## Related

- [caddy-architecture § The M17 architectural inversion](../concept/caddy-architecture.md) — the original M17 inversion commitment.
- [H44-T_A1b-cross-domain-transfer](../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the T_A1b mechanism whose EMA target raises this question.
- [H40-schema-fit-modulated-consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — the K2 hypothesis whose load-bearing status this question gates.
- [H42-learned-salience-function](../hypothesis/H42-learned-salience-function.md) — C's role in the architecture, which shifts depending on this reconciliation.
- [consolidation-channel](../concept/consolidation-channel.md) — Kyrja's primary wedge concept; K2+T_A3 ≡ the channel.
- [salience-signal](./salience-signal.md) — adjacent open question on C's signature.
- [hardt-nader-nadel-2013-active-forgetting](../source/hardt-nader-nadel-2013-active-forgetting.md) — the biology source motivating M17.

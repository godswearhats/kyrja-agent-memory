---
type: decision
name: Multi-field memory unit — S1 entries carry event_rep, raw_content, and trajectory_state
status: ACTIVE
last_ingested: 2026-05-19
sources: [../source/wu-2022-memorizing-transformer.md]
epistemic_tags: [asserted]
tags: [caddy, architecture, storage, retrieval, construct-validity]
---

## Decision

Each discrete addressable unit in the caddy's store (op S1 in [caddy-architecture](../concept/caddy-architecture.md)) carries **multiple fields**, not a single vector:

- `event_rep` — the [T_A1b](../hypothesis/H44-T_A1b-cross-domain-transfer.md)-trained learned representation. Used as the retrieval key for tier 3 (analogical) and tier 4 (predictive) queries.
- `raw_content` — preserved token spans or layer-N hidden states from original processing. Used as the retrieval key for tier 1 (literal) and tier 2 (topical) queries.
- `trajectory_state` — the predictor's internal state at write time (a candidate concrete instantiation of [H41 temporal-context retrieval](../hypothesis/H41-temporal-context-retrieval.md)). Used to match analogical queries on "position within an unfolding schema" rather than on the event itself.

The retrieval mechanism (op R1/R2) supports a **hybrid query** that can match on any combination of these fields.

## Motivation

- **T_A1b as a single loss compresses surface detail away.** JEPA-family losses push representations toward what's predictively useful at the event-segmentation granularity; surface details that don't help next-event prediction get squeezed out. If we stored *only* `event_rep`, the caddy would have worse tier 1 (literal) recall than bolt-on incumbents — which preserve raw text and grep it.
- **The tier 3-4 wedge ([decision/tier-3-4-as-wedge](./tier-3-4-as-wedge.md)) requires tier 1-2 as table stakes.** If the architecture regresses tier 1 vs. existing systems, the product loses regardless of how well tier 3-4 works. Multi-field storage gets tier 1-2 capability as a side-effect of tier 3-4 architecture.
- **MemTx is hybrid by accident** `[ASSERTED]` ([Wu 2022 §4](../source/wu-2022-memorizing-transformer.md)). Memorizing Transformer stores raw layer-N KV pairs, which encode both surface and semantic information in one vector — so MemTx is naturally tier 1-2 capable. Our auxiliary-loss-trained `event_rep` is *not* hybrid by default. We must preserve the hybridness deliberately.
- **Trajectory state is a substantial architectural addition surfaced 2026-05-18.** A Web-Claude side-conversation surfaced the observation that the predictor's internal state already encodes "where in the schema arc we are" because that's what's predictive. Storing this state per memory entry lets retrieval match on analogical position rather than on event surface.
- **AJ 2026-05-18:** *"This isn't in the caddy doc yet — it's a small but real architectural addition."* Captured here at the doc stage where the change is cheap, per [[feedback_mvp_doc_not_mvp]].

## Commitments

- S1 entries are tuples, not vectors. Storage cost increases by a small constant factor (one or two additional fields per unit; rounding error vs. learned reps + content).
- The retriever (R1, R2, R4) is hybrid-capable: query has branches for structural-field-match and surface-field-match, with the relative weighting either learned or configurable.
- The cross-attention interface (I1) attends to multi-field memory entries, not single vectors. The implementation may concatenate fields, attend over each field separately, or learn per-field gating — that mechanism choice is deferred.
- The de-risk experiment ([2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md)) operationalizes failure mode 4 (trajectory-state decodability) as a probe of the trajectory_state architectural commitment.
  - **2026-05-25 update** `[MEASURED]`: in the isolated de-risk, the predictor's trajectory state carried essentially *no* recoverable structure — on the one valid (high-rank) run the predictor beat the mean-guess floor by only +1.1% and trajectory-state retrieval was at chance ([derisk run results](../experiment/2026-05-18-T_A1b-isolation-derisk/derisk-run-results.md)). *Construct-validity note:* this measures the trajectory state produced by the auxiliary loss **alone** (no consumer-LM task, no integration), so it weakens — but does not kill — the `trajectory_state` justification. The field's fate now rides on the coupled formulation or the masked-prediction continuation ([masked-vs-forward-prediction](../open-question/masked-vs-forward-prediction.md)), not on the isolated forward objective. Decision held provisional pending those.

## Reversibility

**Cheap at doc stage, expensive after build.** The decision exists at the architecture-specification level; nothing has been built yet. Reversal before implementation is a doc edit. Reversal after implementation requires reshaping the storage layer, retrieval indices, and the cross-attention interface — a multi-week refactor for a prototype, structural for a product. The decision is committed now because retrofitting hybrid retrieval after building a single-field store is meaningfully harder than starting hybrid.

The natural reversal trigger is if the de-risk experiment shows that `event_rep` *retains* surface fidelity strong enough to serve tier 1-2 alone (i.e., T_A1b doesn't compress as aggressively as predicted). In that case, `raw_content` is redundant. Probability assessed low; the JEPA family is empirically lossy on surface reconstruction.

## Related

- [tier-3-4-as-wedge](./tier-3-4-as-wedge.md) — paired decision; this commitment makes that wedge tractable without regressing tier 1-2.
- [caddy-architecture](../concept/caddy-architecture.md) — the architectural spec this decision modifies (op S1, op R1/R2, op I1).
- [caddy-memory-representation-spectrum](../concept/caddy-memory-representation-spectrum.md) — the spectrum-position commitment is independent of this multi-field commitment; both held provisionally.
- [discrete-unit-memory-architecture](../concept/discrete-unit-memory-architecture.md) — the family pattern; multi-field is a refinement, not a deviation.
- [H41-temporal-context-retrieval](../hypothesis/H41-temporal-context-retrieval.md) — trajectory_state is the concrete instantiation of H41's temporal-context binding.
- [H44-T_A1b-cross-domain-transfer](../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the wedge hypothesis whose representation compression makes this commitment necessary.

---
type: concept
name: Caddy memory-representation spectrum — preconfigured vocabulary vs learned representations
status: living
last_ingested: 2026-05-19
sources: [../source/wu-2022-memorizing-transformer.md, ../source/khandelwal-2020-knn-lm.md, ../source/buzsaki-2015-spw-r.md]
epistemic_tags: [asserted, speculated]
tags: [caddy, architecture, deferred-decision, memory-representation]
---

## Definition

`[ASSERTED]` The **memory-representation spectrum** is the architectural design dimension along which the [caddy](./caddy.md) sits between two pure positions: **preconfigured vocabulary + binding policy** at one end (memory items as binding patterns over fixed primitives) versus **learned representations** at the other (memory items as T_A1-trained codes). The caddy currently commits to a hybrid position on this spectrum, leaning learned-rep, held provisionally pending future evidence. This page exists because the position is *deferred* — it will be revisited when learning forces the call — and because the load-bearing T4 research targets (T_A1b, K2+T_A3) are shape-dependent on it.

This page is referenced by [caddy-architecture](./caddy-architecture.md) as a deferred architectural decision.

## The spectrum

```
PURE PRECONFIGURED                                            PURE LEARNED
       │                                                              │
   kNN-LM                       Caddy                          From-scratch
  (LLM activations            (frozen base +                   trained
   used directly)              light encoder +                 memory net
                               learned codes)
       │                            ↑                                 │
                            current position
```

**Pure preconfigured-vocab + binding policy.** Memory items are *binding patterns* over a fixed vocabulary of primitives (the LLM's activations, or a separate fixed reservoir). LoRA at T1 demonstrates the binding-policy-over-fixed-base pattern at production scale. Cerebellum (Marr 1969 / Albus 1971) and Buzsáki 2015 preconfigured-cell-assemblies frame biology this way. Natural fit for one-shot encoding (M01) and catastrophic-interference resistance (M11).

**Pure learned-rep.** Memory items are *learned codes* produced by a T_A1-trained encoder. Memorizing Transformer, EM-LLM, MEGa, RETRO are precedents. Tight co-training with golfer produces geometric alignment; representations can drift and refine over time.

## Current position: hybrid leaning learned-rep

The base LLM is preconfigured (frozen except for ~4% finetune); the caddy encoder is learned (T_A1-trained); memory items are codes in the encoder's output space. This position is *enough of a direction for the current stage* (AJ explicit, 2026-05-17) — the engineering-tractable path with T1/T2 precedent for most components.

## Why the decision is held provisionally

Per [[feedback_mvp_doc_not_mvp]], three reasons not to lock in:

1. **Biology argues for sliding toward preconfigured.** Buzsáki's preconfigured cell assemblies, Marr/Albus cerebellum, and M14's preconfigured-vocabulary framing all point that direction. Evidence to weigh this against learned-rep's engineering tractability does not yet exist.

2. **Load-bearing T4s are *shape-dependent* on position.** T_A1 (auxiliary world-model loss on memory reps) is defined for learned-rep. K2+T_A3 (schema-fit-modulated consolidation) reshapes codes in the learned-rep direction; in the preconfigured direction it would reshape *bindings*, not codes. Sliding position changes what the T4 bets are betting on.

3. **The architecture doesn't have to choose the full extreme.** Hybrid is a valid permanent position; the question is *where* on the spectrum, not which endpoint.

## Implication for load-bearing T4 commitments

T_A1b and K2+T_A3 are currently named as the two load-bearing T4 research targets in [caddy-architecture](./caddy-architecture.md). Their *content* is conditional on the current spectrum position. A future decision to slide toward preconfigured would require revisiting both T4 specifications, not just adding new ops. Real entanglement; worth surfacing whenever the load-bearing T4 claim is being evaluated.

## Tradeoff table

| Axis | Preconfigured-leaning | Learned-rep-leaning |
|---|---|---|
| Training compute | Cheap per item (binding is small) | Expensive (encoder + co-training) |
| One-shot encoding (M01) | Natural fit — bind once, done | Hard — encoder must handle one-shot |
| Catastrophic interference (M11) | Better — bindings are sparse | Real problem; needs mitigations |
| Compositionality (M16, H43) | Structural in vocabulary space | Emerges from training (H43 bet) |
| Engineering tractability | LoRA T1; full preconfig: T3-T4 | T1/T2 — well-understood territory |
| Co-training with golfer | Looser — binding policy co-trains | Tight — T_A1 shapes both sides |
| Storage cost per item | Small (binding pattern) | Larger (full vector code) |
| Biological precedent | Strong (cerebellum + hippocampus) | Weak (biology lacks backprop) |

## Sibling architectures explicitly not pursued

The caddy's hybrid position is between, not derived from, these full alternatives:

- [reservoir-computing](../open-question/reservoir-computing.md) — pure preconfigured-vocab with random reservoir, no separate caddy
- Pure LoRA-as-memory — no separate caddy at all, per-memory adapters on the golfer
- kNN-LM — pure preconfigured at the activation level, no learned encoder

## When this gets revisited

The decision becomes load-bearing when:
- T_A1 training results indicate the learned encoder is the bottleneck (suggests slide toward preconfig)
- One-shot encoding becomes a measured failure mode of the research prototype (suggests slide toward preconfig)
- Catastrophic interference manifests despite the architectural mitigations (suggests slide toward preconfig)
- Co-training succeeds beyond expectations (suggests stay learned-rep or push further)

## Related

- [[caddy-architecture]] — the architecture this spectrum is part of; references this page as deferred decision
- [[caddy]] — the architectural concept
- [[lora]] — M14-shape preconfigured exemplar at T1
- [[reservoir-computing]] — pure-preconfigured sibling architecture
- [multi-field-memory-unit](../decision/multi-field-memory-unit.md) — independent of this spectrum-position decision; the multi-field commitment preserves raw-content access regardless of where the spectrum slider sits.
- [[feedback_inspiration_not_blueprint]] — discipline for biology-borrowing on this axis
- [[feedback_mvp_doc_not_mvp]] — discipline that justifies deferring

## Source archive

- 2026-05-17 — promoted to its own page during caddy-architecture readability restructure; content originated in the M14-M17 reconciliation pass (extracted from caddy-architecture.md Memory-representation spectrum section to manage parent-doc length while preserving the deferred decision)

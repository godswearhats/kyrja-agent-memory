---
type: source
name: "Behrouz, Zhong & Mirrokni 2024 — Titans: Learning to Memorize at Test Time"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [substrate-memory, test-time-learning, gradient-as-surprise, p1]
---

## Citation

Behrouz, A., Zhong, P. & Mirrokni, V. (2024). *Titans: Learning to Memorize at Test Time.* arXiv:2501.00663. Google Research, December 2024.

## Location

- arXiv: https://arxiv.org/abs/2501.00663
- Rubric note: [substrate-survey/notes/behrouz-2024-titans.md](../../../research/library/substrate-survey/notes/behrouz-2024-titans.md)

## Key claims (with our restatements)

### Three-module architecture

**Paper (§3):** Three memory components — (1) **Core** attention as short-term memory; (2) **Long-term memory** — a deep MLP whose weights update at test time via online gradient descent on associative-memory loss `ℓ(M; x_t) = ‖M(k_t) − v_t‖²`; (3) **Persistent memory** — fixed learnable prefix tokens encoding task knowledge. Three integration variants: MAC (memory as context), MAG (memory as gate), MAL (memory as layer).

**Our restatement:** `[ASSERTED]` — Titans deliberately reintroduces categorical separation (Tulving-style short/long/persistent) but each tier is *learned* rather than hand-engineered. Sits in [P1](../concept/substrate-paradigms.md) substrate-as-state with explicit module structure inside.

### Test-time gradient update with momentum-of-surprise

**Paper (§3.1):** Long-term-memory update rule: `M_t = (1 − α_t)·M_{t-1} + S_t` where `S_t = η_t·S_{t-1} − θ_t·∇ℓ(M_{t-1}; x_t)`. Past surprise (momentum) plus momentary surprise. `α_t` gates forgetting. Paper: *"We design this memory module so an event that violates the expectations (being surprising) is more memorable. To this end, we measure the surprise of an input with the gradient of the neural network with respect to the input."*

**Our restatement:** `[ASSERTED]` — gradient-as-surprise is the cleanest published operationalization of "memorable events violate expectations." Replaces hand-engineered importance/surprise/emotion utility functions used by agentic-memory products. The momentum term tracks *memory of memorability* — second-order surprise.

### Test-time learning satisfies the re-encoding stage

**Paper:** Long-term-memory weights mutate during inference, persisting changes within the sequence.

**Our restatement:** `[ASSERTED]` — Titans is the closest published architecture to Schacter's "re-encode a simulation into memory so that it can influence and guide future behaviors" process. Compared to [Mamba](./gu-dao-2023-mamba.md) which mutates *state*, Titans mutates *weights*. Notebook-vs-learning-brain distinction.

### Scaling

**Paper (§4):** Scales to 2M+ tokens. Beats both Transformer (no long-term-memory module) and Mamba (single substrate) on language modeling and needle-in-haystack benchmarks.

**Our restatement:** `[ASSERTED]` — paper-reported magnitudes. Construct-validity caveat: benchmarks remain sequence-modeling, not agent-memory. Gains translate to the foundation-model tier, not directly to agentic-memory deployment.

## Important caveats

- **Categorical separation reintroduced.** Titans cites Willingham 1997 ("memory is a confederation of systems — short-term, working, and long-term"). The categorical view is at odds with more recent neuroscience moves toward dimensional / dissolved categories. Titans does not ablate against a single-module dimensional version, so it's unclear whether *categorical structure* matters or whether the *learned forgetting + surprise + capacity* are doing the work `[ASSERTED]`.
- **No cross-session continuity.** Test-time learning lasts one inference; weights revert at sequence boundaries `[ASSERTED]`. See [cross-session-continuity](../open-question/cross-session-continuity.md).
- **No explicit retrieval surface.** The memory module accepts inputs and produces outputs; you cannot directly query it for "what about X?" `[ASSERTED]`.
- **No active recombination.** Memory updates but does not construct novel scenarios from fragments — Schacter's second process is not implemented.

## Relevance to Kyrja

- Anchors [substrate-paradigms](../concept/substrate-paradigms.md) as the deepest P1 substrate-as-state realization.
- Anchors [substrate-as-memory](../concept/substrate-as-memory.md) — existence proof for learned substrate-level memory.
- Anchors [consolidation-channel](../concept/consolidation-channel.md) as one operator shape — gradient-driven surprise-weighted update to a dedicated memory subnetwork.
- Reusable for Kyrja: gradient-as-surprise as a learned forgetting/encoding signal; momentum-of-surprise for stability; test-time update of a *small subnetwork* (not the whole model) as a deployable agent-memory primitive.

## Audit history

- 2026-05-13 — verbatim read, pp.1-15 (core sections §1-§4), rubric note written.

## Archive location

arXiv:2501.00663. Not in `library/papers/`. Fetch from arXiv for re-verification.

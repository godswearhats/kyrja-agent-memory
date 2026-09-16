---
type: source
name: "Gu & Dao 2023 — Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [substrate-memory, ssm, state-space-model, foundational, p1]
---

## Citation

Gu, A. & Dao, T. (2023). *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* arXiv:2312.00752. Revised May 2024.

## Location

- arXiv: https://arxiv.org/abs/2312.00752
- Code: https://github.com/state-spaces/mamba
- Rubric note: [substrate-survey/notes/gu-dao-2023-mamba.md](../../../research/library/substrate-survey/notes/gu-dao-2023-mamba.md)

## Key claims (with our restatements)

### Selective state-space model

**Paper (§3):** A foundation-model architecture where token output `y_t = C·h_t` is driven by a recurrent hidden state `h_t = Ā·h_{t-1} + B̄·x_t`. The state dimension is `N=16` per channel. The critical move: `(A, B, C, Δ)` are *functions of the input* (selective). Large `Δ` resets the state; small `Δ` persists state and ignores current input. Hardware-aware implementation keeps the recurrence in GPU SRAM rather than HBM.

**Our restatement:** `[ASSERTED]` — Mamba is the architecture-level realization of the substrate-as-state paradigm ([P1](../concept/substrate-paradigms.md)). The hidden state is the memory; there is no separate store.

### Compression-as-memory framing

**Paper (§3.1):** "A fundamental problem of sequence modeling is *compressing context into a smaller state.* ... attention is both effective and inefficient because it explicitly does not compress context at all... recurrent models are efficient because they have a finite state, implying constant-time inference and linear-time training. However, their effectiveness is limited by how well this state has compressed the context."

**Our restatement:** `[ASSERTED]` — useful memory is the *lossy compression* of past experience into state, not the retention of the experience itself. Reframes the design space for [substrate-as-memory](../concept/substrate-as-memory.md) by making selection-pressure on what to retain into a learning problem.

### Selectivity = active forgetting

**Paper (§3.5 Filtering Context):** "Selective models can simply reset their state at any time to remove extraneous history, and thus their performance in principle improves monotonically with context length."

**Our restatement:** `[ASSERTED]` — production-scale evidence that *learned* forgetting (input-dependent `Δ`) improves performance. The agentic-memory products' hand-engineered importance/surprise/emotion utility functions are an unlearned analog of this primitive.

### Empirical performance

**Paper (§4 results):** Matches Transformer quality at half the parameters; ~5× faster inference; works on million-length sequences.

**Our restatement:** `[ASSERTED]` magnitudes are paper-reported on language-modeling benchmarks (Pile, LAMBADA, ARC, HellaSwag). Construct-validity caveat: "matches Transformer quality" is at the model-pretraining tier, not at the agentic-memory tier our thesis cares about. Mamba is foundational pre-condition evidence, not direct agent-memory evidence.

## Important caveats

- **Foundation-model scope.** Mamba is a sequence model. It does not implement cross-session persistence, multi-agent state, or constructive retrieval. See [cross-session-continuity](../open-question/cross-session-continuity.md).
- **State capacity bounded.** `N=16` per channel. Million-token sequences work because most information is forgotten via selection; not because state is large.
- **Hidden-state plateau.** Sun et al. 2024 ([TTT](./sun-2024-ttt.md)) demonstrate Mamba's perplexity plateaus at ~16k tokens — the vector hidden state is too small to keep absorbing information. TTT-MLP keeps reducing perplexity past this point. `[ASSERTED]`

## Relevance to Kyrja

- Anchors [substrate-paradigms](../concept/substrate-paradigms.md) as the P1 (substrate-as-state) foundational reference.
- Anchors [substrate-as-memory](../concept/substrate-as-memory.md) as the foundation-model-scale proof point for the paradigm.
- Anchored in [H29-edge-substrate-memory](../hypothesis/H29-edge-substrate-memory.md) field-consensus evidence (already cited as Mamba-3 successor lineage).
- Reusable for Kyrja: input-dependent `Δ` as a learned forgetting primitive; compression-as-memory framing; boundary-resetting for episode structure.
- Distinct from later [Mamba-3](./mamba-3-2026.md) (March 2026 frontier successor); this page anchors the *original* Mamba paper that established the paradigm.

## RC genealogy (added 2026-05-17)

`[ASSERTED]` Mamba is the modern realisation of a mathematical framework that traces back to reservoir computing. The underlying object — a continuous-time linear state-space model `x'(t) = A·x(t) + B·u(t), y(t) = C·x(t) + D·u(t)` — is the same one underlying ESN/LSM in their linear approximations.

The genealogy abandons progressively more of pure-RC's commitments:

| Era | Paper | A matrix |
|---|---|---|
| 2001/2002 | [ESN](../open-question/reservoir-computing.md) / [LSM](./maass-2002-lsm.md) | Random, fixed |
| 2022 | [S4](./gu-goel-re-2022-s4.md) | Structured (HiPPO-initialised), gradient-trained |
| 2023 | Mamba (this page) | Structured, trained, **input-dependent** (selectivity) |

The fixed-substrate commitment that motivated RC's biological-precedent argument has been **systematically traded for capability** by RC's engineering descendants. Mamba's selectivity is the explicit content-aware-dynamics extension that distinguishes the modern lineage from classical RC. See [reservoir-computing § Literature-review findings, Finding 1](../open-question/reservoir-computing.md#literature-review-findings-2026-05-17) for the full convergence-vs-divergence framing.

## Audit history

- 2026-05-13 — verbatim read, pp.1-15 (core sections §1-§4), rubric note written. Section/equation references in this page anchor to that read.

## Archive location

arXiv:2312.00752. Not in `library/papers/`. Fetch from arXiv for re-verification.

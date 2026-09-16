---
type: source
name: "Graves, Wayne & Danihelka 2014 — Neural Turing Machines"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [substrate-memory, memory-augmented-networks, foundational, p2]
---

## Citation

Graves, A., Wayne, G. & Danihelka, I. (2014). *Neural Turing Machines.* arXiv:1410.5401. Google DeepMind.

## Location

- arXiv: https://arxiv.org/abs/1410.5401
- Rubric note: [substrate-survey/notes/graves-2014-ntm.md](../../../research/library/substrate-survey/notes/graves-2014-ntm.md)

## Key claims (with our restatements)

### Differentiable controller + external memory matrix

**Paper (§3-§4):** Neural network controller (LSTM or feedforward) coupled to an external `N×M` memory matrix via differentiable read/write heads. Each head produces a normalized weighting `w_t` over `N` memory locations. Reads: `r_t = Σ w_t(i)·M_t(i)`. Writes: erase-then-add — `M_t(i) ← M_{t-1}(i)·(1 − w_t(i)·e_t) + w_t(i)·a_t`. Whole system trained end-to-end with gradient descent.

**Our restatement:** `[ASSERTED]` — NTM is the foundational paper for [P2 substrate-as-module](../concept/substrate-paradigms.md). Memory is a separate, addressable, differentiable store the controller learns to use.

### Hybrid content + location addressing

**Paper (§3.3):** Addressing combines content-based focus (cosine similarity to a key `k_t`, sharpened by `β_t`) with location-based shifts (interpolation gate `g_t`; convolutional shift `s_t`; sharpening `γ_t`). Allows both "find similar memory" and "find the memory after the one we just touched."

**Our restatement:** `[ASSERTED]` — agentic-memory products implement only content addressing (vector similarity over an external DB). Location-based access (iteration, structural-position lookup) is a capability the agentic field has dropped from the NTM lineage.

### Differentiability is load-bearing

**Paper (throughout):** The controller LEARNS how to use memory; the addressing policy is not hand-engineered.

**Our restatement:** `[ASSERTED]` — every agentic-memory product ([Mem0](../incumbent/mem0.md), [Letta](../incumbent/letta.md), [Zep](../incumbent/zep.md), [Cognee](../incumbent/cognee.md), [LightMem](../incumbent/lightmem.md)) is a degenerate-P2 descendant of NTM that dropped end-to-end differentiability when it switched to frozen LLMs. The result: NTM's *learnable* memory became the agentic field's *engineered* memory.

### Cog-sci framing

**Paper:** Baddeley's working memory model (cited). Variable-binding (Hadley, Plate, Kanerva — cited).

**Our restatement:** `[ASSERTED]` — NTM scopes to *working memory only*. It does not engage episodic memory, constructive simulation, or active forgetting. Honest scoping. The agentic-memory field over-extended NTM's working-memory pattern to long-term episodic use cases, which is where the cargo-culting begins.

## Important caveats

- **Memory reset between sequences.** No cross-session persistence `[ASSERTED]`. See [cross-session-continuity](../open-question/cross-session-continuity.md).
- **Fixed-size memory.** `N` locations, `M` dimensions per location; doesn't grow with experience.
- **No surprise-driven encoding.** Writes happen whenever the controller chooses; no salience signal `[ASSERTED]`. Compare [Titans](./behrouz-2024-titans.md) gradient-as-surprise.
- **No active decay.** Memory persists until explicitly erased.
- **No constructive retrieval.** Read = weighted sum; no recombination of fragments into novel outputs.

## Relevance to Kyrja

- Anchors [substrate-paradigms](../concept/substrate-paradigms.md) as the P2 substrate-as-module foundational reference.
- Anchors the "memory-as-module vs memory-as-state" design split in [substrate-as-memory](../concept/substrate-as-memory.md).
- Names the agentic-memory field's architectural lineage and the specific capability ([differentiable end-to-end](../concept/active-stages-framework.md)) the field has lost.
- Reusable for Kyrja: differentiable controller-memory coupling (cost: fine-tuning), location-based addressing, erase-and-add as a clean write primitive, multiple parallel read/write heads.

## Audit history

- 2026-05-13 — verbatim read, pp.1-14 (core sections §1-§4), rubric note written.

## Archive location

arXiv:1410.5401. Not in `library/papers/`. Fetch from arXiv for re-verification.

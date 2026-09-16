---
type: source
name: "Adaptive Memory Admission Control (arxiv 2603.04549, Mar 2026)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [admission-control, learned-gate, wedge-relevant]
---

## Citation

*Adaptive Memory Admission Control for Long-Horizon LLM Agents.* arXiv:2603.04549, March 2026.

## Location

- arXiv: https://arxiv.org/abs/2603.04549

## Key claims (with our restatements)

### Learned admission gate

**Paper:** Trains a **learned gate** that decides whether each candidate memory should be admitted to the long-term store. Operates *before* embedding and indexing — i.e., the storage cost of rejected memories is zero, and the retrieval-side scaling problem is reduced at the source.

**Our restatement:** This is the **most important architectural idea for billion-scale agentic memory** in the deep-dive. If 80% of agent memories are redundant or low-value, preventing their creation is orders of magnitude cheaper than storing and searching them. The cascading-failures regime is reduced at the source by reducing the corpus size.

### Empirical claim

**Paper:** Shows that admission control captures the value of consolidation with a fraction of the cost — by deciding upfront whether a memory deserves storage at all.

**Our restatement:** `[ASSERTED]`. We have not read the paper verbatim per [feedback_load_bearing_sources]; the deep-dive's framing rests on this paper but the magnitude of the wedge is paraphrased. Pin to verbatim if downstream decisions ride on the specific numbers.

### The open question the paper raises

If a learned gate decides admission, **what is the training signal?** Utility labels are noisy (we only know which memories proved useful in retrospect). The paper offers one approach; the broader question is open.

## Relevance to Kyrja

- Anchors the **top layer (Admission Control)** of [seven-layer stack](../concept/seven-layer-stack.md).
- Sources [admission control](../concept/admission-control.md) concept page.
- Directly relevant to the **write-side quality gate** decision implied by H-QUAL-FLOOR. If admission control is a learned gate trained on utility signal, our slot-format-encoding work is *complementary* (not redundant) — slot-format handles encoding once admitted; admission decides whether to encode at all.
- LightMem's "sensory memory" filtering stage is a non-learned, entropy-based approximation of the admission-control idea. See [LightMem incumbent page](../incumbent/lightmem.md).

## Archive location

Not currently in `library/papers/`. Fetch from arXiv to verify specific claims before any load-bearing use.

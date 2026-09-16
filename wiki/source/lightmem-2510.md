---
type: source
name: "LightMem — Atkinson-Shiffrin-Inspired Memory Framework (arxiv 2510.18866, ICLR 2026)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [incumbent-anchor, integration-gap, consolidation]
---

## Citation

Authors at ZJU NLP. *LightMem: Lightweight and Efficient Memory-Augmented Generation.* arXiv:2510.18866, ICLR 2026.

## Location

- arXiv: https://arxiv.org/abs/2510.18866
- GitHub: https://github.com/zjunlp/LightMem
- HuggingFace blog: https://huggingface.co/blog/xzwnlp/lightmem

## Key claims (with our restatements)

### Architecture

**Paper:** Three-stage memory inspired by Atkinson-Shiffrin (sensory → short-term → long-term):

1. **Sensory Memory** — rapid filtering via lightweight compression (LLMLingua-2 or entropy-based); groups by topic.
2. **Short-term Memory** — consolidates topic groups, organizes, summarizes.
3. **Long-term Memory** — offline "sleep-time" update decoupled from online inference.

Qdrant as vector backend (HNSW). Retrieval modes: Embedding (semantic), Context (BM25), Hybrid. Hierarchical: session-level summaries first, fine-grained entries second. Configurable score-threshold conflict detection + LLM-based knowledge fusion.

**Our restatement:** LightMem is the first incumbent to take **consolidation as a first-class concern** (the offline "sleep-time" update is the consolidation layer's idea in our [seven-layer stack](../concept/seven-layer-stack.md)). Storage is still HNSW; consolidation is the differentiator.

### Vendor benchmarks

**Paper:** Up to 10.9% accuracy gains on LongMemEval. Token usage reduced 117x. API calls reduced 159x. Runtime reduced 12x+.

**Our restatement:** `[ASSERTED]`. Same construct-validity concern as all LongMemEval-based claims — conversational memory ≠ agentic memory on code/reasoning corpora. The 117x token reduction is large enough to be a structural property of the consolidation design, not benchmark gaming — worth deeper attention than the accuracy delta.

## Relevance to Kyrja

- Anchors [LightMem incumbent page](../incumbent/lightmem.md).
- LightMem is the strongest incumbent on the **consolidation layer** of [seven-layer stack](../concept/seven-layer-stack.md). Also touches admission control (via sensory-memory filtering) and retrieval. Does not address tiered storage, multi-vector embedding, or graph memory.
- The offline-sleep-time consolidation pattern aligns with the streaming-LSM-compaction shape in the consolidation layer of our hypothetical stack.
- Token/API-call reduction at this magnitude is direct evidence for the cost leg of the scale thesis.

## Archive location

Not currently in `library/papers/`. Fetch from arXiv to verify any specific claim.

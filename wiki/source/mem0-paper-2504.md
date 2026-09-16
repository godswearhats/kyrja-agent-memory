---
type: source
name: "Mem0 — Memory Layer for AI Agents (arxiv 2504.19413) and vendor material"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [incumbent-anchor, integration-gap]
---

## Citation

Mem0 team. *Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory.* arXiv:2504.19413, Apr 2025. Plus vendor benchmarks page and component documentation.

## Location

- arXiv: https://arxiv.org/abs/2504.19413
- Vector DB overview: https://docs.mem0.ai/components/vectordbs/overview
- Embedder docs: https://docs.mem0.ai/components/embedders/models/openai
- Memory update operations: https://docs.mem0.ai/core-concepts/memory-operations/update
- Benchmarks: https://mem0.ai/research
- Independent breakdown (Dwarves): https://memo.d.foundation/breakdown/mem0
- Independent eval: https://guptadeepak.com/the-ai-memory-wars-why-one-system-crushed-the-competition-and-its-not-openai/

## Key claims (with our restatements)

### Architecture

**Paper/vendor:** Provider-agnostic vector store (20+ backends via factory pattern: Qdrant, Chroma, PGVector, Pinecone, Upstash, Azure AI Search). SQLite for change history. Two-phase pipeline: Extraction (LLM extracts facts) → Update (vector similarity check, then LLM ADD/UPDATE/DELETE/MERGE). v2.0+ uses single-pass ADD-only at ~half the latency. All LLM ops use GPT-4o-mini.

**Our restatement:** Mem0 delegates indexing to its chosen backend (HNSW in every case). The differentiator is the LLM-mediated dedup pipeline, not the storage. Every write triggers an LLM call (or a vector similarity check at minimum), creating per-write latency that grows with corpus size.

### Vendor benchmarks

**Paper/vendor:** 91.6 LoCoMo, 93.4 LongMemEval, 64.1/48.6 BEAM (1M/10M tokens). P95 ~1.44s (selective pipeline), ~2.59s (graph-enhanced Mem0g). Averages <7,000 tokens per retrieval call. Processing 1B+ tokens/day in production.

**Our restatement:** `[ASSERTED]`. Independent evaluation (Gupta Deepak, cited in deep-dive §4) scored Mem0 at **49.0% on LongMemEval** vs vendor-claimed 93.4 — alternatives scored 63-91%. Construct-validity concern: vendor benchmarks on conversational memory (LoCoMo) approximate but do not equal agentic-memory recall on code/reasoning corpora. The 1B-tokens/day claim is throughput, not vectors-stored.

### Acknowledged limitations

**Paper/vendor:** Weak at temporal reasoning, event ordering, multi-session reasoning at 10M scale. LLM call on every add() creates latency. Graph memory paywalled at $249/month.

**Our restatement:** The temporal/multi-session weakness is the same gap Zep markets against. The 10M-scale break is consistent with the cascading-failures regime onset.

## Relevance to Kyrja

- Anchors [Mem0 incumbent page](../incumbent/mem0.md).
- Mem0 occupies the **admission-control (LLM-mediated, expensive) + embedding + retrieval layers** of [seven-layer stack](../concept/seven-layer-stack.md); it does not address tiered storage, multi-vector embedding, or graph memory as integrated primitives (Mem0g is bolt-on).
- The independent-eval discrepancy (49% vs 93%) is the kind of benchmark-chaos signal that motivates Kerman's MASQ work.

## Archive location

Not currently in `library/papers/`. Fetch from arXiv to verify any specific claim.

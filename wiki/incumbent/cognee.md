---
type: incumbent
name: Cognee
status_current_as_of: 2026-05-12
last_ingested: 2026-05-12
sources: [source/cognee-docs.md]
tags: [incumbent, integration-gap, graph-rag]
---

## What it does

Open-source agentic-memory framework that combines a pluggable vector backend with a pluggable graph backend, plus a six-stage "cognify" pipeline (classify → permissions → chunk → LLM entity/relationship extraction → summarize → embed + commit edges). Retrieval is hybrid GraphRAG with five modes (CHUNKS, SUMMARIES, INSIGHTS, GRAPH_COMPLETION, RAG_COMPLETION).

See [Cognee vendor source](../source/cognee-docs.md) for the underlying material.

## What it doesn't

- **Owned storage primitive.** Cognee delegates indexing entirely to whatever backend the user picks (LanceDB, Qdrant, PGVector, Weaviate, etc.) — all of which use HNSW. Whatever scale limit the backend has, Cognee inherits.
- **Admission control.** Everything that enters the pipeline is processed and stored; no learned gate, no LSH-pre-dedup, no importance scoring before embedding.
- **Multi-vector embedding.** Single-vector dense throughout. Subject to the [LIMIT bound](../source/weller-2025-limit.md).
- **Tiered storage.** Single-tier whatever-the-backend-provides.
- **Billion-scale claims.** Vendor explicitly acknowledges scaling-to-terabyte-datasets as a known gap.

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

| Layer | Coverage |
|---|---|
| Admission Control | ✗ — no gate; everything enters the pipeline |
| Embedding | ◐ — pluggable but single-vector dense; default OpenAI large |
| Multi-Graph Memory | ◑ — one graph (entity/relationships) via the chosen graph backend; not multi-graph (no temporal/causal/structural split) |
| Tiered Storage | ✗ |
| Retrieval | ✓ — five-mode hybrid GraphRAG is genuinely rich |
| Consolidation | ◐ — "memify" pruning exists but is not load-bearing in claims |
| Governance | ✗ |

**Net: ~1.5 of 7 layers materially covered.** The graph layer is the only real differentiator; everything else is delegated.

## Where it fails

- **At scale.** Vendor itself acknowledges scaling-to-terabyte gap. Underlying HNSW backends hit the [cascading-failures regime](../concept/cascading-failures.md) at billion scale.
- **Construct-validity of benchmark claims.** Vendor reports +25% Human-like Correctness and +314% DeepEval F1 vs LightRAG/Graphiti/Mem0 on default settings. `[ASSERTED]`; not independently replicated; benchmark-chaos concern applies.
- **Latency.** The "1 GB in ~40 minutes using 100+ containers" throughput point implies the LLM-mediated cognify pipeline does not scale linearly with hardware in a cost-effective way.

## Adoption signal

1M+ pipelines/month across 70+ companies (Bayer, University of Wyoming named). Strong open-source presence.

## Related

- [Cognee source roll-up](../source/cognee-docs.md) — vendor docs, benchmarks, integration write-ups.
- [Seven-layer stack](../concept/seven-layer-stack.md) — the architecture Cognee partially covers.
- [Cascading-failures product](../concept/cascading-failures.md) — the scale regime Cognee inherits from its HNSW backends.

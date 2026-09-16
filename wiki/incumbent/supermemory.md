---
type: incumbent
name: Supermemory
status_current_as_of: 2026-07-22
last_ingested: 2026-07-22
sources: [source/supermemory-docs.md, ../experiment/2026-07-22-masq-supermemory-smoke.md]
tags: [incumbent, integration-gap, extraction-first, masq-tested]
---

## What it does

Memory and context engine for AI systems. Five-component application surface: Memory Engine (fact extraction + contradiction resolution), User Profiles (static facts + dynamic context), Hybrid Search (RAG + memory in one query), Connectors (Google Drive, Gmail, Notion, GitHub real-time sync), File Processing (PDFs, images, video, code). MIT-licensed core, with pluggable vector backends (bring-your-own Pinecone / Weaviate / Qdrant).

See [Supermemory vendor source](../source/supermemory-docs.md) for the underlying material.

## What it doesn't

- **Owned storage primitive.** Same delegated-backend posture as Cognee and Mem0. Storage scale is whatever the chosen backend provides.
- **Multi-vector embedding.** Single-vector dense throughout. `[ASSERTED]` ([source](../source/supermemory-docs.md); construct-validity note: vendor doesn't publish the embedding dimension explicitly; the multi-vector absence is inferred from architecture descriptions, not directly stated).
- **Multi-graph memory.** A single "memory graph" with ontology-aware edges; not the four-graph split (semantic / temporal / causal / structural) in our [seven-layer stack](../concept/seven-layer-stack.md).
- **Tiered storage.**
- **Independently verified benchmark performance.** Vendor self-reports #1 on LongMemEval (81.6%), LoCoMo, ConvoMem; no third-party replication at this ingest.

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

| Layer | Coverage |
|---|---|
| Admission Control | ◐ — LLM-mediated fact extraction + contradiction resolution at write; not a learned pre-embedding gate |
| Embedding | ◐ — single-vector dense via configurable backend |
| Multi-Graph Memory | ◐ — one ontology-aware memory graph; not multi-graph |
| Tiered Storage | ✗ |
| Retrieval | ✓ — hybrid RAG + memory in one query; sub-300ms claimed |
| Consolidation | ◐ — vendor cites "auto-forgetting"; mechanism opaque, not load-bearing in claims |
| Governance | ✗ |

**Net: ~2 of 7 layers materially covered.** The unusual feature is *application surface* (RAG + memory + connectors + file processing in one API), not depth at any specific layer.

## Where it fails

- **Extraction-first lossiness.** Conversations compressed into discrete facts at ingest discards nuanced technical context. For engineering-team use cases where the *interaction context* matters (not just the surface fact), this is a structural ceiling.
- **First-party MASQ measurement (2026-07-22, PRELIMINARY).** Tested as MASQ system #2 (self-hosted v0.0.3, claude-opus-4-8 extraction): `[MEASURED]` A=8% / B-FAIL on the smoke core — below the scope-blind floor — with 0 scope-bound kernel-entity memories in retrieved sets despite all source sessions naming their scope. Consistent with the lossiness ceiling above in a sharpened, mechanism-specific form (scope qualifiers stripped at write time; candidate mechanism [H46](../hypothesis/H46-consolidation-scope-smear.md)). **Held methodology-suspect pending the audit items in the [experiment page](../experiment/2026-07-22-masq-supermemory-smoke.md)** — do not cite as a settled benchmark number.
- **Benchmark numbers vendor-only.** 81.6% LongMemEval vendor self-report; no independent replication. The [benchmark-replication-gap](../concept/benchmark-replication-gap.md) concern applies.
- **Storage-primitive depth.** Like Cognee, scaling is inherited from the chosen backend (Pinecone / Weaviate / Qdrant), all of which are HNSW-based. Same [cascading-failures](../concept/cascading-failures.md) regime exposure at billion-scale.

## Adoption signal

Early-stage (seed). Named angels with strong AI-infra credibility (Jeff Dean, Cloudflare CTO, etc.). Named customers are small AI startups (Cluely, Montra, Scira per fresh-Claude synthesis May 2026) — no evidence of adoption by established engineering organisations. `[ASSERTED]`; treat as directional.

## Related

- [Supermemory vendor source](../source/supermemory-docs.md).
- [Cognee](./cognee.md) and [Mem0](./mem0.md) — the other delegated-backend extraction-first incumbents.
- [Seven-layer stack](../concept/seven-layer-stack.md).
- [Substrate paradigms](../concept/substrate-paradigms.md) — Supermemory is squarely in the extraction-first quadrant.

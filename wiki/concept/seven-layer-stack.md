---
type: concept
name: Seven-Layer Integration Stack
status: timeless
last_ingested: 2026-05-14
sources: [../source/admission-control-2603.md, ../source/cognee-docs.md, ../source/letta-memgpt.md, ../source/lightmem-2510.md, ../source/mem0-paper-2504.md, ../source/zep-graphiti-2501.md, ../source/supermemory-docs.md, ../source/hindsight-docs.md, ../source/honcho-docs.md, ../source/langmem-docs.md]
epistemic_tags: [asserted]
tags: [integration-gap, architecture, scale-thesis]
---

## Definition

The **seven-layer integration stack** is the architecture that, per our thesis, must exist end-to-end for agentic memory to scale past the cascading-failures regime. Each layer exists in production or peer-reviewed research; no incumbent integrates more than one or two layers.

## The layers

1. **[Admission Control](./admission-control.md)** — learned gate ([arxiv 2603.04549](../source/admission-control-2603.md)), dedup via LSH before embedding, importance scoring. Decides what enters the system at all.
2. **Embedding** — [multi-vector (ColBERT/MUVERA)](./multi-vector-retrieval.md) for code, code-specific models (Qodo-Embed-1), SPLADE sparse vectors in parallel, AST-aware chunking via tree-sitter.
3. **[Multi-Graph Memory](./graph-memory-approaches.md)** — four graphs maintained in parallel: semantic (entity relationships), temporal (fact validity windows), causal (what caused what), structural (code deps, imports).
4. **[Tiered Storage](./beyond-hnsw-approaches.md)** — Hot (0-30d): HNSW in RAM + RaBitQ. Warm (30-365d): DiskANN on NVMe. Cold (365d+): S3 Vectors / TurboPuffer. GPU indexing (CAGRA) for bulk ingestion.
5. **Retrieval** — hybrid dense + SPLADE + BM25, graph traversal (multi-hop), partition-first filtering (per-service), cross-encoder reranking, MemR3-style reflective reasoning loop.
6. **Consolidation** — streaming LSM-style compaction, SimpleMem recursive consolidation, utility-based forgetting, automatic tier migration.
7. **Governance** *— referenced in the thesis's narrative description ("admission control → multi-vector → multi-graph → tiered storage → hybrid retrieval → consolidation → governance") but not drawn in deep-dive §10's diagram. Flagged as a documentation discrepancy needing resolution before this concept is fully load-bearing.*

## Diagram (from deep-dive §10)

```
+---------------------------------------------+
|           Admission Control Layer            |
|  - Learned gate (arxiv 2603.04549)           |
|  - Dedup via LSH before embedding            |
|  - Importance scoring                        |
+----------------------+-----------------------+
                       |
+----------------------v-----------------------+
|            Embedding Layer                   |
|  - Multi-vector (ColBERT/MUVERA) for code    |
|  - Code-specific (Qodo-Embed-1)              |
|  - SPLADE sparse vectors in parallel         |
|  - AST-aware chunking via tree-sitter        |
+----------------------+-----------------------+
                       |
+----------------------v-----------------------+
|         Multi-Graph Memory Layer             |
|  - Semantic graph (entity relationships)     |
|  - Temporal graph (fact validity windows)    |
|  - Causal graph (what caused what)           |
|  - Structural graph (code deps, imports)     |
+----------------------+-----------------------+
                       |
+----------------------v-----------------------+
|          Tiered Storage Layer                |
|  Hot  (0-30d):  HNSW in RAM + RaBitQ         |
|  Warm (30-365d): DiskANN on NVMe SSD         |
|  Cold (365d+):  S3 Vectors / TurboPuffer     |
|  GPU indexing (CAGRA) for bulk ingestion     |
+----------------------+-----------------------+
                       |
+----------------------v-----------------------+
|           Retrieval Layer                    |
|  - Hybrid: dense + SPLADE + BM25             |
|  - Graph traversal (multi-hop)               |
|  - Partition-first filtering (per-service)   |
|  - Cross-encoder reranking                   |
|  - MemR3-style reflective reasoning loop     |
+----------------------+-----------------------+
                       |
+----------------------v-----------------------+
|         Consolidation Layer                  |
|  - Streaming LSM-style compaction            |
|  - SimpleMem recursive consolidation         |
|  - Utility-based forgetting                  |
|  - Automatic tier migration (hot>warm>cold)  |
+----------------------------------------------+
```

(Note: the §10 diagram draws 6 layers; the 7th (governance) appears in the thesis's narrative description but not the diagram. Discrepancy flagged above.)

## Role in Kyrja thesis

This is **the load-bearing claim of the integration-gap leg** of our scale thesis. The argument: every layer exists somewhere, but no incumbent (Cognee, Mem0, Letta, Zep) integrates more than one or two. Whoever ships the integrated stack owns the infrastructure layer for next-generation AI agents.

## Epistemic status

`[ASSERTED]`. Per-layer evidence is sourced from the incumbent papers and vendor docs: [Cognee](../source/cognee-docs.md), [Mem0](../source/mem0-paper-2504.md), [Zep](../source/zep-graphiti-2501.md), [LightMem](../source/lightmem-2510.md), [Letta/MemGPT](../source/letta-memgpt.md). The "no incumbent integrates >2 layers" claim is verifiable from the incumbent-mapping table immediately below (this page) — Kyrja-internal synthesis of those source docs, not an external study. We do **not** have empirical demonstration that integrating all seven outperforms a one-or-two-layer incumbent at any specific task. Goal 5 (MTP build) is the first step toward that evidence.

## Incumbent mapping

Each incumbent page marks which layers it materially covers; see the layer-coverage tables on each page. Per-layer rollup as of 2026-05-14:

| Layer | Cognee | Mem0 | Zep | LightMem | Letta | Supermemory | Hindsight | Honcho | LangMem |
|---|---|---|---|---|---|---|---|---|---|
| Admission Control | ✗ | ◐ | ✗ | ◑ | ◐ | ◐ | ◐ | ✗ | ✗ |
| Embedding | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ |
| Multi-Graph Memory | ◑ | ◐ | ◑ | ✗ | ✗ | ◐ | ◑ | ✗ | ✗ |
| Tiered Storage | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ |
| Retrieval | ✓ | ✓ | ✓ | ✓ | ◐ | ✓ | ✓ | ◐ | ◐ |
| Consolidation | ◐ | ◐ | ◐ | ✓ | ◐ | ◐ | ◑ | ✓ | ◐ |
| Governance | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Materially covered** | ~1.5 | ~2 | ~2.5 | ~2.5 | ~1.5 | ~2 | ~2.5 | ~1.5 | ~0.5–1 |

Symbols: ✓ strong, ◑ partial-strong, ◐ partial-weak, ✗ absent.

**Net:** every layer has at least one incumbent that touches it; no incumbent covers more than ~2.5 layers (now reached by Zep, LightMem, and Hindsight). Governance is uncovered across the entire set of nine memory-system incumbents. This is the [integration gap](../archive/BIG-PICTURE-2026-05-14.md) the (pre-2026-05-14) bolt-on wedge thesis was anchored on. The 2026-05-14 expansion (Supermemory, Hindsight, Honcho, LangMem) does not invalidate the ~2.5-layer ceiling — it widens the population of evidence supporting it. Honcho's strong consolidation coverage and Hindsight's tie with Zep at 2.5 layers are the most architecturally interesting additions; both gesture toward [consolidation-channel](./consolidation-channel.md) shapes that older incumbents lacked.

Pages: [cognee](../incumbent/cognee.md) | [mem0](../incumbent/mem0.md) | [zep](../incumbent/zep.md) | [lightmem](../incumbent/lightmem.md) | [letta](../incumbent/letta.md) | [supermemory](../incumbent/supermemory.md) | [hindsight](../incumbent/hindsight.md) | [honcho](../incumbent/honcho.md) | [langmem](../incumbent/langmem.md).

## Wedge implication

The tool-chain wedge is a deliberately narrow first-product that touches 2-3 of these layers (admission control, embedding, retrieval — see [structured-filter-first](../decision/structured-filter-first.md)). The wedge doesn't claim to solve the seven-layer integration; it claims to *earn the right* to take the integration problem on by paying for itself first.

## Source archive

Concept synthesized from deep-dive §10 (agentic-memory-scaling-deep-dive.md, lines 960-1042).

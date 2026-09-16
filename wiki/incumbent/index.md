---
name: Incumbents — index
status: living
last_ingested: 2026-05-14
sources: []
---

# Incumbents

*Catalog of the products and systems Kyrja's [integration-gap thesis](../archive/BIG-PICTURE-2026-05-14.md#three-legs-of-evidence) tests itself against. (Thesis archived 2026-05-14 pending substrate-vs-bolt-on [path-decision](../NOW.md); the incumbent catalogue remains current evidence regardless of which path Kyrja commits to.) Two categories — full memory systems (which integrate retrieval, storage, and some subset of the seven layers) and vector-DB substrate (which sit at one layer of the stack and are composed into memory systems by others).*

For the per-layer coverage rollup table (✓ / ◑ / ◐ / ✗ across all five memory-system incumbents on each of the seven layers), see [seven-layer-stack § Incumbent mapping](../concept/seven-layer-stack.md#incumbent-mapping).

---

## Memory-system incumbents

Full memory products. The integration-gap claim is that none of these covers more than ~2.5 of the seven layers in [seven-layer-stack](../concept/seven-layer-stack.md), and governance is uncovered across the entire set.

- [Cognee](./cognee.md) — pluggable backends + GraphRAG; ~1.5 layers covered; vendor acknowledges terabyte-scale gap.
- [Mem0](./mem0.md) — provider-agnostic vector layer + LLM-mediated dedup; ~2 layers; the 49% vs 93% benchmark discrepancy (vendor vs independent) is the [benchmark-replication-gap](../concept/benchmark-replication-gap.md) headline data point.
- [Zep / Graphiti](./zep.md) — Neo4j temporal-knowledge-graph + triple hybrid retrieval; ~2.5 layers covered (tied highest in the set); post-ingest retrieval lag.
- [LightMem](./lightmem.md) — three-stage Atkinson-Shiffrin + offline consolidation; ~2.5 layers; 117× token reduction at small-scale benchmarks.
- [Letta](./letta.md) — LLM-OS tiered memory primitive; ~1.5 layers; tier migration is agent-driven (doesn't scale).
- [Supermemory](./supermemory.md) — extraction-first with broad application surface (RAG + memory + connectors + file processing); ~2 layers; depth shallow at every layer, breadth is the differentiator.
- [Hindsight](./hindsight.md) — three biomimetic pathways (World / Experiences / Mental Models) + Reflect operation; ~2.5 layers (tied with Zep); the cleanest existing-incumbent gesture toward a [consolidation-channel](../concept/consolidation-channel.md) read path.
- [Honcho](./honcho.md) — identity-modelling via Peer Paradigm + deriver/dream consolidation; ~1.5 layers but consolidation coverage is uniquely strong; AGPL-3.0 is the structural enterprise barrier.
- [LangMem](./langmem.md) — framework-native memory bundled with LangGraph; ~0.5–1 layers; thin by design, deep ecosystem lock-in.

## Vector-DB substrate

Vector databases composed into memory systems by others. They sit at one layer of the stack — typically retrieval or tiered storage — and don't themselves attempt to cover the full memory-system surface.

- [Turbopuffer](./turbopuffer.md) — object-storage-first vector DB; ~1 layer; [cost-leg](../concept/cost-leg-affordable-substrate.md) anchor (1B+ at affordable per-vector price).
- [Pinecone](./pinecone.md) — managed vector DB (serverless + pod-based); ~1 layer; the price-as-wall counterpoint to Turbopuffer.
- [Qdrant](./qdrant.md) — Rust-native vector DB with hybrid dense+sparse; ~1.5 layers.
- [pgvector / VectorChord](./pgvector.md) — PostgreSQL-native vector indexing; VectorChord runs 1B+ vectors on a single 128GB-RAM PostgreSQL machine via [RaBitQ](../source/rabitq-2024.md); ~1 layer.
- [Milvus](./milvus.md) — vector DB with explicit tiered storage; ~1.5 layers; the tier-aware reference.

## Not promoted (anti-sprawl calls)

Discussed inline in concept pages or referenced once in source pages, but not yet promoted to incumbent pages:

- **LanceDB** — referenced from [pinecone](./pinecone.md); a fourth vector-DB substrate option. Would land here if inbound references accumulate.
- **Bedrock AgentCore Memory / Glean / Cody** — commercial framings live in coral, not the wiki. Promote if the strategic-landscape question pulls them into wiki scope.
- **EverMind / EverOS** — May 2026 fresh-Claude synthesis surfaced as a candidate; AJ-call to skip on procurement-risk grounds (Chinese state-ownership data-handling concerns + benchmark-replication-gap of 38% vs 93% on LoCoMo with two independent reports redirected to private Discord). Not worth the page weight; revisit only if procurement environment changes.
- **DiskANN / SPFresh / RaBitQ / MUVERA** — these are *techniques*, not products. Sourced at [diskann-spfresh](../source/diskann-spfresh.md), [rabitq-2024](../source/rabitq-2024.md), [muvera-2025](../source/muvera-2025.md). Used by the products above.

## Related

- [seven-layer-stack](../concept/seven-layer-stack.md) — the architecture the incumbents are measured against; §Incumbent mapping has the per-layer rollup table.
- [cascading-failures](../concept/cascading-failures.md) — the failure mode the incumbents share at scale.
- [benchmark-replication-gap](../concept/benchmark-replication-gap.md) — recall-leg today-anchor across the incumbent set.
- [cost-leg — affordable substrate](../concept/cost-leg-affordable-substrate.md) — substrate-incumbents drive this leg.

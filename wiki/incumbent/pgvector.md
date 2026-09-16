---
type: incumbent
name: pgvector (and PostgreSQL extensions: VectorChord, pg_vectorize)
status_current_as_of: 2026-05-12
last_ingested: 2026-05-12
sources: [../source/rabitq-2024.md]
tags: [incumbent, vector-db, substrate, postgres, in-database]
---

## What it does

**Vector indexing inside PostgreSQL.** The default pgvector extension supports HNSW and IVFFlat indexes against a `vector` column type. Extensions (VectorChord, pg_vectorize) add RaBitQ-quantized indexes and high-scale deployment patterns. AWS Aurora pgvector 0.8.0 and Google AlloyDB ScaNN are managed variants.

**VectorChord specifically:** runs 1B+ vectors on a single 128GB-RAM PostgreSQL machine via RaBitQ, and reports 3B+ in a follow-up blog ("3 billion vectors in PostgreSQL to protect the earth"). See [RaBitQ source](../source/rabitq-2024.md).

## What it doesn't

- **Not an agent-memory product.** Substrate plus SQL.
- **Not optimized for the agent-memory access pattern out of the box.** pgvector + RaBitQ at scale requires careful index tuning; default pgvector HNSW inherits all HNSW scale limits (see [HNSW scale limits](../concept/hnsw-scale-limits.md)).
- **No multi-vector or hybrid retrieval as native features.** Achievable via SQL composition but not first-class.

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

Covers **1 layer** as substrate (tiered storage / index). The PostgreSQL ecosystem is what makes this option compelling beyond layer coverage: you get the *rest* of relational tooling (transactions, constraints, joins) without bolting on a separate substrate.

## Where it fails

- **Operational profile.** A single-machine 128GB PostgreSQL instance is a significant operational item to scale (vertical, not horizontal). Horizontal scale-out is the open question; Citus and similar exist but aren't the default.
- **Per-feature lag.** Multi-vector, MUVERA, advanced quantization variants arrive in pgvector ecosystem after standalone vector DBs.

## Role in Kyrja thesis

pgvector + VectorChord is the **PostgreSQL-native substrate option** for the wedge. It pairs naturally with [structured-filter-first](../decision/structured-filter-first.md) (because the structured filter *is* SQL) and with the [slot-format-encoding](../decision/slot-format-encoding.md) compound key (because slot fields *are* indexed columns). The "case against pgvector" criticism (Alex Jacobs blog) is mostly about default-HNSW + small-scale; VectorChord/RaBitQ refutes the at-scale variant.

The wedge MTP architecture choice is "SQLite + sqlite-vec for MVP; Postgres + pgvector at scale" per [tool-chain-wedge-as-adoption-path](../decision/tool-chain-wedge-as-adoption-path.md).

## Related

- [RaBitQ](../source/rabitq-2024.md) — the quantization paper that makes pgvector/VectorChord 1B+ viable
- [structured-filter-first](../decision/structured-filter-first.md) — natural fit with SQL substrate
- [cost-leg-affordable-substrate](../concept/cost-leg-affordable-substrate.md) — pgvector/VectorChord is a key anchor for "storage is no longer binding"
- [beyond-hnsw-approaches](../concept/beyond-hnsw-approaches.md) — VectorChord is the RaBitQ-quantized family exemplar
- [seven-layer-stack](../concept/seven-layer-stack.md) — 1-of-7 coverage

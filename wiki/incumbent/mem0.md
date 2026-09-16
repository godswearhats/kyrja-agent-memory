---
type: incumbent
name: Mem0
status_current_as_of: 2026-05-14
last_ingested: 2026-05-14
sources: [source/mem0-paper-2504.md]
tags: [incumbent, integration-gap]
---

## What it does

Memory layer for AI agents. Provider-agnostic vector store with 20+ backend integrations via factory pattern. Two-phase pipeline: LLM-based fact extraction → LLM-mediated ADD/UPDATE/DELETE/MERGE against top similar entries in the vector DB. SQLite for change history. v2.0+ collapses to single-pass ADD-only at ~half the latency. Hybrid search (semantic + keyword + entity boosting); graph variant (Mem0g) bolt-on.

See [Mem0 paper + vendor source](../source/mem0-paper-2504.md) for the underlying material.

## What it doesn't

- **Owned storage primitive.** Same delegated-backend posture as Cognee.
- **Temporal reasoning.** Vendor acknowledges weakness at temporal reasoning, event ordering, and multi-session reasoning at 10M scale. This is exactly the gap Zep markets against.
- **Pre-embedding admission control.** The "admission control" is LLM-mediated post-extraction (ADD/UPDATE/DELETE/MERGE on every write), not pre-embedding. Latency grows with corpus size.
- **Multi-vector embedding.** Single-vector dense (default `text-embedding-3-small`, 2048 token limit).
- **Tiered storage.**

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

| Layer | Coverage |
|---|---|
| Admission Control | ◐ — LLM-mediated, post-extraction, expensive; not a learned gate |
| Embedding | ◐ — single-vector dense via configurable backend |
| Multi-Graph Memory | ◐ — Mem0g graph variant exists, paywalled at $249/mo, not the primary product |
| Tiered Storage | ✗ |
| Retrieval | ✓ — hybrid (semantic + keyword + entity) |
| Consolidation | ◐ — ADD/UPDATE/DELETE/MERGE is consolidation-adjacent but per-write, not streaming/compaction |
| Governance | ✗ |

**Net: ~2 of 7 layers materially covered.**

## Where it fails

- **Construct validity of headline benchmarks.** Vendor: 93.4% LongMemEval. Independent eval (cited in deep-dive §4): **49.0%** vs alternatives at 63-91%. This is the most concrete benchmark-chaos signal in the incumbent set.
- **Per-write LLM latency.** Every add() triggers an LLM call. At 1B-tokens/day-throughput scale this is the binding cost constraint.
- **Temporal weakness at 10M scale.** Vendor-acknowledged. Direct empirical support for the [cascading-failures regime](../concept/cascading-failures.md) starting well before billion scale.
- **Adversarial-risk surface.** April 2026: high-severity SQL/Cypher injection vulnerability disclosed (CVSS 8.1). `[ASSERTED]` — surfaced via fresh-Claude synthesis May 2026; not independently verified at this ingest; CVE identifier and disclosure path remain to be tracked down. Treat as flagged-but-unverified until anchored to a primary CVE / vendor advisory.

## Adoption signal

1B+ tokens/day processed in production (vendor-reported). Broadest backend support of any incumbent. Strong commercial traction.

## Related

- [Mem0 paper + vendor source](../source/mem0-paper-2504.md).
- [Zep](./zep.md) — markets explicitly against Mem0's temporal weakness.
- [Seven-layer stack](../concept/seven-layer-stack.md).
- [Cascading-failures product](../concept/cascading-failures.md) — Mem0's 10M-scale break is consistent with the regime onset.

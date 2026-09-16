---
type: source
name: "Supermemory — vendor documentation and project material"
status: timeless
last_ingested: 2026-05-14
sources: []
tags: [incumbent-anchor, integration-gap, extraction-first]
---

## Citation

Vendor-published documentation, GitHub README, and project material. Not a single paper; a roll-up of project material as of mid-2026.

## Location

- GitHub: https://github.com/supermemoryai/supermemory
- Docs: https://supermemory.ai/docs
- Quickstart: https://supermemory.ai/docs/quickstart
- Console: https://console.supermemory.ai

## Key claims (with our restatements)

### Architecture

**Vendor (README, May 2026):** Five integrated components — (1) Memory Engine extracting and tracking facts with contradiction resolution, (2) User Profiles maintaining static facts plus dynamic context, (3) Hybrid Search combining RAG with memory queries, (4) Connectors for real-time sync from Google Drive / Gmail / Notion / GitHub, (5) File Processing for PDFs, images, video, code. MIT-licensed, TypeScript-primary.

**Our restatement:** `[ASSERTED]`. Supermemory's architecture pattern is **extraction-first** — conversations are compressed into discrete facts at ingest, then queried via hybrid retrieval. The five-component breakdown is broader-surface than most incumbents (memory + RAG + profiles + connectors in one API). The "memory engine" itself is single-graph and single-vector at the storage layer — the breadth is in the *application* surface, not the storage primitive.

### Licensing

**Vendor:** MIT licensed (per GitHub repo).

**Our restatement:** `[ASSERTED]`. This contradicts a fresh-Claude synthesis (May 2026) that claimed Supermemory's core engine was closed-source with "plugins only" open. Verified against the GitHub repo itself, which is MIT-licensed; the synthesis was wrong. Discrepancy noted as a case where the LLM-synthesis route would have introduced false provenance — anchor of [load-bearing-sources discipline](../concept/evidence-anchoring.md).

### Benchmark claims

**Vendor:** Self-reported #1 across LongMemEval (81.6%), LoCoMo, and ConvoMem.

**Our restatement:** `[ASSERTED]`. Vendor-self-reported; not independently replicated. The 81.6% LongMemEval figure differs from a fresh-Claude synthesis (May 2026) that cited 85.4% — vendor README is the canonical source, synthesis was outdated or wrong. Use as directional signal, not ground truth ([benchmark-replication-gap](../concept/benchmark-replication-gap.md) applies across the incumbent set).

### Adoption / company

**Vendor (founder profile + press, mid-2026):** Founded by Dhravya Shah. Seed-stage company. Notable angels include Jeff Dean (Google), Dane Knecht (Cloudflare), executives from OpenAI/Meta/Google. SOC 2 Type 2 / HIPAA / GDPR compliance claimed.

**Our restatement:** `[ASSERTED]`. Funding and compliance claims not independently verified at this ingest; treat as vendor-stated.

## Relevance to Kyrja

- Anchors [Supermemory incumbent page](../incumbent/supermemory.md).
- Supermemory occupies the **extraction-first** architectural pattern. The breadth of its application surface (RAG + memory + connectors + file processing) is a useful counterpoint to memory-only competitors, but storage-primitive depth is shallow.
- Same single-vector-dense exposure to the [LIMIT bound](../source/weller-2025-limit.md) as every other extraction-first incumbent.

## Archive location

Not a single artifact; rolling vendor material. To verify a specific quantitative claim, fetch from the linked URLs above (claims are volatile).

---
type: incumbent
name: Letta (MemGPT lineage)
status_current_as_of: 2026-05-14
last_ingested: 2026-05-14
sources: [source/letta-memgpt.md]
tags: [incumbent, integration-gap, hierarchical-memory]
---

## What it does

LLM-OS framework treating agent memory as a tiered virtual-memory system. Three tiers, with the agent itself making promote/demote decisions via tool calls:

- **Core Memory** — in-context (RAM-equivalent).
- **Recall Memory** — searchable conversation history (disk cache).
- **Archival Memory** — long-term cold storage.

Inherits from MemGPT (Packer et al., UC Berkeley, arxiv 2310.08560). Positioning is on agent-runtime ergonomics and on memory-as-OS-primitive.

See [Letta source](../source/letta-memgpt.md) for the underlying material.

## What it doesn't

- **Independent benchmark claims.** Letta does not publish billion-scale numbers or headline retrieval-quality benchmarks. The product claim sits at the architecture-pattern level.
- **Multi-graph memory.** No knowledge graph; no temporal/causal modeling.
- **Multi-vector embedding.**
- **Automated tier migration.** Tier movement is **explicit, LLM-driven, per-decision** — high fidelity but high cost. At 1B vectors this becomes O(billion) tool-call decisions unless tier migration is learned or batched, which Letta does not do.
- **Streaming consolidation.** Consolidation is whatever the agent decides to write to archival; not LSM-style compaction.

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

| Layer | Coverage |
|---|---|
| Admission Control | ◐ — agent-decided what enters core memory; not a learned gate |
| Embedding | ◐ — single-vector dense via configurable backend |
| Multi-Graph Memory | ✗ |
| Tiered Storage | ✓ — the cleanest tiered-storage primitive of any incumbent; tiers are first-class |
| Retrieval | ◐ — backend-delegated |
| Consolidation | ◐ — agent-driven, not automated |
| Governance | ✗ |

**Net: ~1.5 of 7 layers materially covered**, but tiered storage is the strongest and most architecturally crisp coverage of that layer in the incumbent set.

## Where it fails

- **Tier-migration cost.** Agent-driven tier migration via tool calls does not scale. At billion-scale this is the binding constraint.
- **No published retrieval-quality claims at scale.** Letta has not pinned itself to a benchmark; treat retrieval-quality claims as `[UNVERIFIED]`.
- **Single-vector dense.** Same LIMIT-bound exposure as every other incumbent.

## What is structural (worth borrowing)

The three-tier abstraction (Core / Recall / Archival) is the right vocabulary for the tiered-storage layer. Letta's mistake (per our reading) is making tier migration an *agent decision* instead of an *automated process driven by access patterns and age*. The pattern shape is correct; the cost model is wrong.

## Adoption signal

Strong agent-developer community; positioned at LLM-OS runtime layer rather than competing directly on memory-retrieval quality. **Letta Code** (memory-first coding agent) is ranked **#1 on Terminal-Bench among model-agnostic open-source agents** per vendor claim May 2026 — `[ASSERTED]` ([source](../source/letta-memgpt.md); construct-validity note: Terminal-Bench measures terminal-interaction task completion, an agent-runtime metric, not memory-retrieval quality; the ranking is a runtime signal, not a memory-quality signal).

## Related

- [Letta source + MemGPT origins](../source/letta-memgpt.md).
- [LightMem](./lightmem.md) — the offline-batched-consolidation counterpart to Letta's LLM-driven tier migration.
- [Seven-layer stack](../concept/seven-layer-stack.md).

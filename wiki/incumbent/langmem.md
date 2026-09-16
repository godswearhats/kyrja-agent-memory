---
type: incumbent
name: LangMem (by LangChain)
status_current_as_of: 2026-05-14
last_ingested: 2026-05-14
sources: [source/langmem-docs.md]
tags: [incumbent, integration-gap, framework-native-memory]
---

## What it does

Memory primitive shipped inside the LangChain / LangGraph framework. Two surfaces: **hot-path tools** (primitives the agent calls during conversation to actively manage memory) and **background memory manager** (automatic extraction and consolidation between turns). Two memory types in the README: **semantic** (vector-based search using embeddings, default `openai:text-embedding-3-small`) and **episodic** (specific interactions and conversations). Backend-agnostic storage via LangGraph Long-term Memory Store (any vector DB, MongoDB, or Postgres via pgvector). Namespaced by `user_id` / `team_id` / `app_id`. MIT, Python.

See [LangMem vendor source](../source/langmem-docs.md) for the underlying material.

## What it doesn't

- **Stand-alone product.** LangMem is a **library, not a product** — no dashboard, no monitoring, no opinionated defaults, no managed observability.
- **Graph memory.**
- **Temporal reasoning.**
- **Multi-vector embedding.**
- **Tiered storage.**
- **Coding-agent integrations.** No Claude Code / Cursor / OpenCode plugins.
- **Data-source connectors.**
- **Procedural memory as a first-class shipped feature.** Third-party material describes a procedural memory pattern (agents rewriting their own system prompts based on feedback); whether this is a vendor-supported pattern or community usage is unclear from the README itself at this ingest.
- **Acceptable latency for interactive use.** Third-party reporting cites 59.82s p95 on LOCOMO — `[ASSERTED]` ([source](../source/langmem-docs.md); construct-validity note: number is third-party-cited, not vendor-published; if accurate it is disqualifying for interactive use, so independently verifying this is the single most load-bearing fact-check before any adoption).

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

| Layer | Coverage |
|---|---|
| Admission Control | ✗ |
| Embedding | ◐ — single-vector dense via configurable backend |
| Multi-Graph Memory | ✗ |
| Tiered Storage | ✗ |
| Retrieval | ◐ — backend-delegated similarity search |
| Consolidation | ◐ — background memory manager does extract/consolidate between turns; not LSM-style |
| Governance | ✗ |

**Net: ~0.5–1 of 7 layers materially covered.** The thinnest coverage in the memory-system incumbent set. This is by design — LangMem is a primitive bundled with a framework, not a memory product competing on depth.

## Where it fails

- **Latency** (if the 59.82s p95 figure is accurate) — disqualifying for interactive use at any scale.
- **Ecosystem lock-in** — practically usable only inside LangGraph. For teams already committed to LangChain, zero-friction. For teams not on LangChain, every other purpose-built memory system outperforms LangMem on every dimension that isn't "free with what you already have."
- **No opinionated defaults** — memory quality is whatever your configuration produces.
- **Strategic priority risk** — LangMem is a free component inside a $260M-funded unicorn's revenue-generating ecosystem (LangSmith, LangGraph Platform). Memory investment may not stay a priority.

## What is structural (worth borrowing)

The **hot-path tools vs background memory manager** split is the right vocabulary for distinguishing *agent-driven write actions* from *automatic consolidation*. Most incumbents conflate these or only ship one. The split itself is worth borrowing even if LangMem's implementation isn't.

## Adoption signal

Parent framework: ~100K GitHub stars, ~136 employees, $260M Series B. Powers production deployments at Replit, Uber, LinkedIn, GitLab, Klarna, AT&T, Home Depot — but those are parent-framework numbers, not LangMem-specific.

## Related

- [LangMem vendor source](../source/langmem-docs.md).
- [Letta](./letta.md) — the other incumbent that conflates memory with agent runtime; Letta is "memory as agent OS", LangMem is "memory as framework primitive."
- [Seven-layer stack](../concept/seven-layer-stack.md).
- [Cascading-failures product](../concept/cascading-failures.md) — if the 59.82s p95 number is accurate, this is the cleanest empirical signal of LLM-mediated write-path failure at production scale in the incumbent set.

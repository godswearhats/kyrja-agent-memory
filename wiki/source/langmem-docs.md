---
type: source
name: "LangMem — vendor documentation and project material"
status: timeless
last_ingested: 2026-05-14
sources: []
tags: [incumbent-anchor, integration-gap, framework-native-memory]
---

## Citation

Vendor-published GitHub README and documentation, by the LangChain team. Roll-up of project material as of mid-2026.

## Location

- GitHub: https://github.com/langchain-ai/langmem
- Docs: https://langchain-ai.github.io/langmem/
- Hot Path Quickstart and Background Quickstart are linked from the docs root.

## Key claims (with our restatements)

### Architecture

**Vendor (README, May 2026):** Framework for agents to learn and adapt over time through memory extraction, prompt optimisation, and long-term persistence. Two architectural surfaces:

- **Semantic memory** — vector-based memory search using embeddings (default `openai:text-embedding-3-small`).
- **Episodic memory** — storage of specific interactions and conversations.
- **Hot-path tools** — primitives the agent calls during conversation to actively manage memory.
- **Background memory manager** — automatic extraction and consolidation of agent knowledge between turns.
- **LangGraph Long-term Memory Store integration** — native to LangGraph; provides backend-agnostic storage for any vector DB, MongoDB, or Postgres-via-pgvector.

MIT licence, Python-primary.

**Our restatement:** `[ASSERTED]`. LangMem is a **library, not a product** — no dashboard, no monitoring, no opinionated defaults. The hot-path/background split is the architectural distinction, not a memory-type taxonomy. Procedural memory (self-modifying system prompts) is referenced in third-party material describing LangMem but is not prominent in the current README itself; whether it is a first-class supported pattern or community usage is unclear at this ingest.

### Latency

**Third-party reports (synthesis-cited, May 2026):** 59.82s p95 on LOCOMO.

**Our restatement:** `[ASSERTED]`. Vendor does not publish this number; surfaced from a fresh-Claude synthesis citing third-party benchmarking. If accurate, the latency is disqualifying for interactive use at any scale; this is the single most important factual claim to independently verify before any adoption decision.

### Lock-in

**Vendor:** Documentation positions LangMem as native to LangGraph, with LangGraph Platform integrations as the primary deployment path. Functional primitives are usable with non-LangGraph stacks but the integration surface is asymmetric.

**Our restatement:** `[ASSERTED]`. The "free if you're on LangGraph, friction if you're not" pattern is structural. For teams already committed to LangChain ecosystem, this is the lowest-friction option; for everyone else it is a tax.

### Adoption / company

**Vendor + press:** LangChain ($260M Series B, ~136 employees, ~100K GitHub stars on parent framework). Powers teams at Replit, Uber, LinkedIn, GitLab, Klarna, AT&T, Home Depot (parent-framework adoption; LangMem-specific adoption is not separately published).

**Our restatement:** `[ASSERTED]`. Parent-framework momentum is real and unicorn-funded; LangMem-as-component sits inside that ecosystem rather than competing as a standalone memory product.

## Relevance to Kyrja

- Anchors [LangMem incumbent page](../incumbent/langmem.md).
- LangMem is the **framework-native-memory** pattern: not a memory product, a memory primitive shipped inside an agent framework. Useful as a comparator for what "minimally adequate memory" looks like in the framework-bundled tier.
- The reported latency (if verified) is direct empirical support for the [cascading-failures](../concept/cascading-failures.md) regime affecting LLM-mediated write paths at production scale.

## Archive location

Not a single artifact; rolling vendor material. To verify the p95 latency claim or specific benchmark numbers, the docs URL is the canonical entry point.

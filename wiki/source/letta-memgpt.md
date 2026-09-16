---
type: source
name: "Letta / MemGPT — LLM-OS Memory Architecture"
status: timeless
last_ingested: 2026-05-12
sources: []
tags: [incumbent-anchor, integration-gap, hierarchical-memory]
---

## Citation

Letta team (descended from MemGPT, Packer et al., UC Berkeley). Open-source agent runtime + memory framework. Not a single canonical paper for the current product; MemGPT origins paper anchors the architectural pattern.

## Location

- GitHub: https://github.com/letta-ai/letta
- Architecture write-up: https://www.letta.com/blog/agent-memory
- Lineage paper (MemGPT): https://arxiv.org/abs/2310.08560

## Key claims (with our restatements)

### Architecture

**Vendor:** LLM-OS approach. Three memory tiers managed via tool calls by the agent itself:
- **Core Memory** — in-context (RAM-equivalent).
- **Recall Memory** — searchable conversation history (disk cache).
- **Archival Memory** — long-term cold storage.

The agent autonomously decides what to promote/demote between tiers via explicit tool invocations.

**Our restatement:** Letta is the cleanest expression of the **tiered-storage pattern** as a memory primitive — the only incumbent to make tier migration a first-class agent action rather than a background process. Tier movement is **explicit and LLM-driven**, which is high-fidelity but high-cost compared to the streaming/compaction patterns in [seven-layer stack](../concept/seven-layer-stack.md)'s consolidation layer.

### Scale and benchmark posture

Letta does not publish billion-scale numbers; positioning is on agent-runtime ergonomics and on memory-as-OS-primitive, not on retrieval quality at corpus scale.

**Our restatement:** No vendor benchmark contradicts the cascading-failures regime — Letta's claim is at the architecture-pattern level, not the scale-claim level. This makes Letta the right architectural reference for tier-migration design without committing us to its empirical claims.

### Acknowledged constraints

The agent-driven tier-migration design assumes the LLM can correctly decide what's archival vs recall. At billion-scale, this becomes O(billion) tool-call decisions — a structural problem unless tier migration is batched/learned.

## Relevance to Kyrja

- Anchors [Letta incumbent page](../incumbent/letta.md).
- Letta occupies the **tiered storage + consolidation layers** of [seven-layer stack](../concept/seven-layer-stack.md) most cleanly of any incumbent. Does not address multi-vector embedding, multi-graph memory, or admission control.
- The agent-driven tier-migration pattern is a useful design reference but does not scale; our consolidation layer assumes automated tier migration, not LLM-driven.

## Archive location

MemGPT origins paper at arxiv 2310.08560. Current product material is rolling vendor docs; fetch from GitHub or letta.com.

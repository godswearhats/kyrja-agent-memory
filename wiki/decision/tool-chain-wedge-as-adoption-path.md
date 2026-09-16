---
type: decision
name: Tool-Chain Wedge as Adoption Path
status: ACTIVE
last_ingested: 2026-05-13
sources: [../experiment/2026-05-11-write-quality-variance/exp2-task3-c-replication.md]
tags: [wedge, strategy, adoption]
---

## Decision

Kyrja leads with a **deliberately narrow product**: tool-chain token-usage savings for coding agents on the same repo. The claim a user feels first is "your agent spends fewer tokens completing related tasks because it remembers prior tool-chain sessions on this repo." General-purpose agentic memory is not the v1 pitch; it comes later, on top of the wedge.

## Motivation

- **The seven-layer architecture is not directly sellable.** [Seven-layer integration stack](../concept/seven-layer-stack.md) is the thesis, but no engineer adopts a system because it integrates seven layers. They adopt because something in their day got cheaper, faster, or less painful. The wedge has to pay for itself before the broader architecture earns the right to exist.
- **Token savings is the first measurable benefit.** Cost is observable per-session and accumulates per-engineer per-day. [H-UTIL SUPPORTED](../hypothesis/H23-util.md) shows memory reduces cost on causally-related tasks `[MEASURED]` across two tasks and two distillers; direction stable, magnitudes drift. *Construct-validity:* "cost" is agent-completion token spend per task, which is the wedge's promised benefit — a direct measure of the adoption hook, not a proxy. Distiller and task variation are the noise; the sign and the bracketed magnitude range carry across both.
- **Implementable without users changing how they work.** The MTP hooks Claude Code (MCP server or stream-json capture) and runs async distillation. No new workflow, no new vocabulary.
- **Narrow scope sidesteps the cascading-failures regime.** Repo-bounded, structured-filter-first retrieval at MTP scale avoids the homogeneous-code embedding-crowding mode of [cascading-failures](../concept/cascading-failures.md). The cascade is what we're betting incumbents will hit; the wedge is what gets us in before that bet pays.

## Commitments

- v1 product positioning is **token savings on the same repo**, not "general agentic memory."
- MTP is the first artifact: smallest end-to-end loop on AJ's real work (Goal 5 of tool-chain-wedge-goals-2026-05-11.md).
- Adoption story: an engineer installs the hook, works for a day, and sees a measurable drop in cost on related tasks. No before/after benchmark required from the user.
- Cross-cutting decisions composing the wedge:
  - [repo-bounded-scope](./repo-bounded-scope.md)
  - [precision-over-recall](./precision-over-recall.md)
  - [structured-filter-first](./structured-filter-first.md)
  - [org-wide-store-repo-scoped-queries](./org-wide-store-repo-scoped-queries.md)
  - [slot-format-encoding](./slot-format-encoding.md "pending")
  - [write-side-quality-gate-deferrable](./write-side-quality-gate-deferrable.md)
- Features explicitly deferred until after the wedge: symbol-level extraction, memory TTL, dedup of similar memories, cross-repo default search, real-time inline distillation, multi-model retrieval, write-time secret scanning.

## Reversibility

**Moderate.** The wedge is a positioning and scoping decision, not an architectural lock-in. The storage and retrieval primitives we build for tool-chain memory generalize to broader agentic memory; pivoting to a different first-product framing (e.g., debugging-only, or PR-review-memory) wouldn't require rebuilding the substrate. What it *would* cost: the messaging, the integrations built specifically for Claude Code, and the empirical work already aimed at tool-chain task distributions. Order weeks-to-months of replan, not an architectural rewrite.

## Open hazards

- **Competitive ship.** A native "remember prior sessions" feature from Anthropic or Cursor consumes the wedge. Moat strategy ([org-wide-store-repo-scoped-queries](./org-wide-store-repo-scoped-queries.md), RL-trained encoder, IDE/CI integration depth) must precede or parallel the wedge launch.
- **Encoding ceiling.** If the ~1200-token slot encoding loses too much detail, the wedge underperforms on harder tasks. Build MTP fast to expose this — see [slot-format-encoding](./slot-format-encoding.md "pending").
- **Task distribution.** Production benefit depends on how often a relevant prior memory exists. Unknown until measured on a real codebase, which the MTP provides.
- **Memory-induced overconfidence.** Memory-equipped agents skipped writing verification tests in Exp 2 (0/4 A, 3/4 C skipped vs 4/4 cold wrote). If memory's pattern is *almost* right, the wedge could accelerate wrong solutions. `[MEASURED]` from [Exp 2](../experiment/2026-05-11-write-quality-variance/exp2-task3-c-replication.md). *Construct-validity:* this is a behavioral side-effect observed in forensic review, not the primary cost metric — direction is suggestive, not conclusive.

## Related

- [H23-util](../hypothesis/H23-util.md) — the empirical foundation
- [seven-layer-stack](../concept/seven-layer-stack.md) — the architecture the wedge eventually unlocks
- [cascading-failures](../concept/cascading-failures.md) — the regime the wedge avoids at MTP scale and exploits at v2+ scale

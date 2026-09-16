---
type: decision
name: Caddy is a research program, not a product — commercial track decoupled to Eira's bolt-on
status: ACTIVE
last_ingested: 2026-06-07
sources: []
tags: [scope, research-program, commercial-decoupling, framing]
---

## Decision

The caddy track is a **research program**, not a path to market. The commercial track is owned by Eira and is **bolt-on** (the only commercially viable path to begin with, per AJ + Eira + AJ's trusted human advisors, 2026-05-20). Caddy research and Eira's commercial track are **decoupled at this stage**: they share a name and a high-level concept, nothing else. Data and design from the eventual bolt-on product may inform caddy research later, but that coupling is "a long way away yet" (AJ 2026-05-20).

This decision **supersedes the MVP-product framing** that shaped wiki vocabulary through 2026-05-19. Phrases like "MVP load-bearing," "MVP critical path," "v2 research target," and "MVP wedge demonstration" embedded an implicit assumption — that caddy was both a research bet and a path to first commercial product — which no longer holds.

## Motivation

- **Commercial reality.** Bolt-on is the only path to market that's tractable on a startup timeline. The caddy's structural advantages (debuggability-loss aside) require open-weights LLM access, co-training, and multi-quarter research before any product surface exists. Time-to-market and capital-efficiency arguments converge on bolt-on for v1 commercial.
- **Triangulated input.** AJ-Eira product-side conversation reached the same conclusion as AJ's trusted human advisors independently. Three pressure points on the same answer.
- **Liberation, not loss.** Decoupling removes a constraint that was distorting research scope. The 2026-05-19 K2+T_A3 demotion was explicitly MVP-YAGNI: *"tier 3-4 wedge demonstration doesn't require it for MVP."* With the MVP frame gone, the demotion logic dissolves. K2+T_A3 was scientifically load-bearing all along; only the MVP product-timeline pressure made it deferrable. See [k2-ta3-deferred-to-v2](./k2-ta3-deferred-to-v2.md) — now REVERSED.

## Commitments

- **Tempo constraint is frontier-pacing, not market-timing.** AJ 2026-05-20: *"the tempo is that we have to find answers before someone else does — the usual frontier of science stuff."* Affordability (compute budget, AJ's time, agent context) bounds pace; market deadlines do not.
- **Architecture is treated as a stack-ranked research backlog.** Load-bearing components — T_A1b, K2+T_A3, K6, R5-as-variant, others — are research targets to be ordered, not MVP-scope items to be pruned. Ordering criteria (per AJ 2026-05-20 approval): scientific leverage, tractability with current resources, dependencies, frontier-pacing risk — **all anchored to how each item moves us toward demonstrating tier 3-4 retrieval via the caddy architecture**.
- **One active research thread at a time.** AJ 2026-05-20: *"we can very definitely only do one thing at a time."* The backlog is a queue, not a parallel-work plan.
- **No MVP scope discipline.** Discipline shifts from "what's minimal for first product" to "what's the highest-leverage scientific question we can answer next, within budget." Pre-registration, falsifiability, and construct-validity discipline (all already in force) become *more* important when publication-grade rigor is on the table.
- **Commercial track decoupled at this stage.** Eira's bolt-on work proceeds independently. Eira's pages live in `coral`. The wiki may eventually ingest *findings* from Eira's track when they become relevant to caddy research (real failure modes, real telemetry, real user behavior on memory systems); it does not synchronize live.
- **Research outputs may end up in the eventual company.** AJ 2026-05-20: *"Research will end up being part of whatever company we build, just the time and affordability of it necessitate a different path to market."* Decoupling is about ordering, not separation.

## Reversibility

**Cheap.** This is a framing decision; no implementations or hires are locked. Reversal triggers:

- **Caddy research produces an empirical result so strong it becomes the product directly** — e.g., T_A1b at small scale shows results so striking that frontier labs become interested in acquisition or partnership before bolt-on v1 ships. The decoupling collapses naturally.
- **Eira's bolt-on ships and reveals a constraint** that re-couples the tracks — e.g., users actively demand tier 3-4 retrieval, validating the caddy wedge against real demand, and the commercial roadmap incorporates caddy research as v2/v3 product.
- **Resource constraint changes** — funding, team growth, partnership — such that running both tracks in parallel becomes feasible.
- **AJ decides the bolt-on path can't reach a viable v1** and pivots back to caddy-first. (Treated as evidence to invert this decision, not as a default fallback.)

The decision is held *until evidence inverts it*, not committed forever.

## Implications for wiki vocabulary

The "MVP" qualifier on phrases like "MVP load-bearing T4," "MVP critical path," "MVP-deferred," "MVP target," etc. is removed across the wiki in the 2026-05-20 refactor. Replacements:

- **"MVP load-bearing"** → **"load-bearing"** (scientific sense only)
- **"MVP critical path"** → **"current active research thread"** (or dropped when the queue framing is sufficient)
- **"MVP-deferred" / "v2 research target"** → **"deferred"** with the reason in prose (usually science-affordability or dependency-on-another-result)
- **"MVP architecture / MVP target"** → **"research prototype"** (the thing we'd build to demonstrate the science; still has scope discipline, just not product scope discipline)
- **"MVP choice"** (interface doors, tier semantics, etc.) → **"current choice"** (these are still real architectural commitments for the research prototype)

## Related

- [tier-3-4-as-wedge](./tier-3-4-as-wedge.md) — the wedge claim that defines our goal. Unchanged by this decision; the goal is the same.
- [k2-ta3-deferred-to-v2](./k2-ta3-deferred-to-v2.md) — REVERSED by this decision (the MVP-deferral logic dissolves with the MVP frame).
- [multi-field-memory-unit](./multi-field-memory-unit.md) — paired commitment that preserves tier 1-2 under tier-3-4-shaped representation learning. Unchanged.
- [caddy-architecture](../concept/caddy-architecture.md) — refactored 2026-05-20 to drop MVP-product framing; the architecture itself is unchanged.
- [caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md) — the within-family comparison. The "if T_A1b fails, we pivot to bolt-on" *commercial-pivot* logic dissolves; T_A1b becomes a scientific question whose answer is interesting either way.
- [datadog-of-memory](./datadog-of-memory.md) — the **paired commercial-direction decision**, ratified the same day (2026-05-20). Together: that page records the commercial-direction ratification (bolt-on infrastructure, owned by Eira); this page records the research-program framing (caddy as research, owned by Nils/wiki, decoupled from commercial).
- [memory-retrieval-tiers](../concept/memory-retrieval-tiers.md) — the four-tier taxonomy that defines the goal. Unchanged.
- [[feedback_mvp_doc_not_mvp]] — the discipline that made the prior MVP-scope decisions cheap-to-revisit; still applies to the research prototype scope.
- [[feedback_scientific_vs_mvp_loadbearing]] — the two-axis "load-bearing" distinction; the MVP axis collapses; the scientific axis remains.

## Source archive

- AJ 2026-05-20 conversation: framing-shift from product-MVP to research-program after AJ-Eira product-side conversation + AJ's trusted human advisors converged on bolt-on as the commercial path. Three-step refactor plan approved (this is Step 1).
- This decision is the predecessor decision for the wiki refactor that propagates the new framing across ~24 pages.

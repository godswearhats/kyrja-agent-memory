---
type: open-question
name: Cross-session continuity for substrate-paradigm agents
status: OPEN
last_ingested: 2026-05-26
sources: [../source/lecun-2022-autonomous-mi.md, ../source/hafner-2023-dreamerv3.md, ../source/sun-2024-ttt.md, ../source/behrouz-2024-titans.md]
epistemic_tags: [asserted, speculated]
tags: [substrate-memory, cross-session, kerros-regraded-persistence]
program: kerros
---

> **Program: [Kerros](../concept/kerros.md) (assigned 2026-05-25).** This is a Kerros-relevant research question — *can a substrate paradigm do durable cross-session memory at all?* The bolt-on is the built-in control. Older "defensible wedge" / "product-engineering bet" phrasing below is product-era chronicle.

> **Re-graded 2026-05-26 (the wide-pass [integration gate](../concept/integration-gate.md)).** Cross-session continuity *on its own* is **persistence (product)**, not the Kerros beachhead — its bolt-on control (context replay) is the *weakest* separation on the [capability map](../concept/integration-gate.md), and it weakens further as context windows grow. The Kerros beachhead is now the **composition separation** ([kerros.md § Beachhead](../concept/kerros.md)). Continuity may remain the *setting* a composition task is dressed in (it supplies a shipped bolt-on to measure against), but the contribution is composition, not continuity. The "beachhead" framing below is 2026-05-25 chronicle.

## The question

How does a [substrate-as-memory](../concept/substrate-as-memory.md) architecture maintain durable memory of a single user (or environment) across distinct sessions — separated by hours, days, or months — without (a) catastrophic forgetting from per-sequence state initialization and (b) unbounded growth of an external store that re-creates the database paradigm Kerros aims to move beyond?

This is the gap surfaced during 2026-05-13 Phase-1 temperature checks: every JEPA, every [Dreamer](../source/hafner-2023-dreamerv3.md) variant, every [TTT](../source/sun-2024-ttt.md) descendant, every [Titans](../source/behrouz-2024-titans.md) variant is per-sequence or per-environment `[ASSERTED]` ([source](../source/lecun-2022-autonomous-mi.md)). FAIR's [LeCun 2022](../source/lecun-2022-autonomous-mi.md) architecture has a "short-term memory" KV store but no cross-session continuity mechanism. None of the surveyed papers builds the durable-cross-session piece.

## Why it matters

- **If substrate paradigms cannot durably persist user-specific memory:** Kerros's substrate thesis fails for the cross-session setting. A user who returns tomorrow gets a model that does not remember them; the only repair is a P2-degenerate retrieval bolt-on, which re-creates the agentic-memory products' failure mode (and concedes the contribution to the product side).
- **If a substrate-native cross-session mechanism exists or can be built:** Kerros has a genuine research result — substrate continuity a bolt-on can't replicate. The [consolidation-channel](../concept/consolidation-channel.md) becomes the candidate operator — consolidation as the mechanism that persists session traces into the substrate.
- **This gates the substrate-vs-database question.** Without a cross-session story, the substrate paradigm is research-grade for stateless agents only, and Kerros's central claim is unanchored.

## What evidence would resolve it

Three plausible answers, in increasing order of architectural commitment:

1. **Hybrid path.** Use a substrate (P1 or P3) for in-session reasoning + a P2-differentiable external store for cross-session persistence. The differentiable integration is the differentiator from the agentic-memory products' prompt-concat. Cost: hybrid complexity, but each piece is published. See [H37-pluggable-substrate](../hypothesis/H37-pluggable-substrate.md).
2. **Consolidation path.** Run an offline [consolidation-channel](../concept/consolidation-channel.md) between sessions that consolidates the session trace into either the base model's weights (full fine-tune), a user-specific adapter, or a persistent latent. The Skill-SD recipe is the published precedent. Cost: requires a consolidation operator that does not depend on a privileged-teacher oracle.
3. **Always-on substrate path.** Treat the agent as a single long-lived sequence where session boundaries are dialogue artifacts, not state-machine resets. Requires substrate that scales to million-token contexts ([R2I](../source/sun-2024-ttt.md "pending") SSM-Dreamer hybrid or TTT-MLP). Cost: open scaling questions; per-user state isolation is unsolved.

**Adequate signal:** A working personal-assistant agent that recalls a specific fact established three sessions ago without consulting an external store on the immediate query. The discriminator is not benchmark performance but the architectural property — *where* did the fact get retrieved from.

## Sub-questions

- **Granularity.** Does the substrate need to remember individual exemplars (what the user said last Tuesday) or only consolidated rules (user prefers terse responses)? The first requires P2-exemplar storage; the second can live in P1 or P3 state.
- **Capacity.** What is the per-user storage budget for a substrate that consolidates across sessions? See [forgetting-formalization](./forgetting-formalization.md).
- **Multi-tenant isolation.** If a single base model serves many users, how is per-user substrate state stored, retrieved, and isolated? Adapters? Per-user latent vectors? Cluster-routed shards? See [H37-pluggable-substrate](../hypothesis/H37-pluggable-substrate.md).
- **Interference.** What happens when the same parametric region carries memory for multiple users? Cross-user contamination is a privacy and quality failure mode.

## Related

- [substrate-as-memory](../concept/substrate-as-memory.md) — paradigm whose cross-session story is open
- [consolidation-channel](../concept/consolidation-channel.md) — candidate operator for cross-session persistence
- [substrate-paradigms](../concept/substrate-paradigms.md) — P1/P2/P3 each have different cross-session shapes
- [H29-edge-substrate-memory](../hypothesis/H29-edge-substrate-memory.md) — predicts deployment locus where cross-session continuity matters most
- [H37-pluggable-substrate](../hypothesis/H37-pluggable-substrate.md) — pluggable-substrate as one resolution path
- [forgetting-formalization](./forgetting-formalization.md) — orthogonal but adjacent; forgetting half of the consolidation channel
- [multi-agent-consistency](./multi-agent-consistency.md) — multi-tenant analog of the isolation sub-question
- [H41 — temporal-context retrieval](../hypothesis/H41-temporal-context-retrieval.md) — candidate addressing-mechanism: a maintained drifting context vector as the *retrieval cue* for cross-session items, distinct from content-similarity and timestamp-based recency. Compositional with the consolidation-channel write-side answer; one possible resolution path alongside the hybrid / consolidation / always-on-substrate options above.

---
type: open-question
name: Multi-agent memory consistency — formal definition gap
status: OPEN
last_ingested: 2026-05-12
sources: []
epistemic_tags: [asserted]
tags: [multi-agent, consistency, theory-gap]
---

## The question

**Multi-agent memory consistency lacks a formal definition.** The CMU position paper (arxiv 2603.10062) makes this point as a research-agenda framing: distributed-systems consistency models (linearizable, sequential, causal, eventual) assume well-typed data with deterministic conflict resolution. Agent memory has neither — claims are semantic, conflicts can be subtle (different framings of the same fact), and resolution often requires LLM reasoning.

**What is the right consistency model for multi-agent memory, and what detection framework reveals violations?**

## Why it matters

- **No empirical anchor today.** The current wedge architecture commits to eventual consistency with offline conflict resolution ([H32-eventual-consistency](../hypothesis/H32-eventual-consistency.md)), but the *consistency property* it claims to provide is not formally specified. Without a definition, "is our system consistent?" is unanswerable.
- **Detection precedes defense.** Even before we know what consistency we want, we'd need a detection framework that identifies inconsistencies. Today no such framework exists for agent memory at scale.
- **Theoretical wall, no empirical anchor.** Unlike the [cascading-failures](../concept/cascading-failures.md) product (which has small-scale empirical anchors via [benchmark-replication-gap](../concept/benchmark-replication-gap.md)), this is a *purely theoretical* gap. Closing it requires definitional and conceptual work first, experiments second.

## What evidence would resolve it

- **A consistency taxonomy specific to semantic memory.** What sub-properties (provenance-consistent, claim-consistent, framing-consistent) compose into a useful model? Likely the right answer is a weaker-than-linearizable, stronger-than-arbitrary semantic model.
- **A detection framework.** Given two agents' memories on overlapping topics, what algorithm decides whether they're consistent? LLM-as-judge is the obvious primitive; cheaper structural checks (entity + attribute + value triple comparison) are the engineering path.
- **A verbatim re-read of CMU 2603.10062.** Per [feedback_load_bearing_sources], when this question becomes load-bearing for a decision, pin to the paper's actual claims rather than my summary of them.

## What would close this

A `source/cmu-multi-agent-consistency-2603.md` page once the paper is read verbatim, plus a hypothesis (`H-CONSISTENCY-MODEL-X`) that proposes a specific model and a falsification path for it.

## Related

- [H31-distributed-systems-mapping](../hypothesis/H31-distributed-systems-mapping.md) — the framing this question conditions
- [federation-access-patterns](../concept/federation-access-patterns.md) — the access-pattern decomposition; this question asks what *consistency* the four primitives should compose into
- [H32-eventual-consistency](../hypothesis/H32-eventual-consistency.md) — the wedge's current bet, lacks formal grounding
- [H35-conflict-rate](../hypothesis/H35-conflict-rate.md) — the empirical complement
- [multi-agent-governance](./multi-agent-governance.md) — broader: governance includes consistency but also audit, RBAC, provenance
- THESIS.md Q7 origin: [scale-model/THESIS.md](../../../research/scale-model/THESIS.md)

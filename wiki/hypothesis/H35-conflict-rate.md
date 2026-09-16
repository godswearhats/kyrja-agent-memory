---
type: hypothesis
name: H-CONFLICT-RATE — cross-agent semantic conflict rate is low enough for offline resolution
status: PROPOSED
last_ingested: 2026-05-12
sources: []
epistemic_tags: [speculated]
tags: [multi-agent, conflict-resolution, manage-layer]
---

## Claim

In realistic enterprise multi-agent scenarios, the rate of semantic conflicts between agents' memories is low enough (estimated <10%) that offline batch resolution is acceptable. Real-time conflict detection is not needed.

## What would falsify it

- Empirical measurement shows ≥20% conflict rate in realistic multi-agent scenarios.
- Even low-rate conflicts cause disproportionate harm — a single high-blast-radius conflict per N agents is enough to require real-time detection.
- Conflict detection latency matters: offline resolution creates a window where agents act on contradictory knowledge, and that window causes real failures (which would also falsify [H32-eventual-consistency](./H32-eventual-consistency.md)).

## Evidence for

- **Default architectural assumption.** The current eventual-consistency-with-offline-resolution architecture only works if conflicts are infrequent. We've built around the assumption; the architecture standing intact is weak supporting evidence.
- **Intuitive argument.** Most agents work on different tasks/projects. When two agents write about the same topic, they usually add complementary information, not contradictory claims.
- **CMU position paper** (arxiv 2603.10062) — identifies multi-agent consistency as undefined but does not claim conflicts are frequent; positions it as an open question, not a guaranteed pain. See [multi-agent-consistency](../open-question/multi-agent-consistency.md "pending").

## Evidence against

- **Nobody has measured this.** The conflict rate is genuinely unknown.
- In scenarios with overlapping responsibilities (e.g. two agents both handling deployment), conflict rates could be much higher.
- **"Conflict" is hard to define precisely.** Subtle contradictions (different assumptions, different framings, different mental models of the same system) may be more common than obvious factual disagreements.

## Open sub-questions

- **Operational definition.** Same entity + same attribute + different values? Or broader (different framings of the same fact, conflicting recommendations from different priors)?
- **Distribution across scenarios.** Conflict rate likely varies with overlap-of-agent-responsibilities. What's the distribution in realistic enterprise deployments?
- **Detection methodology.** What's the cost of running conflict detection on every write vs. batch-only? At what conflict rate does real-time detection pay off?
- **Kerman's MASQ data** includes deliberate conflicts; whether MASQ's distribution reflects realistic rates is itself unknown.

## Related

- [H31-distributed-systems-mapping](./H31-distributed-systems-mapping.md) — depended on
- [H32-eventual-consistency](./H32-eventual-consistency.md) — paired hypothesis (this is its empirical complement)
- [multi-agent-consistency](../open-question/multi-agent-consistency.md "pending") — the formal-definition gap
- Kerman's MASQ work at `memory-benchmarks` — the planned data source
- Shelved predecessor: H21 in _archive

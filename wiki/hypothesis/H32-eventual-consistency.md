---
type: hypothesis
name: H-EC-SUFFICIENT — eventual consistency is sufficient for agent memory
status: PROPOSED
last_ingested: 2026-05-12
sources: []
epistemic_tags: [speculated]
tags: [multi-agent, consistency, architecture]
---

## Claim

Agent memory does not require strong consistency. Agents can write freely to their own partitions without coordination; conflicts can be resolved offline. Brief cross-agent disagreement (e.g. two agents holding different beliefs about a deployment process) does not cause failures — worst case is slightly stale advice until the next consolidation pass.

## What would falsify it

- A scenario where an agent acts on a stale or contradicted memory and causes a real, costly failure (not just suboptimal advice).
- [H35-conflict-rate](./H35-conflict-rate.md) is high enough that offline resolution creates unacceptable staleness windows.
- Enterprise customers in regulated industries (compliance, legal, medical) require stronger consistency as a purchase condition.

## Evidence for

- **Architectural argument:** memory isn't transactional. A wrong memory doesn't crash a system the way a wrong database record does. The blast radius of temporary inconsistency is "slightly worse advice."
- **Distributed-systems precedent:** eventually consistent systems (Cassandra, DynamoDB) dominate at scale because strong consistency is expensive and usually unnecessary.
- **Write-path simplicity:** no coordination on writes means lower latency and simpler architecture.
- The [org-wide-store-repo-scoped-queries](../decision/org-wide-store-repo-scoped-queries.md) decision implicitly assumes eventual consistency between engineers' writes; the current wedge doesn't break under this assumption.

## Evidence against

- **Safety-critical scenarios.** If an agent acts on a memory that's been superseded ("deploy without QA sign-off" when that policy changed), the blast radius could be real, not just slightly-stale advice.
- We haven't measured how often temporary inconsistency leads to harmful actions.
- Regulated enterprise use cases may require stronger guarantees — see [f12-retention-wiring](../open-question/f12-retention-wiring.md) for the compliance side.

## Open sub-questions

- What's the operational definition of a "harmful" action induced by stale memory? Quality (wrong advice) vs safety (wrong action) is the axis to formalize.
- Is the "worst case = stale advice" claim falsified by even rare high-blast-radius scenarios, or does the architecture need a probability-weighted treatment?
- Should regulated workloads run a different consistency profile from default? If yes, what's the operational cost?

## Related

- [H31-distributed-systems-mapping](./H31-distributed-systems-mapping.md) — depended on
- [federation-access-patterns](../concept/federation-access-patterns.md) — frames *which* primitives a federated store needs; eventual consistency is one bet on requirement 4 (conflict resolution)
- [H35-conflict-rate](./H35-conflict-rate.md) — the empirical complement
- [org-wide-store-repo-scoped-queries](../decision/org-wide-store-repo-scoped-queries.md) — implicit consumer of this assumption
- [f12-retention-wiring](../open-question/f12-retention-wiring.md) — adjacent regulated-tenant constraint
- Shelved predecessor: H11 in _archive

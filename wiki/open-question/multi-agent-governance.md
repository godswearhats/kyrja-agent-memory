---
type: open-question
name: Multi-agent memory governance
status: OPEN
last_ingested: 2026-05-12
sources: []
epistemic_tags: [asserted]
tags: [multi-agent, governance, seven-layer-stack]
---

## The question

When **N agents** (~500 in a frontier enterprise deployment) are running simultaneously, writing to and reading from the same memory store, **how should governance work?**

This is the **7th layer** of the [seven-layer-stack](../concept/seven-layer-stack.md) — the one no incumbent covers. It is broader than [H32-eventual-consistency](../hypothesis/H32-eventual-consistency.md) (which is about a single architectural choice) and broader than [H35-conflict-rate](../hypothesis/H35-conflict-rate.md) (which is about empirical frequency). Governance covers: concurrent-write semantics, conflict-resolution policy, audit-trail requirements, per-agent permission grants, organizational visibility rules, and provenance tracking.

## Why it matters

- **No incumbent covers this.** [seven-layer-stack § Incumbent mapping](../concept/seven-layer-stack.md) shows governance is uncovered across Cognee, Mem0, Zep, LightMem, Letta. The integration-gap leg of the thesis rests partly on this gap being real.
- **Enterprise procurement.** Regulated industries (compliance, legal, medical) treat audit trail, RBAC, and access controls as table-stakes. While the commercial framing lives in Eira's space, the *architectural* requirements those translate into are wiki-scope.
- **Provenance and revocation.** If memory was learned from a session by Engineer A on a repo Engineer B doesn't have access to, the read-time ACL check ([org-wide-store-repo-scoped-queries](../decision/org-wide-store-repo-scoped-queries.md)) handles visibility but not *provenance erasure*. The latter is a research-grade question.

## What evidence would resolve it

- **A formal model.** What's the minimum governance surface that satisfies (a) audit, (b) RBAC, (c) provenance, (d) revocation — without sinking write-path latency?
- **CMU position paper** (arxiv 2603.10062) frames multi-agent consistency formally; pairs with this question on the consistency side. See [multi-agent-consistency](./multi-agent-consistency.md "pending").
- **Per-cluster decomposition.** Likely the question splits into sub-questions (audit + RBAC + provenance + revocation) each with its own technical answer; the meta-question is whether they compose.

## Related

- [seven-layer-stack](../concept/seven-layer-stack.md) — the architecture context (governance is layer 7)
- [H32-eventual-consistency](../hypothesis/H32-eventual-consistency.md) and [H35-conflict-rate](../hypothesis/H35-conflict-rate.md) — narrower hypotheses inside this question
- [org-wide-store-repo-scoped-queries](../decision/org-wide-store-repo-scoped-queries.md) — the wedge's narrow ACL model (read-time check inheriting from repo permissions)
- [f12-retention-wiring](./f12-retention-wiring.md) — adjacent compliance-side gap
- [multi-agent-consistency](./multi-agent-consistency.md "pending") — formal-definition gap
- Deep-dive §11 Q4 origin: agentic-memory-scaling-deep-dive.md

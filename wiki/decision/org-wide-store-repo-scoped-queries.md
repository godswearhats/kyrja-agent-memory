---
type: decision
name: Org-Wide Store, Repo-Scoped Queries
status: ACTIVE
last_ingested: 2026-05-12
sources: []
tags: [wedge, scoping, moat]
---

## Decision

Storage is **org-wide**: a single pooled memory store spans every engineer and every repo within an organization. Default query scope is **per-repo**: retrieval narrows to the active repo's slice before any structured filter or semantic re-rank runs. ACLs inherit from repo permissions — an engineer sees only the repo-slices they can already access in source control.

## Motivation

- **The moat lives in pooled cross-engineer memory within an org.** Token savings on a single engineer's own prior sessions is a feature; cross-engineer memory within the org is the defensible part. See the moat discussion in tool-chain-wedge-goals-2026-05-11.md.
- **Per-repo query scope is forced by the read-path constraints.** Engineers work primarily in 1 repo, sometimes 2-3. Repo-scoped queries make the structured filter (path, entity, task type) sharp; cross-repo retrieval requires cross-repo entity resolution we don't have. See [repo-bounded-scope](./repo-bounded-scope.md).
- **Org-wide storage is cheaper than per-engineer storage** for the same coverage, and avoids the "new hire sees nothing" cold-start problem.
- **ACL inheritance from repo permissions** is the simplest correct authorization model — if you can read the code, you can read the memory about the code.

## Commitments

- Storage layer must support an `org_id` partition above `repo_id`; every memory carries both.
- Default query API takes `(org_id, repo_id)` as required arguments. Cross-repo within the same org is a fallback, not a default.
- Compound key indexes on `(org_id, repo_id)`, `(org_id, repo_id, task_type)`, `(org_id, repo_id, path)`.
- ACL check happens at query time against the caller's repo permissions, not at write time. Writes are unrestricted within the engineer's accessible repos.
- Cross-org sharing is **not** a v1 feature and is not currently on the roadmap.

## Reversibility

**Expensive.** Once an org-wide store has accumulated memories from multiple engineers, retracting to per-engineer storage discards the pooled value (which is the moat). Retracting in the other direction — from org-wide to *unrestricted* cross-org — is plausible but reintroduces the ACL and embedding-crowding problems we've explicitly designed away. Treat the org boundary as a hard architectural commitment for v1.

## Related

- [repo-bounded-scope](./repo-bounded-scope.md) — the per-query scope this decision composes with
- [precision-over-recall](./precision-over-recall.md) — what tunes the read path within the scoped candidate set
- [structured-filter-first](./structured-filter-first.md) — the retrieval order that runs inside the repo scope
- [tool-chain-wedge-as-adoption-path](./tool-chain-wedge-as-adoption-path.md "pending") — the wedge whose moat this decision protects

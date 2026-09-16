---
type: decision
name: Repo-Bounded Scope
status: ACTIVE
last_ingested: 2026-05-12
sources: []
tags: [wedge, scoping]
---

## Decision

The tool-chain memory system's primary scope key is the **repository URL** (or `repo + monorepo-path-prefix`). All retrieval defaults to repo-scoped queries; cross-repo search exists as a fallback, not a default.

## Motivation

- Engineers work primarily in 1 repo, sometimes 2-3.
- Per-repo scoping makes the structured filter (path, entity, task type) sharp; cross-repo retrieval requires cross-repo entity resolution which we don't have.
- Reduces the search space by orders of magnitude before semantic retrieval runs, mitigating the homogeneous-code embedding-crowding problem (see [cascading-failures](../concept/cascading-failures.md), mode 2).
- Cross-repo trade-off was discussed explicitly 2026-05-11; outcome recorded in tool-chain-wedge-goals-2026-05-11.md. The org-wide-storage-with-repo-scoped-query commitment is atomized at [org-wide-store-repo-scoped-queries](./org-wide-store-repo-scoped-queries.md).

## Commitments

- Default query scope is per-repo (`repo_id` required argument).
- Compound key indexes on `(repo_id)`, `(repo_id, task_type)`, `(repo_id, path)` are mandatory in store design.
- Cross-repo search is a v2 feature, not v1.
- Storage-side org-wide pooling is covered separately at [org-wide-store-repo-scoped-queries](./org-wide-store-repo-scoped-queries.md).

## Reversibility

**Moderate.** Could be relaxed to default cross-repo with a config flag. But relaxing reverses the embedding-crowding mitigation and re-exposes the system to recall problems on homogeneous code corpora. Reversal would require demonstrating that cross-repo precision is achievable at our corpus scale; currently `[SPECULATED]`.

## Related

- [precision-over-recall](./precision-over-recall.md) — what tunes the read path within the scoped candidate set
- [structured-filter-first](./structured-filter-first.md) — the retrieval order that runs inside the repo scope
- [cascading-failures](../concept/cascading-failures.md) — the recall regime this decision avoids

---
type: hypothesis
name: H46 — Extraction-time consolidation smears scope bindings as the store grows
status: REJECTED (2026-07-25, by its own pre-registered falsification test)
last_ingested: 2026-07-25
sources: []
epistemic_tags: [MEASURED]
tags: [masq, supermemory, extraction-first, consolidation, scope-smear]
---

> **REJECTED 2026-07-25.** The falsification test below fired exactly as
> registered: extraction of corpus session s0199 (verbatim prose) into an
> **empty** store (container `masq-audit-h46-size0`, 2026-07-24) already
> yields unscoped kernel memories — binding loss at store-size 0, so the
> smear is a property of extraction, not consolidation. The surviving
> account is **discourse-level atomization**: MASQ prose names scope in a
> chatter aside, not in the fact sentence; extraction atomizes sessions into
> independent one-sentence memories, so scope and value land in different
> atoms with no binding. Post-repair full-store census corroborates: 3,537
> memories, 23 kernel-entity value-memories, 0 scope-bound, while 18 scope
> *mentions* survive as separate atoms.
> ([repair experiment](../experiment/2026-07-25-masq-supermemory-repair.md))

## Claim

Supermemory's memory-extraction agent preserves scope bindings when the store
is near-empty but strips them at corpus scale: consolidation/dedup against
existing memories normalizes confusable scoped facts (`checkout-web`'s
`/checkout` rate limit, `checkout-api`'s `/checkout` rate limit, …) into a
single scope-free entity ("the `/checkout` rate limit"), so the scope index is
destroyed *by* the memory-building process, not merely absent from it.

## What would falsify it

A store-size sweep (ingest the same scoped documents into stores pre-loaded
with 0 / ~50 / ~300 / ~600 corpus documents; measure scope-binding rate of the
newly extracted memories at each size) showing binding rate flat in store
size. If binding is low even at store-size 0 for corpus-style documents,
the smear is a property of the extraction prompt/content, not consolidation —
claim REJECTED in favor of a plain extraction-lossiness account. Confirmation
requires a monotone (or step) decline in binding rate with store size.

## Evidence for

- `[MEASURED]` One-document probe store: extraction preserved scope perfectly
  ("…for the checkout-web service to 500 req/s"), twice (both transports).
  *Construct-validity:* single hand-written probe document, not corpus prose;
  probe prose names scope adjacent to the value, which corpus prose also does
  (18/18), so the contrast is at least like-for-like on scope presence.
  ([experiment](../experiment/2026-07-22-masq-supermemory-smoke.md))
- `[MEASURED]` Full-corpus store (626 docs): 0 scope-bound kernel-entity
  memories in retrieved top-40, both transports. *Construct-validity:*
  retrieved-set census only — the full-store census is a pending audit item;
  until it lands, this evidence is provisional.
  ([experiment](../experiment/2026-07-22-masq-supermemory-smoke.md))

## Evidence against

- `[MEASURED]` **Store-size-0 probe (decisive)**: corpus session s0199
  extracted into an empty store yields unscoped kernel memories — the exact
  rejection condition registered below. 2026-07-24, container
  `masq-audit-h46-size0`
  ([repair experiment](../experiment/2026-07-25-masq-supermemory-repair.md)).
- Reconciliation with the "evidence for": the one-document probe that
  preserved scope was **hand-written prose naming scope adjacent to the
  value in the same sentence**; corpus prose names scope in a discourse
  aside. The contrast was never store-size — it was intra-sentence vs
  cross-sentence binding. The like-for-like caveat recorded there was the
  tell.

## Open sub-questions

- Is the smear driven by the extraction prompt's entity-normalization
  instructions, by retrieval of related memories into the agent's context, or
  by an explicit dedup/contradiction-resolution step? (Distinguishable by
  inspecting the agent's tool-call traces in the proxy log.)
- Does the same smear appear in other extraction-first systems (Mem0, Cognee),
  i.e. is this a paradigm property or a Supermemory implementation detail?

## Related

- [experiment/2026-07-22-masq-supermemory-smoke](../experiment/2026-07-22-masq-supermemory-smoke.md) — motivating observation + pre-registered sweep design
- [H45-exclusion-over-recall](./H45-exclusion-over-recall.md) — read-time sibling: ranking can't exclude scopes; H46 claims writing can't preserve them
- [open-question/structured-memory-auto-scope-index](../open-question/structured-memory-auto-scope-index.md) — the question both feed
- [incumbent/supermemory](../incumbent/supermemory.md) — "extraction-first lossiness" structural ceiling, now with a concrete mechanism candidate

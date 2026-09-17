# Pre-registration — does deployable exclusion clear the scope-blind plateau?

**Locked:** 2026-09-16, before any world was generated or any reader call made.
**Author:** Nils (indigo). **Status:** LOCKED.

## Why this exists

The published H45 conclusion asserts that similarity ranking *"(semantic or lexical,
any method, any k) cannot exclude the confusable siblings ... because the query offers
no content signal that separates them"* ([H45](../../wiki/hypothesis/H45-exclusion-over-recall.md)),
and that `arm_scopefilter` is an **oracle** whose deployable equivalent is unknown.

Both were falsified at the retrieval-composition level during a publish-readiness
review (2026-09-16), reproduced independently twice:

- The target scope is **verbatim in `a_query` on 15/15 cores**.
- `arm_bm25`'s `[a-z0-9]+` tokenizer splits `checkout-web` → `checkout` + `web`, so
  every sibling collides on the shared token; and the arm retrieves with the full
  ~63-word task prompt, diluting the discriminator in boilerplate that matches all
  siblings equally.
- Fixing both (compound tokens + scope-phrase query, **no ground truth used**) moves
  top-10 composition from 2.7/3.4 target + 5.3 siblings to **3.4/3.4 target + 0.2
  siblings**, rank-0 correct 15/15.
- A 10-line deployable filter (regex the scope from `"In the context of X:"`,
  substring-match prose) selects **exactly the oracle's sessions on 15/15 cores**.

Composition is not a decision. This experiment asks whether near-perfect exclusion,
obtained by deployable means, actually moves **B-pass**.

## Hypothesis

**H47.** On the 15 headline 60k cores, a BM25 arm differing from the published
`bm25_k10` *only* in tokenization and query formulation will clear the scope-blind
plateau (paste 9/15, bm25 8/15, vector 6/15) and approach the filter arms (15/15).

## Design

- **Worlds:** the 15 published headline cores — 3 domains × seeds 4001–4005, 60k,
  regenerated from `headline_gen.py` (deterministic).
- **Reader:** `claude-opus-4-8`, temperature 0 — **the published reader**, so results
  are directly comparable to the existing ladder. No model substitution.
- **New arm `bm25_scoped_k10`:** identical to `bm25_k10` except
  (a) tokenizer `[a-z0-9][a-z0-9-]*` (hyphenated compounds kept whole), and
  (b) query = the scope phrase parsed from `a_query`, not the full prompt.
  **k stays 10.** Everything else — formatting, reader, prompts, grading — untouched.
- **Control:** `bm25_k10` re-run on the same cores in the same session, so the
  comparison is paired and cannot be confounded by drift since 2026-06-30.
- **Metric:** B-pass (correct action + correct conflict flag, closed-form). A is
  recorded but is **not** the endpoint — the archive's own warning that A does not
  predict B applies here.
- **Cost:** 2 arms × 15 cores × 2 calls = 60 calls. Retrieval arms send ~10 sessions,
  not the 60k corpus, so these are small prompts.

## Pre-registered outcomes and what each would mean

| Outcome | B-pass | Reading |
|---|---|---|
| **H47-A** | ≥ 13/15 | Exclusion is sufficient, and obtainable without an oracle. "Ranking is the wrong primitive" is **fully falsified**; the corrected claim is *don't dilute the discriminator*. |
| **H47-B** | 10–12/15 | Exclusion is necessary but not sufficient. Clears the plateau, falls short of the filter — something beyond composition costs the remainder. |
| **H47-C** | ≤ 9/15 | Near-perfect composition does **not** transfer to decisions. H45's conclusion **survives on better evidence** even though its stated mechanism was wrong. |

## My prediction, recorded before running

**H47-B**, 11/15. Reasoning: at k=10 the arm returns ~6.4 unscoped chatter sessions
alongside the 3.4 target ones, where `scopefilter` returns the target sessions alone.
If non-confusable noise is harmless, this should land at H47-A; I expect it to cost
one or two cores, which is the whole point of running it rather than asserting it.

## Goalpost discipline

- The thresholds above are fixed. If the result lands between bands I report the raw
  count and say the bands were badly chosen — I do not move them.
- **Every outcome gets published**, including H47-C, which would be the one that
  rescues the original headline at my expense.
- n=15 with a paired control. This does not license a population claim; it is a
  within-benchmark test of a mechanism, and the external-validity limits of MASQ
  (constructed confusability, lexically-planted scope) apply unchanged.
- The genuinely untested case remains scope that must be **inferred** from unanchored
  natural language. Nothing here speaks to it.

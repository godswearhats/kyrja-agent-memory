# Results — H47: deployable exclusion clears the plateau

**Run:** 2026-09-16/17. **Pre-registration:** [PREREG-scoped-bm25.md](./PREREG-scoped-bm25.md), locked before any world was generated.
**Reader:** `claude-opus-4-8`, temperature 0 — the published reader, unsubstituted.
**Worlds:** the 15 published headline cores (3 domains × seeds 4001–4005, 60k), regenerated from `headline_gen.py`.

## Result

| arm | B-pass | Wilson 95% | mean A |
|---|---|---|---|
| `ceiling` (oracle, published) | 15/15 | [80,100] | 0.97 |
| `scopefilter` (oracle, published) | 15/15 | [80,100] | 0.79 |
| **`bm25_scoped_k10`** (deployable, new) | **14/15** | **[70,99]** | **0.87** |
| `bm25_k10` (control, re-run this session) | 9/15 | [36,80] | 0.73 |
| `paste` (published) | 9/15 | [36,80] | 0.68 |
| `vector_k10` (published) | 6/15 | [20,64] | 0.79 |

Paired against its own control on the same cores in the same session:
**5 FAIL→PASS, 0 PASS→FAIL**, 9 PASS→PASS, 1 FAIL→FAIL.
Exact McNemar two-sided **p = 0.0625** (one-sided 0.031).

The control re-ran at 9/15 against the 8/15 published in June — one core of drift,
which is why the control was re-run rather than compared across sessions.

## Verdict against the pre-registered bands

Bands were A ≥ 13 · B 10–12 · C ≤ 9. Outcome **14/15 → H47-A**.

**My recorded prediction was H47-B at 11/15. It was wrong — I under-predicted by 3.**
The reasoning was that the arm returns k=10 and so carries ~6 unscoped chatter
sessions that `scopefilter` does not, and that this noise would cost a core or two.
It cost at most one. Non-confusable noise is close to harmless here; *confusable*
noise was doing all the damage.

## What this establishes

The published conclusion — *"similarity ranking (semantic or lexical, **any method,
any k**) cannot exclude the confusable siblings ... because the query offers no
content signal that separates them"* — is **falsified at the decision level**, not
merely at the composition level.

Two changes were sufficient, neither of which reads any ground-truth field:

1. **Tokenization.** `[a-z0-9]+` (the Lucene default) splits `checkout-web` into
   `checkout` + `web`, so every sibling collides on the shared prefix. Keeping
   hyphenated compounds whole makes the full scope string the high-IDF term.
2. **Query formulation.** Retrieving with the full ~63-word task prompt dilutes the
   one discriminating token among boilerplate every sibling matches equally. The
   scope phrase is already present in the query the benchmark hands every arm.

Measured cost of the dilution: the scope-discriminating token contributes ~20% of
the BM25 document score under the published configuration, against 100% of the
decision under a filter.

## The corrected claim

Not *"ranking is the wrong primitive, the task needs an index."*

Instead: **a discriminator that is present in the query must not be diluted — by
tokenization that splits it, or by burying it in prompt boilerplate. Ranking is
sufficient here once it isn't.** That is a smaller claim about paradigms and a much
more useful one for anyone building retrieval, because it names a bug rather than a
law.

## Limits

- n=15, one size (60k), one reader. A within-benchmark mechanism test, not a
  population claim.
- Two-sided p = 0.0625 does not clear 0.05. Five discordant pairs is the most the
  design can produce given the control's 9/15; the effect is a clean 5–0 sweep but
  the test is underpowered by construction. Seeds, not sizes, buy power here.
- MASQ **plants** the scope string lexically in the prose and names it in the query.
  This result therefore says nothing about scope that must be **inferred** from
  unanchored natural language. That remains the honest open boundary — and it, not
  "the filter is an oracle", is what the archive should have been claiming was hard.
- `arm_bm25`'s docstring argues that hyphen-splitting is lexical retrieval's
  "strongest fair shot." It is the opposite: it is the single choice that guarantees
  sibling collision. The intent was to avoid strawmanning BM25; the effect was to
  strawman it precisely where the benchmark was measuring.

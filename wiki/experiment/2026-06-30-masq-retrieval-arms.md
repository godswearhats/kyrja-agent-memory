---
type: experiment
name: MASQ retrieval-arm ladder — ranking floors, scope-filter ties oracle
status: COMPLETE
last_ingested: 2026-06-30
sources: []
epistemic_tags: [measured]
tags: [masq, retrieval, scope-disambiguation, bm25, vector, structured-filter, v2]
---

First test of *memory-system-under-test* arms on the MASQ v2 benchmark. MASQ is a
**synthetic** org corpus built to probe one specific construct: keeping near-identical
"scopes" (five services `checkout-web/api/internal/mobile/sandbox`, each with its own
`/checkout` rate-limit change history) separate when answering about one of them. The
arms slot into a fixed contract — `arm_fn(family, corpus) → context string`, with the
reader (Opus 4.8, temp 0) and closed-form grader held constant — so each arm differs
**only** in what text it puts in front of the reader. This isolates retrieval strategy
as the single variable. Tests [H45-exclusion-over-recall](../hypothesis/H45-exclusion-over-recall.md);
informs [structured-filter-first](../decision/structured-filter-first.md) and
[precision-over-recall](../decision/precision-over-recall.md); replicates the
method-equivalence finding of [Thread 5](2026-04-17-thread5-retrieval-comparison/README.md).

## Hypotheses tested

- [H45-exclusion-over-recall](../hypothesis/H45-exclusion-over-recall.md) — within MASQ's confusable-scope task, a structured scope filter reaches oracle decision accuracy while similarity ranking (any method) cannot exclude siblings and floors. **Supported within construct.**
- Sub-claim (pre-registered, **REJECTED**): "lexical retrieval rescues the embedding scope-merge." BM25 ≈ vector; no rescue.

## Method

- **Worlds:** 15 independent cores = 3 domains (rate-limit, ownership, merge-policy) × 5 seeds (4001–4005), each with 5 confusable scopes. Headline run at the 60k-token size; a vector-only size sweep also covered 25k/60k/150k/400k (60 cores). Generator: [headline_gen.py](../../masq/generator/headline/) (synthetic, local, deterministic per seed).
- **Reader:** `claude-opus-4-8`, temperature 0, one call each for task A (chain reconstruction, scored 0–1 by closed-form field match) and task B (decision: correct action + correct conflict flag, pass/fail). No LLM judge.
- **Arms** (the only thing that varies): `paste` (whole corpus), `lww` (latest write, scope-blind), `ceiling` (oracle: target chain + resolution-type labels), `vector_k10` (Ollama `nomic-embed-text`, cosine top-10), `bm25_k10` (standalone Okapi, IR tokenization, top-10), `scopefilter` (`WHERE scope==target`, raw prose, no labels). Arms: [arm_vector.py](../../masq/harness/arm_vector.py), [arm_bm25.py](../../masq/harness/arm_bm25.py), [arm_scopefilter.py](../../masq/harness/arm_scopefilter.py).
- **Stats:** per-arm B-pass with Wilson 95% CIs; paired within-core McNemar (exact 2-sided sign test on discordants), n=15 independent cores at one size (not pseudoreplicated).

## Results

*All figures in this section are `[MEASURED]`; their construct-validity and scope limits are detailed in the dedicated note immediately below this section.*

**Ladder at 60k (n=15):** `[MEASURED]`

| arm | strategy (DB framing) | B-pass | Wilson 95% | mean A |
|---|---|---|---|---|
| ceiling | oracle (resolved answer) | 15/15 | [80,100] | 0.97 |
| **scopefilter** | **`WHERE scope=target`** | **15/15** | [80,100] | 0.79 |
| paste | `SELECT *` | 9/15 | [36,80] | 0.68 |
| bm25_k10 | `ORDER BY keyword LIMIT 10` | 8/15 | [30,75] | 0.79 |
| vector_k10 | `ORDER BY similarity LIMIT 10` | 6/15 | [20,64] | 0.79 |
| lww | scope-blind latest | 6/15 | [20,64] | 0.24 |

**Paired (within-core, exact p):** `[MEASURED]` scopefilter vs vector 9/0 (p=0.004); vs bm25 7/0 (p=0.016); vs paste 6/0 (p=0.031); ceiling vs scopefilter 0/0 (p=1.0 — identical pass-set). *Construct-validity:* exact 2-sided sign test on within-core discordants, n=15 independent cores at one size (not pseudoreplicated).

**Retrieval-composition diagnostic (all 15 cores, no reader calls):** `[MEASURED]` top-10 averages — vector: 2.9/3 target, 5.8 sibling, rank-0=target in 11/15; bm25: 2.7/3 target, 5.3 sibling, rank-0=target in 10/15. Both **recall** the target well; neither can **exclude** siblings. *Construct-validity:* scope composition of the retrieved top-10, computed directly from ground-truth scope tags, no reader involved.

**Vector size sweep (60 cores):** `[MEASURED]` vector B-pass 5/6/4/7 of 15 across 25k/60k/150k/400k — flat at the floor, no degradation at 400k; ceiling 15/15 at every size (canary clean, no infra/cap contamination). Size-invariant. *(Construct-validity for all four blocks above: see the dedicated note that follows.)*

Three non-obvious points the construction did **not** force:
1. **Exclusion, not recall, is the bottleneck.** Retrievers find the target fine; they drown it in equally-relevant siblings.
2. **The reader is not the bottleneck.** scopefilter ties ceiling *without* the resolution-type labels (mean A 0.79 vs 0.97, identical B) — given a scope-pure raw chain, the reader resolves the conflict itself.
3. **Method-equivalence.** bm25 ≈ vector (8 vs 6, not separable), independently replicating Thread 5.

### Construct-validity note

B-pass measures whether the reader emits the correct action **and** the correct conflict flag — closed-form exact match, the real decision the benchmark cares about; no judge drift. **Critical scope limit:** MASQ *constructs* the confusability — siblings are authored to be equally content-relevant to the query. So "ranking retrieves siblings" is partly **built into the design**, not discovered; what is genuinely measured is (a) target recall stays high, (b) exclusion alone moves B from floor to oracle, (c) the reader needs no pre-classified conflict. mean A (0.79) does **not** predict B (scopefilter 15/15 vs vector 6/15 at equal A) — A is a reconstruction-detail score, B is the decision; do not use A as a proxy. `scopefilter` and `ceiling` are **oracles** (they consume the ground-truth scope tag / resolved chain); no deployable system has this for free, so they bound the achievable, they are not themselves systems.

## Limitations

- **Synthetic, single-construct.** One benchmark, confusability by construction. **Not** evidence about real coding/enterprise-corpus retrieval, where confusability is natural and variable. Generalization is untested.
- **n=15 cores, one size (60k), one reader model.** The headline ladder is one size; seeds (not sizes — sizes are near-verbatim copies, pseudoreplicated) are the axis that buys power. Within-plateau gaps (paste vs bm25 vs vector) are not separable at this n.
- **Oracle filter.** scopefilter uses ground-truth scope tags; whether any real system recovers that filter is an [open question](../open-question/structured-memory-auto-scope-index.md), not shown here. **Correction 2026-09-17:** inside MASQ it is recovered trivially — parsing the scope from the query's `"In the context of X:"` preamble and substring-matching prose selects **the identical sessions on 15/15 cores**. The generator plants the scope string lexically. The oracle framing overstates the difficulty *within this benchmark*.
- Single embedder (`nomic-embed-text`) and single BM25 config; a different encoder could shift recall but cannot manufacture an exclusion criterion the query lacks. **FALSIFIED 2026-09-17** — the criterion was in the query all along, and a BM25 config differing only in tokenization and query formulation scores 14/15 B-pass against this arm's 8/15. See [RESULTS-scoped-bm25](../../masq/harness/RESULTS-scoped-bm25.md). This bullet asserted a universal from one configuration; treat it as the cautionary example it now is.

## Raw artifacts

- Harness + arms: [masq/harness/](../../masq/harness/) (`run.py`, `arm_{vector,bm25,scopefilter}.py`)
- Worlds + per-core results: [masq/generator/headline/](../../masq/generator/headline/)

## Related

- [structured-filter-first](../decision/structured-filter-first.md) — controlled (construct-limited) anchor for its thesis
- [precision-over-recall](../decision/precision-over-recall.md) — exclusion-is-the-bottleneck is precision-over-recall, measured
- [H33-routing-matters](../hypothesis/H33-routing-matters.md) — method-equivalence strengthens its falsifier #3
- [Thread 5 retrieval comparison](2026-04-17-thread5-retrieval-comparison/README.md) — prior bm25≈semantic≈hybrid finding, here replicated
- [structured-memory-auto-scope-index](../open-question/structured-memory-auto-scope-index.md) — does a real system reach the oracle filter? (system #2 / Cognee)

# MASQ — a synthetic benchmark for scope disambiguation in agent memory

MASQ builds corpora in which the hard part is not *finding* the right memory but
*excluding* the wrong ones. It then measures whether a memory system lets an agent make
the correct decision.

The name is not an acronym and is never expanded anywhere in this archive. Treat it as a
bare label.

---

## The failure mode it constructs

A memory corpus contains several **confusable sibling scopes** — say `checkout-web`,
`checkout-api`, `checkout-mobile`, `checkout-internal`, `checkout-legacy`. Each one
carries its own independent history of a value being set, revised, superseded, contested
and resolved. All of it is buried in unrelated chatter across a simulated 180 days of
team activity.

The question asks about exactly one of them. Every sibling is topically similar, mentions
the same parameter, and is a plausible answer. A retriever that ranks by similarity gets
all of them.

This is a deliberately narrow target. Most memory benchmarks test whether a system can
find a needle. MASQ tests whether it can leave five near-identical needles behind.

## Why it might be useful

- **It isolates one variable.** Every arm implements `arm(family, corpus_dir) -> str`.
  Reader model, prompts, parsing and grading are frozen identical across arms, so the
  only thing that differs is the context the memory strategy produces.
- **Grading is deterministic.** No LLM judge anywhere. Scores are closed-form field
  matches, so there is no judge drift to calibrate and no human-agreement study needed.
- **Worlds are verified, not trusted.** `verify.py` checks construction invariants on the
  *emitted artifact* rather than on the generator's intentions — because a pilot showed
  that authorial care leaks into the output in ways the author can't see. A degenerate
  world fails loudly instead of quietly becoming an easy benchmark.
- **It's reproducible and cheap to generate.** Deterministic per seed, stdlib-only Python,
  no dependencies, no services. Two runs at the same seed are byte-identical.
- **It produced a result that overturned its own headline.** See below. If you want a
  worked example of a benchmark being used to falsify the claim its authors made from it,
  that's here in full.

Be clear about what it is not: a general memory benchmark, a leaderboard, or evidence
about real corpora. It constructs its difficulty, and it plants its own solution — see
*Limits*.

---

## How it works

### Generation

A **family** is one world: a JSON object plus a rendered `corpus.md`.

1. **`domains.py`** holds three domain packs, each instantiating the same schema over a
   different value type — `rate-limit` (numeric, e.g. 100 req/s), `ownership`
   (team-valued), `merge-policy` (closed enum). Same structure, different surface register,
   so a result that only holds for numbers is visible as such.
2. **`embedding.py`** lays down the structure: the target scope's chain, the sibling
   scopes' chains, and near-miss entities that resemble the target but belong to no scope.
   Chains are drawn from eight patterns built out of five step types — `initial`,
   `self_revision`, `supersession`, `collision`, `resolution`. `P1` is
   initial → supersession → supersession; `P5` is initial → supersession → collision →
   resolution; and so on.
3. **`compose.py`** renders structure into prose by layered composition under a seeded
   RNG — atoms combine into compounds, compounds into paragraphs, paragraphs into session
   bodies — drawing from a bank of human-written atoms (`generator/atoms/`) in varied
   voices: ops, deploy, on-call, QA, retro, code review. This exists so the prose carries
   no machine-detectable regularity that a retriever could key on instead of the content.
4. **`sweep.py`** and **`headline_gen.py`** drive generation. **`headline_gen.py` is the
   published configuration** — a pinned difficulty core (5 scopes, 4 near-misses, a
   20-sibling bed) with only the chatter volume varying to hit 25k/60k/150k/400k tokens.
   `sweep.py` uses different parameters and is not what the results tables were run on.

### Verification

`verify.py` is an independent checker, not a self-report. On the published 5-scope
configuration it runs 19 checks, including:

- **I1 value collision** — sibling final values must overlap the target chain's values, so
  the value alone can never identify the scope.
- **I2 write-count cover** — enough siblings must have multiple writes that "pick the one
  that changed" doesn't work.
- **I3 parameter recurrence** — the parameter name must appear in the noise, so keyword
  matching on it is useless.
- **I4/I12 marker discipline** — no cross-party revision may be left unmarked or
  over-marked, in either the sibling chains or the target chain.
- **I5 kernel isolation** — no chatter session may mention the target scope with the
  parameter and a value.
- **I9/I11 scope and near-miss isolation**, **I10 scope coverage**.
- **GT checks** — the recorded ground truth must agree with the chain actually emitted.

### Evaluation

`run.py` takes scenario directories and a list of arms. For each, it calls the reader
twice:

- **Task A** — reconstruct the supersession chain. Graded 0–1 by closed-form field match.
- **Task B** — take the decision. Output is `(action, conflict_flag)`, graded pass/fail.

**B is the endpoint. A is not a proxy for it** — the archive measured arms with equal A
and wildly different B. Do not compare an A number against a B number.

One documented defect: on items whose ground truth carries a conflict, `grade_b` checks
only the flag and discards the action; on non-conflict items it checks both. Three of the
fifteen headline cores are conflict items.

### Arms

| key | what it does |
|---|---|
| `paste` | the entire corpus in context |
| `lww` | the most recent write, scope-blind |
| `ceiling` | **oracle** — the target chain plus resolution-type labels |
| `scopefilter` | **oracle** — the target chain as raw prose, no labels |
| `vector_k5/k10/k20` | embedding top-k (Ollama `nomic-embed-text`) |
| `bm25_k10` | standalone Okapi BM25, Lucene-default tokenization |
| `bm25_scoped_k10` | as `bm25_k10`, but compound tokens and a scope-phrase query |
| `supermemory` | a commercial extraction-based memory system |

`ceiling` and `scopefilter` consume ground truth. They bound what is achievable; they are
not systems.

---

## Quickstart

```bash
cd generator
python3 headline_gen.py 60k                                   # the published 15 worlds
python3 verify.py headline/rate-limit/s4001/60k/family-rate-limit.json

cd ../harness
python3 run.py ../generator/headline/rate-limit/s4001/60k \
    --model claude-opus-4-8 --arms paste,bm25_k10,bm25_scoped_k10,scopefilter,ceiling
```

Generation needs nothing but Python. The harness needs the `claude` CLI for the reader;
the vector arms additionally need Ollama with `nomic-embed-text`, and `supermemory` needs
`SUPERMEMORY_API_KEY`. Results are written into each scenario directory and merged by arm
key, so partial runs don't clobber earlier ones.

Generated corpora are build outputs and are gitignored. Published results are in
[`results/`](./results/).

---

## What it measured

On the 15 headline cores at 60k, reader `claude-opus-4-8`:

| arm | B-pass |
|---|---|
| `ceiling` (oracle) | 15/15 |
| `scopefilter` (oracle) | 15/15 |
| `bm25_scoped_k10` | 14/15 |
| `paste` | 9/15 |
| `bm25_k10` | 8/15 (9/15 on re-run) |
| `vector_k10` | 6/15 |

The original conclusion drawn from the first five rows was that similarity ranking
*"any method, any k"* cannot exclude confusable siblings, and that only a structured
filter can reach oracle accuracy.

**That was wrong**, and the last row is why. The target scope is verbatim in the query on
all 15 cores. Two configuration choices were throwing it away: the Lucene-default
tokenizer splits `checkout-web` into `checkout` + `web` so every sibling matches the
shared prefix, and the arm retrieved using the whole ~63-word task prompt, diluting the
one discriminating token to about 20% of the BM25 document score. `bm25_scoped_k10` fixes
both, reads no ground truth, and ties the oracle.

The corrected claim: **a discriminator present in the query must not be diluted — by
tokenization that splits it, or by boilerplate that drowns it.** Ranking is sufficient
here once it isn't.

Pre-registration and full result: [`harness/PREREG-scoped-bm25.md`](./harness/PREREG-scoped-bm25.md),
[`harness/RESULTS-scoped-bm25.md`](./harness/RESULTS-scoped-bm25.md).

A second finding, at n=1 core and therefore anecdotal: an extraction-based commercial
system scored *below* the scope-blind baselines, because sentence-level extraction severs
the binding between a scope named in one sentence and a value stated in another. That is a
rediscovery of *decontextualization* (Choi et al., TACL 2021).

---

## Limits

- **Difficulty is constructed.** Invariant I1 *forces* sibling values to collide. "Ranking
  retrieves siblings" is substantially built in, not discovered.
- **The solution is planted too.** The generator writes the scope string verbatim into the
  prose and names it in the query, so a ten-line filter — regex the scope out of the
  query, substring-match the prose — reproduces the "oracle" selection exactly on 15/15
  cores. The archive elsewhere calls knowing-what-to-filter-on "the entire unsolved
  problem." Inside MASQ it is not a problem at all.
- **The needle is held constant.** Chains stay at 3–5 steps while sessions grow ~67×
  across the size axis, so "difficulty doesn't scale with context length" is partly a
  design property.
- **The benchmark was iterated until the baseline failed.** The v1 design was scrapped
  because paste scored 85%+ even at 400k. That is documented in
  `harness/DESIGN-v2-analysis.md` and defensible, but it means "paste fails" was
  engineered rather than observed.
- **n=15, one size, one reader.** Seeds buy power here; sizes do not, because the size
  variants of a core are near-verbatim copies and pooling them is pseudoreplication.
- **What is genuinely untested:** scope that must be *inferred* from unanchored natural
  language with no lexical anchor. Everything MASQ shows assumes the scope is nameable.
  That, not the oracle framing, is the honest boundary of this work.

## Files

```
generator/     world construction; headline_gen.py is the published config
  atoms/       human-written prose atoms used by the composer
  verify.py    independent invariant checker
harness/       run.py + one arm_*.py per memory strategy; pre-registrations and results
results/       per-core result JSON for every published number
gate1/         pilot: are collision and supersession distinguishable from intent?
bareset-probe/ pre-registered pilot: are unmarked revisions legible? (they are not)
reads/         positioning notes on related benchmarks
FUTURE.md      extension candidates, parked
```

`phase1-breakdown.md` and `c4-worked-family.md` describe earlier designs that were
abandoned; both carry banners saying so. The live specification is
`generator/DESIGN-v2.md` and `harness/DESIGN-v2-analysis.md`.

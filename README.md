# Kyrja — an agent-memory research archive

Four months of research into memory for LLM agents (April–July 2026), published as-is
because the work stopped and the alternative was losing it.

This is not a library, a product, or a paper. It is a working research wiki plus the
code and data behind the experiments that fed it. Some of the findings are solid, some
are broken, and one of them was falsified during preparation for this release — that
correction is documented here rather than quietly removed.

**Status: parked.** Nothing here is maintained. Issues and PRs will probably go
unanswered. Take whatever is useful.

---

## Start here

| If you want | Read |
|---|---|
| What the abbreviations mean | [`wiki/GLOSSARY.md`](wiki/GLOSSARY.md) |
| Where the work had got to when it stopped | [`wiki/NOW.md`](wiki/NOW.md) |
| The full page catalogue | [`wiki/index.md`](wiki/index.md) |
| A narrative of how the thinking changed | [`wiki/log.md`](wiki/log.md) |
| How the wiki is structured, and why | [`wiki/SCHEMA.md`](wiki/SCHEMA.md) |
| Reading notes on 86 papers and vendor docs | [`wiki/source/`](wiki/source/) |
| The benchmark: what it is and how to run it | [`masq/README.md`](masq/README.md) |

`wiki/NOW.md` is a status file written for the person who wrote it, in dense shorthand.
If it bounces you, the glossary and `wiki/index.md` are the gentler doors.

---

## What's here

```
wiki/            269 markdown pages — concepts, hypotheses, experiments, decisions,
                 paper notes, open questions. Obsidian-compatible, plain markdown.
masq/            MASQ: a synthetic benchmark for scope disambiguation in agent memory.
                 Generator, evaluation harness, pre-registrations, and results.
masq/results/    Per-core result JSON for every published number.
experiments/     Thread 5 (retrieval-tier ablation), write-quality-variance
                 (encoding-format cost study), and probe corpora.
```

Generated corpora are **not** shipped — they rebuild deterministically from a seed, and
they run to hundreds of megabytes. `masq/.gitignore` marks the build-output directories.

### The wiki

269 pages under a schema that separates what was **measured** from what was **asserted**
from what was **speculated**, enforced by `wiki/lint/lint.py`. Page types: 86 `source/`
(paper and vendor notes), 41 `concept/`, 32 `open-question/`, 29 `experiment/`,
24 `hypothesis/`, 19 `incumbent/` (memory-system vendor analyses), 18 `decision/`, plus
lint reports, archived logs and root files.

Hypothesis pages carry an explicit status — PROPOSED, SUPPORTED, REJECTED, FALSIFIED —
and several are rejected or falsified by their own experiments. That's the intended use.

### MASQ

A synthetic benchmark that constructs the failure mode directly. A memory corpus contains
several **confusable sibling scopes** — `checkout-web`, `checkout-api`, `checkout-mobile`
— each carrying its own chain of supersessions (a value set, revised, revised again),
buried in unrelated chatter. The question asks about one scope. Every sibling is topically
similar and plausibly retrievable.

Grading is factorial and fully deterministic — no LLM judge:

- **A** — did the system reconstruct the correct supersession chain?
- **B** — did the agent take the right action, and flag the conflict when there was one?

The two do not track each other, and the original work was emphatic about this: A is a
reconstruction-detail score, B is the decision the benchmark cares about. Don't use A as
a proxy for B, and don't compare an A number in one section against a B number in another.

Arms implement one contract, `arm(family, corpus_dir) -> context_string`, with reader,
prompts, parsing and grading frozen identical across all of them.

Generate the **published** worlds — 3 domains × seeds 4001–4005:

```bash
cd masq/generator
python3 headline_gen.py 60k
python3 verify.py headline/rate-limit/s4001/60k/family-rate-limit.json
```

`verify.py` checks construction invariants — value collision across siblings, kernel
isolation, marker discipline, ground-truth agreement — on the *emitted artifact* rather
than the generator's intentions. A degenerate world fails there instead of silently
becoming an easy benchmark.

`sweep.py` also generates worlds but with different parameters (4 scopes, 60 siblings at
60k). It is not the published configuration; `headline_gen.py` is.

Running the harness needs the `claude` CLI for the reader and, for the vector arm, Ollama
with `nomic-embed-text`. The Supermemory arm needs `SUPERMEMORY_API_KEY`. Everything else
is dependency-free stdlib Python.

`masq/gate1/` and `masq/bareset-probe/` are pilots that ran before the design was frozen.
The bare-set probe is a genuine pre-registration — thresholds locked in `PREREG.md`, the
model reader's output sealed to file so the human reader stayed blind, contaminations
declared up front. **`gate1/` is not pre-registered**; its threshold appears only in
results written afterwards. They are not equivalent and shouldn't be cited as such.

---

## What was found

**1. A discriminator that is present in your query gets diluted away — and that, not the
ranking paradigm, was the bug.**

This finding replaces an earlier and stronger one. The archive originally concluded that
similarity ranking *"(semantic or lexical, any method, any k) cannot exclude the
confusable siblings, because the query offers no content signal that separates them,"*
and that only a structured `WHERE scope = target` filter could reach oracle accuracy.

That was asserted from two retrievers at one k with one query formulation and no
ablation, and it is false. The target scope is **verbatim in the query on 15/15 cores**.
Two configuration choices destroyed it:

- The `[a-z0-9]+` tokenizer — the Lucene default — splits `checkout-web` into `checkout`
  + `web`, so every sibling collides on the shared prefix.
- The arm retrieves using the entire ~63-word task prompt, so the one discriminating
  token competes with boilerplate that matches every sibling equally. Measured: the
  scope token contributes **~20%** of the BM25 document score.

Fixing both — neither reads any ground-truth field — moves top-10 composition from
2.7/3.4 target + 5.3 siblings to **3.4/3.4 target + 0.2 siblings**. On a pre-registered
re-run with the original reader it scores **14/15 B-pass**, against a same-session
control at 9/15, effectively tying the oracle filter at 15/15. Paired: 5 FAIL→PASS,
0 PASS→FAIL, exact McNemar two-sided p = 0.0625.

Pre-registration in [`masq/harness/PREREG-scoped-bm25.md`](masq/harness/PREREG-scoped-bm25.md),
results in [`masq/harness/RESULTS-scoped-bm25.md`](masq/harness/RESULTS-scoped-bm25.md).
The prediction recorded in that pre-registration was 11/15. It was wrong.

The corrected claim is smaller about paradigms and more useful in practice: **don't
dilute a discriminator you already have.** If a user names a service, tenant or repo in
natural language, extract it and apply it as a predicate — don't hand the whole string to
a ranker.

**2. Difficulty comes from confusability, not context length.**
The vector arm is flat at the floor — 5/6/4/7 of 15 — across 25k, 60k, 150k and 400k.
On the earlier world set, paste showed no separable trend across 6k–400k either (58/25/
25/33/50% at n=12 per size; no two cells have separable CIs). There is **no** paste-by-
size measurement on the headline worlds; the headline ladder is 60k only. Note also that
the chain length stays at 3–5 steps while the haystack grows, so the needle is held
constant by design.

**3. Extraction-based memory loses the scope binding at write time.** *(n=1 core.)*
Running Supermemory as a system under test gave A=31% on a single core, below the 69%
chain-reconstruction score of paste on that same core. A census of the full store (3,537
extracted memories) found 23 carrying the kernel value and **zero** carrying a scope
binding, while scope mentions survived as separate orphan atoms. The mechanism is
discourse-level: scope is named in one sentence and the value in another, extraction
atomises sentence by sentence, and the binding is lost. The competing explanation — that
consolidation smears scopes as the store grows — was tested and **rejected**, since it
fails at store size zero.

The wiki calls this "anecdote-level" and it is. One vendor, one core, one domain, one
seed. It is also a rediscovery of *decontextualization* (see below).

**4. Structured slot encodings cost less than prose briefings.**
$0.142 against $0.295 cold and $0.247 for a prose briefing. Both pre-registered
hypotheses were rejected, one in reverse. **The pass-rate claims from this experiment are
retracted** — in replication every arm scored 0/4, cold and prose and slots alike. Only
the cost claims stand, and see the caveats below before using those either.

---

## Known problems with this data

Read this before citing anything.

**MASQ constructs its own difficulty, and plants its own solution.** The confusability is
synthetic and deliberate. More importantly, the generator writes the scope string
verbatim into the prose and names it in the query — so a ten-line filter that regexes the
scope out of the query and substring-matches prose reproduces the "oracle" selection
exactly on 15/15 cores. The archive repeatedly frames knowing-what-to-filter-on as "the
entire unsolved problem." Inside this benchmark it isn't a problem at all. The genuinely
untested case is scope that must be **inferred** from unanchored natural language, and
nothing here speaks to it.

**The v1/v2 split.** MASQ was redesigned mid-flight. `masq/phase1-breakdown.md`,
`masq/c4-worked-family.md` and `masq/generator/README.md` describe designs that were
abandoned and now carry banners saying so. The live specification is
`masq/generator/DESIGN-v2.md` and `masq/harness/DESIGN-v2-analysis.md`.

**The B-rubric was chosen after seeing that the stricter one didn't discriminate.**
`masq/gate1/RESULTS.md` records that an escalation-based bar flattened the metric,
including for the oracle ceiling. The reasoning given is principled and fully disclosed,
but it is post-hoc metric selection on the headline endpoint.

**Statistics.** "p ≤ 0.03" appears in several places for a value that is 0.031. There is
no multiplicity correction across the three paired comparisons; under Bonferroni the
paste comparison does not survive. The write-quality-variance confidence intervals come
from a percentile bootstrap over n=4 and are roughly half the width of the correct
t-intervals — though C-vs-cold shows complete rank separation and survives an exact
Mann-Whitney at p=0.029, so the direction holds independently.

**The B grader is asymmetric.** On conflict items `run.py` grades only the conflict flag
and discards the action; on non-conflict items it grades both. Three of fifteen headline
cores are conflict items.

**Thread 5 reports a bootstrap statistic as a p-value.** `experiments/thread5/findings.md`
prints `p=1.000`; the underlying field is `p_a_better`, the bootstrap probability that A
exceeds B, so 1.000 means "better in every resample" — the opposite of what a p-value of
1.0 would mean. Its confidence intervals are sound. Its LLM-judge scores rest on ground
truth generated by a small local model, so the 98%-wrong figure may measure the reference
answers rather than encoding loss. The findings that depend on those judge numbers are
struck in place rather than deleted.

**write-quality-variance is n=4** on one task in one repository, with an acknowledged
distiller-model confound. The cost effect also tracks encoding length at r=0.94 and turn
count at r=0.99, write cost is excluded from the comparison, and the "cold" baseline
isn't truly cold — the task's issue text contains the fix. Treat it as a pilot.

**Some of this is a rediscovery.** Finding 3 restates *decontextualization*, a known
problem with existing treatment (Choi et al., TACL 2021; Gunjal & Durrett, 2024).
Findings 1 and 2 overlap with arXiv:2605.11325, which uses similar construct names; it
decouples retrieval from generation and measures retrieval accuracy rather than answer
quality, so the axis differs, but read it before assuming novelty. These citations were
added at publication time — the wiki pages underneath still read as discovery.

---

## What's deliberately not here

**Thread 5's raw data.** The per-item files are verbatim transcripts of real Claude Code
sessions and contain private source code and third-party email addresses. Only the
aggregate statistics and the scripts that produced them are published. The pipeline is
complete enough to re-run against your own session history, though you'll need to write
your own session indexer.

**Generated corpora** (~700 MB) and two large model-training trees (~97 GB). Corpora
regenerate from seed. Many wiki links point into these — those links are dead by design.

**The T_A1b and factored-operator experiment trees**, referenced from several wiki pages
and not shipped for the same reason.

---

## A note on how this was written

The wiki was produced by a small team of Claude agents working under persistent personas,
each owning an area — research, prose, benchmarking. That's why pages are signed with
names and the register shifts between sections. The names are not people. It's mentioned
here only because the wiki reads oddly if you don't know.

---

## Licence

Code (`masq/`, `experiments/`, `wiki/lint/lint.py`): MIT — see [LICENSE](LICENSE).
Written content (`wiki/`, prose in `experiments/`): CC BY 4.0 — see
[LICENSE-CONTENT](LICENSE-CONTENT).

Paper notes under `wiki/source/` summarise third-party work and quote from it. Those
quotations remain the property of their authors; the notes and commentary are CC BY 4.0.

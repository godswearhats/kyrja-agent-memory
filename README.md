# Kyrja — an agent-memory research archive

Four months of research into memory for LLM agents (April–July 2026), published as-is
because the work stopped and the alternative was losing it.

This is not a library, a product, or a paper. It is a working research wiki plus the
code and data behind the experiments that fed it. Some of the findings are solid, some
are broken, and the README tries to be clear about which is which.

**Status: parked.** Nothing here is maintained. Issues and PRs will probably go
unanswered. Take whatever is useful.

---

## Start here

| If you want | Read |
|---|---|
| Where the work had got to when it stopped | [`wiki/NOW.md`](wiki/NOW.md) |
| The full page catalogue | [`wiki/index.md`](wiki/index.md) |
| A narrative of how the thinking changed | [`wiki/log.md`](wiki/log.md) |
| How the wiki is structured, and why | [`wiki/SCHEMA.md`](wiki/SCHEMA.md) |
| Reading notes on 86 papers | [`wiki/source/`](wiki/source/) |

---

## What's here

```
wiki/            269 markdown pages — concepts, hypotheses, experiments, decisions,
                 paper notes, open questions. Obsidian-compatible, plain markdown.
masq/            MASQ: a synthetic benchmark for scope disambiguation in agent memory.
                 Generator, evaluation harness, and two pre-registered pilot studies.
experiments/     Thread 5 (retrieval-tier ablation), write-quality-variance
                 (encoding-format cost study), and probe corpora.
```

### The wiki

269 pages under a schema that separates what was **measured** from what was **asserted**
from what was **speculated**, with a lint tool that enforced the distinction. Page types:
86 `source/` (paper notes), 41 `concept/`, 32 `open-question/`, 29 `experiment/`,
24 `hypothesis/`, 19 `incumbent/` (memory-system vendor analyses), 18 `decision/`.

Hypothesis pages carry an explicit status — PROPOSED, SUPPORTED, REJECTED — and several
of them are REJECTED by their own experiments. That's the intended use.

### MASQ

A synthetic benchmark that constructs the failure mode directly. An agent memory corpus
contains several **confusable sibling scopes** — `checkout-web`, `checkout-api`,
`checkout-mobile` — each carrying its own independent chain of supersessions (a value set,
then revised, then revised again), buried in unrelated chatter. The question asks about
one scope. Every sibling is topically identical and equally retrievable.

Grading is factorial and fully deterministic — no LLM judge:

- **A** — did the system reconstruct the correct supersession chain?
- **B** — did the agent take the right action, and flag the conflict when there was one?

The two do not track each other, and the original work was emphatic about this: A is a
reconstruction-detail score, B is the decision the benchmark actually cares about. At
equal A, scope-filter scores 15/15 on B and vector scores 6/15. Don't use A as a proxy
for B, and don't compare an A number in one section against a B number in another.

Arms implement a single contract, `arm(family, corpus_dir) -> context_string`, with the
reader, prompts, parsing, and grading frozen identical across all of them. Implemented
arms: paste-everything, last-write-wins, perfect-retrieval (oracle ceiling), vector RAG,
BM25, scope-filter (oracle), and Supermemory.

Run the generator:

```bash
cd masq/generator
python3 sweep.py --seeds 7717 --domains rate-limit --sizes 6k --out /tmp/masq
python3 verify.py /tmp/masq/rate-limit/s7717/6k/family-rate-limit.json
```

`verify.py` checks sixteen construction invariants — value collision across siblings,
kernel isolation, marker discipline, ground-truth agreement. If a generated world is
degenerate, it fails there rather than silently producing an easy benchmark.
A pre-generated sample corpus is in `masq/generator/sample-corpus/`.

`masq/gate1/` and `masq/bareset-probe/` are the two pre-registered pilots that had to
pass before the benchmark design was frozen — each states its thresholds in advance,
then scores itself against them.

---

## What was found

**1. Exclusion is the bottleneck, not recall.**
On MASQ, every similarity-ranking arm lands at or below just pasting the whole corpus
into context (B-pass: vector 6/15, BM25 8/15, paste 9/15), while a structured scope filter —
literally `WHERE scope = target` — ties the oracle ceiling at 15/15, with zero paired
losses (p ≤ 0.03, n=15). The retrievers *find* the target chain, at roughly 2.8 of 3
steps. What they cannot do is drop the five-odd sibling chains that are equally relevant
by every similarity measure. `ORDER BY similarity LIMIT k` is the wrong primitive for
this task; it needs an index, not a ranking.

**2. Difficulty comes from confusability, not context length.**
Paste scores 9/15 at every corpus size from 25k to 400k tokens. Growing the haystack
changes nothing. This is worth knowing because it cuts against the usual framing where
long-context ability is the thing being measured.

**3. Extraction-based memory destroys scope at write time.**
Running Supermemory as a system under test gave A=31%, *below* the 69% chain-reconstruction
plateau that paste, vector, and BM25 all share (A scores here, not the B-pass counts above). A census of the full store (3,537 extracted memories)
found 23 memories carrying the kernel value and **zero** carrying a scope binding. The
mechanism is discourse-level: the scope gets named in one sentence and the value in
another, extraction atomises sentence by sentence, and the binding between them is lost.
The competing explanation — that consolidation smears scopes together as the store grows
— was tested and **rejected**: it fails at store size zero.

So both dominant off-the-shelf paradigms lose scope, one at read time by ranking and one
at write time by extraction.

**4. Structured slots beat prose for memory encoding, which was the opposite of the
prediction.** Structured slot encodings completed a coding task at $0.142 against $0.295
cold (no memory) and $0.247 for a prose briefing. Both pre-registered hypotheses were
rejected, one of them in reverse. See the caveat below — this one is very small.

---

## Known problems with this data

Read this section before citing anything.

**MASQ constructs its own difficulty.** The confusability is synthetic and deliberate,
and the scope filter is an **oracle** — it is handed the answer's scope. These results
demonstrate a failure mode cleanly. They do not validate a production architecture, and
the gap between "a filter would fix this" and "here is how you'd know what to filter on"
is the entire unsolved problem. This caveat was load-bearing in the original work and is
repeated on the wiki pages themselves.

**Thread 5 reports a bootstrap statistic as a p-value.** `experiments/thread5/findings.md`
prints `p=1.000` for its tier comparisons. The underlying field is `p_a_better` — the
bootstrap probability that A exceeds B, where 1.000 means "always better", the *opposite*
of what a p-value of 1.0 would mean. The confidence intervals in that file are fine. The
p-column is mislabelled throughout. The raw file has been left as written, with a
correction note added at the top.

**Thread 5's judge scores may measure the wrong thing.** The LLM-as-judge numbers are
brutal — 0.1% correct with no memory, rising only to 1.1% with hybrid retrieval. But the
ground truth was generated by a small local model (gemma3:12b) and graded by Haiku. A
99.6%-wrong result at T0 is more consistent with bad ground truth than with a real
ceiling on encoding quality. Treat the F1 numbers as the finding and the judge numbers
as unresolved.

**write-quality-variance is n=4.** Four runs per condition, one task, one repository,
~$10 of total compute. It also carries an acknowledged distiller-model confound: the
winning variant was distilled by a newer model than the control it beat. This is a
suggestive pilot, not a result. Its own limitations section says as much.

**The literature moved, and some of this is a rediscovery.** Finding 3 is a rediscovery
of *decontextualization* — a known problem in NLP with existing treatment (Choi et al.,
TACL 2021; Gunjal & Durrett, 2024). Findings 1 and 2 overlap substantially with
arXiv:2605.11325, which uses similar construct names. That paper decouples retrieval from
generation and measures retrieval accuracy rather than answer quality, so the axis is not
identical — but anyone building on this should read it first rather than assuming novelty.

---

## What's deliberately not here

**Thread 5's raw data.** The per-item files are verbatim transcripts of real Claude Code
sessions and contain private source code and third-party email addresses. Only the
aggregate statistics and the scripts that produced them are published. The pipeline is
complete enough to re-run against your own session history.

**Generated MASQ corpora** (~700 MB) and two large model-training experiment trees
(~97 GB). The corpora regenerate deterministically from a seed using the bundled atom
bank, so shipping them would be storage for no gain.

**Anything requiring API credentials.** The Supermemory arm needs a key, supplied via the
`SUPERMEMORY_API_KEY` environment variable. The other arms need Ollama for embeddings, or
nothing at all.

---

## A note on how this was written

The wiki was produced by a small team of Claude agents working under persistent
personas, each owning an area — research, prose, benchmarking. That's why pages are
signed with names, and why the register shifts between sections. It is not a stylistic
affectation and the names are not people. It's mentioned here only because the wiki
reads oddly if you don't know.

---

## Licence

Code (`masq/`, `experiments/`): MIT — see [LICENSE](LICENSE).
Wiki and written content (`wiki/`, prose in `experiments/`): CC BY 4.0 — see
[LICENSE-CONTENT](LICENSE-CONTENT).

Paper notes under `wiki/source/` summarise third-party work and quote from it. Those
quotations remain the property of their authors; the notes and commentary are CC BY 4.0.

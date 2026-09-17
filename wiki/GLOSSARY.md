---
tags:
  - exclude-from-graph
---
# Glossary

*Added at publication (2026-09-17). The wiki was written for its authors and assumes
vocabulary that is never defined anywhere in it. This page is the missing key.*

## Read this first — overloaded symbols

Several short codes mean different things in different parts of the archive, and both
readings usually resolve to *something*, so you can be confused without noticing. This
is the single biggest hazard for an outside reader.

| Symbol | In Kerros / caddy pages | In MASQ pages | Elsewhere |
|---|---|---|---|
| `R1`, `R2` | caddy **read** operations | — | the Memory-R1 / Memory-R2 **papers** |
| `P1`–`P3` | **substrate paradigms** (state / module / simulator) | `P1`–`P8` = **chain patterns** in the generator | — |
| `C1`–`C4` | `C1` = silent-engram anchor; bare `C` = consolidation op | **factorial cells** of the abandoned v1 design | — |
| `S3`, `S4` | caddy **store** operations | — | Amazon **S3**; the **S4** state-space model |
| `Gate 1`, `Gate 2` | **integration gates** (Kerros research programme) | **pre-build gates** (discriminability, bare-set) | — |
| `K2` | caddy **consolidator** operation | `K ∈ {10,20,40,80}` = retrieval **top-k**, or sibling-**bed size** | — |
| `T1`–`T4` | **maturity tiers** (T1 proven at LLM scale → T4 speculative) | — | Thread 5 **retrieval tiers**; storage tiers (hot/warm/cold) |
| `ACL` | access-control list | — | the **ACL** conference |
| `SR` | successor representation | — | a MemoryArena metric |
| `A` / `B` | — | the two **grading layers** (chain reconstruction / decision) | `A`–`D` = encoding **variants** in write-quality-variance |

## Project and programme names

| Term | Meaning |
|---|---|
| **Kyrja** | The umbrella name for this whole body of work. Not an acronym and not expanded anywhere — it was an arbitrary project name. |
| **Kerros** | The substrate-memory research programme. Finnish for *layer / stratum* — memory at the substrate layer. Parked. Defined in [concept/kerros.md](./concept/kerros.md). |
| **MASQ** | The synthetic scope-disambiguation benchmark. **Never expanded anywhere in the archive**; treat it as a bare name. |
| **MTP** | Appears ~49 times as the name of the intended first shippable product. **Never expanded anywhere in the archive.** From context it is the minimum/first testable product. |
| **caddy** | Design vocabulary, not a product: a co-trained memory module with its own state and learned policies. Named for the golf caddy — a separately-employed expert who carries the player's model of the course. [concept/caddy.md](./concept/caddy.md) |
| **the wedge** | The deliberately narrow initial product scope intended to prove the architecture before the full stack is built. |
| **Thread 1 … Thread 5** | Numbered parallel research threads from the April 2026 period. Thread 5 is the retrieval-tier ablation in [`experiments/thread5/`](../experiments/thread5/). |

## Core concepts used without introduction

| Term | Meaning |
|---|---|
| **scope** | The context a memory belongs to — a service, team, cluster, repo. MASQ's whole subject: distinguishing `checkout-web` from `checkout-api`. |
| **confusable siblings** | Scopes that are topically near-identical and equally plausible answers to a query. The difficulty MASQ constructs. |
| **supersession chain** | A sequence where a value is set, then revised, then revised again. The thing a memory system must reconstruct. |
| **collision** | Two scopes ending up with the same final value, so the value alone can't identify the scope. |
| **near-miss** | A decoy entity that resembles the target but isn't in any scope. |
| **kernel** | The small set of sessions carrying the answer, as opposed to the surrounding chatter. |
| **chatter / bed** | Filler sessions. The haystack. |
| **arm** | One memory strategy under test, implementing `arm(family, corpus_dir) -> context_string`. |
| **ceiling / oracle** | An arm given ground truth, establishing what a perfect system would score. |
| **paste / lww** | Baselines: paste the whole corpus; or take the latest write regardless of scope. |
| **B-pass** | The headline metric: correct action *and* correct conflict flag, graded closed-form. |
| **consolidation channel** | The hypothesised mechanism moving information from retrieval-style memory into model weights. Kerros's central object. |
| **substrate** | Memory the model thinks *with* (in its computation), as opposed to a database it thinks *about*. |
| **integration gate** | The test of whether a memory component can be bolted onto a frozen model or must be co-trained. |
| **MBP** | MERLIN's memory-based predictor — the auxiliary world-model loss that shapes its memory writes. Dropped by later work; whether that mattered is an open question here. |
| **admission control** | Deciding what to store at all, rather than storing everything and filtering at read time. |

## Epistemic tags

The wiki marks every substantive claim with its evidential status. This is load-bearing,
not decoration, and `wiki/lint/lint.py` enforces it.

| Tag | Meaning |
|---|---|
| `[MEASURED]` | We ran it. Must carry a construct-validity note saying what the measurement does and does not support. |
| `[ASSERTED]` | Claimed from reasoning or external sources, not measured here. |
| `[SPECULATED]` | A hypothesis we find plausible and have not tested. |
| `[CONTESTED]` | Sources disagree, or we disagree with a source. |

## Machine-learning acronyms

Standard in the literature, unexplained here. **RL**: reinforcement learning ·
**RLHF** / **RLVR**: RL from human feedback / with verifiable rewards ·
**PPO**, **GRPO**, **DPO**: policy-optimisation algorithms · **SFT**: supervised
fine-tuning · **LoRA**: low-rank adapter fine-tuning · **MoE**: mixture of experts ·
**SSM**: state-space model · **JEPA**: joint-embedding predictive architecture ·
**EMA**: exponential moving average · **BYOL**, **VICReg**: self-supervised learning
methods · **NTM** / **DNC**: neural Turing machine / differentiable neural computer ·
**ROME**, **MEMIT**: weight-editing methods · **HNSW**: the standard approximate
nearest-neighbour index · **BM25**: the standard lexical ranking function ·
**RRF**: reciprocal rank fusion · **IDF**: inverse document frequency ·
**RAG**: retrieval-augmented generation · **LWW**: last-write-wins.

## Known gaps

Honest notes about things this glossary can't fix:

- **`F1`–`F12` and `Scenario A`–`F`** (scale-model factors and bracketing scenarios) are
  defined in a document that is not in this archive. They are unresolvable here.
- **`R5`** is discussed as a declined option but never appears in the R-table, which
  lists only R1–R4.
- **`T2` and `T3`** of the maturity ladder are never defined, only T1 and T4.
- **`event-mode` / `arc-mode`** (used in [`experiments/probes/`](../experiments/probes/))
  are named only in an archived log entry.
- The only page defining the MASQ `C1`–`C4` cells is marked SUPERSEDED, and those cells
  do not exist in the shipped benchmark.

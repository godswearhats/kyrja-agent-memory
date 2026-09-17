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
| `T1`–`T4` | **implementation-feasibility tiers** for caddy operations: T1 proven at LLM scale → T4 speculative | — | Thread 5 **retrieval tiers** (T0 none / T1 BM25 / T2 semantic / T3 hybrid); storage tiers (hot/warm/cold) |
| `tier 1`–`tier 4` | **retrieval-capability ladder** — a *different* scheme from `T1`–`T4` above. tier 2 = semantic; tier 3 = analogical/structural. Whether tier 3 is distinct from good tier 2 is open, after a bag-of-words baseline decoded the structure at 82%. | — | — |
| `ACL` | access-control list | — | the **ACL** conference |
| `SR` | successor representation | — | a MemoryArena metric |
| `A` / `B` | — | the two **grading layers** (chain reconstruction / decision) | `A`–`D` = encoding **variants** in write-quality-variance |

## Project and programme names

| Term | Meaning |
|---|---|
| **Kyrja** | Old Norse for **"chooser"** — the agent noun from the ablaut root of `kjósa`, "to choose". It is the second element of `valkyrja`: `valr` (the slain) + `-kyrja` (the chooser), which Cleasby & Vigfusson gloss as "the chooser of the slain". Not to be confused with the modern Icelandic verb *kyrja*, "to sing or chant", which is a separate development. The umbrella name for this body of work — apt, given that the research's own conclusion was that [admission control](./concept/admission-control.md), deciding what to keep at all, is the only layer that acts on the cause rather than the symptoms. |
| **Kerros** | The substrate-memory research programme. Finnish for *layer / stratum* — memory at the substrate layer. Parked. Defined in [concept/kerros.md](./concept/kerros.md). |
| **MASQ** | **Multi-Agent Session Queries.** The scope-disambiguation benchmark. The name and the core insight — that shared vocabulary across parallel project contexts defeats similarity ranking — carry over from an earlier benchmark of the same name built on simulated multi-agent sessions; that earlier version is not in this archive. What ships here is the v2 redesign: synthetic, invariant-checked, closed-form graded. See [`masq/README.md`](../masq/README.md). |
| **MTP** | **Minimum Testable Product** — the first thing intended to be built, for self-testing on the authors' own work. The expansion is not stated anywhere in this archive; it comes from the wider project notes. |
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
| **MBP** | **Memory-Based Predictor** — an auxiliary world-model loss applied to memory representations, from MERLIN. Later work inherited MERLIN's read head but dropped the MBP; whether that omission mattered is an open question here. |
| **admission control** | Deciding what to store at all, rather than storing everything and filtering at read time. |

## Codes that index another page

| Code | Resolves to |
|---|---|
| `M01`–`M17` | Rows of [concept/mechanism-gap-matrix.md](./concept/mechanism-gap-matrix.md) — biological memory mechanisms scored against what current architectures cover. That page is the index. |
| `H23`–`H46` | Hypothesis pages in [hypothesis/](./hypothesis/), one file each. |
| `E1`, `E2`, … | Event labels *local to a single probe file* — "E1 (discovery, present)". A per-file convention, redefined in each scenario, not a global scheme. |
| `H01`–`H22` | Hypotheses numbered before the wiki existed. Most were shelved or folded into later pages rather than carried over, so they have no page here. Subjects: H01 institutional-memory gap · H02 market window · H03 governance table-stakes · H04 proxy-beats-tools · H05 tools-without-training · H06 dogfood · H07 proxy standalone value · H08 filter-first · H09 scaling crossover · H10 distributed-systems mapping · H11 eventual consistency · H12 z-curve (deferred) · H13 intent-outcome encoding · H14 encoding-too-lossy · H15 RL encoding · H16 retrieval bottleneck · H17 ceiling effect · H18 routing matters · H19 forgetting scores · H20 consolidation ordering · H21 conflict rate · H22 consolidation as RL target. Some were renumbered into the H23+ range — H10 and H11 became [H31](./hypothesis/H31-distributed-systems-mapping.md) and [H32](./hypothesis/H32-eventual-consistency.md). |
| `F1`–`F13` | Parameters of the memory-volume scale model — table below. |
| `Scenario A`–`F` | The six deployment scenarios bracketing that model — table below. |

## Borrowed from cognitive science and the ML literature

Each has a source page under [source/](./source/) with the full citation.

| Term | Meaning |
|---|---|
| **CLS** | **Complementary Learning Systems** — the hippocampus/neocortex dual-store account of memory. The framework behind most of the consolidation reasoning here. |
| **TCM** | **Temporal Context Model** (Howard & Kahana 2002) — retrieval cued by a slowly drifting context vector. |
| **SPW-R** | **Sharp wave-ripple** (Buzsáki 2015) — hippocampal replay events, the biological anchor for replay-driven consolidation. |
| **EM** | **Episodic memory.** Also `EM-LLM` (Fountas et al. 2024), which segments a stream into events by surprise. |
| **RC** | **Reservoir computing** — a fixed random recurrent network with only the readout trained. Investigated as a caddy substrate and closed as empirically dead. |
| **ICAE** | **In-context Autoencoder** (Ge et al. 2024) — context compression into memory slots via a frozen decoder. |

## The scale model — factors and scenarios

A stock-and-flow model of memory accumulation over five years, behind the volume
argument. Inflow is `users × adoption × sessions/day × orchestration_depth ×
memories/session × tool-chain amplifier`; outflow is first-order consolidation. The model
code is not in this archive; these are its parameters and published results.

| Factor | Parameter | Meaning | Sensitivity |
|---|---|---|---|
| `F1` | tool-chain persistence rate | probability a session persists tool traces as memory | high |
| `F2` | orchestration depth | agent sessions spawned per user-initiated task | high |
| `F3` | autonomous agents per employee | background agents running continuously | high |
| `F4` | sessions per user-day | active sessions per active user per working day | medium |
| `F5` | memories per session | persistable chunks created per session, after extraction | medium |
| `F6` | initial adoption rate | fraction of employees using agents in year 0 | medium |
| `F7` | adoption growth rate | annual logistic growth toward saturation | medium |
| `F8` | consolidation rate | fraction of stock removed or merged per year | low |
| `F9` | company size | total employees modelled | low |
| `F10` | software-work fraction | fraction of employees doing agent-using work | low |
| `F11` | deployment-model isolation factor | multiplier for per-deployment effects | structural |
| `F12` | retention floor | minimum years memories must be retained for compliance | structural |
| `F13` | embedding dimension | vector dimension of the embedding model | structural |

| Scenario | Y5 vectors | Peak QPS | Walls crossed |
|---|---|---|---|
| **A** SWE-200 conservative | 55M | 33 | 3 |
| **B** SWE-200 moderate | 166M | 108 | 4 |
| **C** SWE-200 aggressive | 997M | 551 | 5 |
| **D** Enterprise-5000 conservative | 65M | 49 | 3 |
| **E** Enterprise-5000 aggressive | 2.7B | 1,719 | 6 |
| **F** Frontier-1000 (2030) | 8.5B | 4,032 | 6 |

Four factors were audited against outside evidence. `F1` was **demoted** from foundation
to amplifier when none of six audited memory systems turned out to persist tool traces as
first-class memory.

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

- **`R5`** — *read-as-write reconsolidation at zero latency.* Discussed as a declined
  option and absent from the R-table, which lists only R1–R4. It was demoted from a
  load-bearing commitment to a biological constraint that the architecture need not copy.
- **`T2` and `T3`** of the feasibility ladder are never spelled out — only the endpoints
  are stated anywhere. Read them as intermediate confidence between proven and speculative.
- **`event-mode` / `arc-mode`** (used in [`experiments/probes/`](../experiments/probes/))
  are the two probe corpus formats: single-event candidates, and multi-event sequences.
  Arc-mode was the primary falsifier of that probe. The rename that created both terms is
  recorded only in an archived log entry.
- The only page defining the MASQ `C1`–`C4` cells is marked SUPERSEDED, and those cells
  do not exist in the shipped benchmark.

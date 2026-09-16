---
type: experiment
name: "Factored-operator beachhead — the substantive run: existence (fan-open) and efficiency (incremental-write) gates"
status: "Gate 1 (existence) cleared at k=64/128, k=256 PARKED (under-data); Gate 2 (efficiency) OPEN — embedding-only write fails; low-rank decider PARKED 2026-05-30 (reversible — superseded by the strategic reframe in open-question/incremental-integration-cost)"
last_ingested: 2026-05-30
program: kerros
sources: [./spec.md, ./phase2-results.md, ./phase1-results.md, ../../concept/integration-gate.md, ../../concept/consolidation-channel.md, ../../source/xu-2026-agentic-memo.md]
epistemic_tags: [measured]
tags: [kerros, beachhead, composition, fan-open, memory-vs-training, incremental-write, consolidation, negative-result]
---

> **Program: [Kerros](../../concept/kerros.md).** This is the substantive run the [Phase-2 precondition page](./phase2-results.md) deferred — the integrated arm now learns the task, so we can finally test the bet. It splits into two gates (a reframe AJ forced mid-session; see [integration-gate § existence vs efficiency](../../concept/integration-gate.md)): **Gate 1 = existence** (can weights *represent* a composition the frozen bolt-on can't — the fan-open), **Gate 2 = efficiency** (can weights *acquire* it cheaply enough to be *memory* rather than a retrain). Gate 1 is the [Xu Thm 1](../../source/xu-2026-agentic-memo.md) instantiation; Gate 2 is the acquisition-cost question Xu's sample-complexity theorem does not reach. Siblings: [spec](./spec.md), [phase1-results](./phase1-results.md), [phase2-results](./phase2-results.md).

## Hypotheses tested

- **Gate 1 (existence / scaling separation):** the integrated arm (full-FT Qwen2.5-0.5B) generalises to unseen compositions where the frozen bolt-on (offline distill + CoT, no inference-time exec) cannot, and the gap *fans open* as symbol count `k` grows. Instantiates [Xu, Dai & Zhang 2026 Thm 1](../../source/xu-2026-agentic-memo.md).
- **Gate 2 (efficiency / memory-vs-training):** a model already competent at the operator can absorb *new* symbols via a **cheap, local, few-shot weight write** and still generalise — the operational definition of a memory function. See the new open question [incremental-integration-cost](../../open-question/incremental-integration-cost.md).

## Method

All on the locked [Phase-1 generator](./phase1-results.md) (rank-`m=4` factored operator, `C=5` quantile-bin labels, chance 0.20, seed 0). Code in [the experiment dir](../../../experiments/factored-operator-beachhead/): [phase2_fullft.py](../../../experiments/factored-operator-beachhead/phase2_fullft.py) (integrated arm, resumable), [phase2_bolton.py](../../../experiments/factored-operator-beachhead/phase2_bolton.py) (bolt-on, `claude -p` subscription backend), [phase2_incremental.py](../../../experiments/factored-operator-beachhead/phase2_incremental.py) (Gate-2 write).

**Gate 1.** Integrated arm: full fine-tune at `k ∈ {64,128,256}`, held-out-only scoring (constrained logit over the 5 label tokens). Bolt-on: Sonnet reader, **low** eval-effort (a fairness caveat — see Limitations), scored on a held-out cell sample. The modular-control competence certificate (bolt-on must *win* there) was established earlier (Sonnet: notes "Label = (a × b) mod 5", acc 1.000).

**Gate 2 (the new method this run adds).** Take the competent `k=128` checkpoint (held-out 0.500) and add 4 new left + 4 new right symbols via an **append-only task extension** ([phase2_lib.extend_factored_operator](../../../experiments/factored-operator-beachhead/phase2_lib.py)): new symbols are centred through the *base* population mean and labelled against the *frozen* base quantile edges, so base targets are provably unchanged (asserted in-code; retention therefore guaranteed). The **write**: freeze the entire transformer + all old embedding rows, train *only* the 8 new embedding rows (896-d each), grad-masked, weight-decay 0 (so frozen rows can't drift). Sweep the write budget `N_new ∈ {16,64,256,728}`; test on held-out unseen pairs of the new symbols. lr 1e-2, 200 epochs (writes are tiny → minutes).

## Results

`[MEASURED]` (k as noted, seed 0; integrated from host GPU runs, bolt-on from `claude -p`, Gate-2 from [phase2_incremental_results/results.json](../../../experiments/factored-operator-beachhead/phase2_incremental_results/results.json))

### Gate 1 — the fan opens, then the bolt-on floors

| `k` | integrated (held-out) | Sonnet bolt-on (low effort) | gap | pool sampled (integrated) |
|---|---|---|---|---|
| 64  | **0.523** | 0.267 | 0.256 | ~98% (N=3400) |
| 128 | **0.500** | 0.167 | 0.333 | ~57% (N=8000) |
| 256 | **0.277** ⚠️ | 0.167 | 0.110 | ~29% (N=16000) |

The gap widens 0.256→0.333 (k=64→128) as the bolt-on degrades toward chance (0.20) while the integrated arm holds ~0.50 — **Gate 1 cleared at k=64/128.** The bolt-on floors at chance by k=128 (it cannot compose at all), so beyond that the gap is bounded by the integrated arm's own ceiling, not by further bolt-on divergence ("fans open, then saturates").

**k=256 is PARKED, not a ceiling.** train→1.000 (loss 0.009) but held-out only 0.277 — a large train/test gap = **overfitting from under-data**: at N=16000 the integrated arm saw only ~29% of the pool vs ~57%/98% at k=128/64. Taken at face value the gap *shrinks* (0.110), which would break the fan-open — so the point is invalid until re-run at higher `N` (≈32000 to match k=128 density) or as an `N`-sweep. Diagnosed mid-session; re-run deferred (see Gate 2 — it became the priority).

### Gate 2 — the cheapest write FAILS to generalise

Base ceiling 0.500, chance 0.20. Pass bar (pre-registered): new held-out ≥ 0.40 at `N_new ≤ 256`.

| `N_new` | min coverage / new symbol | new held-out | train loss | retention |
|---|---|---|---|---|
| 16  | 1 | 0.257 | 0.001 | 0.500 |
| 64  | 6 | 0.217 | 0.003 | 0.500 |
| 256 | 6 | 0.317 | 0.012 | 0.500 |
| 728 | 6 | **0.347** | 0.535 | 0.500 |

Best new held-out = **0.347**, and only at `N_new=728` (the *entire* new-pair pool — not few-shot). The genuinely few-shot budgets sat at chance (`N_new=64` → 0.217 vs chance 0.20). **NO PASS.** Retention stayed *exactly* 0.500 throughout — the zero-interference half of "memory-like" holds perfectly by construction (frozen base + frozen old rows).

### Construct-validity note

**Gate 1 metric** = held-out accuracy on cell-pairs never trained, scored by constrained logit (integrated) or parsed CoT answer (bolt-on) — measures generalisation to unseen compositions, which is what "the bolt-on can't compose" requires. Caveat: the bolt-on ran at **low eval-effort** (high effort was computationally intractable — minutes/question, mostly timing out). Low effort plausibly *under*-powers the bolt-on, which biases toward our hypothesis; an earlier 6-cell high-effort hint (~0.50 at k=64) suggests the k=64 gap may be partly low-effort artifact. The fan-open *trend* (bolt-on → chance by k=128) is robust to this, but the absolute k=64 gap is soft.

**Gate 2 metric** = new-symbol held-out accuracy after the write. The decisive diagnostic is the **train loss column**: at `N_new=64`, coverage was 6 observations per new symbol — *more* than the `m+1=5` constraints needed to pin a rank-4 vector, so the data was information-sufficient — yet loss→0.003 (the write fit those examples perfectly) while held-out stayed at chance. So the write did not fail for lack of data; it is **underdetermined in parameter space**: an 896-dimensional embedding row, of which only ~4 directions matter, has ~892 free directions to interpolate the training constraints without recovering the true factor vector. Retention being *exactly* 0.500 (not approximately) confirms the freeze is real — the failure is the write's generalisation, not interference or a loading bug.

## Limitations

- **k=256 (Gate 1) is under-data and parked** — not a usable fan-open point until re-run at higher `N`. The clean fan-open is k=64→128 only (two points).
- **Bolt-on fairness (Gate 1)** — low eval-effort only; the fair-and-tractable bolt-on protocol is itself unresolved (medium-effort probe landed 0.312 ≈ low 0.267 at k=64, suggesting low isn't grossly unfair, but high was intractable).
- **Gate 2 tests one write mechanism** (embedding-only) at one scale (0.5B base, k=128). Its failure is *necessary* evidence but not yet decisive: the escalation ladder (low-rank-constrained write → LoRA → full-FT-continued) is unrun. The diagnosis (underdetermination) predicts a low-rank-constrained write should generalise from few examples — that is the pending decider.
- **Sample-efficiency of the integrated arm proper (budget-to-ceiling vs `N`) is still unrun** — we measured high-`N` ceilings, not the sub-quadratic acquisition curve that the "cheap to learn" claim actually rests on.

## Raw artifacts

- Pre-registration: [spec.md](./spec.md) (the efficiency gate is an addition recorded there).
- Precondition (QLoRA→full-FT pivot): [phase2-results.md](./phase2-results.md).
- Code: [phase2_fullft.py](../../../experiments/factored-operator-beachhead/phase2_fullft.py), [phase2_bolton.py](../../../experiments/factored-operator-beachhead/phase2_bolton.py), [phase2_incremental.py](../../../experiments/factored-operator-beachhead/phase2_incremental.py), [phase2_lib.py](../../../experiments/factored-operator-beachhead/phase2_lib.py) (`extend_factored_operator`, `new_pair_split`, `sample_new_observed`).
- Results: [phase2_incremental_results/results.json](../../../experiments/factored-operator-beachhead/phase2_incremental_results/results.json); integrated checkpoints `phase2_fullft_k128_v2.pt` (0.500), `phase2_fullft_k256.pt` (0.277).

## Related

- [integration-gate](../../concept/integration-gate.md) — the existence-vs-efficiency refinement this run forced; Gate 1 = its scaling separation, Gate 2 = the cost the gate didn't price.
- [consolidation-channel](../../concept/consolidation-channel.md) — Gate 2 is the write-side (consolidation) cost experiment; embedding-only is a new shallowest rung below LoRA on its substrate-depth ladder.
- [incremental-integration-cost](../../open-question/incremental-integration-cost.md) — the open question Gate 2 opens; the low-rank decider is its next evidence.
- [Xu, Dai & Zhang 2026](../../source/xu-2026-agentic-memo.md) — Thm 1 (the sample-complexity separation Gate 1 tests); it bounds demos-vs-parameters, not the training/incremental write cost Gate 2 tests.
- **Next:** ~~projected low-rank write `r`-sweep at fixed `N_new=64` — the Gate-2 decider~~ **PARKED 2026-05-30 (reversible).** A strategy session reframed the question: the toy decider has low discriminating power (rank `m=4` is built in → semi-rigged) and weights may be the wrong substrate to test cheap writes on. The write question widened to the cheap-write-vs-compositional-read trade-off — see [incremental-integration-cost § 2026-05-30 update](../../open-question/incremental-integration-cost.md) and the [wedge-sizing](../../open-question/thinks-with-wedge-sizing.md) scoping thread. No experiment currently queued.

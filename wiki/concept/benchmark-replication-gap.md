---
type: concept
name: Benchmark Replication Gap
status: timeless
last_ingested: 2026-06-08
sources: [../source/memory-surveys-2026.md]
epistemic_tags: [measured, asserted]
tags: [scale-thesis, recall-leg, evaluation]
---

## Definition

The **benchmark replication gap** is the spread between vendor-published scores on agentic-memory benchmarks and independent third-party re-runs of the same systems on the same benchmarks. At conversation scale today — well below any scale-model threshold — incumbents replicate at 49-65% on benchmarks where their own self-reports cluster at 85-95%.

## Role in Kyrja thesis

This is the **today-anchor for the recall leg** of the cascading-failures thesis. The cascading-failures product (`[ASSERTED]`) predicts 30-50% effective recall at billion scale. The benchmark replication gap shows incumbents are already at 49-65% on third-party-replicated evaluations *at <50K-doc, 115k-token-history scale* — before any volume threshold bites. The compounded-failure prediction is consistent with these small-scale numbers projecting *downward* with stock growth, not upward.

The replication gap is distinct from the [billion-scale-benchmark-gap](../open-question/billion-scale-benchmark-gap.md): that page is about the *missing* benchmark at the scale our thesis predicts breakage; this page is about the *existing* benchmarks at small scale and the methodology chaos they reveal.

> **Sourcing correction (2026-06-08, Nils):** the numeric figures below were previously attributed to the [Du survey (2603.07670)](../source/du-2026-autonomous-memory-survey.md); a verbatim sweep found **they are not in that survey** (zero hits for Mem0/Zep/93/49/replicat). They trace to the benchmark-ceilings probe + vendor blogs and need primary re-sourcing before any *load-bearing numeric* citation. **The concept does not depend on the specific numbers** — see "What the claim really is" below.

## The headline numbers `[un-resourced — illustrative, not load-bearing]`

- **Mem0 self-published ~93% on LongMemEval; independent third-party re-run ~49%.** A ~44-point methodology gap. *Construct-validity:* both numbers are on LongMemEval-S; the gap is in evaluation methodology (which subset of questions, what oracle baseline, how the system is wired), not in benchmark identity. Primary source pending re-verification.
- **Zep** independent re-run on LongMemEval: ~**63.8%**. Primary pending.
- **OpenAI ChatGPT memory** independent re-run on LongMemEval: ~**57.73%**. Primary pending.
- **LoCoMo** numbers swing ~25 points across vendor methodologies (Zep self-reports 84%; Mem0's re-run scored Zep at 58.44%; Zep counter-claims 75.14%). No replication consensus. `[CONTESTED]`.
- **Single-vector dense ceiling on the original benchmark papers' own ablations: 52-65%.** Everything above ~80% has bolted on knowledge graphs, cross-encoder rerank, or structured persona extraction. `[ASSERTED]` from the benchmark papers themselves.
- Vendors claiming 95%+ on LongMemEval are claiming to beat oracle GPT-4o reading (which caps at 92.4% on LongMemEval-S with chain-of-note). Cannot all be real.

## What the claim really is

The load-bearing content is **not** any specific number — it is the methodological proposition that **a vendor grading its own benchmark cannot expect to be believed.** Self-reports cluster persistently 30–50 points above independent re-runs across multiple incumbents; the direction and persistence are the evidence, not the decimals. This is the reason an *independent* memory benchmark ([masq-ab-factorial-design](../decision/masq-ab-factorial-design.md)) is a real artifact: the field has no SWE-bench-style independently-authored, pinned-harness occupant. AJ 2026-06-08.

## What this is and isn't evidence for

**Is evidence for:**

- The cascading-failures product's *qualitative* direction. Today's 49-65% numbers under honest replication are in the same band as the 30-50% billion-scale prediction. Stock-growth effects make these numbers go down, not up, on the cascade hypothesis.
- A methodology problem in the field. Vendor self-reports cluster 30-50 points above third-party replications, persistently, across multiple incumbents.
- The "honest measurement" go-to-market story being adjacent-real: there is something to differentiate against.

**Is NOT evidence for:**

- The cascading-failures product being **multiplicative rather than overlap**. The 49% may already be the floor set by the worst single mode (e.g. embedding crowding alone). See [multiplicativity-vs-overlap](../open-question/multiplicativity-vs-overlap.md).
- A specific projected number at billion scale. The compounded-recall prediction (30-50% at 1B) is `[SPECULATED]`. Today's 49-65% at <50K docs is consistent with the prediction but does not establish it.
- Architectural claims about *which* mechanism is dominant. Replication gaps measure aggregate output; they do not decompose into the four modes of [cascading-failures](./cascading-failures.md).

## Why this matters for the wedge

The replication gap is also evidence for [precision-over-recall](../decision/precision-over-recall.md): if production incumbents are at 49% recall, the engineering response is to make sure the 49% you *do* return is right, not to chase a higher-recall ceiling that the field cannot honestly measure. The wedge's cost-asymmetry tuning ([H23-util](../hypothesis/H23-util.md)) is downstream of this insight.

## Related

- [cascading-failures](./cascading-failures.md) — the prediction this concept anchors against
- [multiplicativity-vs-overlap](../open-question/multiplicativity-vs-overlap.md) — the empirical gap this concept does *not* close
- [billion-scale-benchmark-gap](../open-question/billion-scale-benchmark-gap.md) — the future-scale measurement gap
- [Mem0 incumbent](../incumbent/mem0.md) — the canonical 49% vs 93% datapoint
- [memory-surveys-2026](../source/memory-surveys-2026.md) — the survey papers documenting replication chaos

## Source archive

Anchored on the benchmark-ceilings probe at `benchmark-ceilings-2026-04-30.md`, which compiled public scores from LongMemEval, LoCoMo, EMem, and BEAM as of 2026-04-30. The probe itself draws on vendor self-reports and the 2026 survey papers.

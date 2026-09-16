---
type: open-question
name: RL fine-tuning target — encoding vs consolidation
status: OPEN
last_ingested: 2026-05-13
sources: []
epistemic_tags: [speculated]
tags: [rl, consolidation, encoding, post-wedge]
---

## The question

If we have budget for one RL fine-tuning investment in the post-wedge architecture, **which target produces larger gains over a prompted baseline — encoding ([rl-encoding-upgrade](./rl-encoding-upgrade.md)) or consolidation?**

Shelved H22 argued for consolidation. The reasoning: consolidation has better-defined inputs/outputs (cluster of related memories → consolidated insight), more measurable quality signals (does the consolidated memory retrieve well for queries that hit the originals?), and self-generating training data (every consolidation the system performs is a training example). The implication is that the bar to clear is lower for consolidation than for encoding.

## Why it matters

- **The two questions compete for the same investment.** RL fine-tuning at this scale is GPU-expensive and time-expensive; we likely can't pursue both as v1 of Phase 3.
- **Asymmetric promotion creates bias.** If only [rl-encoding-upgrade](./rl-encoding-upgrade.md) is documented as a live question, future investment conversations are anchored toward encoding by default. This open question exists to keep both lanes visible.
- **The MTP usage signal informs both.** If encoding-ceiling pressure is real on AJ's real work, encoding wins the priority. If consolidation pain (memory bloat, redundant memories, conflicting clusters) is what shows up first, consolidation wins.

## What evidence would resolve it

- **MTP failure-mode forensic** ([tool-chain-wedge-as-adoption-path](../decision/tool-chain-wedge-as-adoption-path.md) Goal 5). Sessions where memory was retrieved-but-unhelpful split into:
  - "Right memory found, wrong details preserved" → encoding-ceiling evidence
  - "Multiple overlapping/conflicting memories found, hard to use" → consolidation evidence
  - "Wrong memory found" / "no relevant memory" → retrieval or task-distribution, not RL-target
- **Cheaper escapes for each.** A larger prompted budget or hierarchical encoding may close the encoding ceiling without an RL fine-tune. Better prompted consolidation (LLM merges related memories) may close the consolidation gap. Whichever has the higher non-RL ceiling has less urgent need for RL.
- **Reward-signal quality check.** H22 claimed consolidation's reward signal (downstream retrieval performance on consolidated vs unconsolidated) is reliable. If retrieval has its own quality issues (see [H30-scaling-crossover-point](../hypothesis/H30-scaling-crossover-point.md)), the reward signal could be noisy, weakening the consolidation case.

## What would close this

Promotion to two competing hypotheses, both with falsifiable form, ideally tested in parallel on the MTP corpus. Likely shapes:

> *RL-trained consolidator beats prompted-LLM consolidation on downstream retrieval-quality metrics by ≥ Y% at corpus sizes above N.*

> *RL-trained encoder beats prompted slot-format encoder on cost-per-session by ≥ Z% on tasks of complexity ≥ C.*

## Evidence for consolidation as the better target

- **Well-defined interface.** Input: a cluster of related memories + metadata. Output: a consolidated insight + provenance links. Cleaner than encoding's "arbitrary conversation → memory records."
- **Self-generating training data.** Retrieval-quality feedback after each consolidation is automatic; no human annotation.
- **Lower starting bar.** Prompted consolidation is already decent at factual merging; RL has room to improve on edge cases (conflicting sources, temporal nuance, detail-vs-compression trade-off).

## Evidence against (encoding may be the better target)

- Encoding may be the **harder** problem and therefore the one where RL investment pays off more — the slot-format ceiling at ~1200 tokens is a specific failure mode that RL could learn around.
- Consolidation is a **v2+ layer** in the seven-layer stack; it doesn't exist in the wedge today. Investing in RL for a layer we haven't built is premature.
- The self-generating training-data argument **assumes the retrieval signal is reliable**. If [H30-scaling-crossover-point](../hypothesis/H30-scaling-crossover-point.md) shows retrieval quality is itself store-size-dependent, the reward signal is noisier than the argument requires.

## Related

- [consolidation-channel](../concept/consolidation-channel.md) — paradigm-level concept for the broader CLS-grounded operator that moves information between storage tiers. "Consolidation" in *this* question refers to the narrower within-store merge operation (the H22-shelved framing); the consolidation-channel page is the broader paradigm version. The RL-target question here is "where in Kyrja's stack do we spend RL budget on the consolidation operator?"
- [rl-encoding-upgrade](./rl-encoding-upgrade.md) — the encoding lane of this question
- [H34-forgetting-scores](../hypothesis/H34-forgetting-scores.md) and [H36-consolidation-ordering](../hypothesis/H36-consolidation-ordering.md) — consolidation-layer prerequisites
- [slot-format-encoding](../decision/slot-format-encoding.md) — encoding-layer baseline this question would upgrade
- [admission-control](../concept/admission-control.md) — the third RL-eligible layer; admission as RL target is a candidate not yet captured separately
- Shelved predecessor: H22 in _archive

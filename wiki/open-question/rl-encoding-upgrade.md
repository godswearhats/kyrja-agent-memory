---
type: open-question
name: RL-trained encoder as the post-wedge upgrade path
status: OPEN
last_ingested: 2026-05-12
sources: []
epistemic_tags: [speculated]
tags: [encoding, phase-3, encoding-ceiling]
---

## The question

The current wedge ships **prompted slot-format encoding** ([slot-format-encoding](../decision/slot-format-encoding.md)) at ~1200 tokens. The shelved H15 hypothesis claimed that **an RL-trained encoder can learn from downstream query patterns which details to preserve**, overcoming the information-loss problem that prompted encoding fails on at the limit. Phase 3 of the [tool-chain-wedge-as-adoption-path](../decision/tool-chain-wedge-as-adoption-path.md) treats this as the eventual encoder; the question is whether it becomes *mandatory* (the wedge stalls without it) or *optional* (a nice-to-have v2 improvement).

So: **at what level of encoding-ceiling pressure does prompted slot-format break, and is an RL-trained encoder the right escape?**

## Why it matters

- **[tool-chain-wedge-as-adoption-path](../decision/tool-chain-wedge-as-adoption-path.md)** flags the encoding ceiling as the wedge's first open hazard: "If the ~1200-token slot encoding loses too much detail, Phase 3 (RL-trained encoder) becomes mandatory before the product works for anyone but AJ. Build MTP fast to expose this."
- **[slot-format-encoding](../decision/slot-format-encoding.md)** also flags it as a hazard: harder/longer-horizon tasks may exceed what 1200 slot-tokens can carry, narrowing the measured cost savings.
- **Phase 3 is expensive.** RL fine-tuning needs reward signal, training data, and infrastructure. Investing before evidence of need wastes the wedge runway; investing too late stalls the product on encoding-ceiling pain. Timing matters.
- **The cost-savings asymmetry rides on encoding quality.** [H23-util](../hypothesis/H23-util.md) cost-asymmetry findings (relevant memory −50%, irrelevant +50%) are direction-stable across distillers but magnitude-fragile. A weaker encoder narrows the right-side of the asymmetry; a stronger one widens it.

## What evidence would resolve it

- **MTP usage signal on AJ's real work** (Goal 5). If cost savings *don't* compound on harder tasks, the encoding-ceiling pressure is real and Phase 3 enters the critical path. If savings hold, Phase 3 is genuinely v2.
- **Held-out task forensic.** Look at sessions where memory was retrieved but didn't help. If the failure mode is "the right memory was found but the relevant detail wasn't in it," that's encoding-ceiling evidence. If the failure mode is "the wrong memory was retrieved" or "no relevant memory existed," that's retrieval or task-distribution, not encoding.
- **Worst-case source data.** [worst-case-source](./worst-case-source.md) is adjacent — if fully-failed sessions distill into harmful encodings under prompted slots, an RL-trained encoder with downstream-quality reward could fix both problems at once.
- **Alternative escapes that aren't RL.** A larger prompted budget (e.g. 3000-token slots), hierarchical encoding (compact + drill-down), or retrieval-time re-distillation could close the ceiling without an RL fine-tune. These should be checked first because they're cheaper.

## What would close this

Promotion to a hypothesis with falsifiable form, once the MTP produces usage data. Likely shape:

> *Prompted slot-format encoding at 1200 tokens loses sufficient detail on tasks of complexity ≥ X that an RL-trained encoder beats it on cost-per-session by ≥ Y%, measured on a homogeneous-code corpus.*

X and Y are unknown today. The MTP is the natural vehicle to bound them.

## Adjacent claims

- **H22 (shelved):** Consolidation as RL target may produce larger gains than encoding as RL target — because consolidation has better-defined inputs/outputs, more measurable quality signals, and self-generating training data. If consolidation is the right RL target, the encoder stays prompted longer than expected. See triage at TRIAGE-2026-05-12.md.

## Related

- [slot-format-encoding](../decision/slot-format-encoding.md) — the current encoder this question would upgrade
- [tool-chain-wedge-as-adoption-path](../decision/tool-chain-wedge-as-adoption-path.md) — where the encoding-ceiling hazard is flagged
- [H23-util](../hypothesis/H23-util.md) — the cost-savings hypothesis whose magnitudes depend on encoder quality
- [worst-case-source](./worst-case-source.md) — adjacent open question on degraded-source distillation
- Shelved predecessor: H15 in _archive

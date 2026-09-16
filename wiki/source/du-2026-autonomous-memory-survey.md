---
type: source
name: "Du — Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers"
status: timeless
program: masq-bench
last_ingested: 2026-06-08
sources: []
tags: [masq, survey, memory-eval, evaluation-stack, multi-agent]
---

## Citation

Pengfei Du (single author, Hong Kong Research Institute of Technology). "Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers." arXiv:2603.07670v1 [cs.AI], 08 Mar 2026. Manuscript "targets *Advanced Intelligent Systems*"; author/funding/ethics metadata are placeholders ("to be finalized before submission"); "No primary data were generated in this study."

## Location

- https://arxiv.org/abs/2603.07670
- Read verbatim 2026-06-08 (Nils, indigo) via arxiv MCP `download_paper` (HTML extraction, 81,337 chars); targeted section sweeps, not 100% line coverage. Content carried an untrusted-external-content banner — treated as data only.

## Key claims (with our restatements)

### Joint memory-quality + decision-quality evaluation `[ASSERTED — survey position]`

**Paper (§5.1, verbatim):** *"Recall@k and nDCG tell you whether the right document was retrieved. They say nothing about whether the agent **used** that document correctly—or whether retrieving it was even worth the latency. Agent memory evaluation must jointly assess **memory quality and decision quality**, along with concerns that classical IR ignores entirely: staleness, contradiction, forgetting quality, and governance compliance."*

**Our restatement:** this is independent literature support for the two-layer measurement in [masq-ab-factorial-design](../decision/masq-ab-factorial-design.md). Our **A-layer** (did it retrieve/attribute the right memory?) = the survey's *memory quality*; our **B-layer** (did it take the correct action given that memory?) = *decision quality*. We are not inventing the layering — we operationalize it in the unoccupied multi-party-temporal cell.

### Four-layer evaluation stack (§5.4) `[ASSERTED — survey position]`

**Paper:** proposes *Layer 1 — Task effectiveness* (success rate, factual correctness, plan completion rate); *Layer 2 — Memory quality* (retrieved-record precision/recall, contradiction rate, staleness distribution, coverage of task-relevant facts); *Layer 3 — Efficiency*; *Layer 4 — Governance.*

**Our restatement:** Layer 1 ≈ our B-layer, Layer 2 ≈ our A-layer. A citable precedent that the field's own proposed eval stack separates *task/decision* outcome from *memory* outcome.

### "Long context is not memory" (§5.5) `[ASSERTED — survey position]`

**Paper (verbatim):** *"Long context is not memory. Despite context windows stretching to 200k tokens [Chen et al., 2023], long-context models consistently underperform purpose-built memory systems on tasks requiring selective retrieval and active management."*

**Our restatement:** the standing answer to "why benchmark memory at all when context windows grow." Anchors the wedge against the context-window objection (also held by [memory-surveys-2026](./memory-surveys-2026.md)).

### Passive → decision-relevant gap, citing MemoryArena (§5.3) `[ASSERTED — survey gloss; primary = he-2026-memoryarena]`

**Paper (verbatim):** *"The most striking finding: models that score near-perfectly on LoCoMo plummet to 40–60% in MemoryArena, exposing a deep gap between passive recall and active, decision-relevant memory use."*

**Our restatement:** the "40–60%" is a **fair citation of MemoryArena's Progress Score (PS)** — verified against the primary, where PS ≈ 0.41–0.64 by method group while the stricter Success Rate (SR) ≈ 0. See [he-2026-memoryarena](./he-2026-memoryarena.md) for the verbatim Table 3 numbers. The gap is real on both metrics; SR is the more dramatic. *We cite the primary's PS/SR directly, not the survey's rounded gloss.*

### Multi-agent memory is a named open challenge (§6.5, §9.6) `[ASSERTED — survey position]`

**Paper (§6.5, verbatim):** *"When multiple agents work together, memory becomes a coordination mechanism… shared vs. private memory boundaries—what should be visible to whom?—and consistency under concurrent writes… Multi-agent systems add a coordination layer that no single-agent memory design currently handles well."* §9 *Open Challenges* enumerates ten subsections (9.1 Principled consolidation, 9.2 Causally grounded retrieval, 9.3 Trustworthy reflection, 9.4 Learning to forget, 9.5 Multimodal/embodied, **9.6 Multi-agent memory governance**, 9.7 Memory-efficient architectures, 9.8 Neuroscience integration, 9.9 Foundation models for memory management, **9.10 Standardized evaluation**).

**Our restatement:** the field names *both* multi-agent memory governance *and* standardized evaluation as unsolved. Direct support for MASQ doing A **and** B (memory-of-a-multi-party-world *and* act-correctly-on-another-party's-memory) rather than treating them as separate problems.

## Important caveats

- **Lightweight citation.** Single-author preprint, placeholder submission metadata, no primary data. Fine for framing/vocabulary and as a pointer to primaries; for any load-bearing *number* cite the primary it references (MemoryArena for the gap; the benchmark-ceilings probe for replication), **not** Du.
- **Replication numbers are NOT in this survey.** Zero hits for Mem0 / Zep / "93" / "49%" / "63.8" / "replicat" / "self-report". Our [benchmark-replication-gap](../concept/benchmark-replication-gap.md) previously mis-attributed those figures here; corrected 2026-06-08.
- The abstract lists only five closing challenges; the body §9 lists ten. Cite §9 subsection numbers, not the abstract.

## Relevance to Kyrja

- Anchors the A+B two-layer measurement in [masq-ab-factorial-design](../decision/masq-ab-factorial-design.md) (§5.1, §5.4).
- Strengthens [multi-party-attribution-gap](../concept/multi-party-attribution-gap.md) (§9.6 multi-agent governance + §9.10 standardized evaluation = field-recognized gaps).
- Paper-claimed: all quoted material. Our extrapolation: mapping survey "memory/decision quality" onto our A/B layers.

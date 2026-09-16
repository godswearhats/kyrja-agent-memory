---
type: source
name: "Agent-memory survey papers (2026): Memory in the Age of AI Agents + Memory for Autonomous LLM Agents"
status: timeless
last_ingested: 2026-06-08
sources: []
tags: [survey, taxonomy, open-challenges]
---

## Citation

Two complementary survey papers anchoring the agent-memory research landscape as of mid-2026:

1. *Memory in the Age of AI Agents* (47 authors, updated Jan 2026). arXiv:2512.13564. Organizes memory across **Forms** (token-level, parametric, latent), **Functions** (factual, experiential, working), and **Dynamics** (formation, evolution, retrieval). Positions memory as "a first-class primitive."
2. *Memory for Autonomous LLM Agents* (Du, single-author, Mar 2026). arXiv:2603.07670. Body §9 lists **ten** open challenges (incl. multi-agent memory governance §9.6, standardized evaluation §9.10). **Critical thesis: "Long context is not memory"** — 200K-token windows underperform purpose-built systems on selective retrieval. *Now read verbatim and atomized to [du-2026-autonomous-memory-survey](./du-2026-autonomous-memory-survey.md); see the de-conflation note below.*

Plus *Graph-based Agent Memory* (Feb 2026, arxiv 2602.05665) as a dedicated graph-memory survey.

## Location

- 47-author survey: https://arxiv.org/abs/2512.13564
- Paper list (GitHub): https://github.com/Shichun-Liu/Agent-Memory-Paper-List
- 9-challenges survey: https://arxiv.org/html/2603.07670v1
- Graph-memory survey: https://arxiv.org/html/2602.05665v1
- Awesome-GraphMemory: https://github.com/DEEP-PolyU/Awesome-GraphMemory
- MemAgents ICLR 2026 workshop: https://sites.google.com/view/memagent-iclr26/

## Key claims (with our restatements)

### The 47-author survey

**Paper:** Three-dimensional taxonomy (Forms × Functions × Dynamics). Positions memory as a first-class primitive on par with reasoning and tool-use.

**Our restatement:** Useful as a vocabulary anchor and as evidence that the field has consolidated enough to merit a multi-author survey. **The taxonomy itself is not load-bearing for our thesis** — we work at the architectural layer (seven-layer stack), not the form/function/dynamics layer.

### The "Memory for Autonomous LLM Agents" survey (2603.07670)

> **De-conflation note (2026-06-08):** this is the **single-author Du survey**, now read verbatim and pulled into its own node — see [du-2026-autonomous-memory-survey](./du-2026-autonomous-memory-survey.md). It is NOT the 47-author survey, and the earlier "nine challenges" list below was a paraphrase that did not match the paper. The body §9 lists **ten** open challenges: 9.1 Principled consolidation, 9.2 Causally grounded retrieval, 9.3 Trustworthy reflection, 9.4 Learning to forget, 9.5 Multimodal/embodied, **9.6 Multi-agent memory governance**, 9.7 Memory-efficient architectures, 9.8 Neuroscience integration, 9.9 Foundation models for memory management, **9.10 Standardized evaluation**.

Load-bearing for MASQ (verbatim, see the Du node): **§5.1** *"must jointly assess memory quality and decision quality"* (our A/B layers); **§5.4** four-layer eval stack; **§5.5 "Long context is not memory"**; **§9.6** multi-agent governance + **§9.10** standardized evaluation as named unsolved problems.

**Our restatement:** "Long context is not memory" is the **single most important defense of the wedge thesis from the model-capability side** — passive context underperforms purpose-built memory on selective retrieval. The §5.1 joint memory/decision-quality framing independently anchors the A+B design in [masq-ab-factorial-design](../decision/masq-ab-factorial-design.md). Caveat: lightweight single-author preprint — cite primaries it references for any load-bearing number.

### The graph-memory survey

**Paper:** Dedicated survey on graph approaches to agent memory.

**Our restatement:** Anchors the [graph-memory approaches](../concept/graph-memory-approaches.md) concept page. Complementary to [Zep](../incumbent/zep.md) (the most graph-shaped incumbent).

### Independent benchmark anchor

The "passive recall plummets to **40–60%** on decision-relevant use" line is **Du's §5.3 gloss of MemoryArena**, now verified against the primary: it fairly cites MemoryArena's **PS** (Progress Score ≈ 0.41–0.64), while the stricter **SR ≈ 0**. See [he-2026-memoryarena](./he-2026-memoryarena.md) Table 3 for verbatim numbers. The benchmark gap (passive recall vs decision-relevant *use*) is the construct-validity concern motivating the A+B design of [masq-ab-factorial-design](../decision/masq-ab-factorial-design.md). `[ASSERTED — survey gloss; primary numbers in the MemoryArena node]`

> **Sourcing correction (2026-06-08):** the vendor replication figures (Mem0 93.4%→49%, Zep 63.8%, OpenAI 57.73%, LoCoMo methodology swings) are **NOT in either survey** — verified absent from a verbatim sweep of 2603.07670. [benchmark-replication-gap](../concept/benchmark-replication-gap.md) previously attributed them here in error.

## Relevance to Kyrja

- The "long context is not memory" finding is anchor for the wedge thesis against the "context windows will solve memory" objection.
- The §9 open challenges (ten) validate the seven-layer-stack framing.
- Sources [admission control](../concept/admission-control.md), [graph-memory approaches](../concept/graph-memory-approaches.md), and indirectly [seven-layer stack](../concept/seven-layer-stack.md).
- Anchor for [billion-scale benchmark gap](../open-question/billion-scale-benchmark-gap.md) — neither survey identifies a billion-scale agent-memory benchmark.

## Archive location

Not currently in `library/papers/`. Fetch from arXiv to verify specific claims before any load-bearing use.

---
type: source
name: "Zhang et al. 2026 — Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents"
status: timeless
last_ingested: 2026-05-26
sources: []
tags: [agentic-memory, skill-discovery, compression, bolt-on-foil, field-map, position-paper, cls]
---

## Citation

Zhang, X., Wang, G., Cui, Y., Qiu, W., Li, Z., Zhu, B. & He, P. (2026). *Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents.* arXiv:2604.15877. (CC BY-NC-SA 4.0; v1 17 Apr 2026.)

## Location

- arXiv: https://arxiv.org/abs/2604.15877
- Full HTML read 2026-05-26 (see Audit history).

## Why this paper is load-bearing for Kerros

It is the **single best-articulated map of the bolt-on design space** and, by its own declaration, the cleanest external foil for [Kerros](../concept/kerros.md). The entire framework lives on the memory-for-the-agent side of the [memory-consumer-axis](../concept/memory-consumer-axis.md) — and the authors draw the same scaffold/weights line we draw with the [integration gate](../concept/integration-gate.md), then plant their whole flag on the *scaffold* side. Read alongside [Xu, Dai & Zhang 2026](./xu-2026-agentic-memo.md), the two papers stake out the two sides of our gate.

## Key claims (with our restatements)

### Scope — scaffold-level only (the crux)

**Paper (§1, verbatim):** *"We study knowledge extracted at the **scaffold level** — runtime systems outside model weights. Training-time methods (RLHF, Constitutional AI) are complementary but out of scope."* Repeated in Limitations.

**Our restatement:** `[ASSERTED]` This is the decisive fact. The framework is, by stipulation, entirely memory-for-the-agent — text artifacts retrieved into the context window. The boltability gate we drew is exactly the boundary this paper refuses to cross. Kerros is **orthogonal to the whole spectrum**, not a point further along it.

### The compression spectrum (the framework)

**Paper (§2):** Memory, skills, and rules are points on a single axis of increasing compression of interaction traces:
- L0 — raw trace (1:1)
- L1 — episodic memory (~5–20×): *what happened*; structured event records (Mem0, A-MEM, MemoryOS)
- L2 — procedural skill (~50–500×): *how to act*; reusable routines (Voyager, Trace2Skill, SkillRL)
- L3 — declarative rule (~1000×+): *what principles govern decisions*; NL constraints/policies (largely empty)

**Our restatement:** `[ASSERTED]` This axis is essentially the [substrate-depth ladder](../concept/consolidation-channel.md#substrate-depth-ladder) for *text* — but it stops at the frozen-θ boundary. Their L3 "declarative rule" is the most-compressed *text* form; pushing one rung past it (rule → weights) is the [consolidation-channel](../concept/consolidation-channel.md), which they place out of scope.

### Transferability increases with compression — but it is untested

**Paper (§3.3):** Claims a monotonic relationship: L1 memories transfer across base models, L2 skills transfer across tasks and model sizes (Trace2Skill 35B→122B, +57.7pp), with a concave curve and an L2 "sweet spot." Aggregated cross-level evidence (Table 1): SkillRL L2 vs L1 retrieval +68.5pp (ALFWorld); Trace2Skill L2 vs human skill +21.5pp (SpreadsheetBench).

**Our restatement:** `[MEASURED]` (their aggregation) but the central claim is **not cleanly tested**. Verbatim: *"A controlled experiment holding source experience constant while varying only compression level has not been conducted."* Construct-validity: their own Table 1 states the rows *"cannot be directly compared"* (different benchmarks). So "compression → transferability" is *consistent with* their evidence, not demonstrated by it. This is the rule-vs-episode tradeoff from [Xu's theorem](./xu-2026-agentic-memo.md) reached from a compression angle, without the theorem.

### The missing diagonal

**Paper (§2.4):** Every surveyed system operates at a *fixed, predetermined* compression level. None adaptively selects a level, promotes knowledge upward (many memories → one skill → one rule), or demotes downward. They name this gap the *missing diagonal* and frame it as a meta-learning problem.

**Our restatement:** `[ASSERTED]` Their most ambitious open problem is still entirely scaffold-level. The "diagonal" is a sophisticated *bolt-on*; Kerros's move (promote past L3 into θ) is the rung they ruled out.

### Community fragmentation

**Paper (§1, §3.1):** Citation analysis of 1,136 references across 22 primary papers: cross-community citation rate <1% (memory→skill 0.7%, skill→memory 1.2%).

**Our restatement:** `[MEASURED]` (their citation analysis). The agent-memory and skill-discovery communities don't talk. We observe a *third* gap wider still: neither cites the weight-integration / training-methods work ([Skill-SD](./xu-2026-agentic-memo.md), ParamMem). Kerros sits in that unoccupied bridge.

### CLS invoked — but read as text compression

**Paper (§1, §4):** Grounds "idle-time upward compression (L1→L2→L3)" in CLS (McClelland 1995), "analogous to hippocampal-neocortical consolidation during sleep."

**Our restatement:** `[ASSERTED]` They borrow CLS but **drop its defining feature**: CLS's slow neocortical store is *weights*, not a more-compressed text artifact. [Xu](./xu-2026-agentic-memo.md) reads CLS correctly (slow side = parametric); ECS reads the slow side as text compression. That misreading *is* the boltability gate — same biology, opposite consumer.

### L3 weight-rules dismissed on practicality, not capability

**Paper (§2.3, verbatim):** *"Weight-level rules (via RLHF) are static after training, opaque to inspection, and cannot be updated without retraining. Scaffold-level rules would be inspectable, editable, and deployable without gradient updates."*

**Our restatement:** `[ASSERTED]` This is the bolt-on value proposition stated cleanly — and crucially it is a **practicality** argument, never a **capability** one. They never engage Xu's compositional ceiling and do not cite Xu. But the argument is also the **steelman against Kerros**: inspectability/editability/no-retraining are real virtues (and the same ones that keep [M10 dead](../concept/integration-gate.md) and bound the [evil² problem](./xu-2026-agentic-memo.md)). Kerros's composition win is paid for in inspectability — a real entry on the cost ledger.

### Testable predictions

**Paper (§3.4):** (i) L2 compression should beat L1 retrieval on cross-domain transfer *with source experience held constant*; (ii) multi-level (L1+L2) beats either alone, gap widening with deployment length; (iii) concave transferability curve; (iv) L3 rules help most as constraints not directives (RuleShaping evidence).

**Our restatement:** `[ASSERTED]` Prediction (i) is the **scaffold-level cousin of the Kerros beachhead experiment**. Ours is the boundary-crossing version: weights vs. best L3 scaffold rule, source held constant, on a composition task with `ᾱ < 1` verified. Their design *minus* the gate-crossing is our design — and it slots into a published open problem.

## Important caveats

- **Conceptual, not empirically validated** (their own Limitations): *"the spectrum's utility as a design tool awaits experimental confirmation."* It is a position/survey paper.
- **Q1 2026 snapshot**; they note the field moves rapidly.
- **Text-only focus** (multimodal flagged as extension).
- **Discrete four levels are a simplifying abstraction**; they concede compression may be continuous (EvolveR straddles L2/L3).

## Relevance to Kerros

- **The bolt-on foil and field-map.** Use it to position Kerros: *not more compression — a different consumer.* Their axis runs parallel to the gate; Kerros crosses it.
- **Two-sides-of-the-gate framing.** ECS (compress text, stay scaffold) vs [Xu](./xu-2026-agentic-memo.md) (text can't compose, need weights) — same problem, same CLS anchor, opposite conclusion. The fork is the consumer.
- **Their own discipline extends to us.** ECS's §Problem-3 "minimum plasticity" principle — *promote only when evidence warrants* — carried one rung past their scope boundary (promote to **weights** only the L3 rules that proved stable and cross-domain) is the disciplined Kerros consolidation gate. It also answers the inspectability cost: sacrifice inspectability *only* for the most-validated, most-general knowledge.
- **Field map.** Names ~22 systems (L1: Mem0, A-MEM, MemoryOS, Memory-R1, Mem-α, MemPO, ALMA, MemMA, SSGM, LightMem; L2: Voyager, SkillWeaver, EvoSkill, CASCADE, AutoSkill, Trace2Skill, SkillRL, EvolveR; cross-level: ExpeL, AutoAgent) plus survey anchors worth mining: Hu et al. 2025 *Memory in the age of AI agents* (2512.13564), graph-memory taxonomy (Yang 2026a, 2602.05665), agentic-skill SoKs (Jiang 2026 / Xu & Yan 2026), agentic-RL landscape (Zhang 2026a, TMLR).
- Anchors [integration-gate](../concept/integration-gate.md); reinforces [memory-consumer-axis](../concept/memory-consumer-axis.md) (cleanest external instance of the memory-for-the-agent side).

## Audit history

- 2026-05-26 — full HTML read (arXiv HTML endpoint). Abstract pre-checked 2026-05-25 via `get_abstract`. Treated as untrusted external content (data only). Read in the context of the 2026-05-25/26 Kerros wide-pass literature survey.

## Archive location

arXiv:2604.15877. Not in `library/papers/`. Fetch from arXiv for re-verification.

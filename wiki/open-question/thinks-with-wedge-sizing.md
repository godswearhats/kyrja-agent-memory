---
type: open-question
name: "Where does memory-the-model-thinks-with actually beat bolt-on RAG? (the operand-vs-grammar lens)"
status: OPEN
last_ingested: 2026-05-30
program: kerros
sources: [../concept/integration-gate.md, ./incremental-integration-cost.md, ../concept/caddy.md, ../concept/memory-consumer-axis.md, ../source/xu-2026-agentic-memo.md]
epistemic_tags: [speculated, measured]
tags: [kerros, scoping, wedge-sizing, operand-vs-grammar, market-data, exploratory]
---

> **Exploratory (2026-05-30).** Threads + data from a strategy session, **not** a committed direction — AJ flagged explicitly *"these are interesting thoughts to explore, don't overindex."* Recorded so we don't forget them; to be pressure-tested, not built on. Premature-framework caution per [[feedback_research_methodology]].

## The question

[Gate 1](../concept/integration-gate.md) shows there *exist* problems where memory-the-model-thinks-with beats a frozen bolt-on, with a divergent ([Xu](../source/xu-2026-agentic-memo.md) `Ω(k²)`) gap. But *most* of what people pay LLMs to do may not live in that regime. So the scoping question:

> **What fraction of real, paid LLM work actually sits in the regime where thinks-with memory beats bolt-on RAG — and is it big enough, and growing fast enough, to justify building the harder thing?**

## The operand-vs-grammar lens `[SPECULATED]`

A distinction that fell out of the session — two kinds of "new knowledge" a memory could supply:

- **New operands, fixed grammar.** The task needs new *facts/entities about your world* (this codebase, this customer, this person's preferences), combined via reasoning the model *already has* from pretraining. Only the operands are new; the grammar (how to compose them) is fixed.
- **New grammar from experience.** The task needs a genuinely *new skill/rule/procedure* the model didn't have at training, learned from interaction.

This matters because a frozen, co-trained [caddy](../concept/caddy.md) can supply new operands but structurally *cannot* learn new grammar at runtime (see that page's 2026-05-30 challenges). The lens bounds what the bounded architecture can ever do.

## What the market data says `[MEASURED]` (interpretation `[SPECULATED]`)

2026-05-30 web pull. **Construct-validity note:** these are vendor/analyst surveys (Menlo Ventures, Anthropic, a16z) with differing methodologies; treat the figures as *directional*, not precise, and not atomized as `source/*` pages (external market reports, not research papers).

- **New-operands ≈ p90 of paid spend.** Coding is the biggest single bucket ($4.0B, 55% of departmental spend; ~⅓ of Claude.ai, ~half of API traffic; top task = "modifying software to correct errors"); customer support ~27–32%; copilots 86% of the horizontal layer ($7.2B); RAG-over-docs and ambient scribes ($600M). All "apply pretrained capability to my private context."
- **New-grammar is "niche."** True agents are 10–16% of deployments (mostly fixed-sequence/routing, not *learning*); fine-tuning and RL customization explicitly "niche."

**The catch (interpretation):** most new-operands is *already served adequately by bolt-on RAG* (enterprise customization = prompt design > RAG > fine-tuning). So new-operands ≠ thinks-with-wins. The thinks-with advantage bites **only in the high-composition corner** of new-operands — where combining *many* retrieved facts hits the `Ω(k²)` wall — which is the agentic frontier: small today, plausibly compounding.

**Confound:** today's spend is *supply-constrained* — nobody buys new-grammar memory because nobody ships it. Spend-today is a lagging proxy for latent demand. Read the p90 as "where value is captured *now*," not "where it could be."

## What evidence would resolve it

The decision rule this session converged on (itself `[SPECULATED]`, to be attacked): the go/no-go is **not** "% of spend that is new-operands" (≈p90, but mostly RAG-served) — it is **"how big, and how soon, is the high-composition slice where bolt-on RAG measurably degrades from retrieval-*scaling*, not from model quality."** That slice is exactly Gate 1's fan-open regime, which we showed is real.

Concrete next measurement (if/when we resume): find real paid agentic / multi-hop workloads over large private context and show RAG degradation tracks *retrieval count* (the `Ω(k²)` signature), not model capability. If that corner is p10-and-shrinking → ship RAG. If p10-and-compounding-with-agents → the harder thing earns its keep.

## Related

- [integration-gate](../concept/integration-gate.md) — Gate 1 proves the high-composition regime *exists*; this question *sizes* it.
- [incremental-integration-cost](./incremental-integration-cost.md) — the *write*-tractability question; sibling thread from the same session.
- [caddy](../concept/caddy.md) — the bounded architecture this lens scopes (operands yes, grammar no).
- [memory-consumer-axis](../concept/memory-consumer-axis.md) — thinks-with vs thinks-about; this asks *where* thinks-with is worth the cost.
- [Xu, Dai & Zhang 2026](../source/xu-2026-agentic-memo.md) — the `Ω(k²)` wall that defines the high-composition corner.

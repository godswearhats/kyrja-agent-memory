---
type: incumbent
name: Honcho (by Plastic Labs)
status_current_as_of: 2026-05-15
last_ingested: 2026-05-15
sources: [source/honcho-docs.md]
tags: [incumbent, integration-gap, identity-modelling, consolidation-channel-adjacent]
---

## What it does

Memory infrastructure for stateful agents that **model evolving relationships among peers** rather than store facts to be retrieved. Workspaces contain peers (humans and AI agents are first-class equals — the "Peer Paradigm") participating in sessions with messages. As of Honcho 3 (Jan 2026), the architecture has two agentic components: the **Dreaming Agent** handles asynchronous background derivation (summaries, peer cards, deductive/inductive/abductive conclusions) — replacing the v2 "deriver"; the **Dialectic Agent** handles agentic query-time retrieval (LLM with tool use) — replacing the v2 fixed-path chat endpoint. Retrieval is exposed via `get_context()` (vendor-claimed ~200ms, callable every turn, returns Honcho's curated context). On the ingestion side, **Neuromancer XR** (fine-tuned Qwen3-8B, Aug 2025) extracts atomic logical conclusions from each incoming message and stores them per-peer as text. AGPL-3.0, Python-primary, FastAPI server.

See [Honcho vendor source](../source/honcho-docs.md) for the underlying material and verbatim quotes.

## What it doesn't

- **Fact-retrieval shape.** Honcho deliberately is **not** a fact-store-with-retrieval. Memory is queried through dialectic reasoning, not similarity search. For workflows that need verbatim recall of specific past events, Honcho is the wrong tool.
- **Multi-graph memory.** Peer representations are not graphs in the multi-graph sense; they are typed collections keyed by observer/observed pairs.
- **Tiered storage.**
- **Data-source connectors.** No first-class ingestion from external corpora; peer-message-stream only.
- **Compliance certifications.** No SOC 2 or HIPAA at this ingest.
- **Permissive licensing.** AGPL-3.0 is the most restrictive licence in the incumbent set — triggers copyleft obligations for network services, often blocked by enterprise procurement.

## Layer coverage in the [seven-layer stack](../concept/seven-layer-stack.md)

| Layer | Coverage |
|---|---|
| Admission Control | ✗ — all messages enter; reasoning happens after |
| Embedding | ◐ — present but not load-bearing in vendor framing |
| Multi-Graph Memory | ✗ — peer-pair-keyed collections, not graph topology |
| Tiered Storage | ✗ |
| Retrieval | ◐ — agentic retrieval via dialectic-reasoning chat endpoint; not similarity-shaped |
| Consolidation | ✓ — the **Dreaming Agent + Neuromancer XR** pattern is the most architecturally explicit consolidation primitive in the incumbent set, distinct in kind from Hindsight's Reflect (Honcho consolidates **identity models**, Hindsight consolidates **mental models of the world**) |
| Governance | ✗ |

**Net: ~1.5 of 7 layers materially covered**, but **Consolidation coverage is uniquely strong** — Honcho is the only memory-system incumbent that treats background derivation between sessions as a first-class, named, vendor-shipped feature, *and* ships a custom-trained model (Neuromancer XR) for ingestion-time conclusion extraction.

## Where it fails

- **Consumer-personalisation focus.** Designed for therapy bots, tutoring apps, shopping companions — the peer model is single-user-deep. For multi-contributor engineering teams sharing institutional memory, the peer paradigm doesn't naturally extend.
- **Implicit-learning audit gap.** Background derivation produces conclusions about peers that are hard to inspect: *why* did the system conclude X about user Y? Opaque in current docs.
- **AGPL-3.0 procurement barrier.** Structural enterprise-adoption ceiling, not solvable by engineering.
- **Cost / latency from dialectic reasoning.** Every chat-endpoint query is reasoning-shaped; the deriver and dream pipelines run continuously in the background. Token costs are unbounded in the LLM provider's terms.
- **Small team.** Pre-seed, <10 people.

## What is structural (worth borrowing)

The **Dreaming Agent (consolidation) + Dialectic Agent (retrieval)** split — synchronous ingestion with asynchronous derivation between sessions, plus agentic query-time reasoning — is exactly the [consolidation-channel](../concept/consolidation-channel.md) write-path shape we have been evaluating. Honcho is the existing-incumbent demonstration that this pattern is viable in production-shaped code, distinct from Hindsight's at-retrieval Reflect. The pattern shape is correct; the question is whether the peer-pair-keyed primitive generalises beyond consumer personalisation.

**Neuromancer XR is the concrete learned-operator instantiation.** Fine-tuned Qwen3-8B on ~10k manually curated conversation-turn → atomic-conclusion examples. 86.9% LoCoMo vs 69.6% base Qwen3-8B vs 80.0% Claude 4 Sonnet. The most important Kyrja-relevant fact: this is the cheap rung of the [substrate-depth ladder](../concept/consolidation-channel.md) — text-stored conclusions, not representation- or weight-level consolidation — and it ships from a pre-seed team. Demonstrates that *some* learned consolidation operator is buildable at commodity-fine-tune cost; does **not** demonstrate that deeper rungs are buildable at that cost. See [memory-consumer-axis](../concept/memory-consumer-axis.md) for the depth-vs-cost framing.

The **`get_context()` retrieval primitive** (~200ms vendor-claimed, callable every turn) is worth noting as the production interface — agentic retrieval surfaced through a single fast-enough call, rather than user-managed memory composition.

The **Peer Paradigm** (humans and agents as first-class equals) is the only existing-incumbent gesture toward agent-on-agent memory continuity. Worth engaging with via the [multi-agent-consistency](../open-question/multi-agent-consistency.md) question.

## Adoption signal

Pre-seed-funded ($5.4M led by Variant). Hermes Agent integration is the major distribution channel. Commit-tagged benchmark results (90.4% LongMemEval, 89.9% LoCoMo, 0.630 BEAM at 100K per vendor) — better evidence-shape than most competitors but still vendor-published.

## Related

- [Honcho vendor source](../source/honcho-docs.md).
- [Consolidation channel](../concept/consolidation-channel.md) — Honcho is the cleanest existing-incumbent demonstration of this write-path shape.
- [Hindsight](./hindsight.md) — the other consolidation-channel-adjacent incumbent; consolidates differently (world model vs identity model).
- [Multi-agent consistency](../open-question/multi-agent-consistency.md) — the Peer Paradigm is the closest gesture from any incumbent toward this question.
- [Seven-layer stack](../concept/seven-layer-stack.md).

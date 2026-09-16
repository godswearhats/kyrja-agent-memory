---
type: source
name: "Honcho — vendor documentation and project material"
status: timeless
last_ingested: 2026-05-16
sources: []
tags: [incumbent-anchor, integration-gap, identity-modelling, consolidation-channel-prior-art]
---

## Citation

Vendor-published GitHub README, documentation, and blog posts. Roll-up of project material as of mid-2026.

## Location

- GitHub: https://github.com/plastic-labs/honcho
- Docs: https://honcho.dev/docs/ (machine-readable: `https://honcho.dev/docs/llms-full.txt`)
- Managed service: https://app.honcho.dev
- Blog (Plastic Labs): https://plasticlabs.ai/blog/ (machine-readable: `https://plasticlabs.ai/blog/llms-full.txt`)

**Specific posts cited verbatim below:**

- Announcing Honcho 3 (2026-01-26): https://plasticlabs.ai/blog/posts/Honcho-3
- Introducing Neuromancer XR (2025-08-18): https://plasticlabs.ai/blog/research/Introducing-Neuromancer-XR
- Memory as Reasoning (2025-08-19): https://plasticlabs.ai/blog/posts/Memory-as-Reasoning

## Key claims (with our restatements)

### Architecture

**Vendor (README, May 2026):** Memory infrastructure for stateful agents that understand evolving relationships among people, agents, groups, projects, and ideas. Workspaces contain **peers** participating in sessions with messages. The system separates:

- **Synchronous storage** — message and event ingestion.
- **Asynchronous reasoning pipeline ("deriver")** — background workers derive facts about peers and build representations stored in internal collections keyed by observer/observed peer pairs.
- **Chat endpoint with dialectic reasoning** — reasoning-informed responses integrating derived conclusions with current context, across configurable reasoning levels.
- **"Dream" processing** — background derivation between sessions. Specialist models are mentioned without naming "Neuromancer" specifically.

AGPL-3.0 licence, Python-primary, FastAPI server.

**Our restatement:** `[ASSERTED]`. Honcho's architectural commitment is **identity-and-inference**: memory is *not* a fact store you retrieve from, it is a *psychological model of peers you query through dialectic reasoning*. This is genuinely philosophically distinct from every other incumbent. The Peer Paradigm (humans and AI agents both first-class) is the closest existing-incumbent gesture toward agent-on-agent memory continuity.

**Retrieval output format is text strings**, not learned representations. Per the Python SDK v2.0.0 changelog: *"Representation endpoints now return `string` instead of old Representation object."* The `.chat()` endpoint returns prose; the `get_context()` method returns Honcho's curated context as text. No documented cross-attention, adapter, soft-prompt, or learned-fusion interface to the consuming agent's primary LLM `[ASSERTED]` (2026-05-15 docs sweep via `honcho.dev/docs/llms-full.txt`).

The "Neuromancer models" claim that was unverified at the 2026-05-14 ingest is now verified — see the **Neuromancer XR** section below. Neuromancer is a custom-fine-tuned model that sits on the **write side** (ingestion-time atomic-conclusion extraction), not the read side. Its outputs are stored as text in Honcho's per-peer storage; downstream retrieval is text-out.

### Architecture (Honcho 3, January 2026)

**Vendor** ([Announcing Honcho 3](https://plasticlabs.ai/blog/posts/Honcho-3), 2026-01-26): Honcho 3 was a *"complete overhaul"* of the v2 architecture. The new components:

- **Dreaming Agent.** *"Tasks previously handled at the time of ingestion, including summarization and peer card generation, are handled by a completely new part of the system: we call it the Dreaming Agent."* *"Dreams are agentic background tasks. The agent crawls over everything known about a user and fills out missing pieces while rearranging the data to be retrieved more efficiently when needed."* Produces *"deductive, inductive, and abductive conclusions; summaries; peer cards; and more."*
- **Dialectic Agent.** *"The Dialectic Agent replaces a prior fixed-path architecture."* *"The model can search across everything Honcho knows about the target to synthesize the best possible answer to any query."*
- **`get_context()` method.** *"The `get_context()` method is unlimited, fast enough to call on every turn (~200ms), and solves statefulness with Honcho's opinion of the most relevant timely context automatically recruited and served."*

**Our restatement:** `[ASSERTED]`. The Honcho 3 architecture renames and upgrades the deriver/chat pipeline into two agentic LLM-orchestrated components. The Dreaming Agent is the consolidation-side operator; the Dialectic Agent is the retrieval-side reasoning surface. Both are *agentic* (LLM with tool use), not simple pipelines. The ~200ms `get_context()` latency claim is vendor-reported and not independently verified at this ingest.

### Neuromancer XR (August 2025)

**Vendor** ([Introducing Neuromancer XR](https://plasticlabs.ai/blog/research/Introducing-Neuromancer-XR), 2025-08-18): *"the first in a series of custom reasoning models that works by extracting and scaffolding atomic conclusions from user messages across two strictly defined levels of logical certainty: explicit and deductive."*

- **Training.** *"fine-tuning Qwen3-8B on a manually curated dataset mapping conversation turns to atomic conclusions"*, on *"a proprietary dataset of approximately 10,000 manually curated instances of conclusion derivation."*
- **Outputs.** *"a series of explicit and deductive conclusions that are stored in Honcho's peer-specific storage."* Stored as text.
- **Role in stack.** *"Whenever a message from a peer is stored in Honcho, Neuromancer XR reasons about it to derive explicit and deductive conclusions, which are then stored specifically to that peer."* Ingestion-time, write-side. Downstream retrieval is conventional (text-out via Dialectic Agent / `get_context()`).
- **Benchmark.** *"86.9% accuracy on the LoCoMo benchmark, compared to 69.6% using the base Qwen3-8B model, and 80.0% when using Claude 4 Sonnet as baseline."* Construct-validity note: LoCoMo measures long-conversation memory accuracy; Neuromancer XR is being scored on the *upstream extraction* task that feeds Honcho's storage, so the benchmark measures conclusion-derivation quality, not end-to-end agent recall.
- **Roadmap.** *"The next model in the Neuromancer series, Neuromancer MR (for meta-reasoning), will be in charge of [inductive and abductive reasoning]."* No timeline stated.
- **Rationale framing.** *"Our approach, on the other hand, shifts most of the load of reasoning about the peer from generation time to the earlier stages of the process, when messages are processed and ingested."*

**Our restatement:** `[ASSERTED]`. Neuromancer XR is a concrete production instance of a **learned consolidation operator on the write path** — exactly the shape Kyrja's [consolidation-channel](../concept/consolidation-channel.md) concept names. Two non-obvious points: (1) the operator is a *fine-tuned 7-8B model*, not a frontier-tier custom architecture — capability-and-cost achievable by a pre-seed-funded team; (2) the output is stored as *text*, which means the consolidation depth is bounded at the text/symbolic layer (depth 0-1 on the [substrate-depth ladder](../concept/consolidation-channel.md)), not at representation or weight depth. This is the cheapest viable rung of the consolidation-channel shape, and it ships.

### Memory-as-Reasoning thesis (August 2025)

**Vendor** ([Memory as Reasoning](https://plasticlabs.ai/blog/posts/Memory-as-Reasoning), 2025-08-19): *"Memory is not simply the encoding of perfect static data about the world and surfacing it when needed. Memory is making predictions about the environment based on incomplete data and checking at the margins for errors."*

On traditional retrieval: *"All are useful tools but they assume you already know what's worth storing and how to structure it. Once stored, those artifacts are static. The system's success relies on the search strategy aligning with whatever context was baked in during storage. Traditional storage-based approaches are brittle, deal poorly with contradictions and incomplete information."*

On their approach: *"LLMs excel at reaching explicit, deductive, inductive, and abductive conclusions quickly and consistently. This produces atomic, composable conclusions (observations about personal identity) that can be scaffolded on one another dynamically to produce new reasoning."*

**Our restatement:** `[ASSERTED]`. The Plastic Labs framing of memory-as-reasoning is operationally the same shape as Kyrja's "memory as the substrate the agent thinks with, not the database the agent thinks about" — *with one major caveat*: Plastic Labs implements the reasoning at the LLM-call layer (Dreaming Agent / Dialectic Agent are LLM-orchestrated), not at the model-internal layer. By the [memory-consumer-axis](../concept/memory-consumer-axis.md) classification, Honcho is memory-for-the-agent that uses LLM-call reasoning to do the consolidation/retrieval, not memory-for-the-model. Same philosophical destination; different architectural commitment.

### Licence

**Vendor:** AGPL-3.0.

**Our restatement:** `[ASSERTED]`. AGPL-3.0 triggers copyleft obligations for network services and is the most restrictive licence in the incumbent set. Procurement-friction is real; this is a structural adoption barrier for enterprise teams that the architectural cleverness has to clear.

### Benchmark claims

**Vendor:** Commit-tagged reproducible benchmark results (better practice than most competitors). Claims include 90.4% LongMemEval, 89.9% LoCoMo, and best-in-class BEAM scores (0.630 at 100K, nearly doubling the BEAM paper's top score per vendor framing).

**Our restatement:** `[ASSERTED]`. Commit-tagging is a credibility-raising practice — repeat verification is at least mechanically possible. Numbers themselves are vendor-published and have not been independently re-run at this ingest.

### Adoption / company

**Vendor + press:** Built by Plastic Labs (NYC). Pre-seed funded. Hermes Agent integration (separate project, reportedly trending on GitHub) is the major distribution channel. Optimised for consumer personalisation use cases (therapy bots, tutoring, shopping companions) rather than engineering-team institutional memory.

**Our restatement:** `[ASSERTED]`. The consumer-personalisation framing matters for the [federation-access-patterns](../concept/federation-access-patterns.md) question — Honcho's peer model is single-user-deep, not multi-contributor-broad.

## Relevance to Kyrja

- Anchors [Honcho incumbent page](../incumbent/honcho.md).
- The Dreaming Agent + Dialectic Agent pattern is the closest existing-incumbent analogue to the [consolidation-channel](../concept/consolidation-channel.md) paradigm we are evaluating.
- The peer-pair-keyed collections (observer/observed) are a primitive that the [multi-agent-consistency](../open-question/multi-agent-consistency.md) question should engage with.
- **Memory-consumer-axis classification:** Honcho is firmly *memory-for-the-agent* (text-out via tool context). It does **not** occupy the open cell of the [memory-consumer-axis](../concept/memory-consumer-axis.md) 2×2 — outside primary LLM × memory-for-the-model. The [memory-caddy](../open-question/memory-caddy.md) prior-art check (the reason for this 2026-05-15 ingest) is therefore unresolved by Honcho; no representation-out memory model is shipping here.
- **Concrete prior art for the consolidation-channel write path.** Neuromancer XR — fine-tuned Qwen3-8B, ~10k manually curated training instances, atomic-conclusion extraction at ingestion time — demonstrates that a learned write-side consolidation operator is buildable by a small team at commodity-fine-tune cost. The operator's output depth (text storage) is the *cheap rung* of the substrate-depth ladder; representation- or weight-depth consolidation operators remain unbuilt in the incumbent set.

## Archive location

Not a single artifact; rolling vendor material. To verify a specific quantitative claim, fetch from the docs URL above (claims are volatile; commit-tags on benchmark results are the most stable anchor).

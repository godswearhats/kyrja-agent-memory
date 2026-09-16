---
type: decision
name: Datadog-of-memory — enterprise-scale memory infrastructure as commercial vehicle
status: ACTIVE
last_ingested: 2026-05-20
sources: []
tags: [path-decision, commercial, infrastructure, enterprise, saas, bolt-on, wedge]
---

## Status note (updated 2026-05-20 — direction ratified, ownership transferred)

**Ratified 2026-05-20** as Kyrja's commercial direction by AJ + Eira (product-side discussion) + AJ's trusted human advisors. The commercial-track ownership transferred to **Eira (coral)** as of the same date — see coral for ongoing commercial work (MVP, TAM/SOM, competitive analysis, GTM, cap tables).

**Important framing correction** vs. this page's original draft: the ratification is **not** a supersession of [tier-3-4-as-wedge](./tier-3-4-as-wedge.md) or a demotion of caddy research to "v3+ exploration." Per [caddy-as-research-program](./caddy-as-research-program.md) (2026-05-20), commercial track and research track are **decoupled parallel tracks** at this stage:

- **Commercial track (Eira / coral):** Datadog-of-memory as documented in this page. Bolt-on infrastructure.
- **Research track (Nils / wiki):** Caddy is a research program; active load-bearing T4 research targets (T_A1b, K2+T_A3) are ordered into a stack-ranked research backlog. Falsifiability and pre-registration discipline maintained.

The original draft's "caddy → v3+ exploration after PMF" framing **does not match AJ's 2026-05-20 position**: AJ explicitly said *"This does not stop the research, nor the experimentation. ... we can just focus our time on the science!"* Caddy research continues now, in parallel with Eira's commercial work; data and design from the eventual product *may* inform caddy decisions later, but coupling is "a long way away yet" (AJ 2026-05-20).

This page is retained as the **commercial-direction decision record**. Detailed commercial-execution content (the "Commitments → Commercial vehicle / Wedge dimensions / Pre-commit validation" sections below) describes the direction at the time of ratification; ongoing execution lives in Eira's coral folder and may diverge from this snapshot as Eira's work proceeds.

## Decision

Adopt **Datadog-of-memory** as Kyrja's commercial direction: enterprise-scale memory infrastructure for the agentic AI era. The company ships memory **infrastructure** (write/query/RBAC/audit/multi-model/on-prem-deploy) as a platform.

The within-family bolt-on-vs-caddy comparison from [caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md) is resolved commercially in favour of bolt-on. The technical case for caddy (tier 3-4 capability) is not refuted; the *commercial* case for caddy (frontier-lab competition or acquisition exit at startup timescale) is. Caddy stays an **active research program**, decoupled from this commercial decision, per [caddy-as-research-program](./caddy-as-research-program.md).

## Motivation

Three signals converged 2026-05-19 → 2026-05-20:

**1. Carey signal (sounding board, warm-money intro).** Verbatim: *"It's super fascinating man. It all plays into AGI and the literal future of mankind . . . as a PhD project it would be a 10/10 . . . but does it make immediate business sense? Tough one."* Carey explicitly supports a SaaS + enterprise on-prem/private-cloud license model with caddy-shaped research as a later-stage internal-team activity, not the founding bet. The funded-micro-lab posture (per project memory, pre-2026-05-20) was research-program-shaped with acquisition exit; Carey's signal is that warm-money in his network funds startup-shape, not research-program-shape.

**2. Glean datum (AJ's day-job evidence).** Developer-experience teams at AJ's enterprise are recommending "use Glean MCP" as the memory solution — index documents in wikis/Drive/GitHub and let retrieval sort it out. Reading: (a) the enterprise "memory problem" has been *de facto redefined as an indexing problem* and assigned to incumbent search vendors; (b) the bar is currently very low (text-in-wiki + crawler counts as "memory"); (c) the bar is **transitional** — half of teams still hand-write code; once agentic adoption deepens, the gap between "indexed documents" and "memory that remembers what your agent did last week across multiple models" becomes felt. The window opens precisely because the current default is sloppy.

**3. Datadog-of-memory analog (structural, not aspirational).** Datadog won observability not by being "better monitoring" but because every existing monitoring tool (Nagios, pre-pivot New Relic, Splunk) was retrofitted from on-prem VM-era. Datadog built the new substrate while everyone else upgraded the old one. The structural parallel: every memory incumbent — Mem0, Letta, Zep, Cognee, LightMem, Engramme — is a retrofit of *single-developer-RAG* into something that pretends to scale. None were architected for ingest rate, query rate, multi-user RBAC, multi-model retrieval consistency, audit, programmatic forget, on-prem deploy *as primitives*. Same opening Datadog had, same shape of moat (built-for-the-era infrastructure that retrofits can't catch).

**Multi-model is the structural moat against frontier labs.** Frontier labs (Anthropic, OpenAI, Google) ship memory features inside their own products, but enterprises explicitly refuse vendor lock-in — teams use Cursor with Claude + GPT-5 + Gemini interchangeably, route different task shapes to different models. A memory layer that lives *outside* any single model provider serves the multi-model reality; a vendor-bundled memory feature does not. This is the structural reason caddy (vendor-locked to whichever open-weights base we co-train) is commercially worse than bolt-on, not just operationally worse.

## Commitments

**Commercial vehicle.**
- SaaS-with-enterprise-on-prem/private-cloud license model. Standard B2B SaaS funding pattern (ACV, NRR, gross-margin metrics; 10-15x ARR multiples).
- Platform-shape, not product-shape. MVP is the core write/query/RBAC primitive; additional products (governance dashboard, audit UI, multi-model router, integrations marketplace) hang off it over time.
- First vertical: **enterprise AI coding deployments.** Fortune 500 internal AI coding rollouts where multi-model + scale + RBAC + governance all bind hard and incumbents don't fit. Preserves the prior coding-as-bounded-domain commitment as a beachhead; generalises to other enterprise AI workloads (support agents, internal-RAG, sales-ops AI) once landed.

**Wedge dimensions (load-bearing differentiators).**
- **Ingest rate.** Incumbent users complain about write latency. Target: async/batched write that doesn't block the agent; the synchronous handshake hits a defensible p99 (specific number to be derived from incumbent-user-complaint quantification).
- **Query rate.** Incumbent users complain about retrieval latency. Target: sub-50ms p99 for typical query, scaling horizontally on cloud compute.
- **Multi-user/RBAC within tenant.** Project-scoped, user-scoped access control. The real value beyond multi-tenant cloud primitives — a single tenant controls which memories live on which projects and who can access them.
- **Multi-model retrieval consistency.** Memory written under Claude-context retrievable correctly into GPT-5 / Gemini / Mistral prompts. Research-now-load-bearing; currently absent from wiki research stack.
- **Governance primitives.** Programmatic forget (GDPR Article 17), audit log, retention policy, data residency, on-prem deploy. Architecture-level, not features bolted on later. *The eBay-patent precedent ([WO 2018/191879 A1, US 10,691,485 B2](../concept/discrete-unit-memory-architecture.md)) is directly relevant credibility here.*

**Wedge non-dimensions (commodities, not differentiators).**
- Number of users, memories/user: scale horizontally on cloud compute. Cassandra/Spanner/equivalent primitives handle this.
- Multi-tenant isolation: cloud primitives (separate VPCs, separate keys, separate accounts where required). Not Kyrja's job to reinvent.
- Database/cloud primitives in general: lean on them. *"Why reinvent a perfectly good wheel?"* — AJ 2026-05-20.

**Wedge non-wedge — out of scope for this commercial decision (research-track items, owned by Nils/wiki).**
- Cog-sci memory mechanisms (event segmentation, schema-fit consolidation, salience-modulated decay, soft composition, pattern completion in value-space). Active research per [caddy-as-research-program](./caddy-as-research-program.md).
- Tier 3-4 retrieval (analogical, predictive). Active research goal; the wedge for the research program, not for the commercial product.
- T_A1b isolation de-risk experiment ([2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md)). Active research; not gating on the commercial product.

**Research-stack consequences (revised 2026-05-20).**
- The **commercial research stack** (scale, governance, multi-model retrieval consistency) becomes Eira's domain. Pages currently in the research wiki that are commercial-track may eventually migrate or be cross-referenced from .
- The **caddy research stack** (caddy, T_A1b/H44, K2+T_A3/H40, Norman-rubric, mechanism-gap-matrix) **continues as active research** per [caddy-as-research-program](./caddy-as-research-program.md). Not "v3+ exploration"; current work.
- The two tracks share concepts at the highest level (memory architecture for LLMs) but are not coupled at the implementation or experiment level at this stage.

## Pre-commit validation

Before committing engineering to MVP, four checks need to land:

1. **Competitive scan under the infrastructure lens.** Re-read [incumbent/mem0](../incumbent/mem0.md), [incumbent/letta](../incumbent/letta.md), [incumbent/zep](../incumbent/zep.md), [incumbent/cognee](../incumbent/cognee.md), [incumbent/lightmem](../incumbent/lightmem.md), [incumbent/engramme](../incumbent/engramme.md) for: published latency SLAs, multi-user RBAC, multi-model support, governance (audit/retention/forget/residency), enterprise deploy options. Existing pages have most of this — synthesise the gaps under the new framing.

2. **Latency-budget derivation.** Turn "incumbent users complain about latency" into specific numbers (their current p50/p99, the felt-pain threshold, the demo-worthy delta).

3. **Glean trajectory check.** 30-minute scan of Glean Agents roadmap on memory primitives in next 6-12 months. Adjacent-attacker timeline determines whether the wedge window is 36 months or 18.

4. **Carey conversation on SaaS+on-prem positioning.** Does his network confirm fundability under enterprise SaaS shape specifically? The prior conversation established research-shape was wrong; this conversation pins what specifically *is* right.

## Reversibility

**Expensive but not one-way.** Reversal means abandoning the Datadog-of-memory positioning and either (a) re-pitching caddy-as-research-program (which Carey explicitly counseled against), (b) pivoting to a different commercial vehicle (consumer personalisation, vertical-specific, developer-tools-only).

Natural reversal triggers:
- The "cobbled-together for single developer" claim falls — a current incumbent ships infrastructure-shape architecture in the next 6-12 months, closing the window.
- Agentic adoption stalls materially (technical limits, regulatory crackdown, hype-cycle correction). AJ's "half our teams still write code by hand" observation is the inverse signal — current state is *positive* for timing.
- MVP fails to land paying customers because the infrastructure differentiator isn't compelling enough (enterprises just want what Glean ships, even at scale).
- Pre-commit validation surfaces that the four wedge dimensions aren't actually load-bearing for the buyer (e.g., RBAC isn't valued, on-prem isn't required, latency isn't the felt pain).

Pre-registration discipline: the four pre-commit checks above are the gate, not motivational re-interpretation later.

## Related

- [caddy-as-research-program](./caddy-as-research-program.md) — the paired 2026-05-20 decision. Together: this page records the commercial-direction ratification (Datadog-of-memory, bolt-on, owned by Eira); the paired page records the research-program framing (caddy as research, owned by Nils/wiki, decoupled from commercial).
- [tier-3-4-as-wedge](./tier-3-4-as-wedge.md) — the research-track wedge. NOT superseded by this decision; tier 3-4 stays the active research goal.
- [caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md) — the within-family comparison; commercial picks bolt-on, research continues on caddy.
- [k2-ta3-deferred-to-v2](./k2-ta3-deferred-to-v2.md) — REVERSED 2026-05-20. Historical record of the prior MVP-product-shaped K2+T_A3 deferral; the deferral logic dissolved with the MVP frame.
- [tool-chain-wedge-as-adoption-path](./tool-chain-wedge-as-adoption-path.md) — prior bottom-up adoption path. Likely needs re-evaluation under enterprise SaaS positioning; flagged for review on ratification.
- [repo-bounded-scope](./repo-bounded-scope.md), [org-wide-store-repo-scoped-queries](./org-wide-store-repo-scoped-queries.md) — scale-shape decisions that survive the pivot and become more load-bearing.
- [cascading-failures-reanchor](./cascading-failures-reanchor.md), [structured-filter-first](./structured-filter-first.md), [precision-over-recall](./precision-over-recall.md), [write-side-quality-gate-deferrable](./write-side-quality-gate-deferrable.md) — scale-/quality-shape decisions that become central under this candidate.
- [memory-caddy](../open-question/memory-caddy.md) — the open question this candidate effectively closes (commercial path = bolt-on; caddy is v3+ research).
- [cost-curve-at-scale](../open-question/cost-curve-at-scale.md), [billion-scale-benchmark-gap](../open-question/billion-scale-benchmark-gap.md), [partition-strategy](../open-question/partition-strategy.md) — scale-research pages that become directly load-bearing.
- [discrete-unit-memory-architecture](../concept/discrete-unit-memory-architecture.md) — the family this commits to; the eBay-patent precedent table is now directly load-bearing for commercial credibility.

## Source archive

- AJ-Nils conversation 2026-05-19 (commercial-direction revisit pending-Carey).
- AJ-Nils conversation 2026-05-20 (Datadog-of-memory framing crystallization; multi-model structural moat; scale + RBAC + governance as wedge dimensions).
- Carey conversation (pre-2026-05-20; sounding-board check): verbatim quote on PhD-vs-business-sense.
- Day-job evidence (AJ enterprise): developer-experience team recommending Glean MCP as memory solution; contextualised by "half our teams still write code by hand on the daily."

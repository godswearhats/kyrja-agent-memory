---
type: open-question
name: Salience signal — how do agent-memory systems compute "this matters" reliably?
status: OPEN
last_ingested: 2026-05-17
sources: [../source/yang-et-al-2024-selection-of-experience.md, ../source/redondo-morris-2011-stc.md, ../source/mcclelland-mcnaughton-oreilly-1995-cls.md]
epistemic_tags: [asserted, speculated]
tags: [salience, importance-scoring, admission-control, consolidation, deferred-persistence, load-bearing, aj-originated, matrix-walkthrough-pattern]
---

## The question

`[ASSERTED]` During the 2026-05-17 M15 walk (Redondo & Morris 2011 synaptic tagging and capture), AJ identified the **salience signal as the load-bearing variable across multiple matrix rows**, downstream of the architectural choice. The exact framing from his mid-walk comment:

> "I think there are probably other ways to implement the same effect... we've already talked about having a hot store for all events, and then some offline decision making process that promotes to cold store, this just happens to be biology's way of handling it. Whether we use this mechanism or a different one, understanding which memories are salient seems critical."

The question:

> **How does an agent-memory system reliably compute which memories matter, given that (a) the answer often depends on events that haven't happened yet, (b) the current state of the art (LLM-call importance scoring at write time) ignores temporal non-locality, and (c) biology uses convergent multiple modulatory systems rather than a single signal?**

Salience computation is the input variable to:
- Admission policies (M05 schema-fit modulation, [admission-control](../concept/admission-control.md))
- Consolidation operators (M03 replay-mediated transfer, [consolidation-channel](../concept/consolidation-channel.md))
- Forgetting policies (M17 active forgetting, [H34](../hypothesis/H34-forgetting-scores.md))
- Selection-for-replay (M04 — [Yang 2024](../source/yang-et-al-2024-selection-of-experience.md))
- Tag-to-PRP commit gating (M15 [synaptic tagging](../source/redondo-morris-2011-stc.md))

All five matrix rows + concepts stall on the same problem. The architectural choice (STC-shape vs hot-store-with-promotion vs anything else) is largely a downstream implementation detail. The salience signal is invariant across architectures and not yet solved by the field.

> **M17 confirms the fifth-row dependency (2026-05-17 M17 walk):** the M17 walkthrough confirmed [active forgetting](../source/hardt-nader-nadel-2013-active-forgetting.md) as the fifth matrix row whose policy gates on this signal. Hardt et al.'s metaplastic regulation (recent strong memories have reduced GluN2b → resistance to depotentiation → resistance to forgetting) is a salience-driven decay-rate modulator. The five-row dependency strengthens the "load-bearing input variable" claim — multiple architecturally distinct mechanisms all stall on the same upstream computation, suggesting the salience problem is more fundamental than any one architecture's design choice.

> **Query head as the online-side salience computation (2026-05-17 M16 walk):** A dedicated query head in the golfer (a separate attention head whose sole job is producing memory queries — see [concept/caddy § Interface fork](../concept/caddy.md)) is the explicit *ask-the-caddy* operator at runtime. Its output is "what does the golfer need to know right now" — which is a salience computation by another name. **The query head *is* the learned salience function on the read side.** [H42](../hypothesis/H42-learned-salience-function.md) becomes the falsifiable claim that this learned function beats LLM-call importance scoring at lower cost. The query head is the online complement to the off-line salience signal that drives consolidation, admission, and forgetting; both are applications of the same upstream computation at different surfaces (online runtime vs off-line batch).

## Why it matters

`[ASSERTED]`

- **If a robust, cheap salience signal exists:** the caddy gains cheap-write semantics with temporal-non-locality. Architectural choices (STC vs hot-store) become reducible to engineering trade-offs. Multiple matrix rows (M03, M04, M05, M15, M17) reduce to instantiations of the salience-input + persistence-operator decomposition.
- **If salience cannot be reliably computed cheaply:** the field's current LLM-call importance scoring becomes the local optimum and admission-control-shape designs dominate. The biological off-line-decision-making architecture becomes uncompetitive against simpler at-write-time scoring. Consolidation-channel-shape products optimise the LLM-call cost rather than the architecture.
- **If salience must be computed *post-hoc* via outcome attribution:** the architecture forces an episode-with-outcome structure that not all agent tasks have. Conversational agents, long-running assistants, and exploratory tasks become structurally harder than reward-driven tasks.

The question gates `[caddy](../concept/caddy.md)` design choices, `[consolidation-channel](../concept/consolidation-channel.md)` design choices, and the broader bolt-on-vs-caddy fork.

## What evidence would resolve it

`[SPECULATED]` Multiple paths exist; ordered by cost-feasibility:

1. **Benchmark learned vs heuristic salience functions** (cheapest first step). [H42](../hypothesis/H42-learned-salience-function.md) is the formal hypothesis. Train a small learned salience function on (retrieval-success, memory-features, downstream-outcome) tuples generated by a baseline agent. Compare to LLM-call importance scoring on a multi-task agent benchmark, controlling for storage cost. Outcome: directional evidence on whether learned-salience is a viable architectural commitment.

2. **Ablate salience signals in current bolt-on systems.** Take Mem0 / Letta / Zep and run with: LLM-call only, LLM-call + surprise, LLM-call + outcome-attribution, surprise-only. Compare retention quality. Reveals which signals carry information.

3. **Map biology's convergent signals to software equivalents.** Behavioural tagging requires dopamine + novelty + protein synthesis. Surprise + outcome + reflection is the rough software analogue. Test whether convergent multi-signal salience outperforms single-signal.

4. **The Norman rubric's Box 4 benchmark proposal** ([source/dong-2025-norman-episodic](../source/dong-2025-norman-episodic.md)) may operationalise this evaluation in the published-benchmark-tracking sense.

**Adequate signal:** for the load-bearing claim ("salience is the bottleneck"), even one task where learned-salience clearly beats LLM-call salience at lower cost is informative. The cleaner falsification handle is whether *both* learned and heuristic approaches fail equally on a task that has no clean outcome signal — that would suggest salience is fundamentally hard and architectures should design around the absence of it rather than for its presence.

## Sub-questions

`[SPECULATED]` The question decomposes into several narrower threads:

1. **Which salience signals are actually computable cheaply at the agent loop?** Surprise (token-likelihood) is free; outcome attribution requires episode boundaries; reflection requires LLM-calls; user feedback is sparse. The cost-vs-signal-quality Pareto frontier is unmapped.

2. **What latency profile does each signal have?** Surprise is immediate; outcome attribution is delayed; reflection can be scheduled. STC-shape architectures specifically need delayed-signal capability; admission-shape architectures specifically need immediate-signal capability. Different architectures have different signal requirements.

3. **Is salience task-dependent or general?** A learned salience function trained on one task class may not transfer. If yes, the function is small but per-task — a deployment-engineering question. If no, a general-purpose salience model becomes feasible.

4. **Do convergent multi-signal scores beat single-signal scores?** Biology uses dopamine + novelty + attention + valence converging. Software systems mostly use single proxy signals. Empirical question.

5. **Can salience be computed from retrieval-graph topology alone?** Memories that are referenced by many others, retrieved often, or sit at high-betweenness positions in a memory graph carry signal independent of content-based scoring. Bootstrap problem (need some memories first), but eventually self-bootstrapping.

6. **What's the relationship to importance-scoring in current bolt-on products?** Mem0, Letta, Zep, Honcho all do *some* form of importance scoring. None publish their function in detail. Reverse-engineering this from their APIs may give the floor of the field's current state.

7. **Does the architecture's salience-signal sensitivity change the system's behaviour at retrieval time?** A poorly-tuned salience function may produce a memory store that's biased toward easy-to-score content, missing important-but-hard-to-score content. The retrieval failure mode is then an artifact of the salience function, not of retrieval itself.

8. **Is post-hoc salience (outcome attribution) compatible with the STC-shape architecture's ~90-min window?** Biology's window is bounded; software systems can have arbitrary windows. What window-length is right for typical agent loops?

## Salience signal candidates with rough latency profiles

`[ASSERTED]` Sketch of the landscape (not exhaustive):

| Signal | Latency | Source | Cost | Notes |
|---|---|---|---|---|
| Surprise / prediction error | Immediate | LLM forward-pass entropy | Free (already computed) | The cheapest single signal; how informative is open |
| Reflective importance | Immediate-ish | LLM-call asking "is this important?" | Expensive per write | The field's current default |
| Outcome attribution | Delayed | Backwards from task outcome | Cheap per memory, expensive to define outcome | STC's biological substrate |
| User feedback | Variable | User reactions, corrections, follow-ups | Sparse and noisy | Strong when present |
| Inter-memory reference | Delayed | Retrieval frequency, graph centrality | Bootstrap problem | Self-supervised once seeded |
| Cross-session convergence | Very delayed | Multiple agents/sessions converge | Slow but reliable signal | Only relevant at scale |
| Salience-modulator analog | Immediate | Engagement, dwell-time, downstream-action density | Cheap, requires environment integration | Biology's dopamine equivalent |

Each carries information; none has been demonstrated sufficient alone. The likely correct answer is convergent multi-signal, as biology uses.

## Related

`[ASSERTED]`

- [[H42-learned-salience-function]] — first falsifiable claim derived from this open question
- [[mechanism-gap-matrix]] — multiple rows (M03, M04, M05, M15, M17) depend on this signal
- [[consolidation-channel]] — Kyrja's primary wedge; salience is its load-bearing input
- [[admission-control]] — admission policies are salience-application at write time
- [[H34-forgetting-scores]] — forgetting-as-learned-policy is the dual of salience-as-learned-policy
- [[H40-schema-fit-modulated-consolidation]] — schema-fit is one specific salience signal
- [[caddy]] — caddy commitment 2 (learned consolidation policies) is exactly the place a salience function lives
- [[memory-caddy]] — open design question for which a salience function is a prerequisite
- [[redondo-morris-2011-stc]] — STC's PRP-emission is the biological salience signal
- [[yang-et-al-2024-selection-of-experience]] — biological-level salience in SPW-R replay selection
- [[hardt-nader-nadel-2013-active-forgetting]] — metaplastic salience-gates-forgetting
- [[buzsaki-2015-spw-r]] — preconfigured-vocabulary framing has its own implicit salience question

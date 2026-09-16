---
type: concept
name: Cognitive maps and conjunctive coding — the hippocampal mechanism for relational binding
status: living
last_ingested: 2026-05-16
sources: [../source/josselyn-tonegawa-2020-engrams.md, ../source/mcclelland-mcnaughton-oreilly-1995-cls.md]
epistemic_tags: [asserted, speculated]
tags: [biology, hippocampal-mechanism, relational-binding, caddy-prior, m11-derivative, matrix-walkthrough-pattern]
---

## Definition

`[ASSERTED]` **Cognitive maps and conjunctive coding** name the hippocampal/entorhinal mechanism for binding events to positions in a structured relational space. The mechanism has three observable properties:

1. **Conjunctive units of encoding.** Hippocampal neurons fire for conjunctions of multiple cues (place × event × context), not for single dimensions. The atomic unit of biological memory is multi-dimensional binding, not single-key indexing.
2. **Multiple overlapping maps.** The same event has coordinates in many parallel cognitive maps simultaneously. Physical place, time, abstract feature spaces, goal proximity all coexist as independent coordinate systems.
3. **Domain-general structure.** The "map" mechanism evolved for physical navigation but applies to any relational space the agent moves through. Place cells aren't really place cells; they are *relational-position* cells where physical space is the evolutionarily ancient instance.

This concept exists because the M11 walkthrough (2026-05-15) surfaced that biological memory's atomic encoding unit is structurally richer than "store an event by timestamp" or "store an embedding by similarity." A caddy that aims to instantiate the [biological mechanism set](./mechanism-gap-matrix.md) needs this binding structure as an *architectural prior*, not as something that emerges from generic training. The page documents what the biology actually does so design discussions can be specific about which structural properties the architecture must support.

## The biology

### Place cells (the historical entry point)

`[ASSERTED]` O'Keefe & Dostrovsky 1971 discovered hippocampal neurons in rats that fire when the animal is in a specific location. Each cell has a *place field* — typically 10-30cm in rats — and different cells tile the available space. O'Keefe shared the 2014 Nobel Prize for the discovery and the subsequent cognitive-map framework.

`[ASSERTED]` Subsequent work showed the naming is misleading. What place cells encode is not pure location.

### Conjunctive coding — the atomic unit is multi-dimensional

`[ASSERTED]` Wood, Dudchenko & Eichenbaum 1999 (Nature 397:613-616) showed hippocampal cells encode **conjunctions** of multiple cues, not single dimensions:

- A cell that fires at location X may not fire at location X under a different task context.
- A cell that fires for "approach left arm of maze" may not fire for "approach right arm" even when both are at the same spatial location.
- Very few cells fire on any single dimension alone; the majority require specific *combinations* of place + event + context to fire.

The functional consequence: the hippocampus binds memories at the level of *what-happened-where-while-doing-what*, not at the level of any single dimension. This is fundamentally different from a vector database keyed by similarity in a single embedding space, or a key-value store keyed by a single identifier.

### Time cells — the same architecture encodes time

`[ASSERTED]` MacDonald, Lepage, Eden & Eichenbaum 2011 (Neuron 71:737-749) showed that when place is held constant (rat running on a treadmill during a delay period), the same hippocampal population encodes *elapsed time* — different cells firing at different time bins.

`[SPECULATED]` Interpretation: the hippocampus has a domain-general "binding-against-a-coordinate" mechanism. When the salient coordinate is space, it does place coding. When the salient coordinate is time, it does time coding. When the salient coordinate is something else, it presumably does that too.

### Temporal context as a read-side primitive (M13)

`[ASSERTED]` Time cells provide the *write-side* of temporal binding — events are bound to a temporal coordinate at encoding. [Howard & Kahana 2002 TCM](../source/howard-kahana-2002-tcm.md) (matrix row [M13](./mechanism-gap-matrix.md)) names the *read-side* counterpart: a slowly-drifting context vector that carries the "smell" of recent events and serves as a retrieval cue.

The mechanism: every memory trace is encoded with the current temporal context vector bound in. Retrieval reinstates the bound context, which then biases the next retrieval toward items whose stored contexts overlap — temporal contiguity (recall of one item biases recall of items experienced nearby in time) falls out of the mechanism without a dedicated parameter. The asymmetry (forward contiguity stronger than backward) emerges from a preexperimental-vs-newly-learned split in how context updates on retrieval.

`[SPECULATED]` The two primitives compose. Time cells (M11-walk material — write-side temporal binding) plus drifting context vector (M13 — read-side temporal cue) give the full *when* axis. Together with conjunctive coding's *what + where* binding, this is the complete hippocampal binding signature: *what + where + when*, each independently cueable, each bound into the same trace at encoding.

For a caddy implementation, the consequence is that the temporal coordinate is not a timestamp column. It is a continuous coordinate axis with the same architectural status as place/event/context — bound into traces at write, queryable as a retrieval cue at read. See [mechanism-gap-matrix M13](./mechanism-gap-matrix.md) and [H41 — temporal-context retrieval](../hypothesis/H41-temporal-context-retrieval.md) for the full development including the falsifier specification.

### Remapping — the map is context-dependent

`[ASSERTED]` Place cells exhibit two forms of context-dependent change ([Josselyn & Tonegawa 2020](../source/josselyn-tonegawa-2020-engrams.md) review and references therein):

- **Rate remapping** — same cells active in both contexts, different firing rates.
- **Global remapping** — different cell populations active in different contexts.

The functional consequence: there is no single "map of the world" in the hippocampus. Each context has its own map, and the mapping between context and active cell population is itself learned.

### Cognitive maps generalise beyond physical space

`[ASSERTED]` Constantinescu, O'Reilly & Behrens 2016 (Science 352:1464-1468) demonstrated that hippocampal/entorhinal grid-cell-style coding tiles *abstract conceptual spaces*, not just physical space. Human subjects learned a 2D conceptual space (constructed from bird-leg-length × bird-neck-length); fMRI showed grid-cell signatures over the abstract space identical to those over physical space.

`[ASSERTED]` Aronov, Nevers & Tank 2017 (Nature 543:719-722) showed analogous results in rats navigating a *sound-frequency* "space" — sweeping pitch up and down a continuous tone landscape. The same hippocampal cells that do physical place coding do abstract relational position in any continuous space the animal navigates.

`[SPECULATED]` Synthesis: the hippocampal mechanism is **map-of-relations**, with physical space being the evolutionarily ancient instance. The architectural prior is "tile any structured domain the agent moves through." For an artificial agent operating in code, conversation, or task space, the relevant maps are those domains — not physical space.

### Multiple overlapping maps run in parallel

`[ASSERTED]` from the collective findings above. A single event in biological memory has coordinates in multiple cognitive maps simultaneously:

- Physical location at time of event
- Elapsed time since event
- Goal/task context active at time of event
- Reward/salience level associated with event

These coordinate systems are not collapsed into a single representation. They are stored as separable bindings that can be queried independently. A retrieval cue matching any of them activates the bound event.

`[SPECULATED]` This is structurally different from any current artificial memory architecture. Vector databases collapse all signals into a single embedding space; knowledge graphs use a single relational structure; episodic stores use timestamp ordering. None maintain multiple parallel independently-queryable coordinate systems.

## Reward and salience firing

`[ASSERTED]` The biology binds reward as a first-class dimension, not as metadata on stored events.

- **Goal cells** fire preferentially at reward locations (Hollup, Molden, Donnett, Moser & Moser 2001, J. Neurosci.).
- **Replay over-represents rewarded trajectories** (Singer & Frank 2009, Neuron 64:910-921) — sequences leading to reward are replayed disproportionately during sharp-wave ripples.
- **Reverse replay** specifically follows reward events (Foster & Wilson 2006, Nature 440:680-683) — the replay runs from the salient outcome backwards through the preceding trajectory.
- **Dopaminergic modulation** — VTA dopamine neurons fire on reward-prediction-error (Schultz, Dayan & Montague 1997, Science 275:1593-1599) and modulate hippocampal synaptic plasticity, biasing what gets consolidated.

`[SPECULATED]` Interpretation: salience is not a tag on stored events; it is a *coordinate axis* in the binding structure. The hippocampus stores "where this event sits in the reward landscape" alongside "where it sits in physical space" and "when it happened." Reverse-replay is then automatic credit assignment along the reward axis. See [consolidation-channel](./consolidation-channel.md) for the credit-assignment framing.

## Implications for an agent memory architecture

`[ASSERTED]` The biology suggests the atomic unit of memory for an agent should be conjunctive, with multiple parallel maps:

- **Position(s)** in one or more relational maps — for a coding agent, possibly: file-tree position, call-graph position, commit-graph position, dependency-graph position.
- **Event** — what action was taken.
- **Outcome** — environmental result (build pass/fail, test result, merge, user response).
- **Context** — active goal or task at time of event.
- **Salience** — reward/surprise level (cross-link to retrospective surprise — see [memory-caddy § granularity-ladder of surprise](../open-question/memory-caddy.md#sidebar--granularity-ladder-of-surprise)).

`[SPECULATED]` This is meaningfully richer than what current bolt-on memory systems store. Mem0/Cognee/Letta/Zep all store events with metadata; none maintains multiple parallel cognitive maps with conjunctive binding as a first-class architectural property.

### Architectural priors a caddy model would need

`[SPECULATED]` Biology cheats — it has hundreds of millions of years of evolutionary pre-bias. Pure tabula-rasa learning of cognitive-map structure would be intractable. The hippocampus has *architectural priors* that constrain what schemas it can learn. A caddy would need analogous priors:

- **Discrete addressable memory units** (basic binding primitive)
- **Continuous coordinate systems** (the grid-cell prior — given a domain, can tile relational positions)
- **Conjunctive binding mechanism** (something like attention but discrete and addressable)
- **Multi-scale granularity** (atomic events, short sequences, full episodes — each bindable independently)
- **Salience-modulated plasticity** (a built-in plasticity-rate signal)
- **Multiple parallel coordinate systems** (the maps are not collapsed into one)

With these priors in place, the *content* of bindings (what counts as "place" in this domain, what counts as "event," what counts as "outcome") can be learned from experience. This is the **schema induction** that AJ surfaced during the M11 walkthrough — biology learns the bindings, not the binding architecture. See [memory-caddy § schema-induction](../open-question/memory-caddy.md) for the path-decision implications.

## How current ML touches fragments of this

`[SPECULATED]` Adjacent ML work has reached parts of the structure without integration:

- **World models** ([Ha & Schmidhuber 2018](../source/ha-schmidhuber-2018-world-models.md), Dreamer line) — learn structured latent representations of an environment. Closest to biological cognitive maps. But the representations are *continuous latents*, not discrete addressable memory units with conjunctive binding.
- **Slot attention / object discovery** (Locatello et al. 2020) — models that learn to discover discrete entities from unstructured input. The slot abstraction is closer to "addressable memory unit" than typical embeddings. But these are typically used for visual scenes, not for agent memory.
- **Differentiable Neural Computers** (Graves 2016) — read/write memory with content addressing. Has the addressable-unit property; lacks conjunctive coding and multi-map architecture.
- **MERLIN** ([Wayne et al. 2018](../source/wayne-2018-merlin.md)) — external memory matrix with content-addressed read head; closest existing template for parts of the caddy. Single map, no explicit conjunctive coding.
- **Grid-cell-inspired representation learning** (Whittington et al. 2020 Tolman-Eichenbaum Machine) — explicitly grids-cells-as-architectural-prior, the closest direct ML implementation of the cognitive-maps framing. Not yet at agent-memory scale.

What none of these does: **discrete addressable memory units with multi-dimensional conjunctive binding across multiple parallel cognitive maps, salience-modulated, consolidated from a hot store via replay.** That combination is the caddy-with-biological-priors frontier. Fragments exist. Integration doesn't.

## Scope limits

- This page documents the **biological mechanism set** as it stands in 2026. It does not commit Kyrja to any specific architectural translation of these priors.
- Many of the cited primary sources have not yet been read verbatim (see Source archive). The high-level picture is well-established neuroscience consistent across textbook treatments, but specific numerical claims (place-field sizes, compression ratios, etc.) should be verified against primary sources before becoming load-bearing for Kyrja design decisions.
- The page does not address the *temporal* aspect of cognitive maps (how the maps update over time as the agent learns) — that is covered in [consolidation-channel](./consolidation-channel.md) and [mechanism-gap-matrix](./mechanism-gap-matrix.md) M11.

## Related

- [[mechanism-gap-matrix]] — this concept is derivative of the M11 walkthrough; the biological priors documented here are what M11's consolidation mechanism operates on. M13 (temporal context as retrieval primitive) extends this concept's *when* axis to the read side.
- [[caddy]] — the canonical architectural definition of the within-family alternative to bolt-on. The architectural priors documented on this page are candidate inductive biases a caddy implementation would bake in.
- [[discrete-unit-memory-architecture]] — the family-level architectural framing; cognitive-maps-and-conjunctive-coding is the *content* of what a discrete-unit family member needs to support.
- [[consolidation-channel]] — the operator that moves cognitive-map bindings from hot to cold store; cross-link M11 walkthrough findings on credit assignment and reverse replay.
- [open-question / memory-caddy](../open-question/memory-caddy.md) — schema-induction discussion; this page documents what biology suggests the *architectural priors* should be, the open-question discusses whether bolt-on can do schema induction with these priors too. The 2026-05-16 M12+M13 walk subsection extends the binding architecture documented here to the *when* axis read-side.
- [H41 — temporal-context retrieval](../hypothesis/H41-temporal-context-retrieval.md) — falsifiable hypothesis derived from M13; the read-side counterpart to time-cell write-side binding documented here.
- [[complementary-learning-systems]] — McClelland 1995 grounding; the hippocampal fast store implements these binding mechanisms.
- [[silent-engrams]] — M06 of the matrix; cognitive-map coordinates can be silent (stored but cue-inaccessible).

## Source archive

Pending verbatim reads (cited inline above; promote to `source/*` if any becomes load-bearing for a specific Kyrja design decision):

- **Wood, Dudchenko & Eichenbaum 1999** — Nature 397:613-616. Conjunctive coding in hippocampal cells.
- **MacDonald, Lepage, Eden & Eichenbaum 2011** — Neuron 71:737-749. Hippocampal time cells.
- **Constantinescu, O'Reilly & Behrens 2016** — Science 352:1464-1468. Grid-cell coding in abstract conceptual spaces.
- **Aronov, Nevers & Tank 2017** — Nature 543:719-722. Hippocampal coding in sound-frequency space.
- **Hollup, Molden, Donnett, Moser & Moser 2001** — J. Neurosci. Goal cells.
- **Singer & Frank 2009** — Neuron 64:910-921. Over-representation of rewarded trajectories in replay.
- **Foster & Wilson 2006** — Nature 440:680-683. Reverse replay after reward.
- **Schultz, Dayan & Montague 1997** — Science 275:1593-1599. Dopamine reward-prediction-error signal.
- **Whittington et al. 2020** — Cell 183:1249-1263. Tolman-Eichenbaum Machine. (ML translation of grid-cell priors.)
- **O'Keefe & Dostrovsky 1971** — Brain Research 34:171-175. Original place-cell discovery.

These citations are informational pending Kyrja decision-level use. The conceptual synthesis in this page is the M11 walkthrough's working understanding; the source pages would be the verbatim record if any specific claim becomes load-bearing.

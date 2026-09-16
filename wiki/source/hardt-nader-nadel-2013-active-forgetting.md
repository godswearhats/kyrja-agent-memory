---
type: source
name: "Hardt, Nader & Nadel 2013 — Decay happens: the role of active forgetting in memory"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [cog-sci, active-forgetting, decay, ampa-internalization, pkm-zeta, promiscuous-encoding, gist-formation, m17, inverse-mechanism, load-bearing]
---

## Citation

Hardt, O., Nader, K., & Nadel, L. (2013). *Decay happens: the role of active forgetting in memory.* Trends in Cognitive Sciences, 17(3), 111–120. DOI: 10.1016/j.tics.2013.01.001. Published March 2013.

## Location

- PDF: [library/papers/hardt-nader-nadel-2013.pdf](../../../research/library/papers/hardt-nader-nadel-2013.pdf) (10 pages)
- DOI: 10.1016/j.tics.2013.01.001 (https://doi.org/10.1016/j.tics.2013.01.001)
- McGill University, Department of Psychology, Montréal (Hardt, Nader); University of Arizona, Department of Psychology (Nadel)

## Why this paper is load-bearing for Kyrja

This paper anchors **M17 (active forgetting)** — the first row in the matrix that catalogues a **constructive forgetting mechanism**. All matrix rows M01-M16 catalogue storage, consolidation, or retrieval primitives. M17 is the inverse: a regulated removal process that operates as a default state and is gated by salience signals to preserve important memories.

The structurally novel claims:

1. **Memory loss is active, not passive.** Forgetting is a well-regulated process operating predominantly during sleep, systematically removing selected memories. Standard view: decay is radioactive-style passive process. Hardt et al.: decay is a regulated, modulable, salience-gated mechanism.

2. **"Promiscuous encoding + selective forgetting" is the biological architecture.** The brain encodes liberally because significance often becomes evident only after the fact. Forgetting policies — not encoding gates — determine what survives.

3. **Forgetting generates abstraction.** Hippocampal contextual traces decay faster than neocortical content traces. Over time, memories transition from episodic specifics to semantic gist. **This is biology's automatic mechanism for extracting regularities from experience — by forgetting the specifics.**

4. **Different forgetting mechanisms in different brain areas.** Pattern-separated systems (hippocampus) decay; pattern-overlapping systems (early sensory cortex) suffer interference. Both serve forgetting, but via different mechanisms.

For Kyrja, this directly informs:

- [consolidation-channel](../concept/consolidation-channel.md) — forgetting is the partner operator to consolidation. The two together maintain capacity AND build abstraction.
- [H34 — forgetting scores](../hypothesis/H34-forgetting-scores.md) — already-existing hypothesis on learned forgetting policies; this paper is the cog-sci anchor.
- [open-question/memory-caddy.md](../open-question/memory-caddy.md) — a caddy with active forgetting as a learned policy is structurally novel; no current architecture has graded, metaplastically-modulated forgetting.
- The **fourth unification observation** in the matrix walk: M03 (consolidation) and M17 (active forgetting) may be the same sleep-based replay mechanism viewed from opposite angles.

## Key claims (with our restatements)

### Thesis (abstract, verbatim)

> "Although the biological bases of forgetting remain obscure, the consensus among cognitive psychologists emphasizes interference processes, rejecting decay in accounting for memory loss. In contrast to this view, recent advances in understanding the neurobiology of long-term memory maintenance lead us to propose that a brain-wide well-regulated decay process, occurring mostly during sleep, systematically removes selected memories. Down-regulation of this decay process can increase the life expectancy of a memory and may eventually prevent its loss. Memory interference usually occurs during certain active processing phases, such as encoding and retrieval, and will be stronger in brain areas with minimal sensory integration and less pattern separation. In areas with efficient pattern separation, such as the hippocampus, interference-driven forgetting will be minimal, and, consequently, decay will cause most forgetting."

### Two forgetting mechanisms — interference vs decay (pp 112-113)

`[ASSERTED]` Two classes of memory loss with different mechanisms:

- **Interference-driven forgetting** — dominates in densely-overlapping representational areas (early sensory cortex). Happens during active processing (encoding, retrieval). New similar inputs overwrite or scramble existing representations.
- **Decay-driven forgetting** — dominates in pattern-separated areas (hippocampus). Happens largely off-line (sleep). Active reversal of learning-induced synaptic potentiation.

`[ASSERTED]` Our restatement: forgetting is not one mechanism. The matrix has implicitly treated forgetting as a single phenomenon (e.g., in M11's catastrophic-interference framing). Hardt et al. partition it: pattern separation handles interference; decay handles capacity. The architecture has BOTH mechanisms operating in different subsystems.

### Promiscuous encoding (p112)

`[ASSERTED]` Verbatim:

> "Our proposal views forgetting of consolidated long-term memory as an active process that systematically removes learning-induced changes in synaptic potentiation over time. [...] In our view, decay-driven forgetting is a direct consequence of a memory system that engages in promiscuous encoding. The benefit of such promiscuity is access to a lot of information, so that 'choices' about what to keep and what to delete can be made off-line, mostly during certain sleep phases."

> "An organism cannot know a priori whether a long-lasting memory should be formed, and if so, which aspects of an event should be encoded and which aspects ignored. The ability to quickly acquire as much information as possible is highly adaptive, increasing the probability of having captured knowledge that might prove important later. Since significance often becomes evident only after the fact, preserving as much detailed information as possible is important."

`[ASSERTED]` Our restatement: **the intelligence is in the forgetting policy, not the encoding gate.** Biology's solution to the "what should I remember" problem is to encode everything and forget intelligently. AI memory architectures typically reverse this: they try to be smart at encoding (admission control, salience scoring at write time) and have weak or no forgetting. The biological architecture suggests the opposite tradeoff may be better.

### Pattern separation as the prerequisite for decay (Figure 1, pp 113-114)

`[ASSERTED]` Two-component memory framework:

- **Hippocampal component** — spatial-contextual index. Provides pattern separation: even similar inputs get orthogonal representations.
- **Neocortical component** — content representations. Dense overlap; vulnerable to interference without hippocampal support.

`[MEASURED]` From cited amnesic-patient studies (Cowan et al. 2004, McTighe et al. 2010, Dewar et al. 2007, 2009, 2012):

- Amnesic patients (compromised hippocampal function) show extensive interference even with brief delays
- "Memory retention in amnesic patients can be dramatically enhanced when periods of rest and reduced sensory stimulation follow memory encoding"
- "When similar material is learned or when other activity follows memory encoding, amnesic patients forget much more than healthy controls"

`[ASSERTED]` Our restatement: **the hippocampus is the interference-suppressor.** Without it, similar memories overwrite each other. With it, orthogonal coding keeps memories separate enough that decay rather than interference is the dominant forgetting mechanism.

### Episodic-to-semantic transition via decay (Figure 1c, p113)

`[ASSERTED]` Verbatim (Box 1):

> "In our model of forgetting, the hippocampal component of most memories is ultimately lost, such that long-term human memories will generally be of a semantic rather than an episodic nature (Figure 1c). This episodic-to-semantic shift over time is very similar, if not identical, to the context generalization phenomenon, that is, the tendency to express behavior that once was specific to the learning context in other contexts over time."

`[ASSERTED]` Our restatement: **forgetting generates abstraction.** Memories don't just disappear; they lose their context-specificity over time and become available as gist or general knowledge. The hippocampal-trace decay IS the mechanism by which episodes become schemas.

This is structurally significant for Kyrja:
- M12 (quasi-regular handling) needs both episodes and regularities
- M17 provides the *mechanism* by which regularities are extracted from episodes — selective forgetting of specifics
- This is the consolidation-vs-forgetting unification at work: same process viewed from two directions

### Molecular substrate — PKMζ and AMPA receptor internalization (pp 116-117)

`[MEASURED]` Cited evidence (Sacktor et al. and successors):

- PKMζ (protein kinase M zeta) is necessary and sufficient for maintaining LTP
- Synthesized upon LTP induction; phosphorylated; remains constitutively active
- Transient inhibition of PKMζ abolishes fully established memories, even months old
- Mechanism: PKMζ prevents internalization of GluA2-containing AMPA receptors
- Active forgetting = PKMζ degradation → AMPA receptors internalized → LTP lost → memory faded

`[ASSERTED]` Caveat noted by Hardt et al.: PKMζ-knockout mice show preserved LTP, suggesting compensatory mechanisms (PKCι/λ proposed) exist. The PKMζ findings indicate a mechanism, not necessarily the only mechanism.

### Metaplastic regulation — strong memories are protected (p117)

`[ASSERTED]` GluN2b-containing NMDA receptors play a metaplastic role:

- Recent strong memories have reduced GluN2b expression
- Lower GluN2b → resistance to LTD/depotentiation → resistance to forgetting
- High GluN2b → susceptibility to LTD signals → vulnerable to forgetting

`[ASSERTED]` Our restatement: **memory strength gates forgetting susceptibility.** The metaplastic state (NMDA receptor composition) is the signal that distinguishes "this memory is important, protect it" from "this memory is routine, let it decay." For an AI memory system, this corresponds to a graded protection signal — not a binary "keep / delete" decision but a continuous decay-rate modulator per memory.

### Sleep as the active-forgetting window (p115)

`[ASSERTED]` Verbatim:

> "It seems that the best time for this form of well-organized memory removal of consolidated memories is during sleep, when the brain is not engaged in the encoding of new memories."

`[ASSERTED]` Different sleep phases play different roles:

- Slow-wave sleep (SWS) — synaptic homeostatic downscaling (Tononi & Cirelli 2003)
- REM sleep — possibly synaptic downscaling preferentially (Grosmark et al. 2012)
- SPW-R rich periods — selective protection AND removal during the same window

`[ASSERTED]` Our restatement: sleep is doing TWO things simultaneously — consolidating selected memories (via M03 replay-mediated consolidation) AND actively forgetting unselected memories (via PKMζ-modulated AMPA internalization). **These may be two outcomes of the same replay-driven mechanism** — replay strengthens what gets replayed; non-replay produces decay. The same machine, looked at from two angles, produces both consolidation and forgetting.

This is the **fourth unification observation** in the matrix walk.

### Adult neurogenesis and pattern separation (p117)

`[MEASURED]` Dentate gyrus neurogenesis:

- Young adult-born granule cells preferentially support pattern separation (Nakashiba et al. 2012, McHugh et al. 2007)
- Suppression of neurogenesis impairs spatial learning (cited)
- Hardt et al. predict: less neurogenesis → more interference; more neurogenesis → better separation → decay-dominant forgetting

`[ASSERTED]` Our restatement: the brain *grows* its pattern-separation capacity throughout life. Capacity is not fixed at architecture-time. AI memory architectures with fixed embedding dimensions are missing this mechanism; the caddy could have adaptive representation capacity if neurogenesis-style continuous expansion is a useful operational primitive.

## Mechanism implications for Kyrja

### M17 as the first inverse mechanism in the matrix

`[ASSERTED]` All matrix rows M01-M16 catalogue storage, consolidation, or retrieval primitives. M17 is the first inverse mechanism — a regulated *removal* process. This changes the matrix's character: it's no longer just a catalogue of "things the brain does to keep information." Forgetting is a first-class memory function, not a failure mode.

For the substrate-antagonism count maintained in the matrix walk, M17 is **strongly substrate-antagonistic.** Substrate LLMs have no analog of graded, metaplastically-modulated forgetting. Either weights persist forever (frozen) or full retraining replaces them; there is no "let this trace decay at a salience-modulated rate" primitive.

For bolt-on, M17 is **weakly antagonistic.** Pruning policies exist (LRU, capacity bounds, salience-based deletion in commercial agentic-memory products) but they are not learned, not graded, not metaplastically regulated. The candidate primitive — a *learned forgetting policy operating on a separate representation, modulated by salience signals* — is absent from the field.

For caddy, M17 is **a natural fit.** A separately-addressable memory representation can carry per-memory decay rates as learnable state. A consolidation channel that operates in parallel with a decay channel can implement the same sleep-window behaviour biology has.

### The "intelligence is in the forgetting policy" reframe

`[ASSERTED]` This is the load-bearing architectural insight. Current AI memory systems put intelligence at admission: classifier-based salience scoring at write time, structured extraction at ingest, hand-crafted importance heuristics. Hardt et al.'s biology suggests the opposite tradeoff:

| Architecture | Encoding | Forgetting |
|---|---|---|
| Standard bolt-on | Smart admission gates (salience scoring, structured extraction) | Weak or no policy (capacity cutoffs, LRU) |
| Biological | Promiscuous (encode liberally) | Smart decay policy (salience-modulated, metaplastically gated) |

The caddy could test this tradeoff explicitly: write everything cheaply, prune intelligently. The intelligence shifts from a write-time gatekeeper to a decay-rate modulator. The decay modulator can be a learned policy informed by salience signals available in the agent loop (outcome success, user feedback, reflective surprise — see [memory-caddy § granularity-ladder of surprise](../open-question/memory-caddy.md)).

### The fourth unification observation — M03 + M17 may be the same mechanism

`[SPECULATED]` Sleep-window replay (M03) and active forgetting (M17) may be two outcomes of the same underlying mechanism:

- Replay strengthens what gets replayed (via PRP capture → STC stabilisation — M15 mechanism)
- Non-replay produces decay (PKMζ degradation → AMPA internalisation)
- Salience modulates which memories get replayed
- The same selection signal drives both consolidation and forgetting outcomes

This is the **fourth unification observation** during the matrix walk:

1. M10/M11 — reconsolidation and interleaved consolidation may be same mechanism at different timescales
2. M11/M12 — interleaved learning and quasi-regular handling may be same architectural commitment, two views
3. M05/M10/M15 — schema-fit, reconsolidation, synaptic tagging all behavioural-level outputs of STC
4. M03/M17 — consolidation and active forgetting same sleep-based selection mechanism, opposite outcomes

Four data points in 17 rows strongly suggests the matrix-as-rows framing is observing *consequences* of a smaller architectural primitive set, not the primitives themselves. The "primitive-set page" speculation from prior matrix walks gains substantial support from M17.

### Cross-row implications

| Matrix row | Connection |
|---|---|
| M03 (consolidation operator) | Partner mechanism; possibly same selection process viewed from opposite angle |
| M04 (selective replay) | Replay determines what is protected from decay; non-replay = decay |
| M09 (sparse competitive allocation) | Active forgetting may *generate* sparsity over time; competitive PRP capture + decay maintains sparseness as default |
| M11 (interleaved learning) | Pattern separation enables decay-dominant forgetting; without separation, interference dominates |
| M12 (quasi-regular handling) | Active forgetting is the mechanism by which episodes become schemas — gist generation via specifics-decay |
| M15 (synaptic tagging) | PKMζ-modulated AMPA internalisation is the molecular substrate; STC sets the tags, decay clears the un-captured |
| M16 (constructive memory) | Forgetting transforms specific episodes into generative material — connects to the constructive-memory hypothesis |

## What this paper does NOT establish

`[ASSERTED]` Scope limits:

- **The PKMζ mechanism is contested.** PKMζ-knockout mice show preserved LTP, suggesting compensatory mechanisms. The molecular substrate for active forgetting is not closed.
- **The "decay vs interference" partition is a working framework,** not a settled finding. Many cognitive psychologists still favor interference-dominant accounts.
- **Most experimental support is from rodents,** with limited direct human evidence. The cross-species generalisation is presumed but not directly demonstrated.
- **Sleep's exact role is debated.** Whether active forgetting happens preferentially during SWS, REM, or both is open.
- **The architecture-vs-disease distinction matters.** Hardt et al. propose that *dysregulated* forgetting may play a role in Alzheimer's (Box 1). They are not claiming all decay is healthy — they are claiming healthy decay is a designed mechanism.

## Source archive

This is a 10-page Trends in Cognitive Sciences "Opinion" article — a comprehensive synthesis of the cellular-molecular literature on active forgetting. Key sections read verbatim:

- Abstract (p111)
- "Current thinking on forgetting" (p111-112)
- "Forgetting in multiple memory systems: hippocampus and neocortex" (p112-114)
- "A role for decay in everyday forgetting" (p115-116)
- "Possible molecular pathways of decay-like forgetting" (p116-117)
- "Box 1. Predictions" (p117)
- "Box 2. Questions for future research" (p118)
- "Concluding remarks" (p118)

The references list (pp 118-120) was scanned but individual cited papers were not verbatim-read.

## M17 walk findings (2026-05-17)

`[ASSERTED]` Walked this paper with AJ during the M17 matrix walk on 2026-05-17. Five findings beyond the per-claim restatements above:

1. **"Encode promiscuously, forget intelligently" inverts current AI practice.** This is the load-bearing architectural reframe of the walk. Biology's "what should I remember" solution is cheap encoding + expensive forgetting. Current AI memory systems are the opposite: sophisticated admission gates (LightMem entropy filtering, Mem0 LLM-mediated ADD/UPDATE/DELETE/MERGE, hand-crafted importance heuristics) + weak forgetting (LRU, capacity cutoffs) or no forgetting at all (frozen weights). DB analogy: write-through cache with smart admission (current AI) vs write-everything log with intelligent compaction (biology). Both are valid architectures; the field picked the first by default without testing alternatives.

2. **Two forgetting mechanisms map to two AI problems.** The walk made the partition explicit and mapped it:

   | Biology | AI counterpart | Status |
   |---|---|---|
   | Interference (overlap-driven, during active processing) | Catastrophic forgetting in continual learning | Well-known problem; [catastrophic-interference](../concept/catastrophic-interference.md) concept page covers it |
   | Decay (off-line, salience-modulated) | Graded, learned forgetting policy | Capability we *don't* have; [H34](../hypothesis/H34-forgetting-scores.md) target |

   One is a problem we're trying to avoid; the other is a capability we're trying to gain. The matrix had implicitly treated forgetting as a single phenomenon; this partition is operationally important.

3. **Pattern separation as architectural prerequisite for graded decay.** The crucial conditional from this paper, made explicit during the walk: decay-dominant forgetting only becomes possible once pattern separation is in place. Without orthogonal coding, similar memories collide and *interference* dominates as the forgetting mode; per-memory decay rates have no meaningful referent. DB analogy: per-key TTLs require non-colliding keys; sharding has to come first. Promoted to [pattern-separation concept page](../concept/pattern-separation.md) as a load-bearing architectural primitive.

4. **H34 architectural reweighting.** Before the walk, [H34](../hypothesis/H34-forgetting-scores.md) was "one good tool in the toolkit alongside admission control and salience scoring; belongs in the wedge but not load-bearing." After the walk, the architectural framing shifts: forgetting may be *the* place intelligence belongs, and the admission-side bias of current systems may be a category error. The admission-control page's "every other layer fights symptoms; admission control treats the cause" claim now reads as defensible only under the assumption that knowing-in-advance-what-will-matter is tractable; M17 challenges that assumption.

5. **Salience signal is the fifth-row dependency.** M17 joins M03, M04, M05, M15 as a matrix row whose policy gates on a salience signal. Reinforces the [salience-signal](../open-question/salience-signal.md) page's "load-bearing input variable" claim. The fourth unification observation (M03 + M17 as same sleep-window mechanism with opposite outcomes — replayed → consolidated; non-replayed → decayed; same selection signal) was already on this source page; the walk confirmed it as load-bearing for the matrix's "primitive set" speculation.

`[ASSERTED]` Substrate-antagonism rating confirmed: strongly antagonistic for substrate (weights persist forever or full retraining wipes them; no graded metaplastically-modulated decay primitive); weakly antagonistic for bolt-on (capacity heuristics exist but learned graded forgetting policy is absent); natural fit for caddy (separately-addressable memory representation can carry per-memory decay rates as learnable state).

## Related

- [matrix row M17](../concept/mechanism-gap-matrix.md) — promoted from candidate row to numbered row, anchored to this page
- [pattern-separation](../concept/pattern-separation.md) — architectural prerequisite for the graded decay this paper describes; surfaced during the M17 walk as a load-bearing primitive
- [H34 — forgetting scores](../hypothesis/H34-forgetting-scores.md) — pre-existing hypothesis on learned forgetting policies; this paper is the cog-sci anchor
- [matrix row M03](../concept/mechanism-gap-matrix.md) — consolidation operator; partner mechanism, possibly same selection process viewed from opposite angle
- [matrix row M04](../concept/mechanism-gap-matrix.md) — selective replay; replay determines what survives decay
- [matrix row M12](../concept/mechanism-gap-matrix.md) — quasi-regular handling; active forgetting is the mechanism by which episodic specifics decay into semantic regularities
- [matrix row M15](../concept/mechanism-gap-matrix.md) — synaptic tagging; PKMζ-modulated AMPA internalisation is the molecular substrate
- [consolidation-channel](../concept/consolidation-channel.md) — forgetting is the partner operator to consolidation
- [open-question/memory-caddy](../open-question/memory-caddy.md) — a caddy with active forgetting as a learned policy is structurally novel
- [mcclelland-mcnaughton-oreilly-1995-cls](./mcclelland-mcnaughton-oreilly-1995-cls.md) — the broader CLS framework Hardt et al. operate within
- [josselyn-tonegawa-2020-engrams](./josselyn-tonegawa-2020-engrams.md) — engram-level perspective on what gets remembered vs forgotten
- [redondo-morris-2011-stc](./redondo-morris-2011-stc.md) — synaptic tagging is what gets *captured* by PRPs; decay is what happens to *uncaptured* tags

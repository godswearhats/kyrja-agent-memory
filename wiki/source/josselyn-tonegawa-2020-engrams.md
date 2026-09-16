---
type: source
name: "Josselyn & Tonegawa 2020 — Memory Engrams: Recalling the Past and Imagining the Future"
status: timeless
last_ingested: 2026-05-14
sources: []
tags: [cog-sci, engrams, cell-ensembles, silent-engrams, sparse-coding, neuronal-allocation, systems-consolidation, modern-cog-sci, review]
---

## Citation

Josselyn, S. A., & Tonegawa, S. (2020). *Memory engrams: Recalling the past and imagining the future.* Science, 367(6473), eaaw4325. DOI: 10.1126/science.aaw4325. Published 3 January 2020.

## Location

- PDF: [library/papers/josselyn-tonegawa-2020-engrams.pdf](../../../research/library/papers/josselyn-tonegawa-2020-engrams.pdf)
- DOI: 10.1126/science.aaw4325
- MIT Open Access: https://dspace.mit.edu/handle/1721.1/126261

## Why this paper is load-bearing for Kyrja

Engrams are the *cellular substrate* of memory — the level beneath McClelland 1995's system-level account. Josselyn & Tonegawa 2020 is the canonical modern review showing engrams are now causally verified, with the **silent engram** concept introducing a genuinely new architectural primitive that current AI memory has no analogue for. Cited in [online-vs-offline-consolidation](../open-question/online-vs-offline-consolidation.md) as relevant to the engram-debate sub-point and as a `[pending]` source until 2026-05-14.

## Engram definitions (Box 1, verbatim)

> An "engram" refers to the enduring offline physical and/or chemical changes that were elicited by learning and underlie the newly formed memory associations.
>
> "Engram cells" are populations of cells that constitute critical cellular components of a given engram. These cells may (or may not) also be critical components of engrams supporting other memories. Engram cells are (i) activated by a learning experience, (ii) physically or chemically modified by the learning experience, and (iii) reactivated by subsequent presentation of the stimuli present at the learning experience (or some portion thereof), resulting in memory retrieval.
>
> "Engram cell ensemble" refers to the collection of engram cells localized within a brain region. Engram cell ensembles in each brain region are connected, forming an "engram complex," which is the entire brainwide engram supporting a memory.

## Key claims (with our restatements)

### Engrams are now causally verified through four experimental criteria

`[MEASURED]` Adapting Martin & Morris (2000)'s criteria for synaptic plasticity:

| Criterion | Evidence |
|---|---|
| **Observational** | Above-chance overlap (~10-40%) between cells active during training and testing, across DG/CA3/CA1, amygdala, cortex. Multiple labs, multiple tasks (fear conditioning, social discrimination, novel object exploration). |
| **Loss-of-function** | Ablating CREB-overexpressing (preferentially-allocated) engram cells erases memory; ablating equal numbers of non-engram cells leaves memory intact (Josselyn et al. 2009). |
| **Gain-of-function** | Optogenetic reactivation of tagged engram cells in absence of natural cues induces memory expression (freezing in untrained context after activating fear engram from training context) — Liu et al. 2012 Nature. |
| **Mimicry** | Memory implantation: pairing optogenetic stimulation of a context-A engram with footshock in context-B creates a false memory of context-A being shocked (Ramirez et al. 2013 Science). Pure-intracranial conditioning via olfactory glomerulus activation paired with appetitive/aversive pathway activation creates real behavior toward odors never experienced (Vetere et al. 2019 Nat Neurosci). |

**Our restatement:** `[MEASURED]` — engrams are no longer a hypothesis; the cellular substrate of memory is empirically established. Lashley's 1950 "elusive engram" was *methodologically* elusive (lesion tools were too coarse), not ontologically.

### Sparse competitive allocation determines engram identity

`[MEASURED]` (Fig. 3) Within a brain region, a *small subset* of eligible neurons become engram cells supporting any specific memory. **Allocation is determined by relative neuronal excitability at the time of training**:

- Increasing CREB (transcription factor that increases excitability) in random subset → those neurons preferentially recruited to engram
- Decreasing excitability → those neurons preferentially *excluded*
- Same mechanism observed across DG, CA1, prefrontal cortex, insular cortex, retrosplenial cortex, lateral amygdala, piriform cortex

The competition is **Darwinian** at cellular level: eligible neurons compete; relative excitability wins.

**Our restatement:** `[ASSERTED]` — the brain does NOT have a global "where should I store this memory" router. Engram allocation emerges from **local excitability competition**. This is mechanistically distinct from the global controller architecture implicit in most agentic-memory systems (vector-DB routers, MoE gating).

### Engrams are distributed (engram complex)

`[MEASURED]` A single memory is supported by engram cell ensembles distributed across many brain regions. Brainwide mapping (Roy et al., bioRxiv 668483; Vetere et al. 2017 Neuron 94:363-374) identified 100+ candidate regions for contextual fear memory using CLARITY-like tissue clearing + IEG immunohistochemistry. Graph-theory analysis identifies "hub" regions necessary for retrieval.

**Engram complex** = entire brainwide engram = engram cell ensembles in multiple regions, functionally connected via engram-cell pathways.

**Our restatement:** `[ASSERTED]` — for AI translation: memory is **not localized to a single substrate**. The "vector store" vs "model weights" dichotomy may be too coarse. The biological reality is many specialized substrates with structured connectivity, each storing different aspects of the same memory.

### Engrams show enduring synaptic and structural changes

`[MEASURED]` Engram cells, 1 day after training, show:

- **Higher AMPA/NMDA receptor ratio** (basal excitatory synaptic strength)
- **Increased dendritic spine density**
- **Greater functional connectivity** to downstream engram cells (specifically DG → CA3 engram pairs show stronger coupling than non-engram pairs)
- **Greater synaptic connectivity** with presynaptic engram cells (lateral amygdala fear engram cells; Kaang lab)

`[MEASURED]` Engram *size* (number of cells) is **invariant to memory strength**. Stronger memory engages **more synapses between engram cells**, not more cells.

**Our restatement:** `[ASSERTED]` — memory strength is **synaptic-density encoded, not cell-count encoded**. An ensemble of N cells can represent memories of varying strength via varying intra-ensemble connectivity. Direct AI analogue: in a parameter-efficient framing, you don't add more "memory slots" — you add more *weights between* existing slots.

### Silent engrams — the major conceptual innovation

`[MEASURED]` Memories can be **stored without being retrievable**. Silent engrams are engrams that **cannot be reactivated by natural cues** but **CAN be reactivated by direct optogenetic stimulation**.

**First demonstration (Ryan et al. 2015 Science):**

- Fear-conditioned mice given anisomycin (protein synthesis inhibitor) immediately post-training → no freezing 1 day later (apparent amnesia)
- BUT optogenetic activation of DG engram cells tagged during training → freezing recovers, even 8 days after training
- The memory was stored; only the *retrieval handles* were missing

**Silent engrams have:**
- Lower spine density than active engrams
- Lower synaptic strength
- Cannot be reactivated by sensory cues

**Silent engrams can be unsilenced:**
- LTP-like optogenetic stimulation of entorhinal → DG inputs restores spine density AND ability of natural cues to elicit retrieval
- Genetic restoration of spine density (PAK1 overexpression) also unsilences

**Silent engrams in normal memory:**
- Social discrimination memory: vCA1 engram becomes silent ~1 hour post-training (memory dissipates); artificial activation at 24 hours restores memory expression
- **Implication: engram silencing is a normal regulatory mechanism, not just pathological**

**Silent engrams in Alzheimer's disease (Roy et al. 2016 Nature):**
- APP/PSEN1 transgenic mice show memory deficits
- DG engrams are intact but silent (reduced spine density)
- Optogenetic activation rescues memory
- LTP-like stimulation restores natural-cue retrieval

**Our restatement:** `[MEASURED]` — **storage and retrieval are dissociable.** This is a categorical departure from the cognitive-psychology model where "memory accessible = memory stored" is implicit. Tulving's 1966 availability-vs-accessibility distinction (cited as ref 174) is now mechanistically validated.

### Silent engrams and systems consolidation (Fig. 4)

`[MEASURED]` Kitamura et al. 2017 Science — engram-level demonstration of systems consolidation:

- **Recent (1 day post-training):** hippocampal DG engrams = ACTIVE (high spine density, naturally retrievable); mPFC engrams = SILENT (low spine density, only artificially activatable)
- **Remote (2 weeks post-training):** hippocampal DG engrams DEMATURE → SILENT; mPFC engrams MATURE → ACTIVE

The engram **migrates** from hippocampus to cortex during systems consolidation. **The hippocampal engram is not lost — it goes silent.** Artificial activation can still reactivate it.

**Our restatement:** `[MEASURED]` — McClelland 1995's CLS framework predicted exactly this: gradual hippocampal-to-cortical transfer. Engram-level evidence now visualizes the migration at cellular resolution. **But adds a refinement McClelland 1995 did not predict: the hippocampal engram persists in silent form**, not lost. This is a deeper finding than CLS — the slow store doesn't replace the fast store; the fast store goes silent while remaining present.

### Memory linking through temporal coallocation (Fig. 5)

`[MEASURED]` (Cai et al. 2016 Nature, Rashid et al. 2016 Science) Neurons that win allocation to an engram remain *more excitable than neighbors* for several hours afterward. This creates a temporal coallocation window:

- **Event 2 within ~6 hours of Event 1:** allocated to overlapping ensemble → memories become LINKED (retrieving one retrieves the other; extinguishing one extinguishes the other)
- **Event 2 after >24 hours:** previously-allocated neurons are refractory; new event allocates to distinct ensemble → memories remain SEPARATE

**Behavioral confirmation:** behaviorally extinguishing one of two coallocated memories also extinguishes the other; same does not happen for separately-allocated memories.

**Our restatement:** `[MEASURED]` — biological memory has a **time-windowed integration mechanism**: similar experiences within a short window get bound together; separated experiences stay distinct. There is **no direct AI analogue** in current agent-memory systems. RAG concatenates retrieved chunks regardless of when they were stored; fine-tuning doesn't have temporal-coallocation semantics.

### Reconsolidation through engram lens

`[ASSERTED]` (paper's interpretation, p. 19) Reconsolidation (Nader, Schafe & LeDoux 2000) — retrieved memory enters labile state; protein synthesis inhibition during this window causes amnesia.

Engram framework reinterpretation: retrieval *reactivates* the engram and creates a coallocation-like window during which the engram can be updated, silenced, or strengthened. "Reconsolidation may be the mechanism by which memories are updated to incorporate new information."

This bridges to [Nader et al. 2000](./nader-schafe-ledoux-2000-reconsolidation.md).

## Mechanism-gap question — engram concepts in current AI memory

`[ASSERTED]` Answer: **No, in multiple senses.**

| Engram concept | AI memory analogue | Implementation status |
|---|---|---|
| Sparse competitive allocation | Sparse MoE / expert routing | ⚠ Partial — MoE is *load-balancing* competition, not memory-allocation competition |
| Specific ensembles encode specific memories | Parameter-efficient FT (LoRA, adapters) | ⚠ Architecturally similar but not Darwinian-allocated |
| Engram complex (distributed ensembles in many regions) | Multi-substrate memory (vector + parametric) | ⚠ Conceptually similar; agent-memory systems don't have a "ensemble" granularity |
| **Silent engrams (storage ≠ retrieval)** | **No AI equivalent.** | ❌ No mechanism for "stored but currently inaccessible to natural cues, accessible to direct activation" |
| **Engram migration over time** | **No AI equivalent.** | ❌ No system migrates memory representation between substrates as a function of time-since-encoding |
| **Time-windowed coallocation (linking)** | **No AI equivalent.** | ❌ No mechanism for "events within ~6h share memory substrate; events >24h get separate substrates" |
| Memory strength = synaptic density not cell count | Adapter rank / parameter count | ⚠ Conceptually similar — adapters can be made stronger by adding parameters, but not by post-hoc strengthening of connections |
| Reconsolidation update window | Knowledge editing (MEMIT, ROME) | ⚠ Partial — MEMIT-style edits resemble "open the engram and rewrite" but lack temporal-window semantics |

**The four ❌ items are genuine novel architectural primitives the AI agentic-memory field has not built.** Each is independently implementable.

## What this confirms / refines in the existing wiki

### Confirms

- **[McClelland 1995 CLS framework](./mcclelland-mcnaughton-oreilly-1995-cls.md):** systems consolidation is empirically visible at engram-cell resolution. The hippocampal-to-cortical migration prediction is verified.
- **The "no current system implements this" framing** in [consolidation-channel](../concept/consolidation-channel.md) is **stronger after this read**, not weaker. Silent engrams, engram migration, and temporal coallocation are three additional missing primitives.
- **[active-stages-framework](../concept/active-stages-framework.md):** the "selection" stage is real at biological-allocation level (excitability competition). The "consolidation" stage is real at engram-migration level. The "updating" stage is real at reconsolidation-window level.

### Refines

- **McClelland 1995 treats the hippocampal trace as *decaying*** (`D_h` parameter in their model). The engram literature shows hippocampal engrams **don't decay — they go silent**. The mathematical model is right about *behavioral* accessibility decay but wrong about the underlying substrate.
- **CLS predicts a binary fast-store / slow-store dichotomy.** The engram literature shows the fast store doesn't disappear when the slow store takes over — they coexist, with the fast store silenced. This is a *continuum*, not a hand-off.

### Adds (genuinely new for the wiki)

- **Silent engrams as a category.** Not currently in the wiki at all. Worth a dedicated concept page if the AI-translation question proves load-bearing.
- **Temporal coallocation as a memory-linking mechanism.** Not currently in the wiki. Falsifiable hypothesis: agent memory systems with time-windowed linking outperform those without on multi-turn coreference and contextual continuity tasks.
- **Sparse competitive allocation as the *mechanism* for sparse coding.** McClelland 1995 said sparse coding is needed but didn't specify how the brain decides which cells to use. Engram literature: local excitability competition.

## Open questions raised (potentially Kyrja-relevant)

- **What is the *signal* for silencing an engram?** The biology specifies that engrams can become silent, but the conditions under which silencing happens during normal memory are not fully characterized. AI-relevant: when *should* memory go "silent" rather than be deleted?
- **What is the *function* of silent engrams?** Why preserve them at all? Hypotheses: efficient reactivation if needed, raw material for future schema integration, latent capacity for context-dependent reactivation. AI-relevant: stored-but-not-retrieved knowledge as a design primitive.
- **How does engram silencing interact with the ~6-hour coallocation window?** Are silent engrams less likely to coallocate with new events? More likely? The paper doesn't address.
- **Whether engram literature scales beyond rodent fear conditioning** is the dominant construct-validity question for the entire field. Translating to agent memory requires assuming the mechanism generalizes — not yet established.

## Caveats

- **All findings are in rodents** (mice, rats) using fear conditioning, social discrimination, or contextual exploration. Generalization to human memory is `[ASSERTED]` extrapolation.
- **Engram tagging methods (IEG promoters) are imprecise** — they can over-tag or under-tag the "real" engram. The 10-40% overlap between training-active and testing-active cells is the methodological ceiling, not necessarily the biological reality.
- **The relationship between engram cells and place cells is not 1:1** — most place cells are not engram cells; engram cells code "context" in a different way than place cells code "location" (McHugh lab work, cited as ref 107).
- **"Mimicry" experiments don't necessarily prove memory implantation in a strong sense** — the artificially-induced behavior is task-appropriate but may not have the rich phenomenological content of natural memory.
- **The review is rodent-centric and does not address declarative/semantic memory** at engram level. The framework is most empirically secure for procedural and emotional memory.

## Relevance to Kyrja

- **Refines the McClelland 1995 CLS picture** with cellular-level mechanism: allocation is competitive, ensembles are distributed, migration is observable, hippocampal engrams persist (silent) rather than decay.
- **Introduces four new architectural primitives** for AI agent memory: silent engrams, engram migration, temporal coallocation, sparse competitive allocation. All four have empirical biological backing; none are implemented in current agent-memory products.
- **The silent-engram concept is the most novel.** It introduces a categorical distinction between *storage* and *retrieval-handle availability* that no current AI memory system makes. The closest AI analogue might be "knowledge that the LLM has in weights but cannot access via natural prompting" — but this is implicit, not architecturally controlled.
- **Engram migration over time** is the cellular-resolution version of McClelland's consolidation rate `C` — but the engram literature shows it's not a single rate; it's a maturation/dematuration dynamic across regions.
- **Construct-validity caveat:** all four primitives are rodent-validated for procedural/emotional memory. The Kyrja application is dialogue-based agent memory. The translation is plausible but unproven.

## Predicted follow-up reads

- **Ryan et al. 2015 Science (engram cells retain memory under retrograde amnesia)** — the first silent-engram demonstration. Cited as ref 71. Not in library; **P0 priority** if silent engrams become load-bearing for Kyrja design.
- **Kitamura et al. 2017 Science (engrams in systems consolidation)** — the migration evidence. Cited as ref 51. Not in library; high priority.
- **Cai et al. 2016 Nature (memory linking via temporal coallocation)** — the time-window mechanism. Cited as ref 216. Not in library; high priority.
- **Rashid et al. 2016 Science (competition between engrams)** — the Darwinian allocation. Cited as ref 215. Not in library; medium priority.
- **Norman & O'Reilly 2003 (Modeling hippocampal and neocortical contributions to recognition memory: A complementary-learning-systems approach)** — modern computational follow-up to McClelland 1995, cited as ref 209. Not in library; medium priority.
- **[Nader, Schafe & LeDoux 2000](./nader-schafe-ledoux-2000-reconsolidation.md)** — reconsolidation. In library, next P0 read.

## Audit history

- 2026-05-14 — verbatim read in two passes (pp. 1–20, pp. 21–40 including refs and figures). Full coverage of all five main figures and Box 1 definitions. Reading session ~70 min.

## Archive location

Library: `josselyn-tonegawa-2020-engrams.pdf`. Science 367, eaaw4325 (2020). HHS Public Access version (PMC7577560).

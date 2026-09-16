---
type: source
name: "Nader, Schafe & LeDoux 2000 — Fear Memories Require Protein Synthesis in the Amygdala for Reconsolidation After Retrieval"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [cog-sci, reconsolidation, memory-lability, amygdala, fear-conditioning, update-stage, load-bearing]
---

## Citation

Nader, K., Schafe, G. E., & LeDoux, J. E. (2000). *Fear memories require protein synthesis in the amygdala for reconsolidation after retrieval.* Nature, 406(6797), 722–726. DOI: 10.1038/35021052. Published 17 August 2000.

## Location

- PDF: [library/papers/nader-schafe-ledoux-2000-reconsolidation.pdf](../../../research/library/papers/nader-schafe-ledoux-2000-reconsolidation.pdf)
- DOI: 10.1038/35021052 (https://doi.org/10.1038/35021052)
- W. M. Keck Foundation Laboratory of Neurobiology, NYU

## Why this paper is load-bearing for Kyrja

The McClelland 1995 CLS framework treats memory retrieval as a *read* operation. Nader, Schafe & LeDoux 2000 — the canonical modern reconsolidation paper — shows that **retrieval is read-modify-write**: a consolidated memory, when retrieved, returns to a labile state during which it can be updated, strengthened, or silenced. This is the biological precedent for the [active-stages-framework](../concept/active-stages-framework.md)'s "updating" stage, and provides a categorically different operational model for memory than the read-only retrieval assumed by current AI agent-memory systems. Cited in [complementary-learning-systems](../concept/complementary-learning-systems.md) as the modern refinement of CLS, and load-bearing for the [Josselyn & Tonegawa 2020](./josselyn-tonegawa-2020-engrams.md) silent-engram framing.

## Key claims (with our restatements)

### Thesis (abstract, verbatim)

> "'New' memories are initially labile and sensitive to disruption before being consolidated into stable long-term memories. Much evidence indicates that this consolidation involves the synthesis of new proteins in neurons. The lateral and basal nuclei of the amygdala (LBA) are believed to be a site of memory storage in fear learning. [...] Here we show that consolidated fear memories, when reactivated during retrieval, return to a labile state in which infusion of anisomycin shortly after memory reactivation produces amnesia on later tests, regardless of whether reactivation was performed 1 or 14 days after conditioning. The same treatment with anisomycin, in the absence of memory reactivation, left memory intact."

### Setup — auditory fear conditioning

`[MEASURED]` Rats receive single pairing of tone (CS) + foot-shock (US). Freezing behavior in response to CS = index of fear memory. Anisomycin (protein synthesis inhibitor) infused bilaterally into lateral/basal amygdala. The amygdala is the established locus of fear memory storage (LeDoux 2000, ref 19).

### Experiment 1A — Retrieval makes consolidated memory labile (Fig. 2)

`[MEASURED]` Day 1: CS-US training. Day 2: single CS presentation (Test 1) → immediate intra-LBA infusion (anisomycin high-dose 62.5μg, low-dose 6.2μg, or ACSF control). Day 3: three CS presentations (Test 2).

- High-dose anisomycin: dramatically reduced freezing in Test 2 (P < 0.01 vs ACSF)
- Low-dose anisomycin: no effect (similar to ACSF)
- **Memory of original CS-US pairing was disrupted by post-retrieval anisomycin**

**Our restatement:** `[MEASURED]` — when a consolidated memory is retrieved, blocking protein synthesis in the amygdala for a short window after retrieval *erases* the memory. The retrieval itself made the memory labile.

### Experiment 1B — Effect requires reactivation (control, Fig. 2d-e)

`[MEASURED]` Same procedure BUT Test 1 = chamber exposure WITHOUT CS, then anisomycin. **No amnesia.** Freezing in Test 2 comparable to ACSF controls.

**Our restatement:** `[MEASURED]` — the labile-state effect is specifically tied to memory **reactivation**, not to anisomycin exposure or to the test chamber. The retrieval IS the destabilizing event.

### Experiment 2 — Reconsolidation has a time window (Fig. 3)

`[MEASURED]` Same Test 1 (with CS), but anisomycin delayed **6 hours** after retrieval. **No amnesia.** Freezing in Test 2 was normal.

**Our restatement:** `[MEASURED]` — the reactivation-induced labile window is **time-limited** (minutes-to-hours). Outside this window, protein synthesis is not required for memory stability. The window has the same temporal structure as the original consolidation window after learning.

### Experiment 3 — Even 14-day-old memories become labile (Fig. 4)

`[MEASURED]` Same paradigm but Test 1 occurred **14 days** after conditioning. Anisomycin after Test 1 still produced amnesia (P < 0.01).

**Our restatement:** `[MEASURED]` — **memory age does not protect against reconsolidation lability**. Even "well-consolidated" memories return to a labile state when reactivated. The McClelland 1995 framework predicting a transition from labile-hippocampal to stable-cortical doesn't capture this — *any retrieved memory is labile*, regardless of age or substrate.

### Experiment 4 — Effects are specific to long-term reconsolidation (Fig. 5)

`[MEASURED]` Test 1 + anisomycin. Post-reactivation short-term memory (PR-STM) test at 4h: **normal freezing**. Post-reactivation long-term memory (PR-LTM) test at 24h: **amnesic**.

**Our restatement:** `[MEASURED]` — rules out non-specific drug effects (amygdala is functionally intact 4h after anisomycin). Reconsolidation has a **short-term phase that does NOT require protein synthesis** (similar to original consolidation) and a **long-term phase that does**.

### The proposed framework — "active" memories are labile

`[ASSERTED]` (Discussion, verbatim):

> "A definition of consolidation based on 'new' memories is insufficiently broad to describe these data. We propose, in keeping with the original suggestion by Misanin et al. (1968), that as a first approximation 'active' rather than 'new' memories be viewed as labile, subject to disruption, and requiring protein-synthesis-dependent consolidation processes."

> "Reconsolidation may reflect the dynamic nature of the process by which new information is added to existing stores. It has long been believed that memory retrieval is an active or constructive process by which old information is integrated with the current knowledge base of the organism (Bartlett 1932). Reconsolidation may be part of the neural mechanism through which constructed memories are stored for later constructions."

`[ASSERTED]` Speculative mechanism (paper's Discussion):

> "It is possible that some modification of the synaptic tagging hypothesis (Frey & Morris 1997), which proposes that active synapses are given molecular markers that help stabilize synapses by capturing proteins made in the cell nucleus, might account for lability and reconsolidation, although this remains to be seen."

## The full operational model — retrieval as read-modify-write

`[ASSERTED]` Synthesized from the four experiments:

1. **Stable phase:** consolidated memory in amygdala. Resistant to disruption.
2. **Retrieval event:** CS presentation activates the engram. Memory enters labile state.
3. **Labile window:** ~minutes-to-hours. During this window, the memory is subject to disruption AND, presumably, to update.
4. **Reconsolidation requirement:** to *remain* stable, the memory must undergo de novo protein synthesis during the labile window.
5. **Default outcome:** re-stabilization without modification → memory persists as before.
6. **Disruption outcome:** if protein synthesis is blocked → memory is lost/silenced.
7. **Update outcome (inferred, not directly tested in this paper):** if new information arrives during the labile window → memory may be modified at re-stabilization.

**This is structurally identical to a database transaction model:** retrieval initiates a transaction; the transaction either commits (re-stabilize), commits with modifications (update), or aborts (silence). After the window, the memory is back to stable.

## Mechanism-gap question — reconsolidation in current AI memory

`[ASSERTED]` Answer: **No agent-memory system implements retrieval as a read-modify-write operation.**

| Reconsolidation component | AI memory analogue | Implementation status |
|---|---|---|
| Retrieval makes memory labile | RAG retrieval is pure read | ❌ Retrieved chunks are immutable copies |
| Labile time window | No temporal-window semantics | ❌ Memory edits in AI systems are not coupled to retrieval events |
| Same machinery for consolidation and reconsolidation | Distinct FT vs edit operations | ⚠ MEMIT/ROME do edit existing knowledge but not via retrieval-triggered windows |
| Default outcome = re-stabilize unchanged | Default = no change to vector store on retrieval | ✅ Matches by accident — but the default in biology is not "no change," it's "re-encode the same content" (active maintenance) |
| Update outcome = modify during labile window | Knowledge editing | ⚠ Possible architecturally but not retrieval-triggered |
| Silence outcome | LRU eviction, manual deletion | ⚠ Possible but not retrieval-triggered |
| Memory age doesn't protect against lability | Long-term storage is treated as more stable | ❌ AI memory systems generally treat older info as more stable, not less |

**Direct AI translation candidate:** an agent-memory architecture where retrieval triggers a brief "update window" during which the retrieved memory can be modified based on the current interaction context. After the window closes, the memory is re-committed. Three patterns:

1. **Default re-encoding:** retrieved memory committed back unchanged (database analog: read with no write-back).
2. **Refresh-with-update:** retrieved memory committed back with new context integrated (database analog: read-modify-write).
3. **Silencing:** retrieved memory not re-committed, allowing it to fade (database analog: read with explicit delete).

The selection between these three modes is itself an open design problem — biology selects based on prediction error, salience, and reward (cf. modern reconsolidation literature post-2000).

## What this confirms / refines / adds in the existing wiki

### Confirms

- **[active-stages-framework](../concept/active-stages-framework.md):** the "updating" stage is real at biological level. Reconsolidation provides the neuroscience analogue. The framework's claim that updating requires conflict detection + supersession semantics is consistent — the conflict is detected via the retrieval-induced labile window, and supersession happens via differential re-encoding.
- **[Josselyn & Tonegawa 2020](./josselyn-tonegawa-2020-engrams.md):** the engram-framework reinterpretation (reconsolidation works by silencing engram cells during the labile window) is consistent with — and predicted by — Nader 2000's findings. Anisomycin during reconsolidation likely *silences* the engram rather than erasing it.

### Refines

- **[McClelland 1995 CLS](./mcclelland-mcnaughton-oreilly-1995-cls.md):** treats retrieval as read-only and consolidated memory as terminal-state-stable. Nader 2000 refutes both — retrieval makes memory labile, and "consolidated" memories remain mutable through re-retrieval. The McClelland framework needs a `re-encoding rate` parameter alongside the `consolidation rate C` and `decay rate D_h`.
- **[consolidation-channel](../concept/consolidation-channel.md):** the operator is not just write-then-decay; it's write-retrieve-modify-rewrite. The wiki's current framing should incorporate retrieval as an update trigger, not just a read.

### Adds (genuinely new for the wiki)

- **Reconsolidation as the "updating" operator's biological mechanism.** Not currently explicit in the wiki. Worth promoting.
- **Memory transaction model.** Direct database-systems analog: retrieval-triggered labile window = transaction; protein synthesis requirement = commit; default re-encoding = no-op transaction; silencing = abort. This framing may be a fruitful translation lens for AI architecture design.
- **The Misanin 1968 historical precedent.** Reconsolidation was reported 32 years before Nader 2000 but largely ignored. The methodological revival in 2000 (specific brain-region targeting, modern fear-conditioning paradigm) made the phenomenon undeniable. This is a useful precedent for the agent-memory field: real architectural primitives can be "discovered" decades before they're acted on.

## Caveats

- **Single paradigm.** Auditory fear conditioning in rats. Generalization to declarative/semantic memory in mammals (and to AI memory in agents) is `[ASSERTED]` extrapolation. Subsequent literature has shown the phenomenon in many memory types, but this 2000 paper itself is narrow.
- **Single brain region.** Lateral/basal amygdala. The reconsolidation phenomenon has since been demonstrated in hippocampus, cortex, and many other regions — but not in this 2000 paper.
- **Single intervention.** Anisomycin. Other protein synthesis inhibitors give similar results; non-pharmacological interventions also disrupt reconsolidation (electroconvulsive shock, behavioral interference). But Nader 2000's evidence is specific to anisomycin.
- **The authors explicitly note** "It is possible that not all memories require reconsolidation. There may be a range of parameters within which reactivation of a memory converts it into a labile state, possibly involving the extent of experience with the particular learning situation, the kind of learning system engaged, and the motivational state of the subject."
- **Fear memories may be special** (strong emotional valence, well-defined neural circuit). Subsequent work has generalized reconsolidation to other domains but the 2000 finding alone shouldn't be assumed universal.
- **No direct test of update outcome.** Experiments tested disruption but not "what happens if new info arrives during the labile window?" That question was developed in subsequent literature (Hupbach et al. 2007 et seq.) but is not in this paper.

## Relevance to Kyrja

- **Provides the biological precedent for the "updating" active stage.** [active-stages-framework](../concept/active-stages-framework.md) lists updating as needing "conflict detection + supersession semantics" — reconsolidation is the biological implementation of exactly that.
- **Refutes the read-only retrieval assumption** baked into current AI agent-memory systems. RAG, vector-DB retrieval, KV-cache lookups — all are read-only by design. Reconsolidation suggests retrieval should be coupled to a brief update window.
- **Concrete architecture suggestion:** the consolidation channel should support retrieval-triggered update windows. When a memory is retrieved into the active context, it should be flagged as "currently labile"; the agent should consider whether the new context warrants modification, strengthening, or silencing of the memory; and at the end of the window, the memory commits back to stable storage with any changes.
- **Connects directly to [Josselyn & Tonegawa 2020](./josselyn-tonegawa-2020-engrams.md):** reconsolidation may be the mechanism by which engrams transition between active/silent states. The two papers are mutually reinforcing.
- **Database transaction analog** may be a useful framing for AJ (background in distributed systems): retrieval = BEGIN TRANSACTION; default = COMMIT no-op; update = COMMIT WITH WRITE; silence = ROLLBACK. The biological substrate already operates this way.

## Predicted follow-up reads

- **Misanin, Miller & Lewis 1968 (Science 160:203-204)** — the original observation of reactivation-induced retrograde amnesia. Cited as ref 13. Not in library; historical-priority read, low practical priority.
- **Frey & Morris 1997 (Nature 385:533-536, synaptic tagging)** — the candidate molecular mechanism Nader et al. cite. Already named in [Tse et al. 2007 schemas](./tse-et-al-2007-schemas.md) follow-ups. Not in library; high relevance.
- **Hupbach, Gomez, Hardt & Nadel 2007** (and follow-ups) — show that *new information* introduced during the reconsolidation window updates the existing memory. The "update outcome" not directly tested in Nader 2000. Not in library; **P0 priority** for Kyrja if reconsolidation-as-update becomes load-bearing for design.
- **Hardt, Nader & Nadel 2013 — `library/papers/hardt-nader-nadel-2013.pdf`** (IN LIBRARY) — modern review of reconsolidation and forgetting. Not yet read; potential P1 read.
- **Schiller et al. 2010 (Nature 463:49-53)** — clinical application: reconsolidation update prevents return of fear in humans. Cited in Josselyn & Tonegawa 2020 as ref 194. Not in library; high relevance if human-applicability becomes load-bearing.

## Audit history

- 2026-05-14 — verbatim read (single pass, 5 pages of paper + 0.5 page methods). Full coverage of all four experiments and all five figures. Reading session ~25 min.

## Archive location

Library: `nader-schafe-ledoux-2000-reconsolidation.pdf`. Nature 406, 722-726 (2000).

---
type: source
name: "Redondo & Morris 2011 — Making memories last: the synaptic tagging and capture hypothesis"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [cog-sci, synaptic-tagging-and-capture, stc, behavioural-tagging, ltp, prps, intermediate-state, m15, load-bearing, substitute-anchor]
---

## Citation

Redondo, R. L., & Morris, R. G. M. (2011). *Making memories last: the synaptic tagging and capture hypothesis.* Nature Reviews Neuroscience, 12(1), 17–30. DOI: 10.1038/nrn2963. Published January 2011.

## Location

- PDF: [library/papers/redondo-morris-2011-stc.pdf](../../../research/library/papers/redondo-morris-2011-stc.pdf)
- DOI: 10.1038/nrn2963 (https://doi.org/10.1038/nrn2963)
- Laboratory for Cognitive Neuroscience, Centre for Cognitive and Neural Systems, University of Edinburgh (Redondo); Picower Institute for Learning and Memory, MIT (Redondo, present address at time of writing); University of Edinburgh (Morris)

## Substitute-anchor note

`[ASSERTED]` This page anchors [matrix row M15](../concept/mechanism-gap-matrix.md) as a **substitute primary source** for the originally-listed Frey & Morris 1997 (Nature 385:533-536). The 1997 paper is paywalled at Nature and could not be obtained via Semantic Scholar (open-access PDF unavailable as of 2026-05-16). AJ fetched the 2011 Redondo & Morris review directly to the library 2026-05-16.

The substitution is defensible: Morris is co-author of the 1997 paper, the 2011 review is the canonical synthesis of the synaptic tagging and capture (STC) hypothesis, and it covers the 1997 findings plus 14 years of mechanistic follow-up (behavioural tagging, molecular components of the tag, structural-vs-functional plasticity dissociation, competitive-maintenance phenomena). For the matrix's purpose — anchoring the STC mechanism to a primary source — the review is arguably stronger evidence than the original letter would have been, since it surveys the converging experimental support that has accumulated since 1997.

The matrix's load-bearing-sources discipline is respected by *flagging the substitution here and in the M15 row itself,* not by silently using the review as if it were the 1997 paper. If the Frey & Morris 1997 paper becomes available later, the M15 row should be re-anchored.

## Why this paper is load-bearing for Kyrja

The synaptic tagging and capture (STC) hypothesis names a **molecular mechanism** that underlies multiple behavioural-level matrix rows: M05 (schema-fit modulation), M09 (competitive allocation under capacity bounds), M10 (reconsolidation), and the candidate row M15 itself. The mechanism describes how synaptic encoding produces a *transient intermediate state* — a synapse-specific "tag" with ~90 minute lifetime — that is converted to persistent storage only if plasticity-related proteins (PRPs) happen to be captured within the window. Otherwise the synapse reverts to baseline.

This adds a **third architectural tier** to the standard fast/slow (hot/cold) memory model: encoded-but-uncommitted. Most of the interesting consolidation biology lives in this middle tier. The behavioural-tagging experiments (Wang & Morris 2010 and follow-ups) demonstrate that the molecular mechanism scales up to behavioural-level memory consolidation — specifically, that **memory persistence at 24h depends on global PRP availability during the tagging window, modulated by events that occur up to several minutes before *or after* the encoding event.**

For Kyrja, this directly informs:
- [consolidation-channel](../concept/consolidation-channel.md) — the cellular-consolidation half of McClelland's framework operates via STC; the channel design needs a tagged-intermediate-tier concept.
- [H40 — schema-fit-modulated consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — behavioural tagging is the molecular substrate for schema-fit modulation. H40's mechanism may unify with STC.
- [active-stages-framework](../concept/active-stages-framework.md) — STC is the molecular substrate for the updating stage (M10 reconsolidation).
- [open-question/memory-caddy.md](../open-question/memory-caddy.md) — a caddy implementing STC-like semantics is structurally novel: no current bolt-on or substrate system has a tagged-intermediate tier.

## Key claims (with our restatements)

### Thesis (abstract, verbatim)

> "The synaptic tagging and capture hypothesis of protein synthesis-dependent long-term potentiation asserts that the induction of synaptic potentiation creates only the potential for a lasting change in synaptic efficacy, but not the commitment to such a change. Other neural activity, before or after induction, can also determine whether persistent change occurs. Recent findings, leading us to revise the original hypothesis, indicate that the induction of a local, synapse-specific 'tagged' state and the expression of long-term potentiation are dissociable. Additional observations suggest that there are major differences in the mechanisms of functional and structural plasticity. These advances call for a revised theory that incorporates the specific molecular and structural processes involved. Addressing the physiological relevance of previous *in vitro* findings, new behavioural studies have experimentally translated the hypothesis to learning and the consolidation of newly formed memories."

### The original STC hypothesis (Frey & Morris 1997 framing, p18)

`[ASSERTED]` Two-pathway LTP experiment: it is possible to induce protein-synthesis-dependent late-LTP (L-LTP) during inhibition of protein synthesis if a separate strong stimulation has occurred recently on a different pathway. The original framing proposed four steps:

1. Expression of synaptic potentiation at a stimulated synapse, with the setting of a local **synaptic tag**.
2. Synthesis and distribution of **plasticity-related proteins (PRPs)** at the soma or in dendrites.
3. **Capture** of PRPs by tagged synapses.
4. Stabilization of synaptic strength (L-LTP).

If prior activity has upregulated PRP availability, tags will be captured locally and stabilize L-LTP. Conversely, if PRP synthesis occurs *after* tag setting, stabilization will occur at that later time, with the temporal duration of the tag being the main determinant of whether stabilization occurs at all.

> "By contrast, we propose that heterosynaptic events that occur before or after encoding can determine the fate of memory traces."

`[ASSERTED]` Our restatement: encoding is cheap and synapse-local; persistence is gated by a **global resource (PRP pool)** that other events can modulate. This is structurally different from any current AI memory architecture, where storage commitment is decided at write time and global state plays no role.

### Limitations of the original 1997 model (p19)

`[ASSERTED]` Three limitations of the original STC hypothesis:

1. **Tag and LTP expression treated as simultaneous** — new evidence dissociates them. Early-LTP (E-LTP) can express without tagging; tagging can occur without LTP expression.
2. **Tag treated as a single molecule or small set of molecules** — revised view: tag is a **state of the synapse**, involving many proteins and their interactions. Permissive "unlocking" process rather than a single phosphorylation event.
3. **PRP synthesis assumed to be somatic only** — new evidence of **dendritic mRNA synthesis** and targeting to specific compartments. PRPs include activity-regulated cytoskeleton-associated protein (ARC), Homer1a, GluR1 AMPA receptor subunit, immediate early gene products.

### The revised STC model (p23-24, Fig. 4-5)

`[ASSERTED]` Tag setting and synaptic potentiation are now treated as independent processes that can co-occur or dissociate:

- **Weak tetanization** → tag setting + transient E-LTP. Without PRP capture within ~90 min, both fade; synapse returns to baseline.
- **Strong tetanization** → tag setting + E-LTP + PRP synthesis. Tagged synapse captures local PRPs → L-LTP.
- **Cross-capture (heterosynaptic):** Strong tetanization at pathway A produces PRPs cell-wide; weakly tetanized tagged synapses at pathway B (within the window) can capture them and convert to L-LTP. **Critical**: any tagged synapse on the same cell within the window can capture PRPs, regardless of which pathway produced them.

> "Capture of PRPs is the first step in the stabilization of both the functional and structural alterations to a dendritic spine. The molecular identity of all the PRPs is unknown, but includes GluR1, Homer1a, PKMζ and ARC."

### The lifetime of the tag (p23)

`[ASSERTED]` Tag lifetime ~90 minutes:

> "The prolonged but temporary activity of particular kinases may account for the limited lifespan of the tagged state — approximately 90 min as revealed by 'weak before strong' brain slice protocols. For LTP, an autophosphorylated form of CaMKII remains active in the PSD even after the calcium concentration returns to baseline levels."

`[ASSERTED]` Our restatement: the tag has a **specific timeout** for its persistence-window. This is the molecular substrate for the time-limited labile window observed in M10 reconsolidation (~1-6h) and the consolidation window observed in M11 interleaved-replay biology.

### Behavioural tagging (p27, Fig. 6) — the experiment that matters for M05 schema-fit

`[MEASURED]` Wang & Morris 2010 (cited as ref 108). Within-subjects appetitive paradigm in an "event arena":

- Rats trained in event arena, asked to remember the location of food each day (location changed daily).
- **No intervention:** memory good at 30 min; forgotten at 24h.
- **Intervention — novel-box exploration (5 min) before or after encoding:** memory persists to 24h.
- **Effect blocked by:** intrahippocampal SCH23390 (dopamine D1/D5 antagonist) OR anisomycin (protein synthesis inhibitor). Both at encoding time.
- **Increasing food pellets (1→3) without novelty exploration:** memory also lasts longer (stronger encoding produces more PRPs locally).
- **Prior novelty exploration rescues otherwise-fading memories of separate weak tasks.**

> "We also observed that unexpected novelty exploration could convert these rapidly forgotten spatial memories into more lasting traces, and that this effect was dependent on hippocampal dopamine receptors D1/D5 and protein synthesis."

`[MEASURED]` Our restatement: **memory of an event can be retroactively saved by a separate novelty experience 5 minutes later** — the novelty upregulates PRPs cell-wide, which the tagged synapses from the food event capture. This is a worked behavioural-level example of schema-fit-modulated consolidation, with PRP availability as the operational signal.

This directly informs [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md): the schema-fit-modulation isn't a separate mechanism, it's the synaptic-tagging machinery applied at behavioural level with novelty/salience as the upregulation signal.

### Competitive maintenance under PRP scarcity (p27)

`[ASSERTED]` Fonseca et al. 2006 (cited as ref 33). Two pathways simultaneously expressing LTP show **competitive** rather than synergistic interactions when PRPs are scarce (under protein synthesis inhibitors). The implication:

> "The STC hypothesis, drawing upon the phenomenon of 'competitive maintenance' and findings in contextual fear conditioning, proposes that first, synapses encoding the memory engram are routinely tagged when memories are retrieved; and second, sufficient levels of PRPs, available under normal conditions, allow these tagged synapses to stabilize any changes (memory updating), or to revert to the stable memory state, leaving the network functionally unchanged; but third, if PRPs are made scarce (that is, by protein synthesis inhibitors), proteasomal degradation of some of the scaffolding molecules to allow synaptic tagging is not complemented by the arrival of new PRPs. Consequently, the synapse cannot sustain its memory state and the network will lose its engram."

`[ASSERTED]` Our restatement: this is the molecular substrate for **capacity-bounded competition** between memories. M09 (sparse competitive allocation) and the broader "scarcity is generative" thread that emerged in the M09 walkthrough have a synapse-level mechanism in PRP competition. Limited PRP pool means strong recent memories displace weaker ones via literal resource starvation, not just interference.

### Tag re-setting / depotentiation (p20-21)

`[MEASURED]` Low-frequency stimulation (LFS, 250 pulses at 1 Hz) within the first 10 min after E-LTP induction can **depotentiate** the synapse AND **reset the tag**. After 10 min the tag-reset window narrows; depotentiation effect on the LTP itself remains but the tag persists.

`[ASSERTED]` Our restatement: the tag is **actively erasable** within a narrow window. This is biology's mechanism for "forgetting" tag-marked encoding before commitment to persistence. Connects to candidate row M17 (active forgetting) at molecular level — tag-resetting is a worked example of active de-marking distinct from passive decay.

### The conclusion's framing of cellular vs systems consolidation (p28)

> "We end by pointing out that this is entirely desirable, because a memory system that retained everything would rapidly saturate to a point where information could not be retrieved. We think that the molecular players and processes identified in this Review are behind the neuronal algorithms that determine the persistence of synaptic and network changes and that are engaged by the multitude of everyday events that characterize animal and human life. A grand challenge for the future of the neuroscience of memory is to better understand the neural circuits and patterns of neural activity that intersect between cellular and systems consolidation."

> "If systems consolidation determines which memory traces last in neocortical networks, cellular consolidation can be thought of as the filter that determines the subset of newly encoded information that may be subject to systems consolidation."

`[ASSERTED]` Our restatement: STC is **the gating filter** between encoding and systems-level consolidation. Most encoded events never make it past the tag-window. This is biology's mechanism for capacity management — the filter operates *before* expensive systems consolidation, not after.

## Mechanism implications for Kyrja

### The tagged-intermediate-tier as an architectural primitive

`[SPECULATED]` Most current AI memory architectures use a binary write/no-write decision at encoding time. STC suggests a **three-state pipeline**:

1. **Encoded but tagged** — synapse-specific transient state, cheap, time-limited (~90 min)
2. **Captured via PRPs** — persistence committed, structural change established
3. **Tag fades / depotentiated** — synapse reverts to baseline, encoding lost

The middle state is where most of the interesting biology lives. Schema-fit (M05), salience modulation (M04), behavioural tagging (M15 / Wang & Morris 2010), competitive maintenance (Fonseca 2006), and reconsolidation (M10) all operate via the tagged-intermediate-tier under one mechanism or another.

For a caddy implementation, this implies an architectural commitment that no current proposal has: an explicit transient-intermediate-tier with a global resource budget gating persistence. The two-phase-commit-with-timeout DB analog is close but not exact — the biological mechanism uses *global resource availability* as the commit signal, not a local decision.

### Cross-row unification candidate

`[SPECULATED]` M05 (schema-fit modulation), M10 (reconsolidation), M15 (synaptic tagging) may all be **behavioural-level consequences of the same molecular primitive.** Together with the M10/M11 and M11/M12 unification observations from prior matrix walks, this is the third unification candidate.

Candidate primitive being surfaced: **transient intermediate state with global-resource gating.** A separate architectural primitive from the discrete-addressable-units primitive (M01-M02-M06 cluster) and from the dual-timescale-with-consolidation primitive (M01-M02-M03-M11-M12 cluster). Status: working observation, not load-bearing for a current design decision; flagged for development if the smaller-primitive-set framing crystalises.

### Behavioural-tagging as the H40 mechanism

`[ASSERTED]` [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md) currently proposes schema-fit-modulated consolidation as a falsifiable hypothesis without a specified mechanism. Behavioural tagging (Wang & Morris 2010, summarised above) provides the **molecular and behavioural** mechanism: schema-fit operationalises as PRP availability, modulated by novelty/salience/reward signals via dopamine-D1/D5 and immediate-early-gene upregulation.

For H40 to be testable in an AI memory system, the analog of "PRP availability" needs operationalisation. Candidates:
- A global "consolidation budget" updated by salience/novelty signals
- A second-order learning-rate signal that all encoded-but-tagged memories share
- A bottleneck on the consolidation channel's throughput, with tagged memories competing for slots

This is now a design question downstream of H40, not a separate hypothesis.

## Relevance to specific matrix rows

| Matrix row | Connection |
|---|---|
| M03 (consolidation operator) | STC is the cellular-consolidation operator; PRP capture is the within-cell consolidation event |
| M04 (selective replay) | Salience-modulated PRP synthesis biases which tagged memories persist; the read-side analog of selective replay |
| M05 (schema-fit modulation) | Behavioural tagging is the molecular mechanism for schema-fit gating of persistence |
| M06 (silent engrams) | Tag-without-PRP-capture is a candidate for a "silent" state — the synapse retains tag information but has not committed structurally |
| M07 (engram migration) | STC operates on the cellular-consolidation side of the McClelland 1995 hippocampal-to-cortical migration |
| M08 (temporal coallocation) | The ~90 min tag window is a candidate substrate for temporal-coallocation effects at the synapse level |
| M09 (sparse competitive allocation) | PRP-pool competition is the molecular substrate for capacity-bounded competition |
| M10 (reconsolidation) | Retrieval re-tags the synapse and re-engages the STC cycle; reconsolidation operates via the same machinery |
| M15 (candidate row, this paper) | Direct |
| M17 candidate (active forgetting) | Tag-resetting via LFS is a molecular example of active de-marking distinct from passive decay |

## What this paper does NOT establish

`[ASSERTED]` Scope limits on what this review primary-source-anchors:

- **It does not establish that PRP-pool-style global resource gating is the only consolidation mechanism.** The McClelland 1995 systems-consolidation argument operates at a different timescale and likely involves different mechanisms.
- **Behavioural tagging is in rodents.** Human evidence is indirect; the cellular mechanism in primates is presumed similar but not directly demonstrated.
- **Tag identity remains incompletely specified.** The paper revises the tag concept from "single molecule" to "state of the synapse" but does not provide a closed list of tag components.
- **The molecular details may not transfer to AI.** AI memory systems do not have synapses; the *architectural primitive* (transient intermediate state with global-resource gating) is what transfers, not the protein-by-protein mechanism. Implementation choices are downstream.

## M15 walk findings (2026-05-17)

`[ASSERTED]` Walkthrough of M15 with AJ produced three load-bearing findings beyond the verbatim-read content above:

1. **AJ's WAL-plus-credit-pool-plus-rescue restatement.** AJ initially mapped STC to his 2018 eBay patents but with two reversals worth correcting. Reversal one: **tags are free / automatic, not gated**. Every encoding sets a tag at low cost; the scarce resource is PRPs, not tags. Reversal two: **the rescue mechanism is bottom-up, not top-down**. New strong events don't "look around" for old neighbours to bundle with — they passively *emit PRPs into the shared pool*, and all currently-tagged synapses passively *capture* from that pool. No coordinator, no matching logic. Biology achieves the rescue effect with zero coordination overhead by offloading coordination to a shared physical resource. The clean software analog is **token-bucket rate limiting with shared buckets** — tags wait passively; salient events refill the bucket; whoever's tagged when tokens are available gets persisted.

2. **Fifth unification observation — M08 + M15.** AJ identified high correlation between M15 (~90 min PRP-pool tagging) and M08 (~6h temporal coallocation, Cai 2016). The likely relationship: **M08 names the temporal-binding phenomenon at population/cell-ensemble level; M15 names the molecular substrate AND adds the salience-mediated commit mechanism**. Different observation scales of the same architectural feature. This is the fifth unification observation in the matrix walk (after M10/M11, M11/M12, M05/M10/M15, M03/M17), further strengthening the speculation that the matrix rows are observable consequences of a smaller primitive set. M15's *unique* contribution beyond M08: (a) the tagged-intermediate-tier as discrete architectural state; (b) **temporal non-locality of persistence decision via salience signal** (behavioural tagging — Wang & Morris 2010); (c) capacity-bounded competition for commit slots (Fonseca 2006). The first two are the genuinely novel architectural contributions.

3. **Load-bearing reframe: salience signal is the variable downstream of architecture.** AJ surfaced mid-walk that the architectural choice (STC-shape vs hot-store-with-promotion vs anything else) is largely an implementation detail. **The salience signal is the invariant load-bearing input across all these architectures, and it is unsolved by the current field.** Promoted to its own open question at [salience-signal](../open-question/salience-signal.md). The cheapest first falsifiable claim derived: [H42 — learned salience function](../hypothesis/H42-learned-salience-function.md). This reframe refines M15's contribution: the tagged-intermediate-tier with PRP-pool-gating is real and architecturally novel, but its load-bearing-ness drops once salience-signal-computation is recognised as the upstream bottleneck. Both STC-shape and hot-store-promotion-shape stall on the same problem.

**Temporal non-locality as M15's unique contribution.** AJ's reframe sharpened the H40 anchor too: behavioural tagging (Wang & Morris 2010) is the *molecular mechanism* for [H40 schema-fit-modulated consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md). Whether a memory persists depends on what happens nearby in time, not on its own intrinsic features at write time. This is structurally different from every current AI memory system (all of which decide at write time) and is what makes STC genuinely novel beyond M08's binding observation.

## Source archive

Original Frey & Morris 1997 (Nature 385:533-536) cited extensively throughout this review as ref 17. The 1997 paper itself is unavailable to Kyrja due to paywall as of 2026-05-16; if obtained later, the M15 row should be re-anchored to it.

This review's references include several papers cited in other Kyrja source pages:

- Nader, Schafe & LeDoux 2000 (ref 111) — primary anchor for M10 [reconsolidation](./nader-schafe-ledoux-2000-reconsolidation.md)
- McGaugh 2000 (ref 110) — classical consolidation review

## Related

- [matrix row M15](../concept/mechanism-gap-matrix.md) — promoted from candidate row to numbered row, anchored to this page
- [matrix row M10](../concept/mechanism-gap-matrix.md) — reconsolidation; mechanism shares STC machinery
- [matrix row M05](../concept/mechanism-gap-matrix.md) — schema-fit modulation; behavioural tagging is the molecular substrate
- [consolidation-channel](../concept/consolidation-channel.md) — STC is the cellular-consolidation half of the channel
- [active-stages-framework](../concept/active-stages-framework.md) — updating stage operates via STC machinery
- [H40 — schema-fit-modulated consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — falsifiable hypothesis derived from M05; STC is the candidate mechanism
- [H39 — silent-state primitives](../hypothesis/H39-silent-state-primitives.md) — tag-without-PRP-capture is a candidate silent state
- [complementary-learning-systems](../concept/complementary-learning-systems.md) — McClelland 1995 framework; STC operates on the cellular-consolidation side
- [nader-schafe-ledoux-2000-reconsolidation](./nader-schafe-ledoux-2000-reconsolidation.md) — reconsolidation primary source; cites STC speculatively as candidate mechanism (verified by this review)
- [josselyn-tonegawa-2020-engrams](./josselyn-tonegawa-2020-engrams.md) — engram-cell primary source; engram-cell ensembles use STC-style tagging at population level
- [open-question/memory-caddy](../open-question/memory-caddy.md) — tagged-intermediate-tier as a candidate architectural primitive for the caddy

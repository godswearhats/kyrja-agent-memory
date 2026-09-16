---
type: source
name: "Dong, Lu, Norman & Michelmann 2025 — Towards LLMs with human-like episodic memory"
status: timeless
last_ingested: 2026-05-16
sources: []
tags: [norman-rubric, memory-augmented-llm, episodic-memory, evaluation-rubric, caddy-validation, princeton-norman-lab]
---

## Citation

Dong, C.V., Lu, Q., Norman, K.A. & Michelmann, S. (2025). *Towards large language models with human-like episodic memory.* Trends in Cognitive Sciences, Article In Press. DOI: 10.1016/j.tics.2025.06.016. Published online June 2025.

Affiliations: (1) Department of Psychology, Princeton University; (2) Zuckerman Institute, Columbia University; (3) Princeton Neuroscience Institute; (4) Department of Psychology, New York University.

## Location

- Journal: https://www.cell.com/trends/cognitive-sciences/abstract/S1364-6613(25)00179-2
- DOI: https://doi.org/10.1016/j.tics.2025.06.016
- Local archive: [`dong-2025-norman-episodic.pdf`](../../../research/library/papers/dong-2025-norman-episodic.pdf) (14 pages)

## Key claims (with our restatements)

### Architectural endorsement of the caddy shape

**Paper (page 3, verbatim):** *"LLMs can also use this solution by adding a memory system that rapidly stores information in a latent and lasting form (like the hippocampus in humans) and is separate from both the context window (which can be limited in size, like working memory in humans) and the weights of the main LLM (which are updated incrementally, like neocortex in humans)."*

**Our restatement:** `[ASSERTED]` The Princeton/NYU Norman lab — the leading academic group on hippocampal-CLS modelling — has explicitly endorsed the [caddy](../concept/caddy.md) architectural pattern by name (memory system separate from both context window and main-LLM weights). This is external validation from the most credentialed source in the field for what we have been calling the caddy. *Citation-load-bearing for the VC pitch.*

### Internal representations over verbatim text

**Paper (page 4, verbatim):** *"The latter approach [storing internal representations like keys/values rather than verbatim text] aligns better with human EM, insofar as humans store internal representations rather than verbatim input."*

**Our restatement:** `[ASSERTED]` Direct endorsement of activation-level injection (C4 of our caddy commitments) over text-injection (bolt-on). Distinguishes RAG (stores verbatim stimulus) from Memorizing-Transformer-shaped systems (stores keys/values). The latter is the caddy shape; the former is bolt-on.

### Five evaluable properties of human-like EM

**Paper (sections "Dynamic memory updating" through "Competition at retrieval"):** Five properties human EM exhibits that current MA-LLMs typically don't:

1. **Dynamic memory updating** — "Memories can be altered after having been added" — reconsolidation. Paper explicitly names Titans as "particularly promising in this regard."
2. **Event segmentation** — "People segment continuous real-world experience into discrete events... event boundaries... reflected in the brain as shifts in stable patterns of neural activity." Paper flags EM-LLM (Fountas 2025) as the only MA-LLM doing surprise-based segmentation; everyone else uses fixed-size chunks.
3. **Selective encoding and retrieval** — "Encoding and retrieval occur selectively... event boundaries have been found to be important points for EM retrieval." Paper flags FLARE as a positive example of uncertainty-triggered retrieval.
4. **Temporal contiguity** — "Successive recalls tend to come from nearby timepoints... shown to be scale-invariant (i.e., they apply across multiple timescales)." Paper notes MA-LLMs generally lack this; EM-LLM has local (non-scale-invariant) version.
5. **Competition at retrieval** — "Behavioral data suggest that humans show a strong amount of competition at retrieval, such that only the single best-matching memory comes to mind (or else no memory is retrieved)." Paper notes MA-LLMs typically allow top-k retrieval; humans are winner-take-all.

**Our restatement:** `[ASSERTED]` This is **the rubric** Kyrja's caddy will be evaluated against externally. Documented in [norman-rubric](../concept/norman-rubric.md) as a concept page. Anchors caddy design priorities: schema-fit admission addresses (3), reconsolidation addresses (1), surprise-based segmentation addresses (2), TCM-style context drift addresses (4), winner-take-all retrieval addresses (5).

### Box 4 — benchmark proposal

**Paper (Box 4, page 9):** *"Information is presented continuously, such that the models need to decide when it is best to store and retrieve memories depending on what has been shown thus far. It is not safe to assume that relevant information has been stored in memory. When relevant information is presented, it only appears once (mirroring how, in the real world, information is often only presented once), and it is similar to other, irrelevant information, creating the potential for confusion."* Concrete instantiation: model encodes large number of TV-show episode scripts (one exposure each), then in task phase is shown summaries of TV episodes one sentence at a time; can "continue" reading summary or "take over" and predict the rest. Rewarded for correct predictions, penalised for incorrect details. Compared against no-memory baseline to isolate EM contribution.

**Our restatement:** `[ASSERTED]` Norman et al. specify the benchmark shape that distinguishes caddy-like systems from bolt-on RAG. Standard QA benchmarks (the field's current default) fail to test the key properties because they pre-stage relevant memories and ask well-defined queries. The Box 4 design is what we would build experiments against to demonstrate selectivity wins over brute-force.

### Outstanding questions naming our design space

**Paper (Outstanding Questions box, page 11):** Among five open questions, two are exactly what a caddy answers:
- *"How can we better capture the influence of EM on semantic memory? In MA-LLMs, EM is often used to supplement the knowledge of a 'frozen', pretrained LLM, whereas — in the brain — EM is used to train semantic memory through a process of consolidation."*
- *"How well can MA-LLMs explain the dynamic interactions that occur between EM and working memory? Recent work has demonstrated that information is shuttled back and forth between an actively represented state (in working memory) and latent representation in EM depending on task demands."*

**Our restatement:** `[ASSERTED]` These are not just open questions — they are the [consolidation-channel](../concept/consolidation-channel.md) and the working-memory-↔-caddy interaction we have been documenting. Norman et al. have written our research programme as their stated open questions. Strong external priority signal.

## Important caveats

- **The paper is a review, not an empirical contribution.** It surveys, names, and synthesises — it does not run experiments. Construct validity of the rubric itself is therefore a matter of cog-sci field consensus, not a single empirical test.
- **The five properties are necessary, not sufficient.** A 5/5 system on this rubric is "human-EM-aligned" — whether this translates to product-relevant performance gains on real agent-memory tasks is the empirical bet Kyrja still has to demonstrate.
- **No system in their survey scores ≥3/5.** EM-LLM (Fountas 2025) at ~2.5/5 is the published ceiling. The rubric is aspirational, not descriptive of current state-of-the-art.
- **The rubric is published but not widely-acted-on.** 11 months after publication (as of [NOW.md](../NOW.md) 2026-05-16), post-Norman publications (Hope, NextMem, GradMem, Auto Dream, AMI Labs, Engramme) do not show systematic engagement with the five properties. See [memory-caddy](../open-question/memory-caddy.md) § "post-Norman gap finding".
- **No explicit benchmark dataset released.** Box 4 is described, not shipped. Building it (or finding a close analogue) is itself work.

## Relevance to Kyrja

- **Anchors [caddy](../concept/caddy.md) as externally-validated architectural pattern.** Norman et al. endorse the sidecar-separate-from-weights-and-context architecture by name — the strongest possible external validation for our wedge.
- **Anchors [norman-rubric](../concept/norman-rubric.md) as the evaluation framework** Kyrja's caddy will be measured against in VC diligence and academic review.
- **Anchors [memory-consumer-axis](../concept/memory-consumer-axis.md) — Norman explicitly endorses memory-for-the-model** (storing internal representations rather than verbatim text).
- **Anchors [consolidation-channel](../concept/consolidation-channel.md)** — the consolidation operator Kyrja has been designing is named in Norman's Outstanding Questions as the missing piece in MA-LLMs.
- **Updates [open-question/memory-caddy](../open-question/memory-caddy.md)** — competitive framing now is "be the first system that scores 5/5 on the Norman rubric," not "novel architectural pattern."

## Audit history

- 2026-05-16 — verbatim read of all 14 pages via PDF render. Coverage: abstract, sections 1-4, all five property subsections, Box 1-4, Outstanding Questions, figures, references (130 entries). Construct validity: rubric properties are cog-sci-field-consensus, not single-experiment claims. Empirical scoring of existing systems against the rubric (EM-LLM=2.5/5, Titans=1.5/5, etc.) is Kyrja-internal synthesis from this paper plus separate readings of those systems — not a Norman et al. claim.

## Archive location

DOI 10.1016/j.tics.2025.06.016. Trends in Cognitive Sciences (Article In Press). Local PDF: [`dong-2025-norman-episodic.pdf`](../../../research/library/papers/dong-2025-norman-episodic.pdf).

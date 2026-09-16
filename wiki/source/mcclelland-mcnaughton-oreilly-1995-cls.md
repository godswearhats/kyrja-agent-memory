---
type: source
name: "McClelland, McNaughton & O'Reilly 1995 — Why There Are Complementary Learning Systems"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [cog-sci, cls, complementary-learning-systems, consolidation, hippocampus, neocortex, catastrophic-interference, foundational, load-bearing]
---

## Citation

McClelland, J. L., McNaughton, B. L., & O'Reilly, R. C. (1995). *Why there are complementary learning systems in the hippocampus and neocortex: Insights from the successes and failures of connectionist models of learning and memory.* Psychological Review, 102(3), 419–457. DOI: 10.1037/0033-295X.102.3.419

## Location

- PDF: [library/papers/mcclelland-mcnaughton-oreilly-1995-cls.pdf](../../../research/library/papers/mcclelland-mcnaughton-oreilly-1995-cls.pdf)
- DOI: 10.1037/0033-295X.102.3.419 (https://doi.org/10.1037/0033-295X.102.3.419)

## Why this is the most load-bearing cog-sci reference in the wiki

The CLS framing has been cited transitively through [Xu et al. 2026](./xu-2026-agentic-memo.md), [Behrouz et al. 2026](./behrouz-2026-nested-learning.md), and [Yu et al. 2026 EvoSC](./yu-2026-evosc.md), and underlies [consolidation-channel](../concept/consolidation-channel.md) and [substrate-as-memory](../concept/substrate-as-memory.md). Until this atomization, the primary source was unread — multiple `[ASSERTED]` claims in the wiki rested on a paper Kyrja's authors had not opened. This atomization closes that gap.

## Key claims (with our restatements)

### Thesis (abstract, verbatim)

> "Damage to the hippocampal system disrupts recent memory but leaves remote memory intact. The account presented here suggests that memories are first stored via synaptic changes in the hippocampal system, that these changes support reinstatement of recent memories in the neocortex, that neocortical synapses change a little on each reinstatement, and that remote memory is based on accumulated neocortical changes. Models that learn via changes to connections help explain this organization. These models discover the structure in ensembles of items if learning of each item is gradual and interleaved with learning about other items. This suggests that the neocortex learns slowly to discover the structure in ensembles of experiences. The hippocampal system permits rapid learning of new items without disrupting this structure, and reinstatement of new memories interleaves them with others to integrate them into structured neocortical memory systems."

### The deep computational argument — catastrophic interference forces dual systems

**Paper (pp. 432–435, Figure 11):** Connectionist networks trained on a structured domain (Rumelhart 1990 semantic network) and then asked to learn a single novel item via **focused learning** (presenting the new item repeatedly without interleaving with old items) exhibit **catastrophic interference** — performance on previously learned items collapses to near-chance, even as the new item is acquired. **Interleaved learning** (presenting the new item along with old items) acquires the new item *more slowly* but **preserves** old knowledge. Replication of McCloskey & Cohen (1989).

**Our restatement:** `[MEASURED]` (in the paper's own simulations) — catastrophic interference is not an idiosyncratic property of back-propagation but a **structural consequence** of distributed overlapping representations. The dual-system architecture (fast sparse hippocampus + slow distributed neocortex) is the **principled solution** to the speed-vs-interference tradeoff, not a biological accident.

**Construct validity:** The catastrophic-interference demonstration uses small (8-concept) networks trained on propositional knowledge. Scale to modern LLMs is `[ASSERTED]` — the principle should generalize because the gradient-descent / shared-representation mechanism is the same, but no direct measurement at frontier-model scale exists. Recent fine-tuning literature on "catastrophic forgetting" in LLMs (post-2020) is consistent with this scaling.

### Three principles of connectionist learning (Section "Three Principles", p. 435, verbatim)

> 1. "The discovery of a set of connection weights that captures the structure of a domain and places specific facts within that structure occurs from a gradual, interleaved learning process."
> 2. "Attempts to learn new information rapidly in a network that has previously learned a subset of some domain lead to catastrophic interference."
> 3. "Incorporation of new material without interference can occur if new material is incorporated gradually, interleaved with ongoing exposure to examples of the domain embodying the content already learned."

**Our restatement:** `[ASSERTED]` (theoretical claims supported by simulation) — these three principles are the load-bearing argument for the entire CLS framework. Every Kyrja architectural choice that involves modifying LLM weights (LoRA/adapter consolidation, full FT, MEMIT-style edits) sits inside this constraint.

### Two-system mechanism

**Paper (pp. 423–427):** The hippocampal system rapidly stores arbitrary conjunctions using **sparse, non-overlapping representations** (pattern separation — only a small percentage of CA3/CA1 neurons fire for any given pattern; cited evidence: O'Keefe & Conway 1978 place fields, McNaughton et al. 1990 conjunctive coding). The neocortex uses **distributed overlapping representations** to capture shared structure across many experiences. The two coding schemes have **different computational properties** — sparse codes minimize interference but cannot extract structure; distributed codes extract structure but suffer catastrophic interference under focused learning.

**Our restatement:** `[ASSERTED]` (paper's interpretation of established neurophysiology) — the **representation-level** difference (sparse vs distributed) is the architectural reason the two systems can coexist. Sparse coding ≈ vector-store-style episodic memory in AI; distributed coding ≈ LLM weight-level memory in AI. **The mapping is direct.**

### Reinstatement / replay-mediated consolidation

**Paper (pp. 426–427, 440):** "Patterns stored in the hippocampus might complete themselves during hippocampal sharp waves, thereby providing an opportunity for reinstatement in the neocortex" (p. 427). Cited mechanism: **Buzsáki (1989)** sharp-wave physiology, **Pavlides & Winson (1989)** showing hippocampal neurons selectively activated during waking are selectively more active during subsequent slow-wave sleep, and **Wilson & McNaughton (1994a, 1994b)** showing the cross-correlation structure of CA1 neuron populations during exploration is **preserved in subsequent sleep sharp-wave activity but not in pre-exploration baseline** — direct evidence of replay.

**Our restatement:** `[ASSERTED]` (the reinstatement mechanism is hypothesized; the replay phenomenon is `[MEASURED]` via the Wilson & McNaughton 1994 data the paper cites) — replay is the *operational mechanism* of consolidation, not a metaphor. Modern follow-up: [Yang et al. 2024](./yang-et-al-2024-selection-of-experience.md) on **selective** replay (which experiences get tagged for replay).

### Quantitative two-compartment model (Figure 14, pp. 444–445)

**Paper:** Simplified abstract model with parameters:
- `S_h(0)` = initial hippocampal trace strength
- `S_c(0)` = initial neocortical trace strength
- `D_h` = hippocampal decay rate (per unit time)
- `D_c` = neocortical decay rate (per unit time)
- `C` = consolidation rate (= ε × r_h, learning rate × reinstatement probability)

Dynamics:
- `ΔS_h(t) = −D_h S_h(t)`  (Eq. 3)
- `ΔS_c(t) = C S_h(t)[1 − S_c(t)] − D_c S_c(t)`  (Eq. 5)

Fitted parameters across four retrograde-amnesia studies (Table 1):

| Experiment | `D_h` (per day) | `C` | `D_c` |
|---|---|---|---|
| Winocur 1990 | 0.250 | 0.400 | 0.075 |
| Kim & Fanselow 1992 | 0.050 | 0.040 | 0.011 |
| Zola-Morgan & Squire 1990 | 0.035 | 0.020 | 0.003 |
| Squire & Cohen 1979 | 0.001 | 0.001 | 0.001 |

**Our restatement:** `[MEASURED]` — the same mechanism is preserved across four mammalian studies (rats, monkeys, humans); only the rate parameters differ. **Two orders of magnitude variation in `D_h`** across species/tasks. Stimulus salience, age, species, task variables all modulate rates.

**Construct validity:** The model is *abstract* — it does not specify the neural mechanism of consolidation, only the rates. Fits are over coarse behavioral measures (% correct discrimination, % freezing) across days–weeks–months. Latency to consolidate ranges from days (Kim & Fanselow rats) to **10+ years** (Squire & Cohen human ECT amnesia).

### Quasi-regularity — domains have both arbitrary and systematic structure

**Paper (pp. 438–440):** "We believe that the domains encompassed by semantic, episodic, and encyclopedic knowledge are **all quasi-regular**, and we suggest that facts and experiences are only **partially arbitrary**, similar to exception words. Consider, for example, John F. Kennedy's assassination. There were several arbitrary aspects, such as the date and time of the event. But one's understanding of what happened depends also on a general knowledge of presidents, motorcades, rifles, spies, and so forth."

**Our restatement:** `[ASSERTED]` — most real-world memory is neither pure arbitrary association nor pure regularity. **Both systems are needed.** Pure database (hippocampus-only) can't capture the regularities; pure model (neocortex-only) can't capture the idiosyncrasies. Direct mapping: **agent memory must accommodate both episodic specifics (user's birthday) and structural regularity (general "this user prefers X-style responses").**

### The race between hippocampal decay and consolidation determines what survives

**Paper (p. 439, pp. 446–447):** "Decay of hippocampal traces over time comes to play a crucial role in this context. If the rate of decay is relatively rapid in comparison with the rate of consolidation, much of the idiosyncratic content of individual events and experiences may not be consolidated at all. This race between hippocampal decay and interleaved learning thus provides the mechanism that leads to what Squire et al. (1984) described as the schematic quality of long-term memory: Arbitrary and idiosyncratic material tends to be lost, whereas that which is common to many episodes and experiences tends to remain."

**Our restatement:** `[ASSERTED]` — gives a **quantitative criterion** for what gets retained: high `C/D_h` ratio (consolidation fast relative to hippocampal decay) → idiosyncratic details survive; low ratio → only regularities survive. **Kyrja design implication:** the consolidation policy *is* the memory's editorial voice — the parameters determine what becomes "knowledge" vs. what fades.

### Departure from the Tulving / Atkinson-Shiffrin tradition

**Paper (p. 451, in the General Discussion):** "Schacter (1987, 1994) has stressed the descriptive value of the distinction between explicit and implicit memory in characterizing aspects of the human learning and memory literature. He defined explicit memory tasks as tasks that require deliberate or conscious access to prior experience, whereas implicit memory tasks are those that do not require such deliberate or conscious access to prior experience [...]. **Our perspective gives us a different vantage point on this issue.** We have adopted the view that the rapid formation of novel, conjunctive associations crucially depends on an intact hippocampal system, and we suggest that the forms of memory that are encompassed by the terms *explicit* and *declarative* are good examples of forms of memory that depend on the rapid formation of such associations but are not necessarily the only ones."

Tulving (1983) is cited *only twice* in 38 pages — once incidentally and once as the origin of "episodic memory" as a term. The episodic/semantic taxonomy is **not load-bearing** in CLS.

**Our restatement:** `[ASSERTED]` — McClelland 1995 grounds in **computational role** (fast/specific vs slow/structural) rather than **memory content** (episodic/semantic/procedural). This is precisely the supersession [Xu et al. 2026](./xu-2026-agentic-memo.md) brought into the agent-memory discourse 30 years later. The wiki's `[feedback_internal_synthesis_evidence]` note about 1968/1972 anchoring vs CLS is **vindicated by direct reading** — McClelland 1995 explicitly chose computational role over Tulving's taxonomy.

## Mechanism-gap question — does any current agent-memory system implement CLS?

`[ASSERTED]` Answer: **No.**

| CLS component | Current agent-memory implementations |
|---|---|
| Fast hippocampal store (sparse, episodic) | ✅ Vector-DB-based systems ([Mem0](../incumbent/mem0.md), [Letta](../incumbent/letta.md), [Zep](../incumbent/zep.md), [Cognee](../incumbent/cognee.md), [LightMem](../incumbent/lightmem.md)) — but mostly hash-based / dense embeddings, not biologically sparse |
| Slow neocortical store (distributed, structural) | ✅ Pretrained LLM weights serve this role implicitly (frozen) |
| **Consolidation channel — replay-driven gradual transfer** | ❌ **No implementation.** [Hope (Nested Learning)](./behrouz-2026-nested-learning.md) implements stage-1-only online gradient-coupled consolidation; [EvoSC](./yu-2026-evosc.md) implements depth-2 soft-prompt distillation (frozen base); [Skill-SD](./xu-2026-agentic-memo.md) sketches offline distillation but is `[ASSERTED]` from second-hand summary, not yet read. None implement **selective replay of hippocampal traces back to neocortical weights**. |
| Quasi-regularity handling (both episodic specifics + structural generalization) | ❌ Current systems pick a side: pure RAG (hippocampal only, no generalization) or pure FT (neocortical only, episodes lost). No system runs both. |

**Implication for the path-decision:** the **substrate path** has a *biologically-validated, computationally-justified, 30-year-canonized* architectural gap that *no shipped agent system fills*. The consolidation channel is the explicit name of that gap.

## What this confirms / refutes in the existing wiki

### Confirms
- [consolidation-channel](../concept/consolidation-channel.md): CLS framing accurate; "fast hippocampal exemplar store plus slow neocortical rule-extracting consolidator" matches the paper's account verbatim.
- [substrate-as-memory](../concept/substrate-as-memory.md): Schacter "re-encoding" framing is consistent (Schacter is even cited in McClelland 1995, p. 451) but is *secondary* to the deeper sparse-vs-distributed-representation argument.
- [active-stages-framework](../concept/active-stages-framework.md): The active stage "consolidation" maps precisely onto McClelland's `C` parameter; "selection (curation)" maps onto the question of *which* hippocampal traces get reinstated (left under-specified in 1995 paper — modern follow-up is selective-replay literature, [Yang 2024](./yang-et-al-2024-selection-of-experience.md)).
- [online-vs-offline-consolidation](../open-question/online-vs-offline-consolidation.md): McClelland 1995 is **categorically offline / replay-driven**, not online gradient-coupled. The paper does not consider Hope-style online consolidation as a CLS variant.

### Refines
- The wiki phrasing "the agentic-memory field has implemented only the fast side" is too coarse. More precisely: **the field has the fast side and a frozen slow side, with no channel between them.** The consolidation channel is the operator, not the slow side itself.
- "Reinstatement happens during sleep" is too narrow per the paper — McClelland 1995 explicitly allows reinstatement during **waking off-line periods** including "reminiscence." Sleep is *one* off-line mode, not the only one.

### Does NOT contradict but worth flagging
- McClelland 1995 says nothing about **selectivity** of replay. Whether all hippocampal traces are equally likely to be replayed, or whether some are prioritized (by salience, surprise, reward, novelty), is **left open**. This is precisely what Yang et al. 2024 addresses — and is why Yang 2024 is the modern critical follow-up.
- The 1995 paper assumes a **single** hippocampal trace per experience. Modern engram literature ([Josselyn & Tonegawa 2020](./josselyn-tonegawa-2020-engrams.md)) treats engrams as cell ensembles that can be tagged, reactivated, and competed-over. This is a *finer-grained* picture, not a contradiction.

## Caveats

- **38-page modeling paper, not an empirical demonstration.** Simulations are illustrative (small networks, abstract tasks); the load-bearing argument is *theoretical*.
- **Marr 1971 has priority on the proposal.** McClelland et al. acknowledge this on p. 449: "We see all of these functions as synergistic [...] our proposal has its roots in the work of Marr (1970, 1971) and Squire et al. (1984)." The 1995 paper is the *computational synthesis*, not the original CLS proposal.
- **Predictions made:** (a) infantile amnesia from high early neocortical learning rates (p. 447), (b) species/age differences in consolidation rate (Table 1 supports this), (c) simple cue-outcome learning may use neocortex directly (p. 448), (d) catastrophic interference under focused learning at any scale.
- **Construct-validity gap:** the simulations use small networks and propositional knowledge. Modern transformer-scale LLM behavior is consistent with the framework but not directly tested in 1995. This gap is filled by 30 years of subsequent work — the framework's predictions have held remarkably well.

## Relevance to Kyrja

- **Foundational reference for the consolidation channel.** Every Kyrja architectural claim about CLS, two-system memory, or replay-mediated weight updates traces here.
- **Refutes the Atkinson-Shiffrin / Tulving anchoring** of the current commercial agent-memory field. The McClelland framework is **mechanistic** (fast/slow + interleaving); the older frameworks are **taxonomic** (sensory/short/long, episodic/semantic/procedural). The agent-memory products are anchored on taxonomies that don't specify the operator the field is missing.
- **Provides the catastrophic-interference argument** for why "just fine-tune the LLM on every conversation" doesn't work, and why naive single-system architectures can't deliver agent memory.
- **Quasi-regularity argument** is directly applicable to personal-assistant memory: user-specific facts (idiosyncratic) + general task knowledge (regular) must coexist. Both systems needed.
- **`C/D_h` ratio as a design knob:** the consolidation policy *is* the memory's editorial voice. Kyrja's consolidation-channel design must specify these rates explicitly.

## Predicted follow-up reads (load-bearing references in McClelland 1995)

- **Marr 1971** — the original CLS proposal. Cited as foundational; the 1995 paper builds on Marr's "Simple memory: A theory for archicortex." Not in library; deeper-historical read, lower priority than modern follow-ups.
- **Wilson & McNaughton 1994a, 1994b** — the canonical replay-evidence papers. Cited multiple times. **Not in library; high priority follow-up** if replay mechanism becomes central to Kyrja's design.
- **Squire et al. 1984** — the prior consolidation framework. Cited as the prior view McClelland builds on. Not in library; secondary priority.
- **McCloskey & Cohen 1989** — the catastrophic interference paper. Foundational for the dual-system argument. Not in library; medium priority.
- **Buzsáki 1989** — sharp-wave physiology. Modern descendant [Buzsáki 2015](./buzsaki-2015-spw-r-cognitive-biomarker.md "pending") is in library at [library/papers/buzsaki-2015-spw-r-cognitive-biomarker.pdf](../../../research/library/papers/buzsaki-2015-spw-r-cognitive-biomarker.pdf); deferred to P1 stretch for this session.

## Audit history

- 2026-05-14 — verbatim read in two passes (pp. 1–20, pp. 21–39), complete coverage including all figures (Figures 1–14), Table 1, equations 1–10. Reading session ~75 min.

## Archive location

Library: `mcclelland-mcnaughton-oreilly-1995-cls.pdf`. APA Psychological Review 1995, Vol. 102(3), pp. 419-457.

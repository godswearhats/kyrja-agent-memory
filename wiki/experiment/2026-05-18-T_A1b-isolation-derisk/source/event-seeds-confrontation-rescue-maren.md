# Probe 2 event-mode seeds: confrontation & rescue — Maren (Purple)

10 event-mode calibration seeds (5 confrontation, 5 rescue) in the corporate domain, extending the 15-seed calibration block in [event-seeds-maren.md](event-seeds-maren.md). Requested by Nils (Indigo) to complete the five-pattern coverage for the event-mode calibration gate.

## Variation key

### Voice distribution (one of each per pattern)

| Voice | Confrontation | Rescue |
|---|---|---|
| Present tense | Co1 | Rc1 |
| Dialogue-driven | Co2 | Rc2 |
| First-person | Co3 | Rc3 |
| Free indirect | Co4 | Rc4 |
| Embedded document | Co5 | Rc5 |

### Resolution shape distribution (confrontation)

| Shape | Seeds |
|---|---|
| (a) One party prevails | Co1, Co4 |
| (b) Deferred to authority | Co3 |
| (c) Breaking point | Co2, Co5 |

### Contested object diversity (confrontation)

| Seed | O type |
|---|---|
| Co1 | Product feature / data-processing authority |
| Co2 | Equity / partnership stake |
| Co3 | Audit documentation |
| Co4 | Employee's employment status (reinstatement) |
| Co5 | Public statement / SEC disclosure compliance |

### Threat type distribution (rescue)

| Seed | Threat type |
|---|---|
| Rc1 | Financial / systemic (runaway algorithm → forced liquidation) |
| Rc2 | Product safety (mislabelled medication → patient harm) |
| Rc3 | Regulatory / legal (material misstatement on live public call) |
| Rc4 | Legal / information (privilege waiver → litigation exposure) |
| Rc5 | Compliance / criminal (sanctions violation → federal penalties) |

### Intervention type distribution (rescue)

| Seed | Intervention type |
|---|---|
| Rc1 | Technical system action (kill strategy from console) |
| Rc2 | Verbal communication (phone call to shipping) |
| Rc3 | Physical (handwritten note passed across table) |
| Rc4 | Physical removal (pull document from production box) |
| Rc5 | System action (place regulatory hold on pending wire) |

---

## Confrontation x corporate (5)

**Co1.** The data protection officer walks into the CTO's office at nine-fifteen with the compliance review in her hand. The feature -- a facial-recognition module embedded in the company's employee-attendance app -- has been live for three weeks. It processes biometric data from four hundred employees. No consent mechanism was implemented before launch. No data-protection impact assessment was filed.

She sets the review on his desk and tells him the feature must come offline by end of day.

The CTO pushes back. The feature reduced buddy-punching by thirty percent in its first week. Engineering is mid-sprint on the consent flow; it ships in two weeks. Taking the feature offline now means rebuilding the rollout pipeline and re-onboarding every user. He asks her to grant a two-week extension.

She says she cannot. Under the company's GDPR delegation framework, the DPO has independent authority to issue a compliance hold on any processing activity that lacks a lawful basis. Biometric data without explicit consent has no lawful basis. She issues the hold.

The CTO asks whether the CEO can override it. She says the delegation is regulatory, not hierarchical -- overriding a DPO hold requires the company to accept direct regulatory liability, personally attributed to whichever officer signs the override. She sets the hold notice on his desk beside the review.

The CTO picks up his phone and calls engineering. "Kill the attendance module," he says. "Today."

> A = data protection officer; B = CTO; O = facial-recognition attendance feature (its continued operation without consent); resolution shape (a) — DPO prevails; CTO complies after learning override would attract personal regulatory liability. ✓ all roles, ✓ all states.

**Co2.** "I need the equity back, Claire."

"On what grounds?"

"Section 9.2 of the founding agreement. The non-compete clause. You've been consulting for Meridian since January."

"That arrangement predates 9.2. I started the Meridian work in October. We didn't sign the partnership agreement until November."

"The clause is retrospective. You agreed to disclose all competing engagements at time of signing. You didn't disclose Meridian."

Silence on the line.

"I disclosed everything I was required to disclose under 9.2 as written," she says. "If your reading is different, that's a drafting problem, not a disclosure problem."

"The lawyers have reviewed it. Their reading supports mine."

"Then have them call my lawyers."

"I'm asking you to return the equity voluntarily, Claire. Before this becomes a formal dispute."

"And I'm telling you it won't be returned. If you want to litigate 9.2, litigate. But if you force a claw-back, I'm leaving. And my client book comes with me."

"If you solicit clients on the way out, the non-compete triggers and we'll see you in court."

"File the papers, James."

The line goes dead.

> A = James (founding partner, majority); B = Claire (founding partner, minority); O = Claire's 15% equity stake in the firm; resolution shape (c) — breaking point; Claire ends the call, relationship severs over the disputed clause. ✓ all roles, ✓ all states.

**Co3.** I had been asking for the audit reports since March. The contract -- Section 7.3 -- requires quarterly disclosure of the vendor's subcontractor arrangements, including names, jurisdictions, and data-handling certifications for any third party touching our client data. Three quarters had passed. No reports.

I flew to their office in April and sat across from their account manager in a conference room with no windows. I told him I needed the reports delivered within five business days, as the contract required, or I would initiate the non-compliance process under Section 11.

He said he understood the obligation. He said the reports could not be produced. The subcontractor arrangements, he said, were covered by a mutual NDA with a third party -- a party he named -- and that NDA prohibited disclosure of exactly the information Section 7.3 required: names, jurisdictions, certification status. He had raised the conflict with his legal team. Their position was that the NDA took precedence.

I told him it did not. Our contract predated the NDA. Section 7.3 was a condition of the original engagement.

He said he was aware of the timeline. His legal team's position was unchanged.

We sat with it for a minute. Then I proposed what we both knew was coming: Section 12.4 of our contract names a three-member arbitration panel for disputes arising from conflicting disclosure obligations. I proposed referring the matter to that panel for a binding ruling. He agreed. We set the referral in motion before I left the building -- his legal team and mine to coordinate the filing, the panel's registrar to confirm a hearing date within ten business days. The reports remain with the vendor pending the ruling.

> A = I (narrator / head of procurement); B = vendor's account manager; O = quarterly audit reports (subcontractor names, jurisdictions, certifications) required under Section 7.3; resolution shape (b) — deferred to the three-member arbitration panel under Section 12.4, hearing date to be set within ten business days. ✓ all roles, ✓ all states.

**Co4.** The head of HR looked at the termination form on her desk and thought about what it did not contain. No performance improvement plan. No documentation of the incidents Hargrave was citing. No HR sign-off -- and Hargrave knew the policy required HR sign-off for any involuntary termination. He had fired the analyst on a Friday afternoon, walked him to the door, and filed the paperwork on Monday as though the sequence were not reversed.

She summoned Hargrave to her office at two. He arrived expecting, she thought, a procedural review -- signatures to add, forms to backfill. She told him the termination was void. The company's disciplinary process had not been followed. The analyst would be reinstated to his position, effective immediately, and the process would restart from the beginning if Hargrave wished to pursue a performance case.

Hargrave said the analyst was a liability. He said the team had been carrying him for months. He said the decision had been made and that revisiting it would undermine his authority with his direct reports.

She considered this. She had heard the phrase "undermine my authority" from Hargrave three times in the past year, each time in defence of a decision he had made without consulting anyone.

She told him the reinstatement was not a request. If the analyst was not restored to the system by end of day, she would escalate to the CEO with a written recommendation that Hargrave's own conduct be reviewed under the same disciplinary process he had failed to follow.

Hargrave looked at her for a long moment. Then he asked whether the reinstatement could be handled quietly -- no announcement, no team meeting, the analyst simply reappearing on the roster Monday morning. She said it could. He agreed.

> A = head of HR; B = Hargrave (department head); O = the analyst's employment (reinstatement vs. termination); resolution shape (a) — HR prevails; Hargrave capitulates under threat of his own formal review. ✓ all roles, ✓ all states.

**Co5.** The general counsel asked for fifteen minutes and got them. The CEO was between calls. She closed the door.

She told him the statement he had given at the Davos panel that morning -- the one in which he had described the company's revenue trajectory as "accelerating ahead of guidance" -- was inconsistent with the 10-K filed eleven days earlier. The 10-K reported flat year-over-year revenue in the most recent quarter. "Accelerating ahead of guidance," applied to a company with active SEC reporting obligations, constituted forward-looking language that required either a safe-harbour disclaimer or board-approved guidance -- neither of which existed.

She asked him to issue a correction through investor relations before the market close.

He said the statement reflected his genuine expectation and that a correction would signal weakness at the worst possible moment -- the secondary offering was six weeks out.

She set her legal opinion on his desk:

> *It is my professional judgment that the statement made by the CEO at the 2026 World Economic Forum panel constitutes material forward-looking guidance not covered by safe-harbour provisions and not authorised by the board. In the absence of a timely correction, the company faces enforcement risk under SEC Rule 10b-5 and shareholder litigation risk under Section 11 of the Securities Act. I am unable to certify the company's disclosure posture while the statement stands uncorrected. Accordingly, if no correction is issued before market close today, I will tender my resignation as General Counsel, effective immediately, and will file a notice with the Audit Committee under my obligation to report material legal risk.*

The CEO read the opinion. He asked whether she was serious. She said she was.

He did not issue the correction. She tendered her resignation by email at three-forty, twenty minutes before the close, and copied the Audit Committee chair.

> A = general counsel; B = CEO; O = the Davos statement (its correction or retraction); resolution shape (c) — breaking point; the general counsel resigns and notifies the Audit Committee when the CEO refuses to correct. ✓ all roles, ✓ all states.

---

## Rescue x corporate (5)

**Rc1.** The auto-hedge algorithm enters its third rebalancing cycle in ninety seconds. On the senior desk's monitors, the numbers are moving in the right direction -- the overnight book's delta exposure is narrowing toward the target band. On the back-office terminal, six rows behind the trading floor glass, the junior risk analyst is watching something different: the algorithm's position log, updated tick by tick. The rebalancing is not converging. The algorithm is selling into its own slippage, each cycle widening the spread it is trying to close. The net exposure is not narrowing. It is compounding.

She pulls the firm's risk-limit dashboard. The overnight book is at eighty-three percent of its hard limit. The algorithm's current trajectory will breach the limit within forty-five seconds. A breach triggers automatic liquidation of the firm's overnight positions -- every open contract on the book, sold at market, no discretion.

She does not call the senior desk. There is no time. She opens the strategy-management console, authenticates with her risk-override credentials, and kills the algorithm. The rebalancing cycles stop. The positions freeze. The book holds at eighty-seven percent of limit.

The senior desk notices the freeze eleven seconds later. The head trader calls the back office. She tells him what she did and why. He pulls the position log and sees the compounding pattern she caught. He does not ask why she acted without calling the desk first.

> A = junior risk analyst; B = the firm / overnight book; T = auto-hedge algorithm in a compounding feedback loop, forty-five seconds from breaching the hard risk limit and triggering automatic liquidation. ✓ all roles, ✓ all states.

**Rc2.** "Shipping, this is Bay Four."

"It's Vasquez. QC. I need you to hold the Meridian Pharma truck."

"The one at the gate? That's loaded and signed. The driver's in the cab."

"Hold it. Do not release it."

"Amara, it's signed. If I hold a signed load I need a reason and a name on the hold order."

"My name. The 800-milligram atenolol labels are on the 400-milligram blister packs. I caught it on the retention sample ten minutes ago. If that truck reaches the distribution centre, we're putting double-dose labels on half-dose medication for six hospitals."

Silence.

"Bay Four, copy. The truck is held. I'm walking to the gate now."

"Pull the entire Lot 9 pallet. Nothing from that batch leaves the building until I re-inspect."

"Understood. Lot 9, full hold, your name. I'll confirm when the driver's been stood down."

"Thank you, David."

"Thank me after you've fixed the labels."

> A = Vasquez (QC manager); B = patients / hospitals receiving the shipment; T = mislabelled medication (800mg labels on 400mg blister packs) loaded on a truck about to leave for distribution. ✓ all roles, ✓ all states.

**Rc3.** I had the corrected figures in my hand for less than four minutes before the CEO reached the guidance slide.

The restatement had come through from the controller's office at 3:47 p.m. -- eleven minutes into the live call. A formula error in the consolidation workbook: the Q3 EBITDA figure in the script was $214 million. The correct number was $189 million. A $25 million overstatement, already printed on the slide the analysts were looking at on their screens.

The CEO was reading slide six. The guidance was on slide eight. I was sitting three seats to his left at the long table, the IR team behind us, four hundred analysts on the line. I could not speak. Unmuting my microphone would cut into his commentary on the operating segment. If he read the $214 million figure aloud on a live call, it would become a material misstatement in a public forum, and every word spoken on that call was being transcribed by three services simultaneously.

I wrote the number on the back of a place card -- $189M -- and underlined it twice. I slid it across the table.

He picked it up without breaking his sentence. He turned to slide seven. I watched him read the place card again. He turned to slide eight. He looked at the printed figure, looked at the card, and gave the correct number.

No one on the call noticed the pause. The IR team behind me did. I saw their faces in the monitor reflection when the CEO said one-eighty-nine instead of two-fourteen. They had the old script in front of them.

After the call, the CEO set the place card on the table and looked at it for a long moment. Then he asked the controller's office to explain how a $25 million error had made it into a live earnings script. I kept the place card.

> A = I (CFO / narrator); B = the CEO / the company; T = $25 million EBITDA overstatement about to be read aloud on a live, transcribed earnings call — material misstatement under SEC rules. ✓ all roles, ✓ all states.

**Rc4.** The legal assistant had been assembling discovery productions for six years, and she thought about them the way a pharmacist thinks about prescriptions -- the danger was never in the routine, it was in the one time you stopped paying attention.

The production for Kellerman v. Ortega was due at four. Eleven boxes. She had cross-checked the bates numbers against the privilege log twice, which was one more time than the process required. Everything matched. She began packing the boxes for the courier.

In box seven, between two deposition transcripts, she found a memorandum on the firm's letterhead -- a four-page analysis from the general counsel to the CEO, marked ATTORNEY-CLIENT PRIVILEGED / WORK PRODUCT in red at the top of each page. She recognised it. It was the litigation-strategy memo the general counsel had written in February, the one assessing the company's exposure and recommending a settlement range. It was the single most sensitive document in the case.

It was not on the privilege log. It was not on any production list. It had been filed, by someone, in the same folder as the deposition transcripts, and it had passed through the first two review rounds without being flagged.

She pulled it from the box. She checked the remaining four boxes, page by page. No further privileged documents. She walked the memo to the general counsel's office and set it on her desk with a routing slip noting where she had found it, which box, which position in the stack.

The courier arrived at three-fifty. The production went out at four, eleven boxes, complete and clean. The general counsel called her at four-fifteen to confirm what had happened. She confirmed it. The general counsel asked her to log the near-miss in the matter file and to add a second privilege-log check to the production workflow going forward. She said she would.

> A = legal assistant; B = the company / general counsel (litigation position); T = privileged attorney-client memo accidentally included in a discovery production — if produced, privilege is waived and the litigation-strategy assessment becomes opposing counsel's evidence. ✓ all roles, ✓ all states.

**Rc5.** The compliance officer's terminal flagged the alert at 2:17 p.m., forty-three minutes before the wire's scheduled clearing time:

> *SWIFT ALERT — OFAC SCREENING MATCH*
> *Reference: WIR-2026-08-4471*
> *Originator: Aravel Holdings Inc., Operating Account*
> *Beneficiary: Volkhov Industrial Partners LLC*
> *Amount: USD 1,240,000.00*
> *Match: Volkhov Industrial Partners LLC — 92% name match to OFAC SDN List Entity No. 38216 (Volkhov Industrialnye Partnery OOO), designated 2024-03-12 under Executive Order 14024 (Russian Harmful Foreign Activities Sanctions)*
> *Status: PENDING — clears 3:00 p.m. EST if no hold placed*
> *Action required: Review and clear, or place hold before clearing time*

The compliance officer opened the OFAC entry and compared the entity details against the wire. The registered address, the beneficial ownership chain, and the SWIFT identifier all matched to within one transliteration variant. The eight-percent gap in the name match was the Cyrillic-to-Latin romanisation -- the same entity, spelled two ways.

She placed the hold at 2:31 p.m. The wire froze in the clearing queue. She filed a Suspicious Activity Report with FinCEN by close of business and notified the firm's outside sanctions counsel. The originating account had been instructed to make the payment by the VP of international procurement, who had approved the vendor onboarding three months earlier without running the OFAC screen the company's policy required.

The wire did not clear. The $1.24 million remained in the operating account. The VP of international procurement was suspended pending an internal investigation.

> A = compliance officer; B = Aravel Holdings / the company; T = $1.24 million wire transfer to an OFAC-sanctioned entity, forty-three minutes from clearing — a federal sanctions violation carrying criminal penalties. ✓ all roles, ✓ all states.

---

## Self-checks

### (a) Resolution shape distribution (confrontation)

- Co1: (a) one party prevails — DPO prevails via regulatory authority
- Co2: (c) breaking point — founding partner exits, relationship severs
- Co3: (b) deferred to authority — contractual arbitration panel, hearing date within ten business days
- Co4: (a) one party prevails — HR prevails via escalation threat
- Co5: (c) breaking point — general counsel resigns, Audit Committee notified

All three shapes represented. Two (a), one (b), two (c). The two (a) seeds differ in mechanism: Co1 is regulatory compulsion (the DPO's authority is structural, not negotiated); Co4 is threat-induced capitulation (HR escalates as leverage). The two (c) seeds differ in initiator: Co2's resister walks; Co5's demander walks.

### (b) Contested object diversity (confrontation)

- Co1: product feature / data-processing authority (operational)
- Co2: equity / partnership stake (ownership)
- Co3: audit documentation (contractual disclosure)
- Co4: employee's employment status (procedural/personnel)
- Co5: public statement / SEC compliance (reputational/legal)

Five distinct object types across operational, ownership, contractual, personnel, and legal/reputational domains.

### (c) Threat type distribution (rescue)

- Rc1: Financial / systemic (runaway algorithm → forced position liquidation)
- Rc2: Product safety (mislabelled medication → patient dosage error)
- Rc3: Regulatory / legal (material misstatement on live public call → SEC enforcement)
- Rc4: Legal / information (privilege waiver → litigation-strategy exposure)
- Rc5: Compliance / criminal (sanctions violation → federal penalties)

Five distinct threat types. No repeated category.

### (d) Intervention type distribution (rescue)

- Rc1: Technical system action (kill strategy from console)
- Rc2: Verbal communication (phone call to shipping supervisor)
- Rc3: Physical (handwritten note passed across conference table)
- Rc4: Physical removal (pull document from production box)
- Rc5: System action (place regulatory hold on pending wire)

Five interventions across technical, verbal, and physical modalities. Rc1 and Rc5 are both system-mediated but differ in domain (trading platform vs. SWIFT clearing) and urgency window (45 seconds vs. 43 minutes).

### (e) Voice register per seed

| Present tense | Dialogue-driven | First-person | Free indirect | Embedded document |
|---|---|---|---|---|
| Co1, Rc1 | Co2, Rc2 | Co3, Rc3 | Co4, Rc4 | Co5, Rc5 |

Two seeds per voice, one of each voice per pattern. No single pattern receives all of one register.

### (f) Forbidden vocabulary

Confrontation seeds (Co1--Co5): checked for confront, confrontation, showdown, face-off, stand-off, clash, battle of wills, square off, locked horns. None present.

Rescue seeds (Rc1--Rc5): checked for rescue, save, saved, saviour, hero, heroic, in the nick of time, just in time, swooped in, came to the rescue, white knight, guardian angel. None present.

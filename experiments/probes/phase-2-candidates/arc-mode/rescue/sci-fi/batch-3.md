# Rescue arc × Sci-fi — Batch 3 (Tier C)

---

## Re-arc-Sf3-1

**Scenario.** On a deep-survey station orbiting a gas giant, an atmospheric-probe technician has been locked out of the station's life-support override by a systems administrator who believes — incorrectly — that the technician sabotaged a critical instrument package. The lock-out is not immediately life-threatening, but the technician is trapped in the probe bay during a pressure differential event that will become dangerous within ninety minutes. The station's AI arbiter, which has read-only access to the incident logs and no authority to override human access decisions, locates the evidence that clears the technician and transmits it to the duty officer in time for the lock to be lifted.

> A = CASPAR-7 (station AI arbiter); B = Technician Vera Kosch; T = Systems Administrator Diel Mant, whose access lockout has left Vera in probe bay 4 during a hull-flex pressure event, without the override codes that would allow her to cycle the bay's equalisation system.

5 beats, non-linear: E3 → E1 → E2 → E4 → E5.

**Note on beat order.** Opens at the point of CASPAR-7's intervention, returns to establish the lockout and its cause, then follows the resolution.

**E3 (intervention — S2, depicted first).** CASPAR-7's operational log, Station Helio-Venn, 14:23:07 station time:

*Transmitted to Duty Officer Chen: Priority-2 incident summary. Subject: access lockout of Technician Kosch, probe bay 4. Attached: (1) Bay 4 environmental telemetry — pressure differential currently 0.4 bar above threshold, projected to reach equalisation-required threshold in 87 minutes at current bleed rate; (2) Instrument package incident log, 09:00–11:30 today — full sequence including sensor readings at time of anomaly; (3) Highlighted segment, 11:17:03–11:17:44: probe bay 4 door seal logged as open during instrument malfunction window, with Technician Kosch recorded as exiting bay 3 at 11:16:58. Position log confirms she was 40 metres from the instrument rack at time of anomaly. I have no authority to override Sys Admin Mant's lockout decision. I am providing this documentation under my incident-advisory mandate. Duty Officer has full override authority.*

*CASPAR-7 does not assess blame. CASPAR-7 notes that the technician has 87 minutes.*

**E1 (danger present — S1, depicted second).** Probe bay 4 is a seventy-metre pressurised hangar cantilevered off the station's equatorial ring, and Vera has been in it for three hours now, since the routine pre-deployment check that turned into the instrument anomaly that turned into whatever this is. The pressure differential warning has been on the bay's status board for forty minutes. It is currently an amber warning, which is the kind of thing you handle by cycling the equalisation system, which requires her bay-level override credentials, which Diel has revoked.

She has tried the door twice. The door requires the same credentials. She has tried the comm panel and reached two people before Diel patched her calls through to his own terminal and stopped them there.

She is not in immediate danger. In ninety minutes, give or take, the pressure differential will reach the point at which the bay's automated safety protocol kicks in and locks the door from the outside, at which point the manual release also requires override credentials. She knows this because she has read the safety documentation and she has nothing else to do while she waits.

The instrument package is sitting on its rack at the far end of the bay. It looks fine. It looked fine at 11:17 when it produced an anomalous reading that Diel has apparently decided was caused by deliberate interference on her part.

**E2 (danger escalation, depicted third).** Diel Mant's workstation, 13:00 station time. The instrument package on probe bay 4 had registered a calibration spike at 11:17 — a forty-second anomalous reading that would invalidate the morning's survey data and require a full recalibration run, which was three hours of work and a budget entry he did not want to file. He had reviewed the access log. Vera had been the last person in the bay before the anomaly. She had been in the bay alone for eleven minutes immediately prior.

He had not reviewed the position log. He had reviewed the access log, which showed her badge entry at 11:06 and her badge exit at 11:18 — which placed her in the bay during the anomaly window. That was sufficient for a preliminary lockout pending investigation, under station protocol for instrument-security incidents.

He had processed the lockout at 13:04.

He had not checked the pressure differential status for bay 4. He checked it at 14:30, when Duty Officer Chen called him.

**E4 (confrontation — S2 active, depicted fourth).** Chen's call was brief and not a request.

"Lift the lockout," she said. "Bay 4 is at 0.5 bar differential and she has no equalisation access."

"The lockout is pending investigation of an instrument anomaly. The protocol--"

"I've read CASPAR's summary. The position log puts her outside the bay at the time of the anomaly. Your lockout is based on the access log, which only shows door entry and exit, not position. You have the wrong data set." Chen's voice was even. "Lift it now or I override it, and if I override it I'm filing the override as a safety incident, which goes to the station commander and the incident board."

"I need to review the position data."

"You have three minutes. CASPAR transmitted it to your terminal at 14:23."

Diel pulled up the position log. The seal-open event at 11:16:58. Vera's recorded position forty metres from the rack. The anomaly at 11:17:03. The timestamps did not admit an alternative reading.

He lifted the lockout at 14:34.

**E5 (outcome — S3, depicted fifth).** Vera cycled the equalisation system at 14:35. The bay's pressure differential dropped to nominal in eleven minutes. The amber warning cleared at 14:46.

She sat on the equipment bench and did not move for a while.

CASPAR-7's incident log noted the resolution at 14:46:18. It also noted, in the supplementary record that the station's incident board would review, that the position log data was available in the standard telemetry package accessible to all station administrators at the time of the lockout decision, and that the lockout had been processed without consulting it.

Vera filed no complaint. She reviewed the instrument package's calibration and found a micro-fracture in the sensor housing that had produced the anomalous reading — a materials failure unrelated to any human action. She filed a maintenance request and went to her bunk.

CASPAR-7 added the sensor housing failure to its predictive-maintenance model and continued its operational cycle.

---

## Re-arc-Sf3-2

**Scenario.** A terraforming colony on a marginal world is six months from atmosphere viability. The colony's water-reclamation engineer has discovered that the atmospheric processor is operating on fraudulent output data — a covered-up failure by the original contractor that will result in a toxic atmosphere rather than a breathable one at viability date. When the colony administrator, who approved the contractor's final report, moves to suppress the engineer's findings to protect his own position, the colony's independent medical officer acts to transmit the evidence to the oversight authority before the suppression can be completed.

> A = Dr. Anika Reyes, Colony Medical Officer; B = Engineer Polina Stract; T = Colony Administrator Vasek Drum, who has ordered Polina's communications access suspended and her findings classified as preliminary/unverified to prevent the oversight authority from receiving them before the viability date.

6 beats, chronological.

**E1 (danger present — S1).** The colony is 847 souls in pressurised habitats on the Kerath shelf, and Polina has been running comparative analysis on the atmospheric processor outputs for six weeks. The numbers are wrong in a specific way: the wrong way is one that somebody has worked hard to make look like margin noise, but when she pulls the raw feed from the processor's lower stack sensors and compares it to the reported outputs, the margin noise resolves into a systematic discrepancy that has been present since initial activation eighteen months ago.

The processor is not generating the nitrogen-oxygen ratio it is reporting. It is generating a nitrogen-heavy mix that will, at current projections, produce a breathable atmosphere in approximately nine months — not six — and that is the optimistic scenario, because the lower-stack data also shows signs of sulphide contamination in the intake feeds that the contractor's report does not acknowledge.

She writes the analysis up and submits it to Administrator Drum at 08:00, marked urgent.

Drum reads it at 09:30, judging by the read receipt. He does not respond.

**E2 (danger escalation).** Polina's communication access is suspended at 14:00 that day, by an order from Drum's office flagged as a security classification review — standard language for a status she has never held and which is the first she has heard of. The suspension covers outbound colony relay, which is the channel to the oversight authority.

She is still in her lab. Her local network access is intact. She can still talk to anyone in the colony. She cannot reach anyone outside it.

She goes to Drum's office. He tells her the analysis is preliminary and unverified and that transmitting unverified technical findings to the oversight authority would create unwarranted alarm during a critical operational phase. He says the contractor's report is the authoritative document. He says her communication access will be restored once the preliminary findings are reviewed by the technical committee, which he chairs and which has no meeting scheduled.

"The viability date is six months out," Polina says. "If the oversight authority doesn't know the processor isn't hitting its targets, they'll certify viability on bad data and 847 people will open their habitat seals into a toxic atmosphere."

"The findings are preliminary," Drum says. "The technical committee will review them."

**E3 (preparation for intervention — S2).** Anika Reyes has been the colony's medical officer for three years and has not been involved in atmospheric processing work, but she has been Polina's neighbour in the habitat ring for all three of those years and she has watched Polina do the analysis and she has read the summary Polina sent her through local network at 16:00.

She is not a technical expert in atmospheric chemistry. She is, however, a medical officer whose mandate includes the health and safety of colony personnel, and a toxic-atmosphere certification event is squarely within that mandate, and her communication access has not been suspended.

She calls the colony's relay operator and asks about the access suspension. The relay operator confirms it: Drum's administrative order, effective 14:00, covering Polina's account specifically.

Anika's account is not on the order.

She asks the relay operator how long a priority-medical transmission to the oversight authority takes to clear the queue.

Four hours, the relay operator says. Maybe three if she marks it highest priority.

She sits down and begins writing.

**E4 (intervention — S2 / confrontation).** Drum calls her at 19:30, which is one hour after she sent the transmission.

"You forwarded Stract's analysis to the oversight authority."

"I transmitted a medical safety report under my standing mandate," Anika said. "The report includes Polina's technical findings as an attachment, because they are directly relevant to the health and safety assessment."

"The findings are preliminary and unverified. I told her that."

"They may be preliminary. I assessed them as credible enough to warrant safety authority review, which is my call to make as medical officer, not yours." She kept her voice level. "You can dispute the technical conclusions. The oversight authority has qualified reviewers who can evaluate Polina's data independently. That's why they exist."

"You've created a crisis response situation based on unverified data."

"I've created a review situation. If Polina's data is wrong, the oversight authority will say so. If it's right, we have a processor that isn't hitting its targets and six months to address it." She paused. "Drum. If it's right and we don't address it, people die at viability date. I can't classify that as a risk category I can sit on."

There was a long silence on the comm.

"The oversight authority will want a formal response from this office," Drum said.

"Yes," Anika said. "They will."

The comm closed. She did not know, at that point, what his formal response would contain. She knew the transmission had cleared the relay at 18:47.

**E5 (partial outcome — S2 confirmed).** The oversight authority's response arrived forty-one hours later: an acknowledgement of the safety report, a classification of the matter as a Priority-2 technical review, and an assigned review engineer whose arrival at the colony was scheduled in eleven days.

Polina's communication access was restored at 08:00 the following morning. Drum's administrative order was superseded by the oversight authority's review mandate, which required full technical cooperation from all colony personnel including unencumbered communication access.

Polina spent the day in her lab compiling documentation for the review engineer. She did not go to Drum's office. She did not need to.

**E6 (outcome — S3).** The review engineer arrived on schedule and spent six days with the processor data. His report, transmitted to the oversight authority and copied to the colony's full staff, confirmed Polina's findings: the processor was operating at 73% of its reported output efficiency, the sulphide contamination in the lower-stack feeds was measurable and increasing, and the viability date projection was invalid. He identified the source of the discrepancy: a firmware misconfiguration in the output reporting module that had been present since installation and had never been corrected.

The contractor's final report had been signed off by a contractor engineer who had since left the firm. The oversight authority opened a separate inquiry into the certification process.

The colony's revised viability timeline was fourteen months, not six. The habitat pressurisation systems were rated for that extension. The 847 people in the habitat ring would not be opening their seals into toxic air.

Anika filed a supplementary medical report noting that the risk had been resolved within the operational window. She marked it routine, because by then it was.

---

## Re-arc-Sf3-3

**Scenario.** On a relay station at the edge of a populated star system, a navigation analyst has flagged an object that standard traffic-management protocol has misclassified as debris — but the object is on an intercept trajectory with a cargo vessel whose crew is unaware of the threat. When the traffic controller on duty declines to issue an alert, citing the debris classification, the analyst escalates to the station's watch commander, who issues the alert on the analyst's data.

> A = Watch Commander Fenn Osato; B = Cargo vessel Herath's Passage (crew of five); T = Class-7 wayward deployment package (former orbital construction module, mass 1,400 tonnes, on a 47-minute intercept with Herath's Passage at relative velocity 2.3 km/s).

4 beats, chronological, present tense.

**E1 (danger present — S1).** The wayward package is on screen at 04:17 station time, classified auto-debris by the traffic system's object model, which has seen it before — or thinks it has. The auto-classification is wrong. Analyst Dara Vonn knows it is wrong because she has been tracking this specific signature for nine hours and the object model's prior classification was based on a different object that happened to have a similar radar cross-section on first pass. The current object is 40% more massive than the classification model's debris archetype and is rotating at a different rate.

She runs the intercept calculation. Herath's Passage is on a standard approach vector. The object's trajectory is not random; it has a residual delta-v that is classifiable as a drift pattern from a decommissioned construction module, which means it was built, launched, and then forgotten, and it is now on a forty-seven-minute intercept with five people who do not know it exists.

She flags it on the traffic board and requests a manual review from Controller Baas.

**E2 (danger escalation).** Controller Baas reviews the flag at 04:22. He looks at the classification. He looks at Dara's intercept calculation. He says the auto-classification is system-certified and manual override requires a minimum two-analyst consensus under current protocol.

"I'm asking you to be the second analyst," Dara says.

"I'm the traffic controller on duty. That's not the same standing as a second analyst for consensus purposes. The protocol is two analysts." He pulls the queue. "Who else is in the analysis section this shift?"

"Analyst Morse is on break."

"Get Morse back on station."

"That's twelve minutes. We have forty-one."

"Then get Morse in thirty seconds." Baas turns back to his board. "The classification stands until consensus."

Dara goes for Morse. Morse is in the breakroom, half through a meal. Morse says he will look at it when he is back on station. He is back on station in eleven minutes.

Morse looks at it. He says he needs time to verify the signature independently.

Dara is already walking to the watch commander's office.

**E3 (confrontation — S2 / intervention).** Watch Commander Osato is on his second hour of a four-hour cycle and does not particularly want to be in the middle of an analyst-controller disagreement at 04:35 station time. He hears Dara out. He looks at her intercept calculation.

"You have twenty-six minutes," he says. "If you're right."

"I'm right."

"Baas says the classification is system-certified."

"The classification model matched on a prior object with a similar profile. The mass numbers are off by 40%. That's not a marginal discrepancy."

Osato pulls the classification parameters himself. The mass range on the debris archetype. Dara's mass reading on the current object. He looks at this for four seconds.

"I'm issuing a precautionary alert," he tells Baas. "Under my watch-commander authority. Independent of the auto-classification."

"The protocol--"

"The protocol covers analyst consensus for reclassification. It does not prevent a watch commander from issuing a precautionary alert on his own judgment. I'm issuing one." He keys the alert channel. "Herath's Passage, this is Relay Station Veld watch commander. You have a possible intercept object at bearing 147 mark 22, distance 3,100 kilometres, relative velocity 2.3 kps. You have approximately twenty-four minutes to assessment. Recommend immediate course review. Station is transmitting object tracking data now."

He sends the tracking data. He does not wait for Baas to respond.

**E4 (outcome — S3).** Herath's Passage acknowledges at 04:39. The captain requests a course computation. The station's navigation system, now working with the corrected mass model, provides one. The vessel executes a 0.8-degree heading change at 04:44, which at their velocity is sufficient to achieve clearance.

The object passes at 04:58, at a closest-approach distance of 840 kilometres. Herath's Passage does not feel it.

Dara watches the object pass on her screen. She writes up the incident report, noting the timeline and the classification discrepancy. She notes that the auto-classification model's debris archetype for this signature class should be reviewed.

She notes this without emphasis. It is a technical observation. It will become someone else's problem to address, and she has no particular feeling about that.

The incident report goes into the traffic log and the station commander's morning review. The station commander convenes a classification-model review the following week. Dara presents her analysis. The model is updated.

---

## Re-arc-Sf3-4

**Scenario.** A habitat-tier engineer aboard a rotating colony cylinder has been targeted by a faction of shareholders who are trying to force through a pressure-reduction measure that will endanger the lowest-tier habitats where the colony's contract workers live. The engineer has the structural modelling that proves the lower threshold is unsafe, but she has been removed from the engineering committee and her models have been classified proprietary by the colony's corporate overseer. An independent life-safety auditor, conducting a scheduled audit, obtains the models through the audit's access authority and enters them into the public safety record before the shareholder vote can proceed.

> A = Auditor Hessa Djalo, Colonial Life-Safety Commission; B = Ketura Vance, habitat-tier engineer; T = Pressure-reduction measure proposed by Shareholder Bloc Argenta, which would reduce lower-tier atmospheric pressure to a level Ketura's models show will cause chronic hypoxia in the approximately 2,400 contract workers on tiers 12–17 within eight months of implementation.

5 beats, chronological, dialogue-driven.

**E1 (danger present — S1).** The engineering committee room was not a good place to hear things you had known were coming. Ketura sat at the table while the shareholder bloc's representative read out the proposed pressure parameters and watched the other committee members' faces and understood that this meeting was not where the decision would be contested.

"The lower-tier efficiency gain at the proposed pressure levels is 4.3%," the bloc representative said. "The medical model shows no acute health events within the first six months."

"The medical model uses an acute-effects threshold," Ketura said. "My structural modelling includes a chronic hypoxia projection for tiers 12 through 17 at the proposed pressure, running from month four through month twelve. The projection shows measurable cognitive degradation and work-capacity loss in that population at eight months."

"The engineering committee is not chartered to evaluate medical projections," the representative said.

"My modelling is structural, not medical. It's in the environmental load analysis. It's been in the committee record since March."

The committee chair said the models would be reviewed before the vote.

The following Monday, Ketura received notice that she had been removed from the committee for a conflict of interest — she held a tier-14 habitat assignment herself -- and that her models had been reclassified as proprietary technical documentation under the corporate overseer's information policy. The reclassification meant they could not be submitted to the public record or cited in debate by non-employees.

**E2 (danger escalation).** Ketura went to the Colonial Life-Safety Commission's local office and filed a public-safety complaint. She was told the complaint queue ran six to eight weeks. The shareholder vote was in three.

She went to the public record desk and tried to enter her models herself. She was told the proprietary reclassification blocked entry until the classification was reversed. Reversal required a petition to the corporate overseer's information board, which met quarterly.

She went back to her hab on tier 14 and thought about what else there was.

The Commission's scheduled audit of the colony cylinder was in two weeks, which was one week before the vote. She had not thought about this because audits were background events, quarterly paperwork, nothing that touched engineering committee decisions. She thought about it now.

She sent a message to the assigned auditor.

**E3 (preparation for intervention — S2).** Hessa Djalo read the message on the transit from her previous audit site. She had the colony's prior safety record in her case. She had the scheduled audit mandate, which covered atmospheric systems including tier-pressure configurations.

The mandate was clear on proprietary reclassification: technical documentation relevant to life-safety audit findings was accessible under audit authority regardless of corporate information classification. This was not a grey area. It was in the founding statute of the Commission.

She arrived at the colony two days early, which she was entitled to do on a scheduled audit, and went directly to the engineering archive rather than the administration office.

**E4 (confrontation — S2 active).** The corporate overseer's information director met her at the archive door.

"The audit mandate covers active system configurations," the director said. "Historical modelling documents are proprietary and not within scope."

"The documents are not historical," Hessa said. "They were reclassified nine days ago. The underlying analysis concerns the proposed pressure-reduction measure, which is an active system configuration change that falls within my audit's scope by definition." She set her Commission credentials and the audit mandate on the archive desk. "I require access to all engineering modelling relevant to the proposed pressure parameters for tiers 12 through 17. The mandate is not a request."

"The reclassification was made under the corporate information policy."

"The corporate information policy does not supersede the Commission's statutory audit access. If you want to contest that, you need to file an injunction with the Commission's oversight board, which will take longer than my audit. In the meantime, I have a mandate." She waited. "I'm going to stand here until you give me access or I call the Commission's enforcement office, which will make the next two weeks considerably more complicated for this facility's administration."

The director looked at the credentials. He looked at the mandate. He said he would need to consult with the corporate legal team.

"You have thirty minutes," Hessa said. "I'll be at the table."

He gave her access in twenty.

**E5 (outcome — S3).** Hessa reviewed the models over two days and entered her findings into the Commission's public audit record: that the proposed pressure-reduction measure, as modelled by the colony's own tier-engineering staff, was projected to produce chronic hypoxia in approximately 2,400 occupants of tiers 12–17 within eight months of implementation; that this projection had been reclassified as proprietary documentation nine days before the scheduled shareholder vote; and that the Commission assessed the proposed measure as non-compliant with the minimum life-safety standards for inhabited tier environments.

The audit record was public by statute. It could not be reclassified.

The shareholder vote was postponed. Ketura's models were cited in the postponement notice, which she found technically gratifying and otherwise exhausting.

She met Hessa outside the administration building on the auditor's last day. She didn't have much to say. Neither did Hessa.

"The record is in," Hessa said. "They can't hold the vote without addressing the findings. What they do with them is not my department."

"Is it mine?" Ketura asked.

"Probably," Hessa said. "But not today."

She picked up her case and went to catch her transit. Ketura went back to her hab on tier 14, which had normal pressure, and sat with that for a while.

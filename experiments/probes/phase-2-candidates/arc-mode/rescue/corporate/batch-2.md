# Rescue arc × Corporate — Batch 2 (Tier B)

## Re-arc-Co2-1

**5 beats, chronological, dialogue-driven**

**Scenario.** A hedge fund's head of compliance discovers that a rogue algorithmic trading module is about to execute a series of orders that will trigger margin calls large enough to bankrupt the fund and wipe out its pension-fund clients' capital. The CTO, who built the module, is unreachable. The compliance officer must convince the exchange liaison to halt the fund's order queue before the market opens.

> A = head of compliance (Nadia Hassoun); B = pension-fund clients (represented by their capital in the fund); T = rogue algorithmic trading module set to execute at market open, triggering cascading margin calls and total capital loss.

**E1 (danger present scene).** The compliance floor, 5:47 a.m., ninety minutes before the opening bell. Nadia's overnight risk monitor flagged the anomaly at 5:31 -- a batch of 1,400 synthetic options orders queued in the execution pipeline, each leveraged at forty-to-one, all timed to fire in the first three seconds of trading. She pulled the order manifest and read it twice. The notional exposure was eleven billion dollars. The fund's total assets under management were six hundred million.

She called the CTO's mobile. It rang through to voicemail. She called his home line. No answer. She called his assistant, who said he had taken a redeye to San Francisco and his phone was off until landing at 9:15 Eastern.

Nadia set the phone down and looked at the order manifest again. If those orders executed, the clearing house would issue margin calls within minutes. The fund could not meet them. Liquidation would begin before lunch. The pension-fund clients -- teachers, municipal workers, firefighters -- held four hundred and twenty million of the six hundred million. She opened the exchange liaison's emergency contact sheet.

**E2 (failed initial response scene).** The same floor, 5:58 a.m. Nadia reached the exchange's night-desk operator and asked to be connected to the order-halt team. The operator asked for the fund's member ID, the nature of the request, and the authorising officer's name.

"I need an emergency queue freeze on our execution pipeline," Nadia said. "Member ID seven-four-one-nine. The authorising officer is me -- Nadia Hassoun, head of compliance."

"Ma'am, a queue freeze requires authorisation from your firm's designated trading principal. That's listed here as Marcus Whelan."

"Marcus Whelan is the CTO. He's on a plane. He's unreachable until after the bell."

"Then I can escalate to our regulatory liaison, but that process takes forty-five minutes minimum, and I'll need a written request on firm letterhead faxed to--"

"We don't have forty-five minutes. The orders fire at open. I need someone with override authority."

The operator paused. "I can transfer you to the senior floor governor's desk. He has discretionary halt authority. But he's not obligated to take the call, and if he does, he'll want documentation I can't waive."

"Transfer me," Nadia said.

The line went to hold music. She watched the clock on her terminal: 6:02.

**E3 (preparation for intervention scene).** The compliance floor, 6:04 a.m. While the hold music played, Nadia pulled up the fund's counterparty risk dashboard and began assembling documentation. She exported the order manifest as a PDF with timestamps. She pulled the margin model and ran the scenario: if the orders executed, the clearing house's automated margin call would hit at 9:33 a.m., the fund would fail to post collateral by the 10:00 a.m. deadline, and forced liquidation would begin at 10:01. She captured the output.

She drafted a one-page summary: the orders, the leverage, the notional exposure, the margin-call timeline, and the client breakdown showing pension-fund capital as a percentage of total AUM. She attached the CTO's travel itinerary showing the redeye departure and the 9:15 landing time. She printed everything and set it beside her phone.

The hold music stopped. A voice answered: "Governor's desk. Morales."

**E4 (intervention scene).** "Mr. Morales, this is Nadia Hassoun, head of compliance at Kerrigan Capital, member seven-four-one-nine. I'm requesting an emergency discretionary halt on our firm's execution queue. I've sent documentation to your secure portal -- order manifest, margin scenario, and client-capital breakdown."

"I see it," Morales said. She heard him clicking through the files. "Fourteen hundred orders. Forty-to-one leverage. And your trading principal signed off on this?"

"He did not. The orders were queued by an automated module. The CTO who manages the module is in transit and unreachable. I do not have credentials to kill the queue from our side -- only the trading principal does, and the backup principal resigned two weeks ago. The position hasn't been filled."

"You're asking me to halt a member firm's queue on the word of a compliance officer who doesn't have trading authority."

"I'm asking you to look at the margin model. If those orders execute, Kerrigan fails its margin call by 10:00. Forced liquidation begins at 10:01. Four hundred and twenty million dollars of pension-fund capital gets unwound in a falling market. Your clearing house takes the counterparty loss on the remainder."

Morales was quiet for several seconds. "That last part -- the clearing-house exposure. What's the number?"

"Worst case, depending on fill prices, between ninety and one hundred and forty million."

"Hold." The line went silent. Nadia watched the clock: 6:11. When Morales came back, his tone had changed. "I'm issuing a discretionary halt on your execution queue effective immediately, pending review by the full regulatory board at 8:00 a.m. Your orders will not fire at open. I need you in our offices by 7:30 with everything you just sent me, plus the CTO's full access log for the last ninety days."

"I'll be there," Nadia said.

**E5 (outcome / aftermath scene).** The exchange's regulatory offices, 7:42 a.m. Nadia sat at a conference table across from Morales and two members of the exchange's compliance review board. Her documentation was spread between them. The order manifest, the margin model, the client breakdown, the CTO's travel itinerary, the automated module's configuration log.

Morales confirmed for the board that he had issued the discretionary halt at 6:12 a.m. The orders had been frozen in the queue. None had executed. The fund's client capital remained in position, unaffected.

The board chair asked Nadia what would have happened without the halt. She walked them through the margin model: the cascade from execution to margin call to forced liquidation, the pension-fund exposure, the timeline. The chair wrote something on his pad and passed it to Morales.

At 9:17 a.m., the CTO's phone came back online. He called the compliance floor and got Nadia's deputy, who told him what had happened. Nadia, still in the exchange's offices, did not take the call. She was reviewing the exchange's incident report, verifying that the frozen orders had been flagged for cancellation rather than deferral. She initialled each page and pushed the stack across the table.

---

## Re-arc-Co2-2

**4 beats, chronological, free indirect style**

**Scenario.** A pharmaceutical company's quality-assurance director discovers that a contaminated ingredient lot has already been blended into sixty thousand units of a paediatric medication scheduled for distribution in thirty-six hours. The plant manager refuses to halt the line. The QA director must escalate through the company's safety-recall chain to pull the batch before it ships.

> A = QA director (Priya Chandran); B = patients (children who would receive the contaminated medication); T = contaminated ingredient lot (Lot 227-K, mycotoxin levels fourteen times above the safety threshold) blended into sixty thousand units scheduled for distribution.

**E1 (danger present scene).** The laboratory on the third floor of the Carrinex manufacturing facility, a Tuesday afternoon. Priya had been reviewing the weekly assay results when the chromatography data for Lot 227-K stopped making sense. The mycotoxin readings were not borderline. They were not ambiguous. They were fourteen times above the threshold the FDA had set for paediatric formulations.

She pulled the blending records. Lot 227-K had been received on Friday, passed the supplier's certificate of analysis, and been blended into production batch PB-4401 on Monday morning. PB-4401 was sixty thousand units of liquid suspension -- a paediatric antibiotic prescribed to children between the ages of two and eight. The batch was in final packaging. Distribution was scheduled for Thursday morning, thirty-six hours from now, to four regional wholesalers who supplied hospital pharmacies across eleven states.

Priya set the chromatography printout on her desk and stared at it. Fourteen times above threshold in a paediatric product. She picked up the phone and called the plant manager's extension.

**E2 (danger escalation / failed initial response scene).** The plant manager's office, twenty minutes later. Ray Ogden sat behind his desk with the chromatography printout in front of him and his production schedule on the monitor to his left. Priya stood across from him. She had explained the readings. She had explained the blending records. She had explained what fourteen times above threshold meant for a two-year-old's liver.

Ray had listened. He was not dismissing the data. But he was looking at the production schedule, and Priya could see the calculation happening behind his eyes -- the calculation that had nothing to do with mycotoxins and everything to do with the quarterly shipment target that Carrinex's CFO had circled in red on the operations dashboard three weeks ago.

He told her the supplier's certificate of analysis had cleared the lot. He told her the in-house rapid screen had not flagged it. He suggested the chromatography equipment might need recalibration. He asked her to rerun the assay before he considered pulling a sixty-thousand-unit batch off the line thirty-six hours before a shipment deadline that the CEO had personally committed to during the last earnings call.

Priya told him she would rerun the assay. She also told him she was required by the company's quality agreement to notify the VP of regulatory affairs whenever a confirmed out-of-spec result exceeded ten times the threshold, and that she intended to do so within the hour regardless of the rerun. Ray said he understood. His tone suggested he wished she hadn't said that part out loud.

**E3 (intervention scene).** The VP of regulatory affairs' office, one floor up, forty-five minutes later. Priya had rerun the assay. The second set of readings matched the first: fourteen times above threshold, plus or minus half a unit. She brought both printouts, the blending records, the distribution schedule, and the company's quality agreement with the section on mandatory batch holds highlighted in yellow.

The VP, Helen Park, read the chromatography data, set it down, and asked one question: had the plant manager agreed to a voluntary hold?

Priya said he had not. He had asked for a rerun, which she had completed. The results were confirmed. He had not yet placed a hold.

Helen picked up her phone and called the plant manager directly. Priya heard Ray's voice through the earpiece -- muffled but recognisable. Helen told him that under Section 9.3 of the quality agreement, a confirmed out-of-spec result at this severity level triggered a mandatory batch hold, that the hold was not discretionary, and that she was entering it into the compliance system now. She told him to stop packaging on PB-4401 and segregate all finished units. Ray said something about the shipment deadline. Helen said the shipment deadline was no longer relevant to this conversation and that she would inform the CEO's office herself. She hung up.

Helen turned to Priya and asked her to draft the lot-isolation order and the distributor notification. She said she would contact the FDA's district office before end of business to file a voluntary field alert. Priya said she would have the paperwork within the hour.

**E4 (outcome scene).** The manufacturing floor, the following morning. Priya walked the line with the quality-assurance team. The packaging stations for PB-4401 were shut down. The sixty thousand units -- thirty-eight thousand already in final packaging, twenty-two thousand still in intermediate containers -- were segregated in the quarantine bay, tagged with red isolation labels, and logged out of the distribution system.

Helen had filed the field alert with the FDA the previous evening. The four regional wholesalers had been notified that the Thursday shipment was cancelled. The CEO's office had been informed. An outside laboratory had been contracted to run an independent confirmation assay, results expected by Friday.

Priya checked the quarantine log against the blending records to confirm that every unit produced from Lot 227-K was accounted for. It was. Nothing from PB-4401 had left the facility. She signed the quarantine verification form, dated it, and filed it with the batch record.

---

## Re-arc-Co2-3

**6 beats, non-linear: E1 (aftermath) -> E2 (danger present) -> E3 (danger escalation) -> E4 (failed initial response) -> E5 (preparation / intervention) -> E6 (outcome), present tense, embedded document**

**Scenario.** A data-privacy officer at a health-insurance company discovers that a scheduled overnight batch process will export the unencrypted medical records of 1.2 million members to an unsecured third-party analytics vendor. The export is fourteen hours away. The CIO, who approved the integration, insists the contract covers the data handling. The privacy officer must invoke the company's data-governance override before the batch runs.

> A = data-privacy officer (Tomasz Krol); B = 1.2 million health-insurance members whose unencrypted medical records are scheduled for export; T = overnight batch export to an unsecured third-party vendor (Meridian Analytics), set to execute at 2:00 a.m.

**E1 (aftermath scene -- depicted first).** The boardroom, three days later. The general counsel reads the following into the incident record:

> *On Tuesday the 14th, the data-privacy officer invoked Governance Override 7.1 to halt a scheduled data export to Meridian Analytics. The override was executed at 11:47 p.m., two hours and thirteen minutes before the batch was set to run. The export did not execute. No member data left the company's systems. An independent audit of Meridian Analytics' infrastructure, completed Wednesday the 15th, confirmed that the vendor's receiving environment lacked encryption at rest, lacked access-control logging, and did not meet the minimum security standards required under the company's data-processing addendum. The CIO's office has acknowledged that the vendor qualification process did not include a security assessment by the privacy office, as required under Section 3.2 of the data-governance charter.*

The general counsel closes the document. The board chair asks if there are questions. There are several.

**E2 (danger present scene).** Tuesday the 14th, 10:15 a.m., the privacy officer's desk. Tomasz is reviewing the weekly data-flow log when he sees the new entry: a batch export scheduled for 2:00 a.m. Wednesday, sending a full member-record extract -- names, dates of birth, Social Security numbers, diagnosis codes, prescription histories, claims data -- to Meridian Analytics via unencrypted FTP.

He reads the entry again. Unencrypted FTP. 1.2 million member records. He opens the vendor registry and searches for Meridian Analytics. The entry is sparse: a signed contract, a scope-of-work document, and a vendor-qualification checklist signed by the CIO's office. The security-assessment field is blank. No penetration test. No encryption audit. No data-handling certification.

He checks the data-governance charter. Section 3.2 requires the privacy office to complete a security assessment of any third-party vendor receiving personally identifiable health information before data transfer is authorised. No assessment has been requested. No assessment has been completed. The export is fifteen hours and forty-five minutes away.

**E3 (danger escalation scene).** The same desk, 10:40 a.m. Tomasz has pulled the batch-export configuration from the integration team's deployment log. The configuration is worse than the data-flow log suggested. The export is not a sample. It is a full extract: every active member, every field in the claims database, no redaction, no pseudonymisation, no tokenisation. The FTP credentials are stored in a plaintext configuration file on a shared drive accessible to the entire analytics department.

He runs a port scan on Meridian's receiving server. The FTP port is open. There is no TLS wrapper. He attempts an anonymous login. It fails, but the server's banner identifies it as running software that was end-of-life two years ago, with three known unpatched vulnerabilities listed in the CVE database. He documents each finding in a timestamped log.

The batch is now fourteen hours and twenty minutes away.

**E4 (failed initial response scene).** The CIO's office, 11:15 a.m. Tomasz presents his findings. The CIO, David Lam, listens. He acknowledges the missing security assessment. He says the contract with Meridian includes a data-processing addendum that places responsibility for security on the vendor's side. He says pulling the export now would delay the analytics project by six weeks and jeopardise a board-level initiative to reduce claims-processing costs by Q3.

Tomasz tells him the data-processing addendum is not a substitute for the security assessment required under Section 3.2. The addendum assigns contractual liability. It does not encrypt the data. It does not patch the server. It does not prevent a breach.

David says he will ask Meridian to confirm their security posture in writing before the batch runs. He asks Tomasz to hold off on any escalation until he has that confirmation.

Tomasz says he cannot hold off. Section 3.2 is not discretionary. The batch must not run until the security assessment is complete. He tells David he is prepared to invoke Governance Override 7.1 if the export is not cancelled by end of business.

David says that is a significant escalation and suggests they revisit the conversation at 4:00 p.m., after he has spoken with Meridian.

**E5 (preparation / intervention scene).** Tomasz's desk, 9:30 p.m. David's 4:00 p.m. update never came. At 5:15, his assistant sent an email saying David was in back-to-back meetings and would follow up in the morning. The morning is after the batch runs.

Tomasz checks the deployment log. The export is still scheduled. No changes to the configuration. No cancellation.

He opens the data-governance charter to Section 7.1: the privacy officer may invoke an emergency override to halt any data transfer that presents an imminent risk of unauthorised disclosure of protected health information, without prior approval from the CIO, provided that the override is documented, time-stamped, and reported to the general counsel within twenty-four hours.

He drafts the override notice, documenting the missing security assessment, the unencrypted FTP configuration, the unpatched server, and the CIO's decision to proceed without remediation. He timestamps the document at 11:47 p.m. He submits the override through the governance system. The system accepts it and pushes a halt command to the batch scheduler.

He refreshes the deployment log. The export status changes from "scheduled" to "halted -- governance override." He saves a screenshot, attaches it to the override notice, and emails the general counsel.

**E6 (outcome scene).** Wednesday morning, 8:00 a.m. Tomasz is at his desk when the general counsel calls. She has read the override notice. She asks him to walk her through the timeline. He does -- the data-flow log, the missing assessment, the server vulnerabilities, the CIO's response, the override.

She tells him she has already requested an independent audit of Meridian's infrastructure, to be completed by end of day. She tells him the export will remain halted until the audit is finished and the privacy office has completed a full security assessment. She thanks him and hangs up.

At 8:45, David Lam's assistant calls Tomasz to ask if he is available for a meeting at 9:00. Tomasz says he is. He gathers his documentation and walks to the CIO's office. The deployment log on his screen still reads "halted -- governance override." The 1.2 million member records remain inside the company's encrypted systems, where they have been all along.

---

## Re-arc-Co2-4

**5 beats, chronological, mixed voice (dialogue in key scenes, tight narration elsewhere)**

**Scenario.** A construction-company safety inspector discovers that a high-rise project's temporary shoring system is critically overloaded and will collapse within hours, burying the ground-floor crew under four storeys of wet concrete. The project superintendent refuses to stop the pour. The inspector must get the site shut down through the general contractor's authority before the next concrete truck arrives.

> A = safety inspector (Luis Reyes); B = ground-floor structural crew (twelve workers); T = critically overloaded temporary shoring system on the verge of collapse under four storeys of wet concrete.

**E1 (danger present scene).** The fourth-floor deck of the Alcott Tower project, 6:20 a.m. Luis was conducting the weekly shoring inspection when he heard it -- a sound like a rifle shot, sharp and percussive, from somewhere below the deck plates. He stopped walking. The labourers working the concrete pump twenty feet away didn't react. Jobsite noise.

He knelt and put his hand flat on the formwork. He felt the vibration in his palm -- a low, arrhythmic tremor that shouldn't have been there. He pulled the shoring calculations from his clipboard and rechecked the specs: the temporary shores on levels one through three were rated for the dead load of the formwork plus the wet concrete of one floor at a time. The pour sequence called for level four to be poured today, with levels two and three already loaded and not yet cured.

The combined load on the level-one shores was three floors of wet concrete, not one. Someone had accelerated the pour schedule without recalculating the shoring. Luis took his phone out and photographed the load chart, the pour schedule taped to the foreman's shack, and the deflection he could see in the nearest shore post -- a lateral bow of roughly two inches that had not been there last Tuesday.

Below the deck, twelve members of the structural crew were tying rebar on the ground floor, directly beneath the shoring system.

**E2 (failed initial response scene).** The superintendent's trailer, 6:35 a.m. Luis spread his documentation on the table -- the load chart, the pour-schedule acceleration, the photographs of the deflected shore post.

"The level-one shores are carrying three times their rated load," he said. "The pour on four needs to stop, and the ground-floor crew needs to be pulled out until we get an engineer to assess the shoring."

The superintendent, Frank Harwell, looked at the photographs. He picked up the load chart and studied it. Then he set it down.

"The concrete trucks are already dispatched. First one's here in forty minutes. If I stop the pour now, I lose the entire batch -- that's eighty yards at a hundred and forty a yard. Plus the pump rental, plus the crew standing around on overtime."

"Frank, the shores are deflecting. I heard a post crack."

"Posts creak on every pour. That's what they do. The shoring was designed by a licensed engineer and it's been holding for three pours. I'm not shutting down a two-hundred-thousand-dollar pour day because you heard a noise."

Luis told him the shoring was designed for one floor of wet load, not three. Frank said the engineer had built in a safety factor and that the schedule acceleration had been discussed with the project manager. Luis asked if the engineer had been consulted on the revised sequence. Frank said he didn't know and that it wasn't the inspector's call to stop the pour. That authority belonged to the general contractor.

**E3 (preparation for intervention scene).** The parking lot outside the trailer, 6:42 a.m. Luis sat in his truck and called the general contractor's project executive, Diane Ortiz. Her phone went to voicemail. He left a message: shoring overloaded, superintendent refuses to halt, ground-floor crew at risk, first concrete truck arriving in thirty-five minutes.

He hung up and called the structural engineer of record, whose number was on the shoring drawings. The engineer answered on the third ring. Luis described the load condition -- three floors of uncured concrete on shores rated for one -- and the deflection he had observed. The engineer was quiet for a moment, then said the words Luis needed to hear: the shores were not designed for that load, there was no safety factor that covered a three-to-one overload, and the pour should be stopped immediately.

Luis asked the engineer to send that in writing. The engineer said he would email it within ten minutes. Luis thanked him and hung up.

At 6:51, the email arrived. At 6:53, Diane Ortiz called back.

**E4 (intervention scene).** Luis was still in his truck when Diane's call came through. He gave her the summary: three floors of wet concrete on shores rated for one, deflection visible, audible cracking, superintendent refusing to halt, engineer of record confirming in writing that the system was beyond its design capacity.

"Forward me the engineer's email," Diane said.

He forwarded it. He heard the notification chime on her end. Thirty seconds of silence while she read it.

"I'm calling Frank now," she said. "No more concrete goes on that deck. Pull the ground-floor crew to the east lot, outside the collapse radius. I'll have a stop-work order in the system in fifteen minutes. Do not wait for the order -- get those people out now."

"I'll need Frank to cooperate. He's not going to take it from me."

"He'll take it from me. I'm his contract. Stay on the line."

He heard her dial out on a second line. He heard Frank answer. He heard Diane tell Frank that the pour was stopped effective immediately by order of the general contractor, that the ground-floor crew was to be evacuated to the east lot, and that a structural engineer would be on site by 8:00 a.m. to assess the shoring. Frank started to say something about the concrete trucks. Diane told him to send them back and that Ortiz & Crane would cover the batch cost. Frank said he understood.

**E5 (outcome scene).** The east parking lot, 7:10 a.m. Luis stood by the site fence and counted the ground-floor crew as they came through the gate. Twelve workers, all accounted for. They gathered near the equipment trailer, some of them still carrying tools, most of them confused about why they'd been pulled off the floor forty minutes into the shift.

The concrete pump on level four was shut down. The first truck had arrived at 7:02 and been turned away by the gate foreman with a copy of the stop-work order. The second truck, five minutes behind, was rerouted to a different project.

At 8:15, the structural engineer arrived with a field technician. They entered the building from the east stair, away from the shoring zone, and spent forty minutes on levels one through three. When the engineer emerged, he walked directly to Luis.

The assessment was straightforward. Two of the level-one shore posts had buckled. A third had sheared its base plate. The engineer estimated that the system would have failed within hours -- possibly sooner if the level-four pour had continued adding load. The failure mode would have been progressive: one post gives, the load redistributes, the next post gives, and the entire deck assembly comes down. Four storeys of wet concrete and formwork onto the ground floor.

Luis looked across the lot at the twelve workers drinking coffee by the equipment trailer. The engineer began writing his report.

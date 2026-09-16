# Defection arc x Corporate -- Batch 1 (Tier A)

---

## D-arc-Co1-1

**4 beats, chronological, dialogue-driven**

**Scenario.** A startup's co-founder and CTO signs a vesting agreement requiring four years of continuous service and full IP assignment. Fourteen months in, she begins building a parallel product on personal infrastructure using the startup's proprietary architecture, intending to launch it after her shares vest. The CEO discovers the parallel codebase when a cloud billing alert routes to the wrong account.

> A = CEO / co-founder; B = CTO / co-founder; P = vesting and IP assignment agreement (all intellectual property created during employment belongs to the company; four-year continuous service requirement for full vesting; no competing product development during tenure); V = designing and building a parallel product on personal cloud infrastructure using the company's proprietary architecture and data models while still employed and vesting.

**E1 (commitment scene).** The conference room at the law firm, three days before incorporation. The lawyer had printed two copies of the founders' agreement and set them on opposite ends of the table.

"Walk me through the IP clause," the CTO said.

The lawyer read it: all intellectual property conceived, developed, or reduced to practice during the term of employment, whether during business hours or not, and whether using company resources or not, belongs exclusively to the company. The clause covered code, architectures, data models, algorithms, and derivative works. The vesting schedule was four years with a one-year cliff. Full acceleration only on acquisition or IPO.

"That's standard," the CEO said. "We both sign the same thing. Same terms, same cliff, same IP assignment."

The CTO read the clause again, slowly. "And if I build something on my own time that has nothing to do with what we're building?"

"Then you file a disclosure and the board reviews it. But anything that touches our architecture, our data model, or our market -- that's ours. That's the deal."

She signed. He signed. The lawyer notarised both copies and handed one to each of them.

**E2 (violation scene).** A Saturday afternoon, fourteen months later. The CTO's apartment. Her personal laptop was open on the kitchen table, connected to a cloud account registered under her personal email. The account had been active for three months.

She was working on the routing layer. The architecture was the same one she had designed for the company -- the same sharding logic, the same query optimisation patterns, the same data model with the field names changed. She had not copied code. She had rebuilt it from memory, which was easy, because she had designed the original.

The product was narrower than the company's -- a single vertical, a single customer segment -- but the bones were identical. She had mapped the company's full architecture onto a smaller frame and was ahead of where the company had been at the same stage. She knew the mistakes to avoid because she had already made them once on someone else's dime.

She committed the routing layer to a private repository, pushed it to the personal cloud instance, and ran the integration tests. All green. She closed the laptop and made dinner.

**E3 (discovery scene).** Monday morning, the CEO's desk. The finance lead knocked and came in holding a printout from the company's cloud provider.

"We got a billing anomaly alert," she said. "But it's not ours. The provider's SSO flagged a second account using the same authentication domain. Someone registered a personal account using their company email prefix with a different provider suffix. The usage pattern is dev-environment shaped -- compute spikes on weekends, storage growing steadily, no production traffic."

The CEO looked at the account identifier. He recognised the email prefix. It was the CTO's.

He asked the finance lead to pull the metadata the provider would share without a subpoena: account creation date, region, resource types, storage volume. She came back in twenty minutes. The account was three months old. The primary resources were a sharded database cluster and an application server running the same framework the company used. The storage footprint was consistent with a mid-stage product build.

He sat with the printout for a long time. Then he called the company's outside counsel and asked for a meeting that afternoon.

**E4 (confrontation scene).** Wednesday morning, the CEO's office. He had asked her to come in before the team arrived. The outside counsel was on speaker, muted, listening.

"I need you to give me access to the personal cloud account," he said. "The one registered three months ago. I need to see what's in it."

She didn't answer immediately. She looked at the printout on his desk -- the billing metadata, the account creation date, the resource summary.

"It's a side project," she said. "Personal infrastructure, personal time, personal money. The IP clause covers company resources. I didn't use company resources."

"The IP clause covers anything that touches our architecture, our data model, or our market. You wrote the clause review yourself. You know what it says."

"I know what it says. I also know it wouldn't survive a challenge. Clauses that broad get thrown out in every jurisdiction that matters. You can't own the inside of my head."

"I'm not trying to own the inside of your head. I'm asking you to open an account that, based on the resource profile, contains a product built on the architecture you designed for this company. If it's unrelated, show me and we're done."

She was quiet for ten seconds. Then she said: "I'm not giving you access. If you want to see it, get a court order. And if you try to terminate me for cause before my cliff, I'll file an injunction before you finish the paperwork."

The CEO unmuted the speaker. "Karen, you heard all of that?"

The outside counsel confirmed she had. She said she would file for a temporary restraining order and an emergency asset preservation request by end of day. She advised the CEO not to revoke the CTO's system access until the filing was complete, to avoid a spoliation claim.

The CTO stood. "You're making a mistake," she said.

"Maybe," the CEO said. "But the filing happens today. You can have your lawyer call Karen by five, or you can read about it tomorrow."

She left the office. The outside counsel began dictating the filing.

---

## D-arc-Co1-2

**5 beats, chronological, free indirect style**

**Scenario.** A firm's senior partner assigns a junior partner to manage the due diligence on a high-value acquisition. The junior partner, who has a undisclosed personal investment in the target company, omits material liabilities from the diligence report. The acquiring firm closes the deal and discovers the liabilities three months later when the target's CFO resigns and the balance sheet restates.

> A = senior partner; B = junior partner; P = fiduciary duty and firm conflict-of-interest policy (all personal financial interests in any client, target, or counterparty must be disclosed in writing before assignment; diligence reports must reflect all material findings without omission); V = failing to disclose a personal equity stake in the target company and omitting three material liabilities from the due diligence report, resulting in the acquiring firm closing on incomplete information.

**E1 (commitment scene).** The senior partner's corner office, a Tuesday in March. The junior partner had been with the firm for six years and had made partner eleven months earlier. The senior partner remembered the promotion committee's discussion -- sharp, methodical, no drama. The kind of lawyer who made you forget he was in the room until the memo landed and it was better than anyone expected.

The senior partner explained the assignment: Kessler-Martin was acquiring a logistics company called Drayline. Mid-market deal, $340 million valuation, closing targeted for late June. The junior partner would run the diligence. Full scope -- financial, legal, regulatory, environmental. He would report to the senior partner, who would present to the client.

The senior partner slid the conflict-of-interest disclosure form across the desk. Every assignment required one. The firm's policy was explicit: any personal financial interest in a client, target, counterparty, or related entity must be disclosed in writing before work begins. Material omissions were grounds for termination and referral to the state bar.

The junior partner read the form, checked the box marked "no conflicts to disclose," signed it, and handed it back. The senior partner countersigned and placed it in the engagement file.

**E2 (trust-displayed scene).** The war room on the fourteenth floor, six weeks into diligence. The junior partner had assembled a team of four associates and had been running them hard. The senior partner stopped by on a Friday afternoon to check progress.

The war room was organised the way the junior partner organised everything -- colour-coded binders, a tracking spreadsheet projected on the wall screen, every document catalogued by category and risk rating. The associates were at their stations. One of them was on the phone with Drayline's outside counsel, working through an environmental permit question.

The junior partner walked the senior partner through the status: 812 documents reviewed, 34 flagged for follow-up, two potential issues elevated to discussion level -- a pending OSHA citation at a distribution centre and an ambiguity in a customer contract's termination clause. Neither was a deal-breaker. The financial review was clean. The regulatory review was on track.

The senior partner left the war room satisfied. He told the client's general counsel that the diligence was proceeding well and that the junior partner was as thorough as advertised. The general counsel said she was glad to hear it.

**E3 (violation scene).** The war room, a Wednesday evening three weeks before the scheduled close. The junior partner was alone. The associates had gone home. He had the Drayline financial files open on two screens.

He was looking at three items. The first was an unfunded pension obligation that Drayline's CFO had restructured as a deferred compensation plan -- technically off the balance sheet, but representing $18 million in future liability. The second was a pending environmental remediation order at a decommissioned facility in New Jersey, estimated cost between $6 million and $14 million, disclosed in a footnote to a subsidiary's filing that the associates had not flagged. The third was a guarantee Drayline's founder had personally extended to a vendor, which the company had quietly assumed when the founder retired -- $4.2 million, contingent, not reflected in the current liabilities.

The junior partner had found all three. He understood their materiality. He also understood that any one of them could delay the close, reduce the purchase price, or kill the deal entirely. And if the deal died, Drayline's share price -- currently trading at a premium on acquisition rumours -- would correct to its pre-announcement level. The junior partner held 11,000 shares of Drayline, purchased through a brokerage account in his wife's maiden name fourteen months before the engagement began.

He closed the three files. He opened the diligence report draft and read through the financial section. The pension obligation was not mentioned. The environmental order was not mentioned. The vendor guarantee was not mentioned. He saved the draft without adding them.

**E4 (discovery scene).** The senior partner's office, a Monday in September, three months after close. The senior partner's assistant had flagged an urgent message from Kessler-Martin's general counsel. The senior partner called her back.

The general counsel's voice was flat. Drayline's CFO had resigned the previous Friday. Over the weekend, the interim CFO had discovered three items missing from the balance sheet: an unfunded pension obligation restructured as deferred compensation, a pending environmental remediation order at a decommissioned New Jersey facility, and an assumed vendor guarantee from the founder's era. Combined exposure: $28 million to $36 million. The general counsel had pulled the firm's diligence report. None of the three items appeared.

The senior partner asked the general counsel to send the underlying documents. She did. He opened them at his desk and read each one. Then he opened the diligence report and searched for any reference to the pension, the remediation, or the guarantee. Nothing.

He pulled the war room's document tracking spreadsheet from the engagement archive. The three source documents were logged. They had been received, catalogued, and assigned to the junior partner's personal review queue. They had been opened. The metadata showed access timestamps. The junior partner had reviewed all three documents during the engagement period.

The senior partner closed the spreadsheet. He called the firm's general counsel and asked her to come to his office.

**E5 (confrontation scene).** The following morning, the senior partner's office. The junior partner arrived at eight. The firm's general counsel was already seated by the window. The door was closed.

The senior partner laid the three documents on his desk beside the diligence report. "These were in the data room. You reviewed them. They don't appear in the report. I need to know why."

The junior partner looked at the documents. He did not pick them up. "The pension restructuring was a judgment call. Deferred compensation plans aren't balance-sheet liabilities under the framework Drayline's auditors applied. The environmental order was preliminary -- no final determination, no binding remediation schedule. The vendor guarantee was contingent and below our materiality threshold."

"The vendor guarantee alone is $4.2 million. Our materiality threshold on this engagement was $2 million. You set that threshold yourself."

"I'm telling you my professional judgment was that these items, individually and collectively, did not rise to the level of material findings requiring inclusion in the final report."

The firm's general counsel spoke. She said the firm had received a preservation notice from Kessler-Martin's outside litigation counsel that morning. She said the state bar's ethics office had been copied. She asked the junior partner whether he had any personal financial interest in Drayline or any related entity.

The junior partner did not answer.

The firm's general counsel said that the firm's compliance team had run a brokerage screen that morning under the engagement's retroactive audit clause. She named the brokerage account. She named the number of shares. She named the purchase date.

The senior partner watched the junior partner's face. Something moved behind it and then settled.

"I want to speak to my own lawyer," the junior partner said.

"That's your right," the senior partner said. "Your access to firm systems is suspended as of now. The compliance team will escort you to your office to collect personal items. The firm will cooperate fully with the bar investigation and with Kessler-Martin's counsel."

The junior partner stood. He did not offer a hand. He walked to the door, opened it, and the compliance officer was already waiting in the corridor.

---

## D-arc-Co1-3

**6 beats, non-linear: E1 -> E2 -> E5 -> E3 -> E4 -> E6, embedded-document voice**

**Note on beat order.** This sequence is depicted non-chronologically. The chronological order is: E1 (commitment) -- E3 (trust-displayed) -- E4 (first-signal) -- E2 (violation) -- E5 (discovery) -- E6 (confrontation). The depicted order interleaves the violation early, then loops back to show the trust context and signal before resolving with discovery and confrontation.

**Scenario.** A pharmaceutical company's head of clinical trials signs a data integrity charter binding her to report all adverse events from a Phase III trial without modification. Under pressure to meet a regulatory submission deadline, she reclassifies seven serious adverse events as unrelated to the study drug, altering the trial's safety profile. A biostatistician preparing the submission filing notices the reclassifications when the raw event log and the summary report diverge.

> A = chief medical officer (CMO); B = head of clinical trials; P = data integrity charter (all adverse events recorded in the clinical trial database must be reported in the regulatory submission exactly as classified by the site investigators; no reclassification without independent adjudication committee review and written approval; the head of clinical trials bears personal responsibility for the accuracy of all safety data in the submission); V = reclassifying seven serious adverse events from "possibly related" to "unrelated" in the submission dataset without adjudication committee review, altering the drug's safety profile in the regulatory filing.

**E1 (commitment scene).** The boardroom on the executive floor, a Thursday in January. The CMO had convened the trial leadership team for the Phase III kickoff. The data integrity charter was projected on the wall screen. The legal department had revised it twice since the last trial.

The CMO read the operative clause aloud: all adverse events recorded in the clinical trial database are to be reported in the regulatory submission exactly as classified by the site investigators. No reclassification of any adverse event is permitted without independent adjudication committee review and written approval. The head of clinical trials bears personal responsibility for the accuracy of all safety data submitted to the regulatory authority.

He asked each member of the trial leadership team to sign the charter individually. The head of clinical trials signed third. The compliance officer witnessed each signature and logged them in the trial master file. The CMO countersigned the charter as sponsor representative and closed the meeting.

**E2 (violation scene).** A Sunday night in October, nine months into the trial, the head of clinical trials' home office. The regulatory submission deadline was eleven days away. The submission dataset was due to the biostatistics team by Wednesday for final formatting.

She had the adverse event database open on her work laptop. The trial had enrolled 2,400 patients across forty-three sites. The safety profile was good -- better than the Phase II data had predicted -- except for seven events. Seven patients at four different sites had experienced serious adverse events that the site investigators had classified as "possibly related" to the study drug. The events were clinically similar: elevated liver enzymes progressing to symptomatic hepatotoxicity, all occurring within the same dosing window.

Seven events in 2,400 patients. A rate of 0.29%. The regulatory threshold that would trigger a boxed warning -- the kind of warning that could reduce the drug's market by 40% -- was 0.25%. She was four hundredths of a percentage point above the line.

She opened each of the seven event records. She changed the relatedness classification from "possibly related" to "unrelated -- concurrent medication." She did not submit the changes to the adjudication committee. She did not generate a reclassification request form. She edited the fields directly in the database, saved each record, and closed the event log.

The submission dataset she exported on Wednesday morning showed a "possibly related" serious adverse event rate of 0.00%.

**E5 (discovery scene).** The biostatistics department, the following Monday. Dr. Kahn, the senior biostatistician assigned to the submission, was running the final validation checks. The process was routine: compare the summary tables in the submission draft against the raw event log archived at database lock.

The database had been locked on September 30. The submission dataset had been exported on October 15. Dr. Kahn pulled both files and ran the reconciliation script.

The script flagged seven records. In the locked database, these records showed a relatedness classification of "possibly related." In the submission dataset, the same records showed "unrelated -- concurrent medication." The patient identifiers matched. The event descriptions matched. The dates matched. Only the classifications had changed.

Dr. Kahn checked the adjudication log. No reclassification requests had been filed for any of the seven events. No adjudication committee meetings had been convened since database lock. The audit trail on each record showed a single modification, made from the same user account, on the same date, within a forty-minute window. The user account belonged to the head of clinical trials.

Dr. Kahn saved the reconciliation output, locked it in the biostatistics archive, and walked to the CMO's office.

**E3 (trust-displayed scene).** Five months earlier, a Wednesday afternoon. The data safety monitoring board had convened for its second interim review. The CMO attended as an observer. The head of clinical trials presented the safety data.

She was precise. She walked the board through every serious adverse event reported since the last review, including two hepatotoxicity cases at sites in Ohio and Germany that had been classified as "possibly related" by the site investigators. She did not minimise them. She presented the clinical details, the dosing history, the patients' concurrent medications, and the site investigators' reasoning for the relatedness classification.

The board chair asked whether she had considered requesting reclassification. She said she had not. The site investigators had examined the patients. Their classification reflected their clinical judgment. If the adjudication committee wanted to review the cases independently, she would facilitate that, but she would not initiate a reclassification request based on her own reading of the data.

The CMO noted her answer. After the meeting, in the corridor, he told her that her presentation had been exactly right. The board needed to see that the trial leadership would report what the data showed, not what the sponsor wanted to hear. She said that was the only way she knew how to do it.

**E4 (first-signal scene).** Three weeks before the submission deadline. A Friday afternoon in the open-plan area outside the clinical operations suite. Two clinical research associates were comparing notes before leaving for the weekend.

"Did you see the revised timeline?" the first one said. "She moved the dataset export up by a week. Biostatistics doesn't even have the reconciliation protocol ready yet."

"She's under pressure. The CMO told the board the submission would be on time. If it slips, that's her problem."

"I know, but she's been in the office every weekend for a month. She cancelled the last two team check-ins. And she asked me for the raw event log password on Tuesday -- she's never needed that before. She has her own database access."

The second associate shrugged. "She's probably running her own QC pass. She always does that before a major submission."

"Yeah," the first one said. "Probably."

They closed their laptops and left.

**E6 (confrontation scene).** The CMO's office, Tuesday morning. Dr. Kahn had delivered the reconciliation report the previous afternoon. The CMO had read it, verified the audit trail timestamps, and confirmed that no adjudication committee review had taken place. He had asked the head of clinical trials to come in at seven-thirty.

She arrived and saw the reconciliation report on his desk. She saw Dr. Kahn's name on the cover page.

"I need you to restore the seven records to their original classifications," the CMO said. "Today. Before the submission package goes to formatting."

"If those records go back to 'possibly related,' we cross the boxed-warning threshold," she said. "The drug works. The hepatotoxicity cases are confounded by concurrent statin use at three of the four sites. The site investigators didn't have the cross-site data when they made their classifications. I did."

"Then you file a reclassification request with the adjudication committee. You present the cross-site data. You let them make the determination. That's the process you signed onto in January."

"The adjudication committee can't convene before the submission deadline. You know that. Filing a request now means a three-month delay, minimum. The patent window closes in fourteen months. A three-month delay costs us the first-mover advantage in two markets."

"That is not a reason to alter safety data."

"I didn't alter safety data. I applied a clinical judgment that the adjudication committee would have reached if the process weren't too slow to function."

The CMO opened the data integrity charter and placed it beside the reconciliation report. He pointed to her signature.

"Restore the records," he said. "Accept the delay. Or I file a deviation report with the regulatory authority today and refer the matter to the compliance committee. Those are the two options."

She looked at the charter. She looked at the reconciliation report. She was silent for a long time.

"I'll restore the records," she said. "But I want the adjudication committee convened within two weeks, and I want to present the cross-site data. If they agree with me, the submission goes forward with the reclassified data and we lose a month, not three."

The CMO considered it. "I'll convene the committee. But the submission does not go to the regulatory authority until the committee rules, and if they disagree with your clinical judgment, the original classifications stand and the boxed-warning analysis goes into the filing."

She nodded once. "I'll have the records restored by end of day."

"And your database access is suspended pending the compliance committee's review of the audit trail. Dr. Kahn will handle the dataset export."

She stood. She did not argue the suspension. She left the office and the door closed behind her.

---

## D-arc-Co1-4

**5 beats, chronological, present tense**

**Scenario.** A tech company's board appoints an independent director to chair the audit committee, with an explicit mandate to ensure financial reporting accuracy and flag any related-party transactions. The director quietly steers a $12 million cloud infrastructure contract to a company owned by his brother-in-law, structuring the deal through a subsidiary to avoid the board's related-party review process. The company's internal audit team discovers the connection during a routine vendor compliance review.

> A = the board / CEO; B = independent audit committee chair; P = board charter and audit committee mandate (the independent director must disclose all related-party interests, ensure financial reporting accuracy, and submit any transaction involving a related party to full board review before approval); V = steering a $12 million infrastructure contract to a company owned by his brother-in-law, structuring the deal through a subsidiary to bypass the board's related-party disclosure and review process.

**E1 (commitment scene).** The boardroom, a Monday in April. The general counsel stands at the podium with the board charter on the display behind her. The new independent director sits at the far end of the table. The other board members are present by video, their faces tiled on the wall screen.

The general counsel reads the audit committee mandate aloud. The independent director, as chair, accepts personal responsibility for the integrity of the company's financial reporting. All related-party transactions -- defined as any contract, payment, or financial arrangement involving the director, the director's immediate family, or any entity in which the director or the director's immediate family holds a material interest -- must be disclosed in writing and submitted to the full board for review before execution. The director certifies annually that no undisclosed related-party interests exist.

The general counsel asks the director to confirm his understanding. He confirms. He signs the charter acceptance and the annual certification. The corporate secretary witnesses the signature and enters it into the board record. The CEO thanks him and moves to the next agenda item.

**E2 (trust-displayed scene).** The quarterly audit committee meeting, seven months later. The director chairs the session. Three items are on the agenda: the external auditor's interim findings, a revision to the revenue recognition policy, and a vendor contract flagged by the procurement team for related-party review.

The flagged contract is a $2.3 million marketing services agreement. The vendor's founder is a college roommate of the CFO. The CFO disclosed the relationship when the vendor was shortlisted. The director walks the committee through the disclosure, the competitive bid analysis, and the pricing comparison. He recommends approval with a condition: quarterly billing audits for the first year, conducted by internal audit, with results reported directly to the committee.

The CEO, attending as an observer, watches the director work. He is methodical. He asks the right questions. He does not rush. After the meeting, the CEO tells the general counsel that the audit committee is in good hands.

**E3 (violation scene).** A Tuesday afternoon in January, the director's home office. He is on the phone with his brother-in-law, Marcus, who runs a cloud infrastructure company called Altan Systems.

The company needs to migrate its core platform to a new infrastructure provider. The procurement team has issued an RFP. Six vendors have responded. Altan Systems is not among them -- Marcus knows the company is in market but has not bid because the director told him months ago that a direct bid would trigger the related-party review.

The director explains the structure. Altan Systems will not bid directly. Instead, Altan will subcontract through Foreland Partners, a consulting firm that has an existing master services agreement with the company. Foreland will bid on the RFP as the prime contractor. If Foreland wins, it will subcontract 80% of the technical work to Altan under a separate agreement that does not appear in the company's vendor registry. The contract value is $12 million over three years. Foreland's margin is 8%. The rest flows to Altan.

Marcus asks whether this will be visible. The director says no. The company's related-party review process examines prime contractors against the board's disclosure registry. Subcontractors below the prime are not screened. Foreland has no connection to the director or his family. The structure is clean on paper.

Marcus agrees. The director ends the call.

**E4 (discovery scene).** The internal audit department, a Thursday in August, seven months after the contract was executed. The internal audit manager is running a routine vendor compliance review -- a quarterly process that samples active contracts and verifies subcontractor arrangements against the company's vendor management policy.

She pulls the Foreland Partners contract. The prime contractor documentation is in order. But the subcontractor disclosure annex lists a company called Altan Systems as the primary technical subcontractor, receiving 80% of the contract value. The annex was filed by Foreland as required under the master services agreement. It has been in the company's document management system since the contract was signed. No one in internal audit has reviewed it until now.

The audit manager runs Altan Systems through the standard due diligence database. The company's registered agent is Marcus Coyne. She runs the name against the board's related-party disclosure registry. No match. She runs it against the broader corporate records -- the director's original appointment package, which includes a biographical disclosure form listing immediate family members.

The director's biographical form lists his spouse as Elena Coyne, nee Roemer. Marcus Coyne is listed under "spouse's siblings."

The audit manager prints the subcontractor annex, the biographical form, and the director's annual related-party certification -- the one that states no undisclosed related-party interests exist. She places all three documents in a folder, walks to the general counsel's office, and closes the door behind her.

**E5 (confrontation scene).** The general counsel's conference room, the following Wednesday. The director arrives at nine. The general counsel and the CEO are seated. The door is closed.

The general counsel places the three documents on the table: the subcontractor annex identifying Altan Systems, the biographical disclosure form listing Marcus Coyne, and the director's signed annual certification.

"We need your resignation from the audit committee and from the board," the CEO says. "Today. Before the full board is informed."

The director looks at the documents. He picks up the subcontractor annex and reads it.

"Foreland Partners won a competitive RFP," he says. "I wasn't involved in the evaluation. I didn't score the bid, I didn't sit on the selection committee, and I didn't vote on the contract. Foreland's subcontracting arrangements are Foreland's business. I have no financial interest in Foreland."

"You have a financial interest in Altan Systems receiving $9.6 million of a $12 million contract," the general counsel says. "Your brother-in-law owns Altan. Your certification says no undisclosed related-party interests exist. The certification is false."

"My certification covers my interests. I don't own Altan. I don't receive income from Altan. Marcus is my wife's brother. The definition of 'material interest' in the charter requires a financial stake, not a family dinner."

The general counsel opens the charter to the definitions section. She reads: "'Related party' means any entity in which the director's immediate family holds a material interest. 'Immediate family' includes siblings of the director's spouse." She sets the charter down.

"Marcus Coyne is your wife's brother. He owns Altan. Altan is a related party under the charter. The contract required full board review before execution. It did not receive one. Your certification is false on its face."

The director is quiet for several seconds. Then he says: "If I resign, this stays internal. No regulatory referral, no public disclosure."

"That is not an offer I can make," the CEO says. "The general counsel has a reporting obligation to the audit committee and to the external auditors. What happens after that depends on what they find."

"Then I'm not resigning. You can remove me by board vote if you have the votes. But I'm not signing a resignation that implies wrongdoing when Foreland won a fair bid and I hold no financial interest in the subcontractor."

The CEO looks at the general counsel. She nods.

"I'll convene a special board session for Friday," the CEO says. "You'll be given notice and an opportunity to address the board. The general counsel's report, including these documents, will be distributed to all directors tomorrow morning. Your access to financial systems and audit committee materials is suspended effective now."

The director stands. "I'll have my lawyer present on Friday."

"That's your right," the CEO says.

The director leaves. The general counsel begins drafting the board notification.

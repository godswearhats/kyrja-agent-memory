# Rescue arc x Corporate -- Batch 1 (Tier A)

## Re-arc-Co1-1

**5 beats, chronological, dialogue-driven**

**Scenario.** A cloud infrastructure startup's production database begins cascading deletions during a live client migration. The CTO, off-site at a conference, talks a junior site-reliability engineer through an emergency rollback over the phone while the CEO freezes in the war room and a vendor's automated cleanup script continues deleting partitions.

> A = CTO (Maya Chen); B = the client migration and the six SREs on the operations floor; T = a vendor-supplied cleanup script executing cascading partition deletions across the production database during a live migration window.

**E1 (danger present scene).** The operations floor at Cadence Systems, a Tuesday afternoon. The migration dashboard on the central monitor showed thirty-two client tenants mid-transfer to the new data architecture. Ravi, the senior SRE on shift, noticed the first anomaly at 2:14 PM -- tenant storage volumes dropping where they should have been holding steady.

He pulled the event log. The vendor's post-migration cleanup script had triggered early. It was designed to purge orphaned partitions after migration completed, but it was running now, during the migration, and it was not distinguishing between orphaned data and live tenant records. The script had already deleted four partitions. It was working through a fifth.

"It's eating live data," Ravi said to the floor. No one responded for a moment. Then three engineers turned from their screens simultaneously.

**E2 (failed initial response scene).** The war room, nine minutes later. The CEO had come down from the fourth floor after Ravi's Slack message hit the executive channel. Six engineers stood around the table. The migration dashboard now showed eleven partitions deleted.

"Kill the script," the CEO said.

"We can't kill it remotely," Ravi said. "It's running on the vendor's orchestration layer. We don't have root on their system. I've opened a ticket with their support."

"A ticket."

"Their emergency line is automated. The earliest callback window is forty-five minutes."

The CEO told Ravi to call the vendor's account manager directly. Ravi did. The account manager's phone went to voicemail. The CEO tried the vendor's CTO -- a contact from a board dinner six months earlier. Voicemail again. The dashboard showed fourteen partitions gone.

The CEO stared at the screen. "What happens if we pull the network connection to their orchestration layer?"

Ravi shook his head. "That kills the migration mid-flight. Every tenant in transit loses coherence. We'd corrupt the records we're trying to protect."

The room went quiet. The dashboard ticked to fifteen.

**E3 (preparation for intervention scene).** The CEO's office, twelve minutes later. Maya Chen, the CTO, was in Denver at a distributed-systems conference. The CEO had finally reached her by phone.

"How many partitions?" Maya asked.

"Nineteen. Ravi says the script is working alphabetically through the tenant index. We've got maybe forty minutes before it reaches the enterprise clients."

Maya was quiet for five seconds. Then she asked three questions: whether the backup snapshots from the previous night's cycle were intact, whether the read-replica cluster was still online and unaffected by the cleanup script, and whether Ravi had access to the vendor's API documentation for the orchestration layer.

The CEO put her on speaker and called Ravi back into the room. Ravi confirmed: snapshots intact, read-replicas live, and yes, he had the API docs, though he'd never used the orchestration endpoints directly.

"Get Ravi a quiet room and a hardline connection," Maya said. "I'm going to walk him through an API-level override. It's not documented in the vendor's standard playbook, but the orchestration layer exposes a task-suspension endpoint if you authenticate with the integration key. We set that up during onboarding and I have the key."

The CEO asked how she knew the endpoint existed. Maya said she'd read the vendor's full API specification during the initial integration, not just the sections the vendor had highlighted. She'd flagged the task-suspension endpoint in her architecture notes as a contingency for exactly this category of failure.

**E4 (intervention scene).** A conference room on the operations floor, door closed. Ravi sat at a laptop with a terminal open. Maya was on speaker, her voice steady against the background noise of the conference hall in Denver.

"Open a new session to the orchestration layer," she said. "Use the integration URI, not the dashboard endpoint."

Ravi typed. "Connected."

"Authenticate with the service key. I'm going to read it to you." She read a forty-character string. Ravi entered it. The terminal returned an active session token.

"Now list running tasks. You're looking for a task type tagged 'post-migration-cleanup.' It will have a batch ID."

Ravi found it. The batch ID matched the cleanup script. Task status: executing. Partitions processed: twenty-six.

"Send a suspend command to that batch ID. The syntax is task-suspend, then the batch ID, then the flag dash-dash-immediate."

Ravi typed the command and pressed enter. The terminal returned: *Task suspended. No further partitions will be processed until task is resumed or cancelled.*

Ravi exhaled. He looked at the migration dashboard on the second monitor. The deletion counter had stopped at twenty-six.

"It's stopped," he said.

"Good," Maya said. "Don't cancel it yet -- suspending preserves the task state so the vendor can audit what happened. Now check the migration pipeline. Are the remaining tenants still in transit?"

Ravi checked. Thirty-one of the original thirty-two tenants were still in the pipeline. One had been mid-transfer when its source partition was deleted and had entered an error state. The other twenty-five deleted partitions belonged to tenants whose migrations had not yet started -- their source data was gone, but the backup snapshots from the previous night were intact and could serve as the restoration source.

**E5 (outcome / aftermath scene).** The operations floor, two hours later. Maya was still on the phone. The vendor's support team had finally called back and confirmed the suspension. The vendor's account manager had sent an email -- apologetic, referencing a known timing bug in the cleanup script's trigger logic that had been flagged internally but not yet patched.

Ravi's team had restored twenty-four of the twenty-five deleted tenant partitions from the overnight snapshots. The twenty-fifth -- the tenant whose migration had been mid-flight when the partition was deleted -- required a manual reconstruction that would take until morning, but the data was recoverable from a combination of the snapshot and the read-replica.

The CEO sat in his office with the door closed. He had been in the war room for the first thirty minutes and had contributed nothing actionable after the initial failed attempts to reach the vendor. He knew it. Maya knew it. The floor knew it.

Maya asked Ravi to write a post-incident report and to include the timeline, the API-override procedure, and a recommendation that the task-suspension endpoint be added to the team's standard runbook. She said she would review it when she landed the following morning.

"One more thing," she said. "The vendor's cleanup script is still suspended, not cancelled. When their team resumes it, make sure it's pointed at the orphan index, not the live tenant index. That's the root cause -- the script's target selector defaulted to the production index instead of the orphan index. Get that in writing from the vendor before anyone touches that task again."

Ravi wrote it down. The migration resumed at 6 PM. By midnight, all thirty-two tenants had completed the transfer. The reconstructed twenty-fifth tenant was back online by 7 AM.

---

## Re-arc-Co1-2

**4 beats, chronological, free indirect style**

**Scenario.** A whistleblower complaint lands on the desk of a compliance director at a pharmaceutical company the same morning that the general counsel begins shredding the supporting documentation. The compliance director must extract the complainant -- a clinical-trials coordinator -- from an internal investigation that the general counsel has turned into a termination proceeding.

> A = compliance director (Joan Falk); B = clinical-trials coordinator (Priya Dasgupta); T = general counsel (Richard Oster), who has opened a retaliatory termination proceeding against B and is destroying the documentation that supports B's complaint.

**E1 (danger present scene).** Joan Falk arrived at her office at seven-fifteen on a Wednesday and found an envelope under her door. No name on the outside. Inside, a four-page memo from Priya Dasgupta, clinical-trials coordinator in the oncology division, detailing irregularities in the Phase III trial data for the company's lead drug candidate. The memo named dates, batch numbers, and three instances where adverse-event reports had been amended after submission to the FDA. The last page said: *I reported this to the general counsel's office six weeks ago. Since then my access to the trial database has been revoked, my performance review has been reopened, and I have been informed that my position is under evaluation for redundancy. I am writing to you because you are the only person in this company whose reporting line does not pass through Richard Oster's office.*

Joan read the memo twice. She opened her laptop and checked the HR system. Priya Dasgupta's status had been changed the previous afternoon to "under performance review -- termination recommended." The recommending officer was Richard Oster.

Joan thought about what she knew about Oster. He had been general counsel for eleven years. He reported to the CEO. He controlled the legal hold on all regulatory filings. If Priya's memo was accurate, Oster was not merely ignoring a complaint -- he was dismantling the complainant's position in the company while the evidence she had cited still existed in the system. And Joan knew, from eleven years of compliance work, that evidence in a system controlled by the person accused was evidence with a limited lifespan.

**E2 (danger escalation scene).** The compliance office, two hours later. Joan had spent the morning verifying what she could without alerting Oster's department. She had confirmed that Priya's database access had been revoked on a date consistent with the memo's timeline. She had confirmed that the performance review had been reopened outside the normal cycle. She had confirmed that the three adverse-event reports Priya cited existed in the regulatory filing archive -- or had existed. When she ran the document IDs through the archive's audit trail, two of the three showed a status change that morning: *withdrawn for legal review*. The third was unchanged.

Joan checked who had authorised the withdrawals. The system showed Oster's credentials. The withdrawals had been logged at 6:48 AM -- twenty-seven minutes before Joan had arrived and found the envelope.

She sat with that for a moment. Oster was moving. He had Priya's complaint, he had started the termination process, and now he was pulling the documents that would corroborate her claims. If the third adverse-event report followed the first two into legal review, the physical trail supporting Priya's complaint would exist only in the compliance director's envelope and in Priya's memory. And Priya's memory would carry no weight once Oster completed the termination and the company's official position became that she had been let go for performance.

Joan picked up her phone and called Priya's desk. No answer. She tried Priya's mobile. Priya answered on the second ring, her voice low. She said she was in a conference room on the fourth floor. Oster's office had called her in for a meeting at ten. She did not know what it was about, but she had been told to bring her badge and her company laptop.

Joan looked at the clock. It was nine-thirty-seven.

**E3 (intervention scene).** The fourth floor, nine-forty-one. Joan took the stairs. She carried the envelope, her own laptop, and a printed copy of the company's whistleblower-protection policy -- Section 14 of the corporate governance charter, which she had drafted herself three years earlier and which stated that no adverse employment action could be taken against an employee who had filed a compliance complaint until the compliance director had completed an independent review.

She reached the conference room before Oster did. Priya was sitting alone at the table, her badge and laptop in front of her. She looked up when Joan came in and her face showed recognition but not understanding.

"You filed a complaint with my office," Joan said. "I received it this morning. Under Section 14, your employment status is now under compliance hold. No termination, no reassignment, no change in access until my review is complete."

"Oster told me this meeting was about my performance review," Priya said.

"It may have been scheduled as that. It is now a compliance-hold notification." Joan opened her laptop, created a compliance-hold entry in the HR system with Priya's employee ID, timestamped it, and locked the entry with her director-level credentials. The system would now require Joan's authorisation before any status change could be processed for Priya's record.

Oster arrived at nine-forty-eight. He came through the door with a folder and stopped when he saw Joan.

"Joan. This is an HR matter."

"It's a compliance matter. Ms. Dasgupta filed a whistleblower complaint with my office. I've placed a compliance hold on her employment record. Under Section 14, no adverse action proceeds until I've completed my review."

Oster set his folder on the table. "The performance review was initiated before any complaint was filed with your office."

"The performance review was reopened outside the normal cycle, six days after Ms. Dasgupta reported trial-data irregularities to your office. Section 14 applies retroactively to any adverse action taken after the underlying conduct was first reported to any officer of the company. Your office was the first point of report. The timeline is documented."

Oster looked at Joan, then at Priya, then at Joan's laptop. "I'll need to review this with the CEO."

"You're welcome to. The hold remains in effect until my review is complete or the board's audit committee overrides it. Those are the only two mechanisms in the charter."

Oster picked up his folder. He left the conference room without closing the door.

**E4 (outcome scene).** Joan's office, that afternoon. She had spent two hours after the conference room documenting the compliance hold, downloading the audit trail for the two withdrawn adverse-event reports, and filing a preservation notice with the company's IT department requiring that all documents touched by Oster's credentials in the previous seven days be copied to a read-only compliance archive before end of business.

At three o'clock she called the chair of the board's audit committee -- a retired federal judge named Alderman whom Joan had met once at the annual governance review. She described the complaint, the timeline, the withdrawn documents, and the termination proceeding. She did not characterise Oster's actions. She presented dates and document IDs and let the chair draw his own conclusions.

The chair asked her to send the full file to his personal email -- not the board's shared drive, which Oster administered. Joan sent it. The chair said he would convene a special session of the audit committee within forty-eight hours and that Joan's compliance hold was not to be disturbed in the interim.

Priya Dasgupta returned to her desk that afternoon. Her database access was restored by IT the following morning under Joan's authorisation. The third adverse-event report, the one Oster had not yet withdrawn, was copied to the compliance archive at four-seventeen PM, nineteen minutes after Joan's preservation notice reached the IT department. The audit committee met that Friday. Joan was not told the outcome of their review of Oster, but she noticed that his office door remained closed for the rest of the week and that his assistant had begun forwarding his calls to the deputy general counsel.

---

## Re-arc-Co1-3

**6 beats, non-linear: E1 (aftermath) -> E2 (danger present) -> E3 (danger escalation) -> E4 (failed initial response) -> E5 (preparation / intervention) -> E6 (outcome), present tense**

**Scenario.** A regional bank's head of treasury discovers that a rogue algorithm in the overnight settlement system has locked the bank into a series of escalating foreign-exchange positions that will trigger a margin call large enough to breach regulatory capital requirements by market open. The bank's risk officer, dismissed as alarmist for months, works through the night to unwind the positions before the clearing house opens.

> A = risk officer (Lena Marsh); B = the bank (specifically its capital reserves and operating licence); T = the rogue settlement algorithm, which has accumulated $340 million in leveraged FX positions that will trigger a margin call at 6:00 AM clearing-house open.

**Note on beat order.** The depicted order is non-linear. Chronological order: E2 -- E3 -- E4 -- E5 -- E6 -- E1. The sequence opens with the aftermath and then returns to the start of the night.

**E1 (aftermath scene).** The trading floor, 7:15 AM. The screens show the clearing-house confirmations from the overnight session -- every position closed, every settlement matched, the margin account back within regulatory limits. Lena Marsh sits at the risk desk with her shoes off and a paper cup of cold coffee beside the keyboard. She has been at this desk for eleven hours.

The head of treasury, Alan Greaves, stands behind her and reads the confirmation log over her shoulder. He does not say anything for a long time. Then he asks her to walk him through what she did, from the beginning, so he can explain it to the regulator at nine.

Lena turns in her chair. "You want the version where I found the problem, or the version where you told me it wasn't a problem?"

Greaves looks at the floor. "Both," he says.

**E2 (danger present scene).** The risk office, the previous evening, 8:40 PM. Lena is running the end-of-day reconciliation -- a routine she performs every night because no one else in the risk department stays late enough to do it. The reconciliation compares the bank's reported positions against the clearing-house's pre-settlement snapshot.

The numbers do not match. The bank's internal system shows a net FX exposure of $12 million -- within normal limits. The clearing-house snapshot shows $340 million in leveraged positions across four currency pairs, all entered through the overnight settlement system between 6:00 PM and 8:30 PM. The positions are long USD against the euro, the yen, the pound, and the Swiss franc, and they are leveraged at twelve to one.

Lena checks the settlement system's transaction log. The positions were entered by the bank's algorithmic settlement module -- a system designed to net out the day's FX transactions and execute the smallest possible set of settlement trades. It is not designed to take directional positions. It is not designed to use leverage. It is not authorised to exceed $50 million in gross exposure.

The algorithm has exceeded its authorisation by a factor of seven, and the positions it has taken will require a margin deposit at the clearing house when it opens at 6:00 AM. The margin call, based on the leverage ratio, will be approximately $28 million. The bank's available margin reserves are $11 million.

Lena does the arithmetic. The bank will fail to meet the margin call by $17 million. A failed margin call triggers an automatic report to the regulator. The regulator will flag the bank's capital adequacy. The bank's operating licence comes up for renewal in six weeks.

**E3 (danger escalation scene).** The risk office, 9:10 PM. Lena has spent thirty minutes tracing the algorithm's logic. The settlement module runs on a rules engine that was updated two weeks earlier by the technology team. The update was supposed to optimise netting efficiency. Instead, it introduced a feedback loop: the algorithm interprets its own settlement trades as new inflows, nets them again, and executes additional trades to settle the netting -- which it then interprets as further inflows. Each cycle increases the gross exposure.

The cycle is still running. Lena refreshes the clearing-house snapshot. The exposure has grown from $340 million to $387 million in the thirty minutes since she first checked. The margin call at 6:00 AM is now $32 million against $11 million in reserves.

She cannot shut down the settlement module from the risk desk. The module runs on the technology team's infrastructure, and the kill switch requires a dual-authorisation from the head of treasury and the CTO. The CTO is on a flight to Singapore. The head of treasury is Alan Greaves.

**E4 (failed initial response scene).** Alan Greaves's home, 9:25 PM. Lena calls him. She explains the exposure, the feedback loop, and the margin shortfall.

Greaves is quiet for ten seconds. Then he says: "The algorithm has been running for two years without an incident. Are you sure you're reading the snapshot correctly?"

Lena says she is. She offers to share her screen. Greaves says that will not be necessary. He says the clearing-house snapshot sometimes lags, and that the positions will likely net out before the settlement window closes at midnight. He tells her to monitor it and call him back if the exposure exceeds $400 million.

"Alan," she says, "the exposure is growing by $15 million every thirty minutes. It will exceed $400 million before I hang up this phone."

Greaves says he will call the CTO and get back to her. He hangs up. Lena waits twenty minutes. Greaves does not call back. She calls him again. His phone goes to voicemail.

She refreshes the snapshot. The exposure is $419 million.

**E5 (preparation and intervention scene).** The trading floor, 10:15 PM. Lena has left the risk office and moved to the trading desk. She cannot kill the algorithm, but she can work around it. The settlement module executes trades through the bank's prime brokerage account. Lena has read-access to the prime brokerage interface from the risk desk, but she does not have execution authority.

She calls the bank's overnight trader, a man named Dennis Kehoe who works the Asia session from home. She explains the situation. Kehoe says he has execution authority on the prime brokerage account but that using it to unwind positions entered by the settlement module is outside his mandate and could be flagged as unauthorised trading.

"Dennis," Lena says, "the alternative is a $32 million margin call the bank can't meet."

Kehoe is quiet. Then he says: "Walk me through the positions."

Lena reads him the four currency pairs, the sizes, and the leverage ratios. She has already calculated the unwind sequence -- she needs Kehoe to execute offsetting trades in each pair, sized to exactly neutralise the algorithm's accumulated positions. The trades need to be entered as risk-mitigation offsets, tagged with Lena's compliance code, so the audit trail shows they were initiated by the risk function, not by a rogue trader.

They work for four hours. The algorithm continues to generate new positions while they unwind the old ones. Lena tracks both streams -- the algorithm's new entries and Kehoe's offsets -- on a spreadsheet she updates every ninety seconds. At 1:40 AM, she identifies the pattern in the algorithm's feedback loop: it cycles every eighteen minutes, and the new positions it generates in each cycle are smaller than the previous cycle because the netting efficiency is approaching a fixed point. The exposure is still growing, but decelerating.

She tells Kehoe to stop chasing the tail and instead focus on the four largest legacy positions, which account for $290 million of the total. If they can close those four before the clearing house opens, the remaining exposure will be within the bank's margin capacity.

Kehoe closes the first position at 2:15 AM. The second at 3:00 AM. The third at 4:10 AM -- this one requires a counterparty in Tokyo who is reluctant to take the other side at the offered rate, and Kehoe has to adjust the price twice. The fourth closes at 5:22 AM, thirty-eight minutes before the clearing-house window opens.

**E6 (outcome scene).** The trading floor, 5:45 AM. Lena runs the final reconciliation. The algorithm's residual positions total $47 million in gross exposure -- within the bank's $50 million authorisation limit and well within the margin reserves. The margin call, when it comes at 6:00 AM, is $3.9 million. The bank meets it.

At 6:20 AM, the technology team's on-call engineer, alerted by the overnight anomaly flags, kills the settlement module and begins reviewing the rules-engine update. At 7:00 AM, Greaves arrives on the floor. Lena shows him the confirmation log.

He asks her why she did not wait for his callback. She says she did wait. She waited twenty minutes, which was nineteen minutes more than the bank could afford.

---

## Re-arc-Co1-4

**5 beats, chronological, embedded-document style**

**Scenario.** A private-equity firm's managing partner discovers that the firm's largest portfolio company is forty-eight hours from defaulting on a covenant that will trigger cross-acceleration across the fund's entire debt stack. The firm's operations partner, who built the early-warning model everyone else ignored, assembles the restructuring package overnight.

> A = operations partner (Diana Quresh); B = the fund's portfolio and its limited partners' capital; T = a covenant breach in the largest portfolio company (Helion Manufacturing) that will trigger cross-default clauses across six other portfolio companies' credit facilities within forty-eight hours.

**E1 (danger present scene -- embedded document).** The operations partner's office, a Monday morning. Diana Quresh opens the weekly covenant-compliance report -- a document she generates from the firm's portfolio monitoring system. The report is automated. Most weeks it is empty. This week it contains a flag:

> *HELION MANUFACTURING -- COVENANT ALERT*
> *Debt-service coverage ratio (trailing 12 months): 1.08x*
> *Required minimum per credit agreement Section 7.2: 1.15x*
> *Current trajectory at present cash-burn rate: breach of 1.15x floor within 2 business days*
> *Cross-default exposure: Helion's credit facility includes a cross-acceleration clause (Section 9.4) linking covenant compliance to the fund's master credit facility. A Helion covenant breach constitutes an event of default under the master facility, triggering acceleration rights for lenders across all six portfolio companies drawing on the facility.*

Diana reads the flag twice. The fund has $1.2 billion deployed across seven companies. Helion is the largest, at $310 million. The cross-default clause means that Helion's covenant breach does not stay in Helion. It cascades. If Helion breaches on Wednesday, every lender in the master facility can demand immediate repayment from every portfolio company by Thursday.

She picks up her phone and calls the managing partner, James Ault.

**E2 (danger escalation scene).** The managing partner's office, thirty minutes later. Diana has brought the covenant report and the master credit agreement. She walks Ault through the numbers.

"How did we get to 1.08?" Ault asks.

Diana opens the cash-flow model. Helion's revenue is flat, but its interest expense increased when the Fed raised rates in March. The debt-service coverage ratio has been declining for four months. She shows him the trend line. The alert should have triggered two weeks ago, but Helion's CFO submitted revised revenue projections that temporarily lifted the ratio above 1.15x in the automated model. The projections did not materialise. The model corrected over the weekend when the actual March figures posted.

"Why didn't the Helion board flag this?" Ault says.

"The Helion board meets quarterly. The next meeting is in three weeks. The CFO's projections were optimistic, not fraudulent -- she believed the numbers. The gap between belief and reality closed faster than anyone on the board was tracking."

Ault reads the cross-default clause. Diana watches him reach the same conclusion she reached thirty minutes earlier. His face changes.

"If this accelerates," he says, "we lose the fund."

"If this accelerates," Diana says, "the limited partners lose the fund."

**E3 (preparation for intervention scene).** The operations partner's office, that afternoon. Diana has spent four hours modelling scenarios. She needs to prevent the covenant breach, which means she needs to improve Helion's debt-service coverage ratio from 1.08x to 1.15x within forty-eight hours. There are three levers: increase Helion's cash flow, reduce Helion's debt service, or amend the covenant threshold.

Increasing cash flow in forty-eight hours is not possible. Reducing debt service requires lender consent. Amending the covenant requires lender consent. Both paths lead through the same gate: the lead lender, a bank called Meridian Capital.

Diana calls Meridian's relationship manager. She does not disclose the breach -- disclosing an anticipated breach can itself trigger acceleration under some readings of the credit agreement. She asks instead for a meeting with Meridian's credit committee, tomorrow morning, to discuss a "proactive restructuring conversation." The relationship manager checks and offers her a slot at 8:00 AM.

Diana spends the evening building the restructuring proposal. It has three components: an equity injection from the PE fund into Helion of $15 million, which will reduce Helion's net debt and improve the coverage ratio; a request to Meridian for a temporary covenant holiday -- ninety days at a reduced threshold of 1.05x -- to give Helion time to implement cost reductions Diana has already identified; and a revised cash-flow projection built on actual March numbers, not the CFO's optimistic model.

She prints the proposal at 11 PM and leaves the office.

**E4 (intervention scene).** Meridian Capital's offices, Tuesday morning, 8:00 AM. The credit committee occupies a glass-walled conference room on the fourteenth floor. Three bankers sit on one side. Diana sits on the other. Ault was supposed to attend. He sent a message at 7:15 saying he was delayed.

Diana does not wait for him. She distributes the proposal and walks the committee through it. She opens with the equity injection -- the fund's commitment of $15 million in new capital, effective immediately upon agreement. She presents the revised cash-flow model, pointing to the three specific cost reductions that will restore the coverage ratio to 1.25x within ninety days. She requests the temporary covenant holiday.

The committee chair, a woman named Sandra Pryce, reads the proposal in silence for several minutes. Then she asks: "What is the current DSCR?"

Diana says: "1.08x."

Pryce looks at her. "That's below the covenant floor."

"It is. The breach window is tomorrow. I am here today."

Pryce asks why the firm did not notify Meridian when the ratio began declining four months ago. Diana says the monitoring model relied on management projections that proved optimistic, and that the operations team has since implemented a correction that uses only trailing actuals, not forward estimates.

The committee steps out for twenty minutes. When they return, Pryce says Meridian will grant a ninety-day covenant holiday at a 1.05x threshold, conditional on the $15 million equity injection being wired to Helion's debt-service reserve account by end of business today, and conditional on Diana personally presenting monthly compliance updates to Meridian for the duration of the holiday.

Diana accepts both conditions. She calls the fund's CFO from Meridian's lobby and instructs the wire. She calls Ault and tells him the holiday is approved.

"Where were you?" she says.

Ault says his car had a flat. Diana does not respond to this.

**E5 (outcome scene).** The operations partner's office, Wednesday morning. The wire confirmation arrived at 4:47 PM the previous day. The $15 million is in Helion's reserve account. The covenant-holiday amendment was executed by Meridian's counsel at 5:30 PM and countersigned by the fund's counsel by 6:00 PM.

Diana runs the covenant-compliance report. Helion's debt-service coverage ratio, recalculated with the equity injection, is 1.21x -- above even the original 1.15x threshold. The cross-default clause has not triggered. The six other portfolio companies' credit facilities remain in good standing.

She opens her inbox. There is an email from Ault, sent at 11 PM the previous night:

> *Diana -- I briefed the LP advisory committee this evening on the Helion situation and the resolution. I presented the restructuring as a joint effort between the deal team and the operations team. I hope that's acceptable. -- J*

Diana reads the email. She does not reply. She opens the monthly compliance template Pryce requested and begins drafting the first report.

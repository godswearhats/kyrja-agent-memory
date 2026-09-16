# Confrontation arc × Corporate — Batch 2 (Tier B)

## C-arc-Co2-1

**5 beats, chronological, dialogue-driven**

**Scenario.** A regional sales director demands that the VP of Product reverse a feature deprecation that will eliminate the integration her largest client depends on. The VP refuses, citing the product roadmap and engineering costs. The dispute escalates through a failed compromise meeting before the CEO is forced to arbitrate.

> A = regional sales director; B = VP of Product; O = the deprecated API integration (client-facing feature scheduled for removal in Q3).

**E1 (positioning scene).** The sales director's office, a Tuesday morning. She had the client's contract open on one monitor and the product deprecation notice on the other. The notice had arrived in her inbox fourteen minutes ago -- a bulk announcement to all customer-facing teams, no prior consultation.

She read it twice. The integration being deprecated was the sole reason her largest account had renewed eighteen months ago. The renewal had been the biggest in the region that year. She had negotiated it personally, and the integration commitment was written into the contract's service appendix -- not as a formal SLA, but as a referenced capability the client had cited in their renewal justification.

She forwarded the deprecation notice to her assistant and asked him to book thirty minutes with the VP of Product before end of day. Then she pulled the client's renewal file and began marking every reference to the integration.

**E2 (demand scene).** The VP of Product's office, four-thirty that afternoon. He was standing at his whiteboard when she came in. She closed the door.

"I need you to reverse the deprecation on the Conduit integration," she said. "Or at minimum, exempt it from the Q3 timeline."

He turned from the whiteboard. "That's not on the table. We announced the deprecation because we're consolidating three integration layers into one. Conduit is the oldest. Keeping it alive means maintaining a separate authentication stack that my team has been trying to retire for two years."

"Your announcement went out without consulting sales. I have a client generating four point two million in annual recurring revenue whose renewal was built on that integration. It's referenced in their contract appendix."

"Referenced, not guaranteed. I read the appendix before we sent the notice. It says 'currently supported capability,' not 'permanent commitment.' Legal reviewed the language."

"Legal reviewed the language. My client didn't. They renewed because I told them the integration would be there. If it disappears six months after renewal, I lose the account and I lose the credibility I spent three years building in that sector."

He sat down. "I understand the revenue risk. But I can't maintain dead infrastructure for one account. Bring me a migration plan that moves them to the new integration layer by Q3 and I'll assign engineering resources to support the transition."

"Migration takes eight months minimum for an enterprise client. You're giving me three."

"Then bring me a proposal," he said. "I'll look at the timeline. But the deprecation stands."

She left without agreeing.

**E3 (escalation scene).** A conference room on the fourteenth floor, the following Thursday. The sales director had requested a cross-functional meeting: herself, the VP of Product, the head of customer success, and the CFO's chief of staff.

She presented the revenue exposure: four point two million at immediate risk, plus seven point eight million across four adjacent accounts in the same sector that used the same integration. Total exposure, twelve million. She laid the client's renewal timeline on the table -- they were eleven months from the next renewal decision, and the procurement lead had already emailed asking about the deprecation notice.

The VP of Product presented the engineering cost of maintaining Conduit: two full-time engineers indefinitely, plus the security surface of the legacy authentication stack. He estimated the annualised cost at four hundred and sixty thousand dollars, but noted that the cost was not the issue -- the issue was architectural. The new integration layer could not fully deploy while Conduit remained active. Every month of delay pushed the new platform's launch further out.

The head of customer success proposed a compromise: maintain Conduit for six months past the deprecation date, long enough to migrate the largest accounts, then shut it down. The VP said six months was insufficient for a clean migration and would leave his team maintaining both systems simultaneously. The sales director said six months was insufficient for the client and would signal instability at exactly the wrong moment in the renewal cycle.

The CFO's chief of staff asked both sides to submit written proposals to the CEO by Monday. Neither party agreed to the other's terms. The meeting ended without resolution.

**E4 (authority involvement scene).** The CEO's office, the following Wednesday. He had read both proposals over the weekend. The sales director sat on his left; the VP of Product sat on his right. The CFO's chief of staff stood by the window with a summary sheet.

The CEO addressed the sales director first. "You're asking me to override a product decision to protect a single client relationship."

"I'm asking you to protect twelve million in revenue that your product team put at risk without consulting the people who sold it."

He turned to the VP. "And you're asking me to let you deprecate a capability that's contractually referenced in our largest regional account."

"I'm asking you to let me ship the platform we've been building for two years. Every month Conduit stays alive is a month the new system can't fully deploy."

The CEO was quiet for a moment. He asked the CFO's chief of staff for the margin breakdown on the twelve million. She gave it to him: blended margin of sixty-two percent, net contribution of seven point four million.

**E5 (resolution scene).** The same room, ten minutes later. The CEO had made his decision.

"Here's what's going to happen," he said. "The deprecation stands. The timeline moves from Q3 to Q1 of next year -- nine months instead of three. Product assigns a dedicated migration engineer to the top five accounts. Sales gets a ninety-day window after the new timeline to close any renewals that need the transition commitment in writing."

The sales director shook her head. "Nine months is better than three, but if the client walks because the integration changes mid-contract, this decision owns that loss."

"Noted," the CEO said. "And logged. If the account churns within twelve months of the migration, the revenue loss is attributed to the product transition, not to sales. That goes in the board reporting."

The VP of Product nodded. The sales director did not nod, but she wrote the timeline in her notebook and asked for the migration engineer's name by Friday. The CEO said she would have it by Thursday.

The meeting ended. The sales director and the VP of Product left through different doors.

---

## C-arc-Co2-2

**4 beats, chronological, free indirect style**

**Scenario.** A founding CTO demands that the board reinstate her veto authority over technical hiring after the new CEO centralised all hiring under a single HR function. The board chair resists, siding with the CEO's reorganisation. The dispute reaches a breaking point when the CTO offers her resignation as leverage and the board accepts it.

> A = founding CTO; B = board chair (representing the board); O = veto authority over technical hiring decisions.

**E1 (demand scene).** The boardroom was empty except for the two of them. She had asked for the meeting privately, outside the regular board calendar, and the chair had agreed -- a courtesy extended to founders that would not have been extended to anyone else.

She set the org chart on the table between them. The old one, with the dotted line from engineering hiring to her office, and the new one, with every hiring function consolidated under the chief people officer who reported to the CEO. Her name appeared nowhere in the new chart's hiring flow.

She told the chair she wanted her veto authority restored. Not the full hiring function -- she understood the rationale for consolidation -- but the final-approval right on any technical hire at the senior staff level and above. She had built the engineering organisation from four people to three hundred and twelve. Every senior technical hire in the company's history had passed through her assessment. The new structure removed that gate entirely, and the CEO had implemented the change without discussing it with her.

The chair listened. He had known her for nine years, since the seed round. He understood what she was asking and he understood why. But he also understood that restoring her veto would undermine the authority the board had granted the CEO six months ago when they had hired him to professionalise the company's operations. The chair said he could not reinstate the veto. The board had approved the reorganisation unanimously. Reversing a piece of it for one executive, even a founder, would signal that the CEO's authority was conditional.

She said the CEO's authority over hiring was not the issue. The issue was that no one else in the company could evaluate whether a senior technical candidate would survive the architecture they had built. The chief people officer was a recruiter. He was good at process. He did not know what a distributed consensus algorithm was, and he would be making final decisions about the people who built them.

The chair said he understood her concern but the answer was no.

**E2 (failed negotiation scene).** A restaurant two blocks from the office, the following evening. The chair had suggested dinner -- neutral ground, no conference table, no recording. He brought the CEO.

The CTO had not expected the CEO to be there. She saw him at the table when she arrived and understood what the chair was doing: forcing the conversation into the room where it belonged instead of letting it run through back channels.

The CEO proposed a compromise. He would create a technical advisory panel -- three senior engineers, appointed by the CTO -- that would review every senior technical hire and provide a written recommendation. The recommendation would be non-binding but would be included in the hiring file and visible to the board.

The CTO asked what happened when the panel recommended against a hire and the chief people officer approved it anyway.

The CEO said the panel's recommendation would be on the record. If a hire failed and the panel had flagged concerns, that would be visible.

She said visibility was not authority. A non-binding recommendation was a suggestion. She had not built the engineering organisation on suggestions. She had built it on judgment, applied at the gate, before the wrong person got through.

The CEO said he could not give one executive veto power over another executive's function. It would make the chief people officer's role untenable.

The CTO said the chief people officer's role was already untenable. He had been in the job for four months and had already advanced two senior candidates to final round whom any competent technical interviewer would have screened out in the first thirty minutes.

The dinner ended without agreement. The chair paid the bill.

**E3 (escalation scene).** The CTO's office, three weeks later. She had spent the interval documenting. She now had a file: fourteen senior technical hires made under the old system, with their performance ratings, retention rates, and project outcomes. And four hires made under the new system in the past five months, two of whom were already on performance improvement plans.

She sent the file to the full board with a single-paragraph cover note. The note did not mention the veto dispute. It simply presented the data and asked the board to review the correlation between hiring process and outcome.

The chair called her within the hour. He told her that sending comparative performance data to the full board, without context, without the CEO's knowledge, was a political act and she knew it. She said the data was accurate and the board had a right to see it. He said the data was accurate and the framing was designed to make the CEO look incompetent. She said the framing was the data.

He told her the board would discuss the matter at the next scheduled meeting, two weeks out, and that she should not send further communications to the full board without his prior review. She said she would comply with that request.

**E4 (resolution scene).** The boardroom, two weeks later. Full board present. The CEO sat at the far end, the CTO near the middle. The chair opened the session by acknowledging the CTO's data file and the underlying dispute.

The CTO made her position explicit one final time. She wanted her veto authority restored on senior technical hires. She said the company's technical hiring quality had measurably declined since the reorganisation and that the data she had circulated demonstrated this. She said that if the board would not restore the veto, she would interpret that as a statement about the role they saw for her going forward, and she would resign from her position effective at the end of the quarter.

The room was quiet. The chair looked at the other board members. Two of them were looking at the table. One was writing something on her pad.

The chair said the board valued the CTO's contribution and her nine years of service. He said the board had discussed the matter in executive session the previous evening. The board's position was that the hiring reorganisation would stand as approved. The board would accept the CEO's proposal for a technical advisory panel with a written recommendation process. The board would not reinstate the veto.

The CTO asked if the board was accepting her resignation.

The chair said the board hoped she would reconsider. But if her position was that the veto was a condition of her continued employment, then the board understood her decision and would work with her on a transition plan.

She looked at the chair for a long moment. Then she said she would have her transition proposal to him by Friday. She gathered her file, thanked the board for their time, and left.

The CEO did not speak during the exchange.

---

## C-arc-Co2-3

**6 beats, non-linear: E1 (aftermath) -> E2 (preparation) -> E3 (demand) -> E4 (resistance) -> E5 (escalation) -> E6 (resolution)**

**Scenario.** A compliance officer demands that the managing director of the firm's most profitable trading desk submit to an immediate audit of his team's client communications after a pattern of irregular trade timestamps surfaces in the quarterly review. The managing director refuses, citing client confidentiality and the desk's revenue contribution, and threatens to move his team to a competitor. The dispute is resolved when the general counsel intervenes with a binding regulatory interpretation.

> A = chief compliance officer; B = managing director of the structured-products desk; O = access to the desk's client communication records for audit.

**Note on beat order.** This sequence opens with the aftermath and then moves to the beginning, proceeding chronologically from there. Chronological order: E2 -- E3 -- E4 -- E5 -- E6 -- E1. Depicted order is E1 -- E2 -- E3 -- E4 -- E5 -- E6.

**E1 (aftermath scene).** A Monday morning in March. The structured-products desk on the thirty-second floor was half empty. The compliance officer walked through it on her way to the elevators, as she did every morning, and counted the occupied seats. Eleven of the twenty-four terminals were active. The managing director's office at the far end was dark, his nameplate still on the door, his desk cleared except for a single monitor showing the firm's screensaver.

She did not pause. She had known the desk would look like this. The general counsel had told her on Friday that the managing director had given notice and that six of his traders had followed. She had spent the weekend updating the regulatory filings to reflect the change in desk leadership. The audit was proceeding under the interim head, a senior trader who had stayed. The client communication records were being produced on the schedule the general counsel had set.

She pressed the elevator button and waited. Thirteen traders remained. The desk would survive. Whether it would generate the same revenue was not her problem. Her problem was the audit, and the audit was now unobstructed.

**E2 (preparation scene).** Six weeks earlier. A Thursday afternoon in the compliance department, ninth floor. The compliance officer sat at her desk reviewing the quarterly trade-timestamp report. The report was generated automatically -- every trade executed on every desk, timestamped against the client instruction log, flagged when the gap between instruction and execution exceeded the firm's internal threshold.

The structured-products desk had forty-three flags. The next-highest desk had nine. She pulled the detail. The flags were not random. They clustered around the same four client accounts, all managed by the same two traders, and they all showed the same pattern: a client instruction logged at one time, the trade executed minutes earlier. Not minutes late -- minutes early. Trades placed before the client instruction appeared in the system.

She did not know what this meant, but she knew what it looked like. She pulled the desk's organisational chart, identified the managing director as the supervisor of both traders, and drafted a formal audit request. The request cited the firm's compliance manual, Section 11: the compliance department had the authority to demand immediate access to any desk's client communications, trade records, and internal correspondence when a pattern of irregularity was identified in the quarterly review.

She routed the request through the general counsel's office for countersignature and sent it to the managing director's inbox at four forty-seven that afternoon.

**E3 (demand scene).** The compliance officer's office, the following Monday morning. She had asked the managing director to come to her, not the other way around. It was a deliberate choice: compliance requesting a meeting on its own floor, in its own space. He arrived twelve minutes late.

"You got my audit request," she said.

"I did."

"I need access to the full client communication archive for your desk -- emails, recorded lines, instant messages -- for the four accounts flagged in the quarterly review. I need the records going back six months. And I need them by Wednesday."

He leaned back in the chair. "What exactly are you looking for?"

"That's not how this works. Section 11 doesn't require me to specify the theory before I get the records. The pattern is in the quarterly report. Forty-three flags, four accounts, two traders. I need the communications."

**E4 (resistance scene).** The same room, continuing. The managing director crossed one leg over the other and spoke without hurry.

"Those four accounts represent a combined notional of one point eight billion. The communications in those files contain proprietary structuring details that my clients shared with us under confidentiality agreements. If I hand those files to compliance and something leaks -- even internally -- I lose the accounts, and the firm loses the revenue."

"The compliance manual is clear. Section 11 --"

"Section 11 gives you the authority to request. It doesn't override the confidentiality provisions in our client agreements, which are legal obligations to external parties. You're asking me to choose between an internal policy and an external contract. I'm choosing the contract."

"That's not your interpretation to make."

"It's exactly my interpretation to make. I run the desk. I signed the client agreements. And I'll tell you something else: if compliance pushes this audit over my objection, I will take it to the CEO personally. My desk produced three hundred and twelve million in revenue last year. That's twenty-three percent of the firm's total. You want to audit me? Fine. But you'll do it with my cooperation or you'll do it without my desk."

She held his gaze. "Is that a threat to leave?"

"It's a statement of fact. My team is portable. Our client relationships are personal. I'm telling you what will happen if you force this."

He stood, straightened his jacket, and left. She let him go and began typing the escalation memo to the general counsel.

**E5 (escalation scene).** The general counsel's corner office, thirty-fifth floor, Tuesday afternoon. The compliance officer sat on one side of the conference table. The general counsel sat at the head, reading the escalation memo and the quarterly timestamp report side by side.

"He's not wrong about the client agreements," the general counsel said. "The confidentiality provisions in the structured-products contracts are among the strictest in the firm. Three of the four accounts have explicit carve-outs prohibiting internal dissemination of deal communications beyond the desk team."

"And Section 11?"

"Section 11 gives compliance the authority to demand access. But it doesn't explicitly address the conflict with external confidentiality obligations. It was drafted before we started writing these kinds of client agreements."

The compliance officer set the timestamp analysis on the table. "Forty-three trades executed before the client instruction was logged. I don't need to tell you what that pattern suggests."

The general counsel looked at the analysis. He was quiet for a long time.

"No," he said. "You don't." He closed the memo and set both documents in his desk tray. "I'll issue a binding interpretation by Thursday. Until then, don't approach the desk and don't communicate with the managing director about the audit. I need forty-eight hours."

**E6 (resolution scene).** The general counsel's office, Thursday morning. The managing director sat on one side of the table, the compliance officer on the other. The general counsel stood at the head with a single-page memorandum.

He read the interpretation aloud. Under the firm's regulatory obligations -- specifically the requirement to cooperate with internal surveillance when a pattern consistent with potential market abuse had been identified -- the compliance department's authority under Section 11 superseded the confidentiality provisions in the client agreements. The client agreements could restrict dissemination of deal communications for commercial purposes, but they could not restrict the firm's ability to conduct a regulatory compliance audit. The distinction was between commercial use and supervisory obligation. The audit would proceed.

The managing director spoke immediately. "If this audit damages a single client relationship, I will hold the firm liable. And I want it on the record that I objected."

"Your objection is on the record," the general counsel said. "It's in the memo. The audit proceeds under compliance's authority, with the following controls: all communications reviewed in a clean room on the ninth floor, access limited to the compliance officer and two designated reviewers, no copies made, no summaries circulated beyond the audit file. The managing director will be notified of any findings before they are reported to the board or to regulators."

"And if I choose to leave rather than comply?"

The general counsel looked at him evenly. "Then your non-compete and your deferred compensation provisions apply as written. You know what's in them."

The managing director sat very still. Then he said he would instruct his assistant to begin producing the communications archive by end of day. He did not say anything else. He stood and left without looking at the compliance officer.

The general counsel set the memorandum on the table. The compliance officer took it and returned to the ninth floor.

---

## C-arc-Co2-4

**4 beats, chronological, present tense**

**Scenario.** A hospital system's chief nursing officer demands that the chief medical officer suspend a surgeon whose complication rates have exceeded the system's safety threshold for two consecutive quarters. The CMO refuses, arguing the data is misleading because the surgeon takes the highest-acuity cases. The dispute is referred to the patient safety board, which orders an independent case review.

> A = chief nursing officer; B = chief medical officer; O = the surgical privileges of Dr. Kaplan (the flagged surgeon).

**E1 (demand scene).** The chief nursing officer's office on the administrative floor of the main campus, a Wednesday afternoon. She sits behind her desk with the quality dashboard open on her monitor. The chief medical officer sits across from her. She has asked him here rather than going to his office -- a signal he has noticed, based on the way he looked at the chair before sitting in it.

She turns the monitor so he can see the screen. Dr. Kaplan's complication panel is highlighted: surgical site infection rate at four point seven percent against a system threshold of two point five. Unplanned return to OR at three point one percent against a threshold of one point eight. Both metrics red for Q1 and Q2.

"I'm requesting that you suspend Kaplan's surgical privileges pending a full case review," she says. "The quality protocol requires suspension when any surgeon exceeds threshold in two consecutive quarters. This is the second quarter."

The CMO looks at the dashboard for a long moment. "I'm aware of the numbers," he says.

"Then you're aware that the protocol is mandatory, not discretionary. Two consecutive quarters above threshold triggers automatic referral for suspension. I'm making the referral."

He does not respond to the referral. He says he will review the data and get back to her by Friday.

She says Friday is not acceptable. The protocol specifies forty-eight hours from the point of referral. She is making the referral now. The clock starts now.

He stands, thanks her for the information, and leaves. He does not acknowledge the forty-eight-hour timeline.

**E2 (resistance scene).** The chief medical officer's office, the following morning. He has asked the chief nursing officer to come to him this time. His office is larger than hers. The case files are stacked on the conference table -- eight folders, each one a flagged complication from the past two quarters.

He tells her he has reviewed every case overnight. He opens the first folder. The patient was a seventy-eight-year-old with a BMI of forty-one, diabetes, and a history of two prior abdominal surgeries. The case had been transferred to Kaplan after two other surgeons in the system declined it. The complication -- a surgical site infection -- occurred on post-operative day nine, consistent with the patient's comorbidity profile.

He opens three more folders. The pattern holds: Kaplan's flagged cases are disproportionately high-acuity patients referred to him because no other surgeon in the system would take them. The complication rates are high because the patient population is high-risk.

"If I suspend Kaplan," he says, "those patients don't get operated on. Not here and not anywhere in this system. He's the only surgeon willing to take the cases everyone else turns away. Suspending him doesn't improve patient safety. It eliminates access for the patients who need it most."

She says she understands the acuity argument. She has heard it before, from other CMOs about other surgeons. The quality protocol exists precisely because clinical judgment alone is insufficient to determine when a surgeon's outcomes have crossed the line from difficult caseload to unsafe practice. The protocol is the check. She is activating the check.

He says he will not suspend Kaplan on the basis of a dashboard metric that does not adjust for case complexity. He says the protocol is flawed and he has raised the adjustment issue with the quality committee three times in the past year.

She says the protocol is the protocol until the quality committee changes it. It has not been changed. It applies.

He says he will not act within forty-eight hours on a suspension that will harm patients. He needs a case-by-case clinical review, not a statistical trigger.

She says the forty-eight hours is not negotiable. If he does not act, she will escalate to the patient safety board.

He says she should do what she needs to do. He will not suspend a surgeon based on unadjusted data.

**E3 (escalation scene).** The patient safety board's conference room, the following Monday. The board meets quarterly, but the chief nursing officer has invoked the emergency-session provision. Seven of the nine board members are present, including three external physician members, two community representatives, the hospital system's general counsel, and the board chair -- a retired surgeon who now teaches at the university.

The chief nursing officer presents the quality data: two consecutive quarters above threshold, the protocol's mandatory suspension language, and the CMO's refusal to act within the specified timeline. She states that she is not making a clinical judgment about Dr. Kaplan's competence. She is reporting a protocol breach by the CMO.

The CMO presents the case files. He walks the board through each flagged complication, the patient's acuity score, the referral history showing that other surgeons declined the case, and the clinical rationale for Kaplan's decisions. He argues that the quality protocol needs a risk-adjustment mechanism and that suspending the system's only high-acuity surgeon will create a patient-access crisis.

The board chair asks the CMO directly: does he believe Dr. Kaplan is practising safely? The CMO says yes, within the context of the cases he is given.

The board chair asks the chief nursing officer directly: does she believe the protocol requires suspension regardless of case-mix? She says yes. The protocol is unambiguous. It does not contain a risk-adjustment exception because the quality committee has not approved one.

The board chair asks the general counsel whether the CMO's refusal to suspend constitutes a protocol violation. The general counsel says it does, under the current language.

**E4 (resolution scene).** The same room, thirty minutes later. The board chair announces the board's decision.

Dr. Kaplan's privileges are not suspended. Instead, the board orders an independent case review of all flagged complications by an external surgical quality assessor, to be completed within thirty days. Kaplan continues to operate during the review period, but all cases above a defined acuity threshold must be co-signed by a second attending surgeon before proceeding. The co-signature requirement applies immediately.

The board further orders the quality committee to develop a risk-adjusted complication metric within ninety days. Until the new metric is in place, the mandatory suspension trigger is modified to require both a statistical flag and a preliminary clinical review before activation.

The chief nursing officer notes for the record that the board has effectively overridden the existing protocol rather than enforcing it. The board chair acknowledges her statement and says it is accurate. He says the board's authority to modify protocol in an emergency session is established in the bylaws. The modification is temporary, pending the quality committee's work.

The CMO thanks the board. The chief nursing officer does not thank the board. She writes the co-signature requirement into her operational log and asks the board chair for the name of the external reviewer. He says he will have it by Wednesday.

The meeting adjourns. The chief nursing officer and the CMO leave at the same time but do not speak in the corridor.
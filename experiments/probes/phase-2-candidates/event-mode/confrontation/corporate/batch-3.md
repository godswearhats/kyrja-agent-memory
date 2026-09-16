# Confrontation × Corporate — Batch 3 (Tier C)

## C-Co3-1

The procurement director's message arrives at 7:48 a.m., before the vendor's account team has finished their coffee: all outstanding invoices for the current contract period are to be placed on payment hold, effective immediately, pending delivery of the missing SLA performance reports for Q1 and Q2. The contract requires monthly reporting. No report has been received since December. The hold will release only when the reports are delivered and reviewed.

By ten o'clock the account director, Fenwick, calls back. He acknowledges the reports are overdue. He says the delay stems from a system migration on his end — the legacy reporting tool was decommissioned in January and the replacement is not yet outputting the correct format. He asks for a thirty-day extension on the hold, during which time he will manually compile the Q1 and Q2 data from raw exports and deliver it in the agreed format. He does not ask for the hold to be removed; he asks only that no formal notice of breach be issued in the interim.

The procurement director says the hold stays. He can have thirty days to deliver the compiled reports before a formal notice of breach is issued, but the invoices will not be released until delivery and sign-off are complete. If the reports are not in her hands by the thirtieth day, she will issue the breach notice and activate the remediation clause under Section 14, which opens a thirty-day cure window before either party may terminate. Fenwick asks whether she will put this in writing. She says she will send the written extension agreement within the hour, and she does.

> A = procurement director; B = Fenwick (vendor account director); O = the overdue SLA performance reports (Q1 and Q2); resolution shape (a) — procurement director's terms prevail; payment hold stays, thirty-day written extension issued in lieu of immediate breach notice. ✓ all roles, ✓ all states.

---

## C-Co3-2

"You need to pull Delacroix off the Halsten account."

Morales looked up from the pipeline. "On what basis?"

"Conflict of interest. His wife took a position at Halsten's parent company last month. That's a direct financial relationship with the client."

"His wife's employment has nothing to do with his client coverage. They keep separate finances."

"That's not the standard, and you know it. Our policy defines a conflict as any situation where a covered person has a material financial interest in a client entity. Spousal employment at a parent company is a textbook covered relationship. I need him reassigned."

"Reassigning him mid-engagement will cost us the account. Delacroix built that relationship over two years. If we pull him now without explanation, Halsten will walk."

"Then explain it to Halsten. Conflicts get managed, not hidden."

"I'm not pulling him based on your reading of a policy that was written before spousal employment at a parent entity was even a recognized scenario. This needs to go to the Ethics Committee."

"Fine. I'll table it for Thursday's meeting. But I'm flagging to the managing partner today that an unresolved conflict exists on the Halsten account. That's a mandatory disclosure under the same policy."

"Flag whatever you like."

"I will. And Delacroix should be aware that if the Committee rules a conflict exists, any fees earned during the pending period may be subject to disgorgement."

Silence. Then: "I'll talk to Delacroix."

> A = compliance officer; B = Morales (practice group leader); O = Delacroix's assignment to the Halsten account; resolution shape (b) — deferred to the Ethics Committee (Thursday meeting), with mandatory disclosure to managing partner in the interim; Morales agrees to inform Delacroix. ✓ all roles, ✓ all states.

---

## C-Co3-3

I am the product lead for the payments integration, and what I am looking at is a push notification from our staging pipeline telling me that the infrastructure team has already begun the migration of the payments database to the new cloud region — a migration that was scheduled for Q3, that requires a forty-eight-hour maintenance window, and for which I have not signed the change-authorisation form that is explicitly required under our deployment governance policy before any change touching payments infrastructure can proceed.

I walk to Okonkwo's desk and tell him to halt the migration.

He says it's thirty percent through. Rolling it back now will corrupt two of the seven transaction tables and require a full restore from backup, which will take longer than completing the migration. He says the team had a scheduling opening and the window they had been waiting for came available this morning. He says the migration will be done by end of day.

I tell him I don't care if it's ninety percent through. The change-authorisation policy exists because payments infrastructure touches PCI scope, and any uncontrolled change in PCI scope is a compliance event that has to be logged and reviewed by the security team before proceeding, not after. Without my authorisation on file before the migration started, this is already a compliance event. He has two choices: halt and restore while I get the security team involved, or keep going and own the audit finding personally.

He keeps going. I open a ticket with the security team, mark it high-severity, and copy the VP of engineering. The security team issues a halt order forty minutes later. The migration is paused at sixty-two percent, pending a security review. The restore takes four hours.

> A = I (narrator / payments product lead); B = Okonkwo (infrastructure lead); O = the in-progress payments database migration (its continuation without authorisation); resolution shape (a) — product lead prevails via security team escalation; migration halted at 62% and paused for review. ✓ all roles, ✓ all states.

---

## C-Co3-4

The request sits on Vandermeer's screen at the top of the approvals queue, where it has sat for eleven days: a capital expenditure requisition for four replacement servers in the analytics cluster, submitted by the data engineering team, approved by their director, routed to Vandermeer as VP of Finance for sign-off at the seventy-five-thousand-dollar threshold. It is within budget. It is within policy. Vandermeer has not acted on it.

The director of data engineering, Prasad, comes to Vandermeer's office at three and asks him to approve the requisition or formally decline it before close of business. The servers have a six-week lead time. The current cluster is running at ninety-four percent capacity, and the risk team has already flagged it as an operational risk in this quarter's infrastructure report.

Vandermeer says he has concerns about the timing. The capital budget is under review in advance of the board's Q3 planning session, and he is holding discretionary approvals until the board provides guidance on capital allocation priorities. He does not know when the board will meet.

Prasad tells him this is not discretionary. The requisition is within the approved annual capital envelope, it has gone through all required approvals below Vandermeer's level, and the eleven-day delay has already extended the lead time into the quarter boundary. He sets a printed copy of the company's approval-policy document on Vandermeer's desk, open to the section specifying that requisitions within the approved capital envelope must be actioned within ten business days of reaching the approving officer. He asks Vandermeer to approve, decline, or escalate to the CFO today.

Vandermeer reads the section. He approves the requisition.

> A = Prasad (director of data engineering); B = Vandermeer (VP of Finance); O = the capital expenditure requisition (its approval for the analytics cluster servers); resolution shape (a) — Prasad prevails; Vandermeer approves after being shown the ten-business-day policy obligation. ✓ all roles, ✓ all states.

---

## C-Co3-5

FROM: Lisette Arnaud, Head of Legal
TO: Brennan Keller, Chief Revenue Officer
DATE: [current]
SUBJECT: Removal of Customer Testimonials — Immediate Action Required

Brennan,

I am writing to require the immediate removal of the six customer testimonials currently displayed on the /enterprise page of the company website. Copies are attached.

Each testimonial was collected and published under the prior marketing team's process, which did not include written consent authorising use of the customer's name, role, or likeness in a commercial context. Three of the six customers are based in EU jurisdictions where the absence of a GDPR-compliant consent record constitutes a live regulatory exposure. The other three are subject to contractual confidentiality provisions that prohibit the use of company names in promotional materials without prior written approval. I have reviewed the contracts. No approval was sought.

I am asking you to remove all six testimonials from the website before the end of business today and to confirm removal in writing to me.

I understand that this page is currently in active use as part of the enterprise sales process. I recognise the disruption. However, the regulatory and contractual exposure cannot be deferred on commercial grounds.

---

FROM: Brennan Keller, Chief Revenue Officer
TO: Lisette Arnaud, Head of Legal
SUBJECT: RE: Removal of Customer Testimonials — Immediate Action Required

Lisette,

Removing those testimonials today will create a gap in the enterprise deck that three active pipeline deals are relying on. Two of those deals are at final committee stage. I need at least a week to replace the content.

I am prepared to commit to removal within seven business days and to add a consent-collection step to the testimonial process going forward. I am not prepared to act today.

---

FROM: Lisette Arnaud, Head of Legal
TO: Brennan Keller, Chief Revenue Officer; Pieter Vos, CEO
CC: Sophia Reinholt, Data Protection Officer
SUBJECT: RE: RE: Removal of Customer Testimonials — Immediate Action Required

Brennan, Pieter,

Given that Brennan has declined to act within the required timeframe, I am escalating to the CEO. I have also copied Sophia Reinholt in her capacity as Data Protection Officer, as the EU exposure requires her awareness under our GDPR governance framework.

Pieter, I am asking you to direct the removal today. If removal does not occur before market close, I will advise external counsel to prepare a voluntary disclosure to the relevant supervisory authorities, which will alter the company's regulatory posture significantly.

The testimonials were removed from the website at 4:47 p.m.

> A = Lisette Arnaud (Head of Legal); B = Brennan Keller (CRO); O = the six customer testimonials on the enterprise page (their removal); resolution shape (b) — deferred to CEO with DPO copied; CEO directs removal, which is completed before close. ✓ all roles, ✓ all states.

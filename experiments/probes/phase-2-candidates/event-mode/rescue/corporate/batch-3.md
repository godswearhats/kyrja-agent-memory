# Rescue × Corporate — Batch 3 (Tier C)

**Re-Co3-1**

The project timeline sits on the wall-mounted display at the front of the conference room: green across every milestone through Q4. The VP of Product is mid-sentence, walking the steering committee through the launch dependencies, when the infrastructure lead raises his hand from the far end of the table.

"Before we lock the date — I need to flag something."

The VP pauses.

"The migration script." The infrastructure lead opens his laptop and turns it so the committee chair can see the terminal output. "It ran clean on staging. But staging has fourteen thousand user records. Production has two-point-three million. The batch operation doesn't paginate. It loads the full record set into memory before it writes. On the production database, at current memory allocation, that process will exhaust heap and crash the instance mid-write." He pulls up the memory profiler output and slides the laptop toward the centre of the table. "If we run this on launch day as planned, we corrupt the user table. Recovery from a mid-write crash on a table that size is an eight-to-twelve hour operation. That's not a delay. That's a launch that opens to a broken product for two-point-three million existing users."

The committee chair looks at the timeline on the wall, then at the laptop screen. "How long to fix it?"

"Pagination rewrite and retest — four days. We push the launch by a week."

The chair nods once. "We push. Mark the milestone amber and schedule the retest." He closes the slide deck on his own tablet. "Thank you for catching this before it was on the record as approved."

> A = infrastructure lead; B = the company / 2.3 million existing users; T = unpaginated migration script that would exhaust heap on the production database mid-write and corrupt the user table on launch day. ✓ all roles, ✓ all states.

---

**Re-Co3-2**

"Procurement, this is Halvorsen in Legal."

"Go ahead."

"The Drentex contract — has it executed yet?"

"We're literally on the signature page. The CFO is countersigning right now. Why?"

"Stop it. Do not let that page leave the room."

"Halvorsen, this has been through three rounds of review—"

"I know. Listen to me. The indemnification clause in Section 14.3 is written against the *prior* version of the Master Services Agreement. Drentex updated their MSA in February. Under the February version, Section 14.3 flips liability — any IP dispute originating from their toolchain becomes our exposure, not theirs. We're talking uncapped indemnification on patent claims."

A beat of silence.

"How did this get through review?"

"The clause language didn't change. The MSA it references changed underneath it. The reviewer flagged the clause as unchanged-from-template. They didn't catch that the template now points to a different document."

"The CFO has the pen in his hand."

"Then tell him to put it down. I'm walking over now with the redline."

"Copy. I'm telling him. Come fast."

> A = Halvorsen (Legal); B = the company; T = contract clause that, under the counterparty's updated MSA, assigns uncapped IP indemnification liability to the company — seconds from being executed by the CFO. ✓ all roles, ✓ all states.

---

**Re-Co3-3**

I noticed the discrepancy at 11:47 p.m., which is when I should have been asleep, but I have a bad habit of re-reading press releases the night before they go out.

The release was embargoed until 7:00 a.m. It announced the acquisition of Veltrum Analytics. The terms were correct. The strategic rationale was correct. The closing conditions were correct. The problem was in the boilerplate at the bottom — the forward-looking statements disclaimer — which had been copied from the prior quarter's release and still named a divestiture that had not been publicly disclosed. The divestiture announcement was scheduled for the following Thursday. The Veltrum release was going to pre-disclose it to every journalist on the distribution list at 7:00 a.m., eleven days early, while the regulatory filing was still pending.

I called the head of communications at home. I told her what I had found and read her the paragraph. She pulled the draft on her phone, confirmed the language, and called the distribution platform's overnight support line while I stayed on hold. They recalled the embargoed release from the queue at 12:14 a.m. and reissued it with the corrected boilerplate at 12:31 a.m. The 7:00 a.m. distribution went out on the corrected version.

No journalist received the original. The divestiture was announced on Thursday as planned.

> A = I (narrator, IR/Legal); B = the company; T = forward-looking statements boilerplate in an embargoed press release that pre-disclosed an undisclosed divestiture eleven days before the regulatory filing — set to distribute at 7:00 a.m. to the full press list. ✓ all roles, ✓ all states.

---

**Re-Co3-4**

The quarterly board pack is twenty-six slides. Slide nineteen is the talent attrition chart. It is the slide the board will spend the most time on, because the attrition numbers are bad, and everyone in the room knows it. What the board does not know — what no one in the room knows yet except Priya — is that the chart on slide nineteen is wrong.

She is the newest member of the People Analytics team. She ran the underlying query herself as a spot-check forty minutes before the board meeting, because the number had seemed low to her when the deck went to print. The query she ran used the correct denominator: headcount at the *start* of each quarter, not the rolling average. The number in the deck uses rolling average. On a headcount base that has been growing, rolling average systematically understates attrition. The chart in the deck shows twelve-point-four percent annualised attrition. The correct figure, using the standard HR industry methodology, is sixteen-point-one percent.

She prints the corrected chart. She walks to the boardroom. The CHRO is outside the door reviewing her speaking notes. Priya hands her the printout and explains the denominator error in forty seconds. The CHRO looks at the two numbers — twelve-point-four, sixteen-point-one — and asks one question: "Is your query right?"

"I checked it twice."

The CHRO takes the printout into the boardroom and replaces slide nineteen with the corrected version before the board chair calls the meeting to order.

> A = Priya (People Analytics); B = the CHRO / the board; T = attrition chart using an incorrect denominator methodology that would have caused the board to make talent decisions on a figure understating attrition by 3.7 percentage points. ✓ all roles, ✓ all states.

---

**Re-Co3-5**

> **INTERNAL INCIDENT REPORT — SEVERITY 1**
> **Submitted by:** T. Okonkwo, Senior Security Engineer
> **Date/Time:** 14 March 2026, 09:12 UTC
> **Incident Reference:** SEC-2026-0314-001
>
> **Summary:** At 08:47 UTC, routine log review identified an active credential in the production environment belonging to a former contractor whose access termination was processed in the IAM system on 28 February 2026. The termination record showed "completed" status. However, the credential — an API key provisioned outside the standard IAM workflow via the legacy developer portal — was not in scope for the automated de-provisioning sweep. The key remained active and had been used to authenticate against the production data export endpoint at 08:31 UTC this morning, sixteen minutes before detection.
>
> **Actions taken:** At 08:49 UTC, I revoked the API key directly via the developer portal admin console. At 08:51 UTC, I confirmed with the data export endpoint logs that the 08:31 UTC session exported the Transactions table schema only — no row data. At 09:00 UTC, I notified the CISO and initiated a full audit of credentials provisioned via the legacy portal outside the IAM workflow. Forty-seven additional orphaned credentials were identified and revoked by 09:10 UTC.
>
> **Status:** Active threat neutralised. Data exposure confirmed as schema-only. Legacy portal de-provisioning gap escalated to engineering for remediation.

> A = T. Okonkwo (Senior Security Engineer); B = the company / production data; T = active API key belonging to a terminated contractor, used to authenticate against the production data export endpoint — credential not covered by the standard IAM de-provisioning sweep. ✓ all roles, ✓ all states.

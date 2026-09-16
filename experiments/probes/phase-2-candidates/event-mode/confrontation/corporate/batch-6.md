# Confrontation × Corporate — Batch 6 (Tier C)

**C-Co6-1**

The notice sits in the centre of Dariusz Wolk's screen when he arrives at seven-fifty: the infrastructure team has submitted a change request to retire the legacy authentication service by end of quarter. He is the platform architect. His sign-off is required. He reads the dependency map attached to the ticket and types a single word into the approval field: *Rejected*.

By nine o'clock, the head of infrastructure engineering is at his desk.

"I need your approval on CR-1140," she says. "We have three engineers dedicated to maintaining a service that was supposed to be decommissioned eighteen months ago. It's a security surface we can't adequately patch and an operational cost we can't justify."

"The billing reconciliation pipeline runs on it," Dariusz says. "Migration is a six-month project minimum. You're asking me to approve a retirement date that precedes any feasible migration timeline."

"The migration plan is in the appendix. It's eleven weeks. We scoped it."

"You scoped the happy path. You didn't scope the reconciliation edge cases. I've filed three separate architecture review requests on this — they were all declined because the service was 'legacy and scheduled for removal.' Now you want to remove it without doing the reviews."

She pulls up the change request on her tablet and turns it toward him. "The CISO has added a security exception to this ticket. It requires a resolution by end of quarter or the exception lapses and we're in a mandatory remediation posture. That's not my timeline — that's his."

Dariusz looks at the CISO's annotation. He looks at the migration appendix. He asks whether the billing team has signed off on the eleven-week estimate. She says they haven't — not formally. He tells her to get the billing team's written sign-off on the migration scope, attached to the ticket, and he will approve within twenty-four hours of receiving it. She agrees. She is back at his desk by three o'clock with the sign-off. He approves the change request before four.

> A = head of infrastructure engineering; B = Dariusz Wolk (platform architect); O = approval of the legacy authentication service retirement (CR-1140); resolution shape (b) — both defer to the CISO's security exception deadline as binding constraint, with Dariusz's condition (billing sign-off) satisfied before formal approval. ✓ all roles, ✓ all states.

---

**C-Co6-2**

TO: n.osei@polarisinvestmentgroup.com
FROM: t.marchetti@polarisinvestmentgroup.com
DATE: [Tuesday, 14:32]
SUBJECT: RE: RE: RE: Trident allocation — mandatory reversion

Nathaniel —

I have asked you three times in writing to revert the Trident position to the approved allocation of 8%. You have held it at 14% for eleven trading days. That is not discretion within mandate — it is a material deviation from the parameters the Investment Committee approved on the 3rd, and it is one that you executed without an amendment request and without notifying Risk.

I am the Chief Risk Officer. I am formally directing you to reduce the Trident allocation to 8% by market close today and to file the post-trade deviation report with Risk Operations before you leave this evening.

— T. Marchetti

---

TO: t.marchetti@polarisinvestmentgroup.com
FROM: n.osei@polarisinvestmentgroup.com
DATE: [Tuesday, 15:09]
SUBJECT: RE: RE: RE: RE: Trident allocation — mandatory reversion

Theresa —

The position is performing. The original 8% allocation reflected a risk model that has since been updated — I briefed Dominic on the revised parameters last Thursday and he indicated he had no objection. If Dominic's verbal clearance is insufficient, I will seek formal IC amendment. But I will not reduce a position mid-run on the basis of a procedural objection when the underlying thesis is intact.

— N. Osei

---

TO: n.osei@polarisinvestmentgroup.com; d.chen@polarisinvestmentgroup.com
FROM: t.marchetti@polarisinvestmentgroup.com
DATE: [Tuesday, 15:44]
SUBJECT: RE: RE: RE: RE: RE: Trident allocation — mandatory reversion

Nathaniel, Dominic —

A verbal conversation with the CEO does not constitute Investment Committee approval under Section 4.2 of the Risk Management Framework. Dominic, I am asking you to confirm in this thread whether you authorised a material deviation from an IC-approved allocation outside the amendment process.

If the answer is yes, I am obliged to escalate to the Board Risk Committee. If the answer is no, Nathaniel reduces the position today.

— T. Marchetti

---

TO: t.marchetti@polarisinvestmentgroup.com; n.osei@polarisinvestmentgroup.com
FROM: d.chen@polarisinvestmentgroup.com
DATE: [Tuesday, 16:02]
SUBJECT: RE: RE: RE: RE: RE: RE: Trident allocation — mandatory reversion

Theresa is correct. My conversation with Nathaniel last Thursday was informational — I did not authorise a deviation. Nathaniel, please revert to 8% today and file the report.

— D. Chen

> A = Theresa Marchetti (CRO); B = Nathaniel Osei (portfolio manager); O = the Trident position allocation (reversion from 14% to the IC-approved 8%); resolution shape (a) — CRO prevails; CEO confirms no authorisation was given and directs reversion. ✓ all roles, ✓ all states.

---

**C-Co6-3**

The redesigned onboarding flow went live at midnight. By six in the morning, I was looking at the funnel data and I knew something was wrong — conversion at step three had dropped from thirty-one percent to eleven percent overnight. Step three is the identity verification screen. We had redesigned it.

I called the head of design at seven.

I told him the screen had to roll back. Not by end of day — by nine o'clock, before the West Coast came online and the session volume climbed. We had already lost four hours of peak traffic.

He said a rollback was not possible. The new screen was tied to a third-party identity provider integration that had gone live simultaneously. Rolling back the front-end without rolling back the integration would break the verification pathway entirely. The integration rollback required sign-off from Legal because of data-handling obligations in the new vendor contract.

I asked how long Legal sign-off would take. He said he didn't know — the deputy general counsel wasn't in until eight-thirty.

I told him to pull the deputy general counsel's personal number from the HR directory and call her at home. He said he wasn't comfortable doing that. I told him I was authorising it and that he could put my name on the call. He made the call. She gave verbal sign-off by seven-forty. The rollback completed at eight-fifty-two, and we had step-three conversion back to twenty-nine percent before nine-fifteen.

> A = I (narrator / VP of growth); B = head of design; O = rollback of the redesigned onboarding screen (step three); resolution shape (a) — VP of growth prevails; rollback executed after Legal verbal clearance is obtained. ✓ all roles, ✓ all states.

---

**C-Co6-4**

The severance offer is for eight weeks. Priscilla Moran has been the regional sales director for six years. The offer on the table is eight weeks.

She reads it in the HR suite on the fourth floor — a small room with a round table and a box of tissues she ignores — and when the HR business partner asks if she has any questions, she has one question: on what basis has the role been deemed redundant.

The HR business partner says the regional structure is being consolidated. Her territory is merging with the northern region. The combined role will be led by the northern director.

Priscilla tells her that she applied for the northern director role fourteen months ago. She was told she was not ready. The person hired into it had eight months' less tenure and targets that were, in her last three performance reviews, lower than hers.

She slides the severance agreement back across the table. She tells the HR business partner that she is not signing an eight-week agreement, and that she is formally requesting the company's written rationale for the redundancy selection criteria within five business days, as is her right under the employment contract. She also says she will be taking independent legal advice before any agreement is signed.

The HR business partner takes the document back. She says she will escalate the request for written rationale to the HR director and employment counsel. The meeting ends without a signature.

> A = Priscilla Moran (regional sales director); B = HR business partner; O = the severance agreement (its signing, and the legitimacy of the redundancy selection); resolution shape (c) — breaking point; Priscilla refuses to sign and formally invokes her contractual right to written rationale, ending the meeting unresolved. ✓ all roles, ✓ all states.

---

**C-Co6-5**

The licensing agreement with Caldecott Media expires in thirty-one days. Fen Nakashima, the head of content partnerships, is in the room to renew it. The VP of content strategy is also in the room. He has decided, three weeks ago, that the Caldecott catalogue is not worth the renewal price — he has not told Fen this. He has told the CEO. The CEO has not told Fen either.

Fen presents the renewal terms she has negotiated: a seven-percent rate reduction from the prior cycle, a content-expansion clause, and a three-year lock-in. She asks for the VP's sign-off so she can take it to Caldecott's team by end of week.

The VP tells her he is not signing it. He says the Caldecott catalogue has forty-percent overlap with content they now produce in-house, and that the renewal cost exceeds the incremental audience value by a margin that doesn't support the investment. He says the partnership is being wound down.

Fen tells him the wind-down is news to her. She points out that she has been in active negotiations with Caldecott for eleven weeks, that the relationship carries a sixty-day non-renewal notice obligation, and that thirty-one days is already inside the notice window. Failing to renew without proper notice triggers a penalty clause: two months of the annual licence fee, payable immediately.

The VP says the penalty cost is lower than the three-year renewal cost. He says the decision has been made.

Fen tells him she needs it in writing — a formal non-renewal directive with his name on it, explicitly acknowledging the penalty clause — before she will notify Caldecott. She is not willing to be the person who calls Caldecott to terminate a partnership she was negotiating to renew without a written instruction from above.

The VP pauses. He drafts the directive that afternoon, signs it, and copies Legal. Fen notifies Caldecott the following morning.

> A = Fen Nakashima (head of content partnerships); B = VP of content strategy; O = the Caldecott Media licence renewal (and the formal non-renewal directive); resolution shape (a) — Fen prevails on the procedural demand; VP provides written directive acknowledging penalty before she will act. ✓ all roles, ✓ all states.

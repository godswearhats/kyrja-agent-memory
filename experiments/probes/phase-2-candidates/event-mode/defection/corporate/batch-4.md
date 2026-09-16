# Defection × Corporate — Batch 4 (Tier A)

## D-Co4-1

The integration is live. Samir watches the API traffic dashboard from his standing desk and sees the handshake requests flowing between his company's payment gateway and the partner platform — the platform whose CTO, Margaux Lefevre, signed a joint-development agreement eleven months ago committing both parties to exclusive data-routing through a shared middleware layer. No direct connections to third-party processors. That was the core clause: all transaction data stays inside the shared pipe. But the traffic Samir is watching now includes a routing prefix he does not recognise. He copies it, runs a reverse lookup. The prefix belongs to Quillan Systems, a payment processor neither company has ever worked with. The requests originate from Margaux's platform. They carry his company's merchant tokens — the ones only accessible through the shared middleware. He screenshots the trace, opens the joint-development agreement on his second monitor, and calls his CEO.

> A = Samir's company / Samir (infrastructure lead); B = Margaux Lefevre (partner platform CTO); P = joint-development agreement requiring exclusive data-routing through the shared middleware layer (no direct third-party processor connections); V = routing transaction data carrying the partner's merchant tokens to an unauthorised third-party processor (Quillan Systems); discovery = Samir identifies the unrecognised routing prefix via reverse lookup on the live API dashboard. ✓ all roles, ✓ all states

---

## D-Co4-2

"I want to show you something before the all-hands." Kenji closes the conference room door and sets his laptop on the table facing Ava, the VP of People.

"This had better not be about the survey again," she says.

"It's about the survey." He turns the screen. "You told the leadership team — in the meeting I attended, in the room where I was sitting — that the engagement results would be reported to the board with no filtering. Direct pipeline, no editorial layer. Your words."

"That's what happened."

Kenji opens two tabs side by side. On the left, the raw export from the survey platform: 2,914 responses, freeform fields intact, a sentiment distribution skewing sharply negative on the question about executive communication. On the right, the version attached to the board packet he obtained from a board member who owed him a favour: 2,914 responses, same summary statistics, but the freeform appendix is missing entirely, and the sentiment chart has been rebinned into three categories instead of seven, compressing the negative tail into a neutral midrange.

"That," Kenji says, pointing to the gap between the two screens, "is not the same document."

> A = leadership team / Kenji (director); B = Ava (VP of People); P = verbal commitment to the leadership team that engagement survey results would reach the board unfiltered (no editorial layer); V = removing the freeform appendix and rebinning sentiment data before transmitting results to the board; discovery = Kenji compares the raw survey export against the board-packet version obtained from a board member. ✓ all roles, ✓ all states

---

## D-Co4-3

I built that supplier qualification matrix myself — three months of site visits, reference calls, compliance checks — and handed the final shortlist to Nadia with one condition attached. I told her, face to face, standing in the corridor outside procurement: do not add any vendor to the approved list that has not passed the full matrix. She agreed. She said she understood. This morning I am reviewing the purchase orders queued for next quarter's production run, and there is a name I have never seen: Orion Thermal Components. No entry in the qualification matrix. No site visit logged. No reference file. But an approved-vendor flag in the system, activated under Nadia's credentials, dated nine days ago. The purchase order against that flag is for sixty thousand units of a part that touches the safety-critical assembly. I print the PO, print the empty matrix row, and walk to her office.

> A = narrator (qualification lead); B = Nadia (procurement); P = verbal personal undertaking to add no vendor to the approved list without full qualification-matrix clearance; V = approving Orion Thermal Components as a vendor without any qualification-matrix entry; discovery = narrator finds the unapproved vendor while reviewing next quarter's purchase orders. ✓ all roles, ✓ all states

---

## D-Co4-4

The CTO's calendar shows the architecture review as blocked — a red bar across Thursday afternoon with Jia-Li Park's name on it. Jia-Li is the principal engineer the CTO appointed six months ago to serve as the sole technical gatekeeper for production deployments: nothing ships without her sign-off, and she is accountable under the company's SOC 2 controls for verifying that every release passes the security scan pipeline. The CTO is reviewing the incident log from an overnight outage when he notices the deployment timestamp. Thursday, 4:47 p.m. During the blocked review window. He pulls the release record. Jia-Li's approval signature is present, but the security scan field is marked SKIPPED — not failed, not pending, but manually overridden. He opens the override log. Her credentials. Her annotation: *Scan unnecessary — code reviewed manually.* The SOC 2 control does not permit manual overrides. He closes the laptop and dials the compliance officer.

> A = CTO / company; B = Jia-Li Park (principal engineer / deployment gatekeeper); P = role-based institutional duty under SOC 2 controls to verify every release passes the security scan pipeline before sign-off (no manual overrides permitted); V = manually overriding the security scan and deploying without the required automated check; discovery = CTO finds the SKIPPED status and manual-override annotation in the release record while investigating an overnight outage. ✓ all roles, ✓ all states

---

## D-Co4-5

*MEMORANDUM — PRIVILEGED AND CONFIDENTIAL*
*To: Board of Directors, Helios Therapeutics*
*From: Dr. Ines Calderon, Chief Medical Officer*
*Re: Clinical-hold compliance — Trial H-471*

*On 14 March, the FDA issued a clinical hold on Trial H-471 pending review of the hepatotoxicity signal reported in our interim data submission. Under the terms of the hold, all dosing of enrolled participants was to cease immediately, and no new participants were to be enrolled until the hold was lifted. I communicated this directive verbally to Dr. Rajesh Anand, VP of Clinical Operations, within one hour of receipt and followed up with the written hold notice, which he acknowledged by email the same day.*

*On 28 March, while preparing the company's response to the FDA, I accessed the trial management system to confirm site-level compliance. The dosing log for Site 09 (Barcelona) shows that four participants received their scheduled doses on 17, 19, 21, and 24 March — all dates subsequent to the hold. The log entries are authorised under Dr. Anand's credentials. Additionally, one new participant was enrolled at Site 09 on 20 March, also under his authorisation. Dr. Anand's acknowledgement of the hold notice is attached as Exhibit A.*

> A = Dr. Ines Calderon (CMO) / Helios Therapeutics; B = Dr. Rajesh Anand (VP of Clinical Operations); P = FDA clinical hold directive requiring immediate cessation of all dosing and prohibition of new enrolments in Trial H-471, acknowledged in writing by Dr. Anand; V = authorising continued dosing of four participants and enrolling one new participant at Site 09 after the hold date; discovery = Dr. Calderon finds the post-hold dosing and enrolment entries in the trial management system while preparing the FDA response. ✓ all roles, ✓ all states
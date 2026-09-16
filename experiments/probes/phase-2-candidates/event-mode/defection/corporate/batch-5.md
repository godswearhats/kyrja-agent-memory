# Defection × Corporate — Batch 5 (Tier B)

**D-Co5-1.** The integration is live. Harumi Sato watches the partner dashboard from her desk at Lumen Analytics, refreshing the page every few seconds as the joint data pipeline finishes its first production run. She is the partnership lead — the one who negotiated the data-sharing agreement with Draymond Health, the one whose name is on the clause specifying that all shared patient-flow models remain within the joint environment and cannot be exported to either party's proprietary systems without written co-approval. The pipeline completes. She opens the transfer log to confirm clean execution and finds an outbound replication job she did not authorize — the entire patient-flow model, weights and metadata, copied to Draymond Health's internal analytics cluster. The job was initiated by her own counterpart at Draymond, Kenji Lam, using the admin credentials she provisioned for him under the partnership terms. The timestamp is forty minutes ago.

> A = Harumi Sato / Lumen Analytics; B = Kenji Lam (Draymond Health counterpart); P = data-sharing agreement clause (shared models remain in joint environment, no export without written co-approval); V = exporting the full patient-flow model to Draymond's proprietary cluster without authorization; discovery = Harumi finds the unauthorized outbound replication job in the transfer log. ✓ all roles, ✓ all states.

**D-Co5-2.** "The thing is," Felix says, leaning against the doorframe of the break room, "she told the Osaka team the restructuring hits their division first. Told them last week."

Annika sets her coffee down. "She told them what?"

"Full details. Timeline, headcount targets, the voluntary-separation numbers. Yuki pulled me aside at the regional sync this morning and asked if she should start preparing her people."

Annika is very still. Grace Park — her chief of staff, the person she brought into the restructuring committee precisely because Grace gave her word, personally, that she would hold the information until the board approved the communication plan. No one outside the committee was supposed to know. The board has not yet voted.

"Did Grace say where she got the numbers?" Annika asks.

"Yuki said Grace presented them as final. Said the board had already signed off."

> A = Annika (executive leading restructuring); B = Grace Park (chief of staff / committee member); P = verbal personal undertaking to hold restructuring details until board-approved communication plan; V = disclosing full restructuring details (timeline, headcount, separation numbers) to the Osaka division prematurely and misrepresenting them as board-approved; discovery = Felix relays what Yuki told him at the regional sync. ✓ all roles, ✓ all states.

**D-Co5-3.** I hired Desmond as our first dedicated ethics officer because we needed someone whose entire job was to review algorithmic bias audits before any model shipped to production. That was the mandate the board wrote into the role description: no model goes live without his signed audit clearance. I am sitting in the boardroom now, reading the deployment log for the lending model that went live nine days ago. The clearance field is blank. Not rejected — blank. The model shipped without review. I pull Desmond's calendar for the deployment window. He was in the building. His access badge logged him entering the ethics-review suite twice that week. The audit was never opened, never run, never filed. The model is live, serving decisions to applicants, and the one person whose institutional purpose was to prevent exactly this simply did not do it.

> A = narrator (executive / board); B = Desmond (ethics officer); P = role-based institutional duty (no model ships to production without his signed audit clearance); V = failing to perform the algorithmic bias audit while the lending model deployed without review; discovery = narrator reads the deployment log and finds the clearance field blank, cross-references badge and calendar records. ✓ all roles, ✓ all states.

**D-Co5-4.** The Slack message appears in the #legal-holds channel at 9:14 a.m., and in-house counsel Radhika Menon reads it twice. It is from the document-management system's automated retention bot: a bulk-delete operation completed overnight on the Greenfield project archive — four hundred twelve files removed. The legal hold on Greenfield has been active for three months, placed by Radhika herself after the regulatory inquiry opened. Every person with archive access received the hold notice, which bars deletion of any Greenfield-related materials until the hold is lifted in writing by Legal. She pulls the deletion audit trail. The operation was initiated by one user: Neil Trask, VP of Operations, using his own credentials. The files are the operational correspondence files that the regulator specifically requested in their second production demand.

> A = Radhika Menon / Legal department; B = Neil Trask (VP of Operations); P = legal hold notice (bars deletion of any Greenfield-related materials until written release by Legal); V = executing a bulk deletion of 412 Greenfield project files subject to the active legal hold; discovery = automated retention bot notification in #legal-holds channel + Radhika pulling the deletion audit trail. ✓ all roles, ✓ all states.

**D-Co5-5.** FROM: facilities-monitoring@hargrove-partners.com
TO: j.osei@hargrove-partners.com
SUBJECT: Badge Access Alert — Restricted Archive Room 4B
TIMESTAMP: 2024-11-03 02:47 UTC

Ms. Osei,

Badge scan recorded at 02:41 UTC for RESTRICTED ARCHIVE ROOM 4B. Badge holder: CHEN, MARGARET — Senior Associate, M&A Advisory. Access authorization on file: NONE. Room 4B is designated client-confidential under the Chinese Wall protocol and restricted to the Arbiter Capital engagement team per your directive of 2024-09-15. Ms. Chen is currently assigned to Kestrel Holdings, the counterparty in the Arbiter transaction. Her badge was used to enter and exit the room within a four-minute window.

This alert is generated automatically and has not been reviewed by Facilities.

Juno Osei, the managing partner, reads the alert on her phone in the back of a taxi. She opens the Chinese Wall registry on her laptop. Margaret Chen's name is on the restricted-access list — explicitly barred from Room 4B, from Arbiter materials, from any contact with the Arbiter engagement. Her Kestrel assignment is the reason the wall exists. Four minutes in a room full of Arbiter's deal documents.

> A = Juno Osei / Hargrove Partners (managing partner); B = Margaret Chen (senior associate, M&A, assigned to counterparty Kestrel Holdings); P = Chinese Wall protocol restricting Chen from Arbiter Capital materials and Room 4B; V = physically entering restricted archive Room 4B containing Arbiter deal documents despite explicit prohibition; discovery = automated badge-access alert email to managing partner + cross-reference with Chinese Wall registry. ✓ all roles, ✓ all states.

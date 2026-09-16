# Rescue × Corporate — Batch 6 (Tier C)

**Re-Co6-1**

The change-management window for the ERP cutover is ninety minutes, beginning at midnight. Yusuf is the senior integration architect, and he is watching the data migration logs from his workstation in the operations centre when he sees the vendor's batch process skip the customer-address normalisation step — not fail, skip, without logging an error, because the normalisation module has a misconfigured dependency that resolves to null instead of throwing. The batch is forty-two percent complete. Forty-two percent of the legacy customer records are migrating without address standardisation, which means they will fail the new system's address-validation constraint on first access. Every order placed by those customers after go-live will reject at checkout.

He opens the vendor's migration-control interface and locates the batch job ID. He cannot restart the full migration — there is not enough time in the window. He can inject a parameter override into the running batch: force the normalisation module to load from the fallback configuration path, which does not have the broken dependency. He has used that path in the test environment. He has never used it against a live migration in progress.

He injects the override. The batch pauses for eleven seconds while the module reloads, then resumes from the address it had reached. The normalisation step appears in the logs. He watches the remaining fifty-eight percent complete with the step running correctly. At 1:47 a.m. he runs the address-validation report against the full migrated dataset. Zero failures.

The go-live proceeds at 6:00 a.m. as scheduled. Yusuf emails the vendor's integration lead with the dependency misconfiguration and the override he used. He marks the incident ticket RESOLVED — SELF-CONTAINED and attaches the before-and-after logs.

> A = Yusuf (senior integration architect); B = the company / its customers (pending post-go-live order rejections across 42% of the customer base); T = misconfigured normalisation module silently skipping address standardisation during live ERP data migration, with go-live scheduled in four hours. ✓ all roles, ✓ all states.

---

**Re-Co6-2**

"Miriam, it's Okonkwo. Stop the Clearwater print run."

"It's on press. We're forty minutes into a six-hour run — forty thousand units."

"Pull it. The liability waiver on page three — the version that went to press is the draft. The one without the indemnification clause the client's legal team added in the final round."

"Okonkwo, I need a sign-off to halt a live run. That's policy. You're account management, not legal."

"I have the email chain open right now. The final approved version came in at 4:52 p.m. yesterday. The file Terrence sent to prepress was the 4:31 version. Twenty-one minutes earlier. The clause covering product liability for end-users is missing. If Clearwater distributes forty thousand of these without that clause, they are handing out an unexecuted warranty document."

A pause on the line.

"That's on us if it ships."

"It's on us regardless. Pull the run and I'll have the corrected PDF in your hands in eight minutes. The client's legal sign-off is already attached."

"Okay. Stopping the press now. Get me that file."

"It's uploading while we speak. Check your shared folder."

> A = Okonkwo (account manager); B = Clearwater (the client) / the print firm; T = incorrect draft of liability waiver — missing final indemnification clause — on press for a 40,000-unit run with client distribution pending. ✓ all roles, ✓ all states.

---

**Re-Co6-3**

The disciplinary hearing for Priya Nair is scheduled for 9:00 a.m. in the fourth-floor conference room, and I am standing outside it at 8:53 with a copy of the investigation report I was not supposed to receive until after the hearing concluded.

I had asked the HR coordinator for the Nair file as part of a routine audit of open matters. She had sent me the wrong version — not the sanitised summary the hearing panel would use, but the full investigation file, including the investigator's working notes. I read it in six minutes. The notes documented that the key witness, a team lead named Brennan, had given materially inconsistent statements across two interview sessions — inconsistent in a way that shifted the weight of the misconduct finding from ambiguous to clear. The investigator had flagged the inconsistency in her notes and then not included it in the summary report the panel was using to conduct the hearing.

Priya Nair was about to be terminated on the basis of a report that omitted the evidence most relevant to whether the finding was sound.

I knocked on the conference room door at 8:58. I told the panel chair that new documentation had come to my attention that was material to the proceeding and that the hearing needed to be deferred until it had been reviewed by the panel and outside employment counsel. The panel chair asked me to be specific. I was specific.

The hearing was deferred. Priya Nair was asked to wait in the lobby. Outside counsel was on the phone by 9:15.

> A = I (internal auditor / narrator); B = Priya Nair (employee facing termination); T = materially incomplete investigation report — omitting witness inconsistency that undermined the misconduct finding — about to serve as the sole basis for a termination decision. ✓ all roles, ✓ all states.

---

**Re-Co6-4**

*INTERNAL INCIDENT BRIEF — CONFIDENTIAL*
*Submitted by: T. Adeyemi, Network Security Operations*
*Incident Reference: INC-2026-0491*
*Time of Detection: 14:22 UTC*
*Time of Containment: 14:38 UTC*

At 14:22 UTC, automated log analysis flagged an anomalous authentication pattern on the Salesforce integration service account (svc-sf-prod-sync). The account had authenticated successfully from an IP block registered to a commercial VPN provider — not from any address associated with internal infrastructure or approved vendor ranges. Over the preceding twenty-two minutes, the account had pulled 14,800 contact records from the production CRM via the bulk-export API.

The account's scheduled sync job does not run on Tuesdays and does not use the bulk-export endpoint. It uses the incremental-change API.

At 14:31 UTC, I revoked the service account's active session tokens and rotated the credentials. The active exfiltration session terminated. No further records were accessed after 14:31. Total records exposed: 14,800 out of 1.2 million in the production database.

At 14:38 UTC, I confirmed the containment and notified the CISO and legal counsel. The VPN IP block has been added to the platform's deny list. Root-cause analysis is ongoing; preliminary indication is that the service account credentials were exposed in a dependency library's public GitHub repository three weeks prior to this incident.

> A = T. Adeyemi (Network Security Operations); B = the company / 1.2 million CRM contacts; T = active credential-based exfiltration of production CRM records via compromised service account, pulling contact data through the bulk-export API. ✓ all roles, ✓ all states.

---

**Re-Co6-5**

The tender submission portal closes at 17:00, and at 16:41 Dara Fenn is reading the final bid document when she finds the unit-price error on line 47 of the pricing schedule.

The estimating team had carried a transposition through four versions of the workbook: the price for the structural steel package was entered as £184,000 rather than £814,000. The difference — £630,000 — had been absorbed into the contingency calculation, which had masked it from the summary totals. The bid's headline number looked correct. The breakdown was not. If the tender was submitted and awarded, the company would be contractually committed to deliver a £814,000 steel package for £184,000, with no mechanism for price adjustment under the fixed-price contract terms.

She called the estimating director. He pulled up the workbook while she held on the line and confirmed the transposition in under ninety seconds. The portal allowed document substitution up to the closing time. He corrected the line item, recalculated the contingency, confirmed the headline figure had changed by £630,000, and uploaded the revised pricing schedule at 16:53.

The original submission was withdrawn. The corrected tender went in at 16:54. The portal confirmed receipt.

> A = Dara Fenn (bid reviewer); B = the company; T = £630,000 transposition error in live tender pricing schedule — if submitted and awarded, would create an unrecoverable fixed-price shortfall on the structural steel package. ✓ all roles, ✓ all states.

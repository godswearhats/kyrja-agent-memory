# Rescue x Corporate -- Batch 5 (Tier B)

**Re-Co5-1.** The integration architect is staring at the data-migration dashboard when the row counts diverge. The source system shows 4.2 million customer records queued for transfer to the new CRM platform. The target system is ingesting them at twelve thousand rows per minute. But the deduplication module between the two systems is silently merging records that share a postal code and first initial -- not a duplicate-detection rule anyone approved. It is a default setting left over from the sandbox environment, now running against production data. Three hundred thousand distinct customer accounts have already been collapsed into roughly ninety thousand composite records. Account histories, billing addresses, consent flags -- merged irreversibly once the target system's referential integrity checks run at midnight.

The integration architect opens the pipeline orchestrator, locates the deduplication module, and examines its matching logic. Postal code plus first initial. She pauses the pipeline. The ingestion stops at 1.7 million records. She rolls back the target database to the last clean snapshot taken before the migration window opened. The 1.7 million records disappear from the target system. The source system is untouched. She reconfigures the deduplication module with the approved matching rule -- full name, date of birth, and account number -- and restarts the pipeline from record one. By morning, 4.2 million records sit in the target system, intact and correctly deduplicated.

> A = integration architect; B = 4.2 million customer accounts (and the company's data integrity); T = misconfigured deduplication module silently merging distinct customer records using a sandbox-era matching rule, with irreversible referential integrity locks scheduled for midnight. ✓ all roles, ✓ all states.

**Re-Co5-2.** "Nora, it's Jameson. Tax."

"It's eleven at night, Jameson."

"I know. The R&D credit filing is going out at six a.m. tomorrow. Fourteen-point-three million. I just pulled up the supporting schedule, and the headcount figure includes the Greenfield contractors."

"They're excluded. We settled that in March."

"The schedule includes them. Forty-one names. If we file that credit with contractor labour classified as qualified research activity, we're making a false claim to the IRS. Fourteen-point-three million in credits we're not entitled to."

"Who built the schedule?"

"Williams. He pulled the headcount from the project-management system. It doesn't distinguish employees from contractors -- it just lists everyone assigned to an R&D cost centre."

"Can you rebuild the schedule tonight?"

"I already started. I need the contractor list from procurement to cross-reference. That's why I'm calling you -- you have access to the vendor master file."

"I'm logging in now. Give me ten minutes."

"The filing queue locks at five. I need the corrected schedule uploaded by four-thirty."

"You'll have the list in ten minutes."

Jameson had the corrected schedule -- twenty-six qualified employees, no contractors -- uploaded to the filing system by three-fifteen a.m. The R&D credit went out at six with the revised figure: $9.1 million.

> A = Jameson (tax analyst); B = the company; T = R&D tax credit filing inflated by $5.2 million due to contractor headcount misclassification, scheduled to be submitted to the IRS at 6 a.m. ✓ all roles, ✓ all states.

**Re-Co5-3.** The visiting auditor notices the smell before she notices the temperature. It is Thursday afternoon, and she is walking through the climate-controlled archive on the third floor of Kerrigan & Boyle's midtown office for a routine document-retention review. The archive holds seventeen years of original client engagement letters, signed tax returns, and workpaper binders -- the paper trail for every audit opinion the firm has issued since 2009. The room should be sixty-two degrees and thirty-five percent humidity. The air is warm and damp. She checks the environmental monitor mounted by the door: seventy-nine degrees, sixty-eight percent humidity. The HVAC unit serving the archive is not running. Condensation is forming on the inside of the sealed windows.

She has seen this before, at a different firm. At sixty-eight percent humidity, paper begins absorbing moisture. Within seventy-two hours, mould colonises the stock. Once mould reaches the binding adhesive, the documents cannot be restored -- they must be destroyed, and the firm loses its only original copies of materials it is legally required to retain.

She walks to the facilities office on the first floor and reports the HVAC failure. She does not file a maintenance request. She tells the facilities manager that the archive's environmental envelope has been breached and that the documents inside are deteriorating. The facilities manager dispatches a technician immediately. By five o'clock, the HVAC unit is back online -- a failed compressor relay, replaced in forty minutes -- and the archive is drawing back down toward its target range. The firm's managing partner sends the auditor a note the following morning, thanking her for what she found. She replies that it was not part of her engagement scope but that she thought he should know.

> A = visiting auditor; B = Kerrigan & Boyle's original client records (17 years of legally required retention documents); T = failed HVAC unit causing uncontrolled humidity in the sealed archive, 72 hours from irreversible mould damage to irreplaceable paper records. ✓ all roles, ✓ all states.

**Re-Co5-4.** I am the only person on the distribution list who reads the attachment, and that is the only reason the Nakamura bid survives the afternoon.

The RFP response is due at the state procurement portal by five p.m. -- a $38 million facilities-management contract, nine months of preparation, four hundred pages of technical specifications and pricing. The submission package was finalised yesterday. This morning, the business-development coordinator circulated it to the internal review list as a courtesy -- a PDF, marked final, no action required.

I open it on my second monitor while eating lunch. Page two hundred and twelve is the pricing summary. The loaded labour rates are correct. The overhead multiplier is correct. The fee percentage at the bottom of the page is 11.2 percent. Our approved fee for this bid, confirmed by the CEO in the pricing-committee meeting I attended on Monday, is 7.8 percent. Someone transposed the figures from the draft model into the final document and pulled the wrong row -- the 11.2 percent rate is from a rejected scenario the committee discarded.

At the 11.2 percent fee, our bid is $2.9 million above the competitive ceiling the business-development team estimated. At 7.8 percent, we are $400,000 below it. The wrong number does not merely weaken the bid. It disqualifies it on price.

I call the business-development coordinator. She pulls page two-twelve and sees it. She contacts the pricing analyst, who corrects the fee schedule, regenerates the summary pages, and re-exports the PDF. The corrected submission is uploaded to the state portal at four-seventeen p.m.

> A = I (narrator, a member of the internal review list); B = the company / the Nakamura bid; T = transposed fee percentage (11.2% instead of approved 7.8%) in the final RFP submission, which would price the bid above the competitive ceiling and disqualify it on price, with the portal deadline at 5 p.m. ✓ all roles, ✓ all states.

**Re-Co5-5.** The new accounts clerk processes the wire at 10:14 a.m. without recognising the name on the beneficiary line. She has been in the role for three weeks. The wire instruction comes through the standard workflow -- $620,000 from the operating account to an entity called Harmon Consulting Group, authorised by the CFO's digital signature.

The treasury manager, reviewing the morning's outbound wire log at 10:40 a.m., sees the entry and stops. Harmon Consulting Group is not in the approved vendor file. He searches the company's accounts-payable system: no invoices, no purchase orders, no contract on file. He checks the CFO's calendar and email -- the CFO is on a flight to Singapore and has been unreachable since 6 a.m. The digital signature on the wire authorisation was applied using the CFO's credentials, but the IP address in the authentication log is in Lagos.

The wire is in the SWIFT queue. It has not yet cleared the correspondent bank. The treasury manager calls the bank's wire-operations desk, provides the reference number, and requests an immediate recall. The correspondent bank freezes the transfer. The $620,000 remains in the intermediary account, pending investigation. The treasury manager locks the CFO's credentials, files an incident report with the information-security team, and notifies the general counsel. The funds are returned to the operating account by end of business.

> A = treasury manager; B = the company / the operating account ($620,000); T = fraudulent wire transfer authorised with compromised CFO credentials, in the SWIFT queue and minutes from clearing the correspondent bank. ✓ all roles, ✓ all states.

# Confrontation x Corporate -- Batch 1 (Tier A)

**C-Co1-1.** "You need to pull the Vantage integration from the release, Priya."

Priya sets her coffee down. The sprint review ended forty minutes ago. The conference room still smells like cold pizza. She looks at Dominic -- VP of Partnerships -- and waits.

"The contract with Vantage requires mutual sign-off on any public-facing integration. Their partnership lead emailed me this morning. They haven't signed off. If this ships Friday with their logo and their data feed visible to our users, we're in breach of Section 4 before the ink is dry on the renewal."

"The integration doesn't surface their logo," Priya says. "It pulls anonymised usage metrics through their API. The partnership agreement covers co-branded features. This isn't co-branded."

"Their legal disagrees. I have the email."

"Their legal is wrong. I had our API counsel review the integration spec against Section 4 three weeks ago. The opinion is in the shared drive. Anonymised metrics accessed through a standard API endpoint don't trigger the co-branding clause."

Dominic slides his phone across the table, the email visible. "Their partnership lead says if this ships without sign-off, they're pausing the renewal discussion. That's a seven-figure contract, Priya."

"And pulling the integration delays our Q3 product milestone, which the board is tracking. I'm not pulling it on the basis of an email that misreads our own contract."

"Then we need to get this resolved before Friday. I'm calling a joint session -- our API counsel and their legal, tomorrow morning. If both sides agree the clause doesn't apply, it ships. If there's any ambiguity, it holds until sign-off is obtained."

Priya considers this. A one-day delay to Friday she can absorb. "Fine. Joint session tomorrow. But if counsel clears it, it ships Friday with no further gates."

"Agreed."

> A = Dominic (VP of Partnerships); B = Priya (product lead); O = the Vantage integration (its inclusion in the Friday release); resolution shape (b) -- both defer to a joint legal session between API counsel and Vantage's legal team for a binding determination before the Friday ship date. All roles, all states.

**C-Co1-2.** The audit committee chair arrives at the CFO's office without an appointment. She is carrying a printed copy of a wire transfer authorisation -- $2.3 million, routed to a subsidiary in Singapore that was incorporated four months ago. The subsidiary does not appear in any board-approved budget. It has no employees on record. The authorisation bears the CFO's digital signature.

She places the printout on his desk and tells him she is freezing the subsidiary's accounts through the audit committee's emergency authority under the corporate charter, effective immediately, until he provides full documentation of the entity's purpose, funding source, and relationship to the parent company's operations.

The CFO tells her the subsidiary is a vehicle for a joint venture that the CEO personally authorised. The structure was designed for speed -- the JV partner required capital commitment within sixty days, and routing it through the standard budget approval process would have taken ninety. He says the documentation exists and is with outside counsel, who is preparing the board disclosure package. He asks her to delay the freeze for seventy-two hours so the disclosure package can be presented to the full board in proper form.

She refuses. The charter grants the audit committee independent authority to freeze any financial activity that was not pre-approved through the documented budget process. The CEO's verbal authorisation does not satisfy the charter requirement. She tells the CFO that if the documentation is genuine and the JV is legitimate, the freeze will be lifted at the next audit committee meeting, which she will convene within five business days. Until then, the accounts are frozen.

The CFO picks up his phone to call the CEO. The audit committee chair tells him he is welcome to do so, but the freeze is already in effect -- she filed the order with the corporate treasurer before walking into his office.

He puts the phone down. The accounts remain frozen.

> A = audit committee chair; B = CFO; O = the Singapore subsidiary's accounts (their continued operation without board-approved documentation); resolution shape (a) -- audit committee chair prevails; freeze is already in effect and CFO has no mechanism to override it. All roles, all states.

**C-Co1-3.** I manage the loyalty programme for a mid-size airline. On Tuesday, our platform vendor pushed a configuration change to production without going through our change-approval process. The change altered the points-expiration window from twenty-four months to twelve months for all members. Fourteen million accounts were affected. No notification was sent to members. I discovered it Wednesday morning when customer service flagged a spike in complaints from members whose points had vanished overnight.

I got on a call with the vendor's delivery manager that afternoon. I told her I needed the configuration rolled back to the twenty-four-month window within four hours, and I needed a written incident report explaining how a change of this magnitude bypassed our approval gate.

She said the rollback was not possible within four hours. The configuration change had triggered a downstream recalculation across all fourteen million accounts. Reversing it required re-processing the entire member base, which her team estimated at thirty-six to forty-eight hours. She also said the change had been requested -- she produced a ticket, logged three weeks earlier, bearing the name of someone on my team. The ticket authorised the twelve-month migration.

I told her the ticket was not authorised. The person named on it is a junior analyst who does not have change-approval authority under our vendor management framework. Any configuration change affecting the member base requires sign-off from the programme director -- me -- and no such sign-off was given. The ticket should have been rejected at intake.

She said her team processes tickets as received and that validating the internal authority of the requester is not within their scope of service.

I told her it was. Section 8.1 of our service agreement requires the vendor to verify that any change request is signed by an authorised representative, as defined in Appendix C. The junior analyst is not listed in Appendix C.

She went quiet, then said she would need to consult her legal team. I said I did not have thirty-six hours. I told her that if the rollback was not initiated by end of business today, I would invoke the service-level breach clause under Section 14 and begin the formal remediation process, which includes fee holdback.

She initiated the rollback before we ended the call.

> A = I (narrator / loyalty programme director); B = vendor's delivery manager; O = the points-expiration configuration (its rollback to the twenty-four-month window); resolution shape (a) -- narrator prevails; vendor initiates rollback under threat of SLA breach and fee holdback. All roles, all states.

**C-Co1-4.** Marcus Insley thinks about the resignation letter in his inbox and decides it changes nothing about what happens next. The letter is from the head of the analytics team -- Dr. Sana Khoury -- tendered this morning, effective in two weeks. Insley is the division president. He has a non-compete and IP assignment clause in Khoury's employment agreement, and he knows exactly where she is going: to the competitor that tried to acquire her team's forecasting model six months ago.

He walks to her office. She is packing a box of personal items. He tells her that under Section 12 of her employment agreement, the forecasting model and all derivative works are company property. The model's training data, architecture documentation, and deployment configurations must remain on company systems. He is directing IT to revoke her access to the model repository and all associated resources, effective today rather than at the end of her notice period. He needs her credentials and any local copies surrendered before she leaves the building.

Khoury sets the box down. She tells him the model was built on an open-source framework she developed before joining the company. Her employment agreement's IP assignment clause, Section 12.3, contains a carve-out for pre-existing intellectual property disclosed at the time of hiring. She disclosed the framework. The disclosure is in her onboarding file. The model is a derivative of that framework, and the carve-out language is ambiguous about derivatives -- her attorney's position is that the carve-out covers them.

Insley says the company's interpretation is that derivatives of pre-existing IP created using company resources belong to the company. He asks her to surrender the materials.

She refuses. She tells him she will not surrender materials that she believes are covered by the carve-out, and if the company disagrees, the arbitration clause in Section 18 provides a mechanism. She suggests they both retain counsel and file for arbitration, and that the model repository remain under dual-key access -- neither party able to modify or delete it -- until the arbitrator rules.

Insley considers this. Revoking her access unilaterally would give her grounds to claim the company destroyed evidence or altered the repository. Dual-key access preserves the status quo.

He agrees. They notify IT together before she leaves for the day.

> A = Marcus Insley (division president); B = Dr. Sana Khoury (head of analytics); O = the forecasting model and its associated IP (ownership and custody); resolution shape (b) -- both defer to the arbitration mechanism under Section 18, with dual-key access preserving the repository pending the ruling. All roles, all states.

**C-Co1-5.** The morning stands still in the glass-walled meeting room on the fourteenth floor. Lena Gaspar, director of product design, sits across from the chief revenue officer, Tom Avery, and thinks that what he is asking her to do will lose them twenty percent of their user base within a quarter.

He has just told her to implement a new default setting: all free-tier users will have their usage data shared with advertising partners unless they manually opt out. The change is to go live in the next release cycle, three weeks from now. He has a revenue projection on his tablet -- eighteen million in new annual ad revenue -- and he tilts the screen toward her as though the number is the argument.

She tells him she will not implement the change. The product's onboarding flow promises users that their data will never be shared without explicit consent. That promise is in the terms of service, version 4.2, which was approved by legal eight months ago. Changing the default to opt-out without updating the terms of service and re-obtaining user consent would put the company in violation of its own published privacy commitments.

Avery says the terms of service are being revised. Legal is working on version 4.3 and expects to have it ready in six weeks. The opt-out default can ship with a banner notification pointing users to the updated terms.

Gaspar says a banner notification is not consent. She will not ship the change until the revised terms of service are published, users have been given the opportunity to review them, and the opt-in mechanism has been preserved. If he wants to override her, he can take it to the CEO, but she will attach her written objection to the request and copy legal.

Avery pushes his chair back. He says he will take it to the CEO this afternoon. He asks whether her objection is going to recommend killing the revenue initiative entirely.

She says no. Her objection will recommend delaying the release until the terms of service are updated and a compliant consent mechanism is in place. The revenue initiative can proceed -- on a timeline that does not expose the company to regulatory action.

Avery picks up his tablet and leaves. Gaspar opens her laptop and begins drafting the written objection.

> A = Tom Avery (chief revenue officer); B = Lena Gaspar (director of product design); O = the opt-out data-sharing default (its inclusion in the next release cycle); resolution shape (b) -- both defer to the CEO, with Gaspar attaching her written objection and Avery presenting the revenue case. All roles, all states.

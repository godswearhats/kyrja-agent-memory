# Defection arc × Corporate — Batch 2 (Tier B)

---

## D-arc-Co2-1

**4 beats, non-linear: E1 → E3 → E2 → E4. Depicted order: discovery opens, then commitment (embedded document), violation (retroactive), confrontation.**

**Scenario.** A pharmaceutical company's head of regulatory affairs is responsible for certifying that clinical trial data submitted to the FDA accurately reflects the underlying study results. Over fourteen months, she edits adverse-event tables in three submissions to reduce the reported severity of side effects, not for personal gain but because she believes the drugs are safe and that accurate reporting would trigger a review cycle that would delay patient access by two years. An internal auditor preparing for an FDA inspection finds the discrepancies.

> A = the CEO; B = head of regulatory affairs (Dr. Lena Marchetti); P = regulatory compliance charter signed at appointment (all submissions to regulatory bodies must accurately reflect underlying clinical data without modification, omission, or reclassification; the head of regulatory affairs bears personal accountability for the integrity of every filing made under her signature); V = editing adverse-event severity classifications in three FDA submissions to understate side-effect profiles, reducing Category 3 events to Category 2 in the filed tables while the source data remained unaltered.

**E1 (discovery scene).** The tenth-floor conference room, a Tuesday afternoon. The internal audit team was three weeks into the pre-inspection review -- standard preparation for the FDA's scheduled visit in April. Daniel Kovac, the lead auditor, had been cross-referencing filed submissions against source databases since Monday. He had started with the most recent filing and worked backward.

The first submission matched. The second submission matched. The third did not. The adverse-event table filed with the FDA listed fourteen Category 2 events and zero Category 3 events for the Phase III trial of Carvelon. The source database recorded eight Category 2 events and six Category 3 events. Kovac checked the export log. The table had been generated correctly from the source data -- six Category 3 entries present -- and then modified after export. The modification timestamp showed Dr. Marchetti's credentials. He pulled the fourth and fifth submissions. The same pattern: Category 3 events reclassified to Category 2 in the filed version, source data untouched, modification under the same credentials.

Kovac printed the comparison tables, walked to the general counsel's office, and set them on her desk. He said he needed to speak with the CEO before the end of the day.

**E2 (commitment scene -- embedded document).** The general counsel's office, that evening. The CEO arrived at six. Kovac was already seated. The general counsel opened Dr. Marchetti's personnel file and read the operative clause of the regulatory compliance charter aloud:

"All submissions to federal and international regulatory bodies prepared under the authority of the head of regulatory affairs must accurately reflect the underlying clinical data without modification, omission, or reclassification. The head of regulatory affairs bears personal accountability for the integrity of every filing made under her signature and accepts that any material discrepancy between source data and filed documents constitutes grounds for immediate termination and referral to the relevant regulatory authority."

The charter bore Dr. Marchetti's signature, the CEO's countersignature, and the general counsel's notarisation. It was dated eighteen months earlier, the day of her promotion.

The CEO read the comparison tables Kovac had prepared. He asked how many submissions were affected. Kovac said three confirmed, with the remaining backlog still under review. The CEO asked if the source data had been altered. Kovac said it had not -- only the filed versions.

**E3 (violation scene -- retroactive).** Kovac continued. He had reconstructed the timeline from system logs. Fourteen months earlier, one week before the Carvelon filing deadline, Dr. Marchetti had exported the adverse-event table from the clinical database. The export was clean -- it matched the source. She had then opened the export file, reclassified six Category 3 events to Category 2, saved the modified version, and uploaded it to the FDA submission portal. The portal's intake log confirmed the modified file. The same sequence appeared in the two subsequent submissions -- export, reclassification, upload -- each time reducing Category 3 counts to zero in the filed version.

Kovac noted that no other credentials appeared in the modification logs. No one else had accessed the files between export and upload. The edits were precise -- only the severity column was changed, and only for Category 3 events. The rest of each table was identical to the source.

The CEO asked if there was any financial incentive -- stock options tied to approval timelines, bonus structures linked to filing outcomes. The general counsel checked the compensation file. There were none. Dr. Marchetti's bonus was tied to departmental headcount retention, not to approval velocity.

**E4 (confrontation scene).** The CEO's office, the following morning. Dr. Marchetti arrived at eight. The CEO, the general counsel, and Kovac were already in the room. The comparison tables were on the desk.

"We need your resignation," the CEO said. "And we need it before we notify the FDA, which will happen by end of business today."

Dr. Marchetti looked at the tables. She did not dispute the data. She said the drugs were safe. She said the Category 3 classifications were artifacts of a reporting protocol that counted transient nausea lasting more than four hours as a severe event -- a threshold she had argued against in three separate protocol review meetings, all of which were in the committee minutes. She said accurate reporting under the current protocol would have triggered a mandatory six-month review extension for each submission, delaying access for patients who needed the drugs now. She had made a clinical judgment, not a financial one.

"The compliance charter doesn't distinguish between clinical judgments and financial ones," the general counsel said. "It requires accurate reflection of source data. You modified the data after export."

Dr. Marchetti said she would not resign. She said if the company terminated her and reported to the FDA, she would request a formal hearing and present the protocol committee minutes showing that she had raised the classification threshold issue through proper channels three times and been overruled each time. She said the company's refusal to fix the protocol had created the situation she was now being asked to take sole responsibility for.

The CEO was quiet for a moment. Then he said: "The FDA notification goes out today with your name on the discrepancy report. Legal will prepare the termination paperwork. If you want a hearing, you'll get one -- but it will be the FDA's hearing, not ours."

Dr. Marchetti stood. "Then I'll see you at the FDA's hearing," she said. "And I'll bring the protocol committee minutes with me."

She left the office. The general counsel began drafting the notification.

---

## D-arc-Co2-2

**5 beats, chronological. Free indirect style.**

**Scenario.** A startup's co-founder and CTO signs a vesting agreement that includes an intellectual-property assignment clause: all technical work product created during the vesting period belongs to the company. Over ten months, he builds a parallel codebase on personal infrastructure that replicates the company's core recommendation engine, intending to launch a competing product after his shares vest. The other co-founder discovers the parallel codebase when a cloud billing alert from a shared personal account surfaces on a financial reconciliation dashboard.

> A = co-founder and CEO (Priya Chandran); B = co-founder and CTO (Marcus Holt); P = vesting agreement with IP assignment clause (all technical work product, including source code, architectures, and algorithms, created during the four-year vesting period is the exclusive property of the company; no parallel or derivative technical work may be undertaken for any competing purpose during the vesting term); V = building a functionally equivalent recommendation engine on personal cloud infrastructure over ten months, using architectural knowledge gained from his role as CTO, for the purpose of launching a competing product after vesting.

**E1 (commitment scene).** The law office on Market Street, a Friday afternoon. The company was four months old and had just closed its seed round. The lawyer had drawn up the vesting agreements -- standard four-year vest with a one-year cliff, and an IP assignment clause that Priya had insisted on after a conversation with her previous company's general counsel.

Marcus read the clause twice. He understood what it meant. Everything he built during the vesting period -- code, architecture, algorithms, even napkin sketches if they were technical -- belonged to the company. He could not build anything for a competing purpose until the vesting term ended. Priya watched him read it and thought he would push back, because Marcus pushed back on everything, but he signed without comment. She countersigned. The lawyer witnessed both signatures and filed the originals.

They walked to the elevator together. Marcus said the clause was tighter than what he had seen at his last company. Priya said it needed to be, because the two of them were the entire technical team and there was no separation between what they knew and what the company owned. He said he understood. She believed him.

**E2 (trust-displayed scene).** Nine months later, the company's first board meeting with outside investors. The conference room in their office was too small, so they used the investor's boardroom downtown. Marcus presented the technical roadmap: the recommendation engine he had built from scratch, the data pipeline architecture, the latency benchmarks that put them ahead of every competitor the board had evaluated during due diligence.

The lead investor asked how defensible the technology was. Marcus said the architecture was novel -- not a wrapper around an open-source model but a purpose-built engine with three patentable components. He walked the board through each one. The investor asked whether Marcus had filed the provisional patents. He had. The filings were in the company's name, under the IP assignment clause.

Priya sat at the far end of the table and watched the board warm to him. Marcus was good at this -- not charming, exactly, but precise in a way that investors found reassuring. He knew what he had built and he could explain why it mattered. The lead investor told Priya after the meeting that the CTO was the reason they had written the check. Priya said she knew.

**E3 (first-signal scene).** A Wednesday evening, eleven months into the vesting period. Priya was reviewing the company's cloud billing dashboard -- a monthly task she had taken on when they were pre-revenue and never handed off. The company's AWS bill was in line. But the dashboard also aggregated billing from a shared personal account that Marcus had linked during the company's first month, when they were running experiments on his personal infrastructure before the corporate account was set up. The personal account was supposed to be dormant. It was not.

The charges were modest -- a few hundred dollars a month -- but they had been accumulating for ten months. Priya expanded the line items. Compute instances, storage volumes, a managed database. The resource names were generic: dev-cluster-01, staging-db, rec-engine-test. The last item caught her eye. She stared at it for a moment, then closed the dashboard and went home.

She did not mention it to Marcus the next morning. She was not sure what she had seen. It could be a side project, a personal experiment, a freelance prototype for someone else. The resource names were suggestive but not conclusive. She decided to wait and look again at the end of the month.

**E4 (discovery scene).** Four weeks later, a Saturday. Priya opened the billing dashboard from home. The charges on Marcus's personal account had increased. She expanded the resource list again. The naming convention had not changed, but there were new entries: rec-engine-v2, feature-store-prod, api-gateway-external. The architecture was legible in the resource names alone. It was their product -- or something very close to it -- running on his personal infrastructure.

She logged into the shared account. Marcus had not restricted her access -- an oversight, or perhaps he had forgotten the account was linked. She opened the compute instance tagged rec-engine-v2 and pulled the deployment manifest. The application was a recommendation engine. The API schema matched their product's schema almost exactly -- the same endpoints, the same data structures, with minor renaming. The commit history in the linked repository showed ten months of development, all from Marcus's personal Git identity. The most recent commit was two days old.

Priya read the commit messages for twenty minutes. Then she closed the laptop and called the company's outside counsel.

**E5 (confrontation scene).** Monday morning, the office. Priya had asked Marcus to come in early. The outside counsel was on speakerphone. Priya had printed the billing summary, the deployment manifest, and the API schema comparison.

"I need you to shut down the personal account infrastructure," Priya said. "Today. And I need the repository transferred to the company."

Marcus looked at the printouts. He was quiet for a long time.

"It's not the same product," he said. "I rebuilt it from scratch. Different codebase, different training data, different infrastructure. The IP assignment covers work product created for the company. This was created on my own time, on my own machines."

"The API schema is a field-for-field match," Priya said. "The architecture mirrors what you presented to the board nine months ago as the company's defensible technology. You built it while you were our CTO, using knowledge you gained in that role. The vesting agreement doesn't carve out personal time or personal machines -- it covers all technical work product created during the vesting period for any competing purpose."

Marcus said the clause was unenforceable as written -- that no court would uphold an IP assignment that claimed ownership of work done on personal infrastructure outside business hours. He said he would not transfer the repository and he would not shut down the account.

The outside counsel spoke. She said the company would seek an emergency temporary restraining order by end of business Wednesday. She said the billing records, the deployment manifest, and the API schema comparison would be attached to the filing. She asked Marcus whether he wanted to retain his own counsel before the filing or after.

Marcus was quiet again. Then he said he would retain counsel. He stood, took his laptop from the desk, and walked to the door. Priya asked him for the laptop -- it was company property. He set it on the desk by the door and left with his personal bag. The outside counsel asked Priya to secure his accounts before noon.

---

## D-arc-Co2-3

**6 beats, chronological. Dialogue-driven, present tense.**

**Scenario.** A hospital system's chief financial officer signs an integrity clause requiring that all financial reports to the board reflect actual operating performance without adjustments beyond standard accounting conventions. Over eight months, she reclassifies operating losses from the system's rural clinics as capital expenditures, making the system appear profitable when it is running a significant deficit. She does this to prevent the board from voting to close the rural clinics, which serve underinsured populations. The controller discovers the reclassifications during the annual audit preparation.

> A = board chair (Richard Talmadge); B = CFO (Janet Yoon); P = financial integrity clause in her employment contract (all financial reports presented to the board must reflect actual operating performance using standard accounting classifications; no reclassification of operating expenses to capital accounts without prior board approval and external auditor sign-off); V = reclassifying $4.2 million in rural clinic operating losses as capital expenditures across eight monthly reports, without board approval or auditor sign-off, to prevent the board from voting to close the clinics.

**E1 (commitment scene).** The boardroom, Janet Yoon's first day as CFO. Richard Talmadge sits at the head of the table. The general counsel stands by the window with the employment contract open on his tablet.

"The integrity clause," Talmadge says. "Read it back to me."

Yoon reads it from the paper copy in front of her: all financial reports presented to the board must reflect actual operating performance using standard accounting classifications. No reclassification of operating expenses to capital accounts without prior board approval and external auditor sign-off. The CFO bears personal responsibility for the accuracy of every financial report issued under her authority.

"We had problems with your predecessor," Talmadge says. "Not fraud -- creative accounting. He moved numbers around to tell the story he wanted the board to hear. By the time we figured out the actual position, we'd approved a capital plan we couldn't fund. I don't want that again."

"You won't get it from me," Yoon says. She signs the contract. Talmadge countersigns. The general counsel witnesses and files it.

**E2 (trust-displayed scene).** Five months in, the quarterly board meeting. Yoon presents the Q1 financials. The numbers are clean -- revenue up three percent, operating margin holding at four percent, the rural clinics running at a loss but within the range the board accepted when it voted to keep them open two years ago.

"This is the first time in three years I've been able to read a financial report and understand it on the first pass," Talmadge says.

"That's because the numbers are what they are," Yoon says. "I'm not smoothing anything."

The board votes to approve the Q1 report without discussion. After the meeting, Talmadge stops Yoon in the hallway. "The rural clinics," he says. "They're going to keep losing money."

"They are," she says.

"At some point the board will have to make a decision about that."

She nods. "I know. But I'm not going to be the one who makes the case for closing them. I'll give you the numbers. The decision is yours."

**E3 (violation scene).** Three months later, a Friday evening. Yoon sits alone in her office with the July financials open on her screen. The rural clinics have crossed a threshold. Operating losses for the quarter are $1.4 million above the range the board accepted. If she presents these numbers at next week's board meeting, Talmadge will call for a closure vote. She has seen the preliminary polling -- five of seven board members will vote to close.

She opens the chart of accounts. She reclassifies $1.4 million in rural clinic operating expenses -- staffing, supplies, facility maintenance -- as capital expenditures under the heading "Rural Infrastructure Modernisation." The reclassification moves the losses off the operating statement and onto the balance sheet, where they appear as investments rather than losses. The operating margin holds at three percent. The rural clinics appear to be breaking even.

She saves the modified report. She does not submit it to the external auditor for sign-off. She does not flag the reclassification for board approval. She uploads the report to the board portal and sends the standard distribution email.

**E4 (first-signal scene).** Two months later, the controller's office. David Park, the hospital system's controller, is reviewing the accounts payable ledger against the capital expenditure register as part of his monthly reconciliation. A line item catches his attention: a $180,000 charge for "nursing agency staffing" that appears in the capital register under Rural Infrastructure Modernisation.

Staffing is an operating expense. It does not belong in a capital account under any standard classification. Park opens the Rural Infrastructure Modernisation account and scrolls through the entries. Nursing staff. Medical supplies. Utility payments. Janitorial contracts. Every line item is an operating expense reclassified as capital.

He checks the account's approval history. No board authorisation. No external auditor sign-off. The reclassifications were entered under the CFO's credentials. He notes the discrepancy in his reconciliation log and flags it for follow-up. He does not raise it with Yoon. He is not sure what he is looking at -- it could be a data-entry error, a system migration artifact, a classification she intends to correct before the annual audit. He decides to complete the full-year reconciliation before escalating.

**E5 (discovery scene).** Six weeks later, the controller's office. Park has completed the annual reconciliation. The pattern is consistent across eight months. Total reclassified operating losses: $4.2 million. All entries under the CFO's credentials. No approvals. No auditor sign-off. The hospital system's reported operating margin for the year is 3.1 percent. With the reclassifications reversed, it is negative 2.4 percent.

Park walks to the general counsel's office with the reconciliation report. He lays it on the desk and explains what he has found. The general counsel reads the report, pulls up the CFO's employment contract, and reads the integrity clause. He picks up the phone and calls Talmadge.

Talmadge arrives forty minutes later. He reads the reconciliation report standing at the general counsel's desk. He reads it twice. Then he asks the general counsel to arrange a meeting with Yoon for the following morning and to have the external auditors on standby.

**E6 (confrontation scene).** The next morning, Talmadge's office. Yoon arrives at seven-thirty. Talmadge, the general counsel, and Park are seated. The reconciliation report is on the table.

"I need you to explain this," Talmadge says. "And then I need your resignation."

Yoon picks up the report. She reads it carefully, though Park can see she recognises the numbers without needing to.

"The clinics serve forty thousand patients a year," she says. "Eighty percent of them have no other provider within sixty miles. If I had reported the actual operating losses, you would have voted to close them in August. I was in the room when you polled the board informally -- five votes to close, two to keep. Those forty thousand patients would have lost their only access to care."

"That wasn't your decision," Talmadge says. "The board votes on closures. You report the numbers."

"I reported numbers that kept the clinics open long enough for the Medicaid expansion to take effect in January," Yoon says. "The expansion changes the revenue model. The clinics will break even by Q2 under the new reimbursement rates. If you'd closed them in August, you'd be trying to reopen them in six months."

"The integrity clause doesn't include a provision for good intentions," the general counsel says. "It requires actual operating performance, standard classifications, and board approval for any reclassification. None of those conditions were met."

Yoon sets the report back on the table. "I won't resign," she says. "If you terminate me, I'll request a hearing before the full board and present the Medicaid projections alongside the reclassification timeline. The board can decide whether what I did was wrong after they see what would have happened if I hadn't."

Talmadge looks at the general counsel. The general counsel says nothing.

"You're suspended, effective now," Talmadge says. "I'm calling an emergency board session for Friday. The external auditors will restate the financials. You'll present whatever you want to present at that session, and the board will make its decision. But you are not to access any financial systems between now and then."

Yoon removes her access badge from her lanyard and places it on the table. "Friday," she says. She stands and leaves. Park watches her go, then begins packing the reconciliation files for the auditors.

---

## D-arc-Co2-4

**5 beats, non-linear: E1 → E2 → E5 → E3 → E4. Depicted order: commitment, trust-displayed, confrontation, then two flashback scenes (violation, discovery). Embedded-document voice.**

**Scenario.** A management consulting firm's senior partner signs a client-confidentiality agreement prohibiting the use of one client's proprietary data or strategic plans in engagements with competing clients. Over six months, he incorporates a retail client's customer-segmentation model into deliverables for a competing retailer, stripping the original client's name but preserving the methodology and data structure. The original client's head of strategy recognises the model in a leaked slide deck.

> A = the managing partner of the firm (Helen Adeyemi); B = the senior partner (Graham Telford); P = client-confidentiality agreement (no proprietary data, methodologies, strategic plans, or derivative work products from any client engagement may be used, referenced, or adapted in any engagement with a competing client; violation constitutes grounds for partnership termination and forfeiture of equity); V = incorporating a retail client's proprietary customer-segmentation model -- its methodology, data structure, and analytical framework -- into deliverables for a competing retailer, with superficial anonymisation but no substantive modification.

**E1 (commitment scene -- embedded document).** The firm's New York office, eighteen months before the present. The annual partnership meeting. Helen Adeyemi, managing partner, reads the updated client-confidentiality protocol into the record:

> *Each partner of the firm acknowledges and agrees that no proprietary data, methodologies, strategic plans, or derivative work products developed in the course of any client engagement may be used, referenced, adapted, or incorporated in any form in any engagement with a competing client, whether or not the original client is identified. This obligation survives the termination of the original engagement. Violation constitutes grounds for immediate partnership termination and forfeiture of all unvested equity. Each partner affirms this commitment by signature below.*

The partnership secretary distributes the signature page. Graham Telford signs on the fourteenth line. Adeyemi countersigns the completed page and files it with the firm's general counsel.

**E2 (trust-displayed scene).** Eleven months later, the quarterly partnership review. Adeyemi is presenting the revenue figures. Telford's practice group leads the firm: three active engagements in retail strategy, two of them Fortune 500 clients, combined fees of $8.4 million for the year. The largest is Harmon Retail, a national chain whose customer-segmentation work Telford has led personally for two years.

Adeyemi notes the Harmon engagement specifically. The client has renewed for a third year -- unusual in an industry where consulting relationships rarely survive two cycles. She attributes the renewal to Telford's work. The partnership votes a performance allocation to his practice group.

After the meeting, Adeyemi stops Telford in the corridor. She says the Harmon relationship is the most important client asset the firm holds. She asks him to present the segmentation methodology at the firm's annual client showcase in October. He says he will.

**E3 (violation scene -- flashback).** Six months before the confrontation. Telford's office, a Thursday evening. He has just been awarded the Pennworth Group engagement -- Pennworth being Harmon Retail's principal competitor in the mid-market segment. The engagement scope is customer segmentation: build Pennworth a model that will let them target the same demographic tiers Harmon has captured.

Telford opens the Harmon engagement file on his laptop. The segmentation model is there -- two years of work, proprietary to Harmon, built on Harmon's customer data and refined through six iterative cycles with Harmon's analytics team. He opens a new file for Pennworth.

He does not copy the Harmon file directly. He rebuilds the framework in a clean document, stripping Harmon's name, its data, and its branding. But the methodology is the same: the same segmentation axes, the same tier definitions, the same analytical framework, the same scoring rubric. The data structure is preserved -- field names renamed, but the schema identical. The intellectual architecture of Harmon's model is reproduced in full.

He titles the Pennworth deliverable "Customer Segmentation Framework -- Proprietary to Pennworth Group" and uploads it to the engagement's shared drive. The junior analysts on the Pennworth team begin building on it the following Monday. None of them have access to the Harmon files. None of them know where the framework came from.

**E4 (discovery scene -- flashback).** Three weeks before the confrontation. A conference room in Harmon Retail's headquarters in Chicago. Sarah Voss, Harmon's head of strategy, is meeting with a vendor who is pitching a data partnership. The vendor, as part of his presentation, shows a slide deck he says was "circulating in the industry" -- an anonymised example of best-practice segmentation work. He does not say where it came from.

Voss looks at the slide. The segmentation axes are hers -- the same three dimensions her team developed with Telford over two years. The tier definitions match. The scoring rubric is identical down to the weighting percentages. The field names have been changed, but the schema is unmistakable. She built this model. She knows every joint and seam of it.

She asks the vendor where he obtained the deck. He says it was shared by a contact at Pennworth Group's analytics team, who described it as work product from their consulting engagement. Voss asks him to send her the file. He does, from his phone, while they are still in the room.

That evening, Voss calls Adeyemi's office directly. Adeyemi's assistant says the managing partner is in London. Voss says she will hold. She sends the slide deck to Adeyemi's email while she waits. Adeyemi calls back from the hotel at eleven p.m. London time. Voss walks her through the deck, slide by slide. Adeyemi listens without interrupting. When Voss is finished, Adeyemi says she will be in New York by Thursday.

**E5 (confrontation scene).** The present. Adeyemi's office in New York, a Thursday morning. She arrived from London the previous night. The Harmon segmentation model and the Pennworth deliverable are open side by side on her screen. Telford is seated across the desk. The door is closed.

"Sarah Voss called me on Monday," Adeyemi says. "She sent me a slide deck that came out of the Pennworth engagement. I've spent two days comparing it to the Harmon model. The methodology is identical. The tier definitions are identical. The scoring rubric matches to the decimal. You stripped the name and changed the field labels. That's all you changed."

Telford looks at the screen. "The Pennworth deliverable was built from scratch," he says. "Different data, different client, different engagement. If the methodology is similar, it's because good segmentation work converges on the same framework. That's domain expertise, not proprietary content."

Adeyemi picks up a printed page from her desk. It is the confidentiality protocol he signed eighteen months earlier. She reads the operative clause aloud: *no proprietary data, methodologies, strategic plans, or derivative work products developed in the course of any client engagement may be used, referenced, adapted, or incorporated in any form in any engagement with a competing client.*

"The protocol covers methodologies," she says. "Not just data. Not just documents. Methodologies. You built the Harmon model over two years and replicated it for their direct competitor. I need your resignation and your equity forfeiture agreement signed before Voss's next call, which is tomorrow at nine."

"If you push this to a partnership vote, I'll argue convergent methodology," Telford says. "Every retail segmentation model in the industry uses similar frameworks. You'll be asking the partners to rule that expertise itself is proprietary -- and half of them use the same playbooks across competing clients."

"You're not describing expertise," Adeyemi says. "The scoring rubric matches to the third decimal place. Expertise doesn't converge to three decimal places. The partnership vote is scheduled for Monday. You can make your case then. But the Pennworth engagement is suspended as of this morning, and your access to both client files is revoked as of now."

She slides a document across the desk -- a temporary suspension of his client access, countersigned by the general counsel. Telford reads it, sets it down, and stands.

"Monday, then," he says.

"Monday," she says. He leaves the office. Adeyemi picks up the phone and calls Sarah Voss.

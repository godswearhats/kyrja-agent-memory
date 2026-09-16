# Defection arc x Sci-fi -- Batch 1 (Tier A)

---

## D-arc-Sf1-1

**5 beats, chronological, dialogue-driven**

**Scenario.** A deep-space relay station's communications officer accepts a charter clause requiring all outbound transmissions to pass through the station's content-integrity filter before broadcast. Over nine months, she routes unfiltered transmissions from the station's science team directly to a corporate research consortium, bypassing the filter and the station commander's oversight. The transmissions contain proprietary survey data from an uncontacted system. The station's signals analyst discovers the bypass when the relay logs show bandwidth consumption that exceeds the filtered queue's throughput.

> A = the station commander; B = the communications officer, Lt. Vasquez; P = relay charter clause (all outbound transmissions from the station must pass through the content-integrity filter before broadcast; no unfiltered transmission may leave the station without the commander's written authorisation; the communications officer bears personal responsibility for ensuring compliance); V = routing unfiltered transmissions containing proprietary survey data directly to a corporate consortium via an auxiliary broadcast channel, bypassing both the content-integrity filter and the commander's oversight, for nine months.

**E1 (commitment scene).** The operations centre on deck two, the day the station went live. The commander stood at the central console. The crew -- fourteen officers and six civilian specialists -- filled the room. The relay charter was on every screen.

"Lieutenant Vasquez," the commander said. "Step forward."

She did. She was the youngest officer on the station by four years. She was also the only one who had built relay infrastructure from scratch -- two years on the Callisto array, another on the Kuiper fence.

"Read Section Seven aloud," the commander said.

She read it. All outbound transmissions from the station must pass through the content-integrity filter before broadcast. No unfiltered transmission may leave the station without the commander's written authorisation, filed in the relay log and countersigned by the duty officer. The communications officer bears personal responsibility for compliance with this section. Violations are subject to immediate suspension of comm privileges and referral to fleet judiciary.

"Do you understand the section as read?" the commander asked.

"I do."

"Do you accept personal responsibility for its enforcement?"

"I accept."

She pressed her palm to the biometric panel. The system logged her acceptance. The commander countersigned. The charter sealed.

"We're seven light-hours from the nearest fleet asset," the commander said. "Everything that leaves this station goes through your board. If it doesn't pass the filter, it doesn't fly. No exceptions. Not for me, not for the science team, not for anyone."

"Understood, Commander."

**E2 (trust-displayed scene).** Five months in. The station had settled into its rhythm. The science team was running long-range surveys of three uncontacted systems, and the data volume was heavy -- terabytes per cycle, all of it classified as proprietary under the exploration charter.

A priority request came in from fleet command: release the preliminary survey data for System Two to the joint research consortium, a civilian-military partnership that funded half the station's operating budget. The commander forwarded the request to Vasquez for processing.

She flagged it. The request specified release of the raw survey feeds, but the content-integrity filter was configured to strip raw data and release only processed summaries. Releasing the raw feeds would require a filter exception -- which required the commander's written authorisation and a modification to the broadcast protocol.

She could have processed it quietly. The request came from fleet command. No one would have questioned it.

Instead, she walked to the commander's office and laid the request on his desk.

"This needs your signature," she said. "The filter will strip the raw data unless you authorise an exception. I can configure the exception in ten minutes, but I won't do it without the paperwork."

The commander read the request, signed the exception, and she processed it through the proper channel. The consortium received their data. The filter log showed the exception, authorised and documented.

The commander told the duty officer that evening that Vasquez ran the cleanest comm board he had seen in fifteen years of station command.

**E3 (first-signal scene).** Month seven. The station's signals analyst, Petty Officer Ruiz, was running the weekly bandwidth audit -- a routine check that compared the relay's total broadcast output against the sum of all transmissions logged in the filtered queue.

The numbers were off. Not by much -- a 3% discrepancy between the relay's reported output and the filtered queue's throughput. In absolute terms, it was a small amount of bandwidth. But the station's relay was a closed system. Every outbound transmission was supposed to pass through the filter, and the filter logged everything. A 3% discrepancy meant that 3% of the station's outbound bandwidth was going somewhere the filter didn't know about.

Ruiz checked the hardware diagnostics. The relay antenna showed no malfunction. The amplifier chain was nominal. He checked the broadcast schedule against the filter log. Every scheduled transmission matched. The discrepancy was not in the scheduled traffic. It was in the total.

He flagged it in his weekly report as a possible calibration error in the relay's output sensor. The commander reviewed the report, noted the flag, and asked Vasquez to run a diagnostic on the output sensor during the next maintenance window. Vasquez said she would.

The following week, the discrepancy was still 3%.

**E4 (discovery scene).** Month nine. Ruiz had been tracking the bandwidth discrepancy for two months. It was consistent: 3% of the relay's outbound capacity, every week, unaccounted for in the filter log. He had replaced the output sensor. The discrepancy persisted. He had recalibrated the filter's throughput counter. The discrepancy persisted. The problem was not instrumentation error. Something was leaving the station that the filter was not seeing.

He pulled the relay's raw transmission log -- the hardware-level record of every signal that passed through the antenna, regardless of whether it went through the filter. The raw log was not normally reviewed. It was a diagnostic tool, stored locally on the antenna controller, and it recorded signal characteristics without content: frequency, duration, power level, beam direction.

He compared the raw log against the filter log. The filter log showed all transmissions directed at the standard relay targets -- fleet command, the research consortium's receiver, the supply depot at Ganymede. The raw log showed the same transmissions plus a second set: a series of narrowband signals, transmitted on an auxiliary channel that the filter did not monitor, directed at a receiver whose coordinates matched the consortium's secondary array -- a private facility, not the official relay endpoint.

The auxiliary channel was a maintenance frequency. It was built into the relay hardware for diagnostic purposes. It was not supposed to carry data traffic. But someone had configured it as a broadcast channel, routed data through it, and aimed it at a receiver that was not in the station's authorised relay table.

Ruiz checked the access logs on the auxiliary channel's configuration interface. One user had modified the channel settings nine months ago. The user was Lt. Vasquez.

He printed the raw log comparison, the auxiliary channel configuration record, and the access log. He carried them to the commander's quarters.

**E5 (confrontation scene).** The commander's office, the following morning. The commander had spent the night reviewing Ruiz's findings. He had pulled the auxiliary channel's signal characteristics and matched them against the survey data transmission schedule. Every auxiliary transmission coincided with a survey data upload from the science team. The bandwidth was consistent with raw, unfiltered survey feeds -- the same kind of data Vasquez had correctly flagged for filter exception five months earlier.

Vasquez arrived at 0700. The commander had asked for her at shift change. Ruiz was not present -- the commander had decided to handle this himself.

He laid the documents on the desk: the raw log comparison, the auxiliary channel configuration, the access log bearing her user ID.

"Shut down the auxiliary channel," he said. "Now. From this console. I want to watch you do it."

She looked at the documents. She looked at the console. She did not touch it.

"The consortium's secondary array is the only receiver that can handle the full survey resolution," she said. "The primary relay endpoint compresses everything to 40% fidelity. The science team's data is being degraded by the filter before it reaches the people who funded the mission. I routed the raw feeds through the auxiliary channel so the consortium could receive the data at the quality they're paying for."

"You bypassed the content-integrity filter for nine months. You used a maintenance frequency to transmit classified survey data to an unauthorised receiver. You did this without my knowledge or authorisation. Shut the channel down."

"If I shut it down, the consortium loses access to the only high-fidelity feed from three uncontacted systems. The data they're receiving through the filtered relay is scientifically useless at compressed resolution. I'm not exporting anything that isn't already authorised for consortium release -- I'm just delivering it at a quality that actually serves the mission."

"The filter exists because fleet command decides what leaves this station and at what fidelity. That is not your decision. It was never your decision. You signed the charter. You accepted personal responsibility. You flagged this exact issue five months ago when you brought me the fleet command request, and you followed the correct process then. You knew the process. You chose to stop following it."

She was quiet for a moment. "The process is too slow. I submitted three filter exception requests after that first one. Two were denied. One is still pending after four months. The data window for System Two closes in six weeks. If the consortium doesn't receive the high-fidelity feeds before then, nine months of survey work is wasted."

"That is not a justification. That is an explanation of why you decided the charter didn't apply to you." He pointed to the console. "Shut it down, or I revoke your access and have Ruiz do it. Either way, the channel closes in the next sixty seconds."

She held his gaze for a long time. Then she sat at the console, entered her credentials, and disabled the auxiliary channel. The broadcast indicator on the relay panel went dark.

The commander logged the shutdown. He suspended her comm privileges, revoked her access to the relay hardware, and assigned Ruiz as acting communications officer. He informed her that the matter would be referred to fleet judiciary at the next courier window, and that she was confined to quarters pending the referral.

She stood. At the door, she turned.

"The data is already there," she said. "The consortium has nine months of high-fidelity survey feeds. Shutting the channel down doesn't undo that."

"No," the commander said. "It doesn't."

She left. He sat at his desk and began drafting the referral.

---

## D-arc-Sf1-2

**4 beats, chronological, free indirect style**

**Scenario.** A terraforming colony's chief atmospheric engineer accepts the colony charter's environmental mandate: all atmospheric modification proposals must be submitted to the colony council for vote, and no compound may be released into the atmosphere without council approval and a 90-day environmental review. Frustrated by the council's repeated rejection of a nitrogen-fixing catalyst she believes is essential for crop viability, she begins releasing the catalyst in small doses through the atmospheric processors during routine maintenance cycles. The colony's environmental monitor, an AI system overseen by the chief science officer, detects the anomalous compound in the atmospheric composition data.

> A = the colony council / governor; B = the chief atmospheric engineer, Dr. Yun; P = colony charter environmental mandate (all atmospheric modification proposals require council vote and 90-day environmental review before any compound release; no unilateral atmospheric modification is permitted; the chief atmospheric engineer certifies monthly that all atmospheric processor outputs match the approved composition profile); V = releasing an unapproved nitrogen-fixing catalyst through the atmospheric processors during maintenance cycles without council approval or environmental review, and certifying monthly that the atmospheric composition matched the approved profile when it did not.

**E1 (commitment scene).** The council chamber was underground, as everything on the colony was underground until the atmosphere could support surface habitation. The governor sat at the head of the long table. The twenty council members occupied the seats along both sides. Dr. Yun stood at the presentation console at the far end, where three months ago she had delivered the atmospheric modelling brief that had convinced the council to extend her contract for the full terraforming cycle.

The colony charter's environmental mandate was projected on the wall behind her. The governor read the operative clause: all atmospheric modification proposals must be submitted to the colony council for vote by simple majority. No compound, biological agent, or physical process may be introduced into the colony's atmosphere without council approval and a completed 90-day environmental review conducted by the science directorate. The chief atmospheric engineer certifies monthly that all atmospheric processor outputs match the approved composition profile. Violations constitute a breach of the colony charter and are subject to contract termination and repatriation.

The governor asked Dr. Yun if she understood and accepted the mandate as read. She said she did. She pressed her hand to the biometric panel on the console. The system logged her acceptance. The council secretary entered it in the charter record.

Dr. Yun thought, as she left the chamber and walked the long corridor back to the atmospheric lab, that the mandate was sensible in principle and crippling in practice. A 90-day review for every compound meant that the terraforming schedule -- already eight years behind the original projection -- would slip further with every proposal. But she had signed it. The council had the authority. The atmosphere, for now, belonged to them.

**E2 (violation scene).** The atmospheric processing station, a maintenance night fourteen months later. Dr. Yun was alone in the control room. The maintenance cycle ran every seventy-two hours: the processors shut down, the filters were cleaned or replaced, and the system restarted with a calibrated output mix. During the restart sequence, the processor's injection ports were open for approximately forty minutes -- long enough to introduce a supplemental compound if the dosage was small and the compound was gaseous at ambient temperature.

She had submitted the nitrogen-fixing catalyst to the council three times. The first proposal had been tabled for further study. The second had been rejected on environmental-review grounds -- the science directorate wanted atmospheric modelling data that would take six months to generate. The third had been rejected by a vote of twelve to eight, with the governor abstaining.

The catalyst worked. She had modelled it exhaustively. She had tested it in the sealed greenhouse lab at concentrations ten times what she planned to release. The nitrogen fixation rates were exactly what the colony's crop programme needed. Without it, the soil amendments would run out in three years, and the colony would be dependent on supply ships for food indefinitely.

She connected the catalyst canister to the processor's secondary injection port. The port was designed for calibration gases -- small volumes, precisely metered. She had modified the metering valve to deliver 200 parts per billion of the catalyst per maintenance cycle. At that concentration, the compound would be undetectable by the colony's standard atmospheric sensors, which sampled at parts per million. It would accumulate slowly in the soil over months, doing its work quietly.

She opened the valve during the restart sequence. The catalyst entered the atmosphere with the standard output mix. She closed the valve, disconnected the canister, and logged the maintenance cycle as routine in the processor's record. She certified the atmospheric composition as matching the approved profile.

She repeated this process every seventy-two hours for eleven months.

**E3 (discovery scene).** The science directorate's monitoring lab, a Tuesday afternoon. The chief science officer, Dr. Patel, was reviewing the quarterly atmospheric composition report generated by the colony's environmental monitor -- an AI system that sampled the atmosphere continuously and compared the results against the approved profile.

The standard report showed no anomalies. The atmospheric composition matched the approved profile at the parts-per-million resolution the system was configured to report. But Dr. Patel had recently upgraded the monitor's sampling resolution as part of a broader sensor modernisation. The new resolution was parts per billion.

He ran the upgraded analysis. The monitor flagged a compound: a nitrogen-fixing catalyst, present at 187 parts per billion, not listed in the approved atmospheric profile. The compound had not been present in the baseline reading taken at the start of the terraforming cycle. It had appeared gradually, beginning approximately eleven months ago, accumulating in a stepped pattern consistent with periodic introduction rather than natural generation. The steps correlated with the atmospheric processor's maintenance cycle schedule.

Dr. Patel pulled the maintenance logs. Every cycle for the past eleven months was logged as routine by Dr. Yun. Every monthly certification stated that the atmospheric composition matched the approved profile. The catalyst was not mentioned in any log or certification.

He ran the compound through the science directorate's database. It was the same nitrogen-fixing catalyst Dr. Yun had proposed to the council three times. The same compound the council had rejected twice and tabled once.

Dr. Patel saved the upgraded analysis, locked the monitoring lab, and went to the governor's office.

**E4 (confrontation scene).** The governor's office, the following morning. The governor sat behind her desk. Dr. Patel stood to her left with the atmospheric analysis on a tablet. Dr. Yun arrived and sat in the chair across from the governor.

The governor placed the atmospheric analysis on the desk. "Dr. Patel's upgraded monitor has detected a nitrogen-fixing catalyst in the atmosphere at 187 parts per billion. The compound matches the catalyst you proposed to the council on three occasions. The council rejected it twice. It is not in the approved profile. Your monthly certifications state that the atmospheric composition matches the approved profile. I need you to account for this."

Dr. Yun looked at the analysis. She looked at Dr. Patel.

"The catalyst is in the atmosphere because I put it there," she said. "I've been introducing it through the processor's secondary injection port during maintenance cycles for eleven months. The dosage is 200 parts per billion per cycle, cumulative. The current atmospheric concentration is within the range I modelled in my third proposal to the council."

"The council rejected that proposal."

"The council rejected it because the environmental review wasn't complete. The review wasn't complete because the science directorate requested modelling data that would take six months to generate. The soil amendments run out in twenty-six months. If I waited for the review, then waited for the council to vote again, then waited for the 90-day implementation period, the amendments would be exhausted before the catalyst reached effective concentration. I did the modelling. The catalyst is safe. The crops need it. I made the decision."

The governor turned to Dr. Patel. "Is the compound dangerous at current concentrations?"

Dr. Patel said he could not answer that question without the 90-day environmental review that had never been conducted. He said the preliminary data from the upgraded monitor did not show obvious harm, but that the review existed for a reason -- to assess long-term accumulation, ecosystem interactions, and effects on colonists' respiratory health at chronic low-level exposure. None of that analysis had been done.

The governor turned back to Dr. Yun. "You certified eleven months of atmospheric reports as matching the approved profile when they did not. The charter is explicit. I'm suspending your access to the atmospheric processors effective immediately. Dr. Patel's team will take over maintenance operations until a replacement is assigned. The council will convene a special session to determine whether the catalyst should be removed from the atmosphere, allowed to remain pending review, or assessed under emergency environmental protocol."

"If you remove the catalyst, you lose eleven months of soil conditioning. The nitrogen fixation is already underway. Reversing it --"

"Is the council's decision. Not yours. It was never yours."

Dr. Yun sat very still. Then she removed her processor access card from her jacket and placed it on the governor's desk.

"I'd like to present the modelling data to the council session," she said.

"You'll have the opportunity to address the council. Whether they hear your data or your resignation is up to you." The governor picked up the access card. "Dr. Patel, please secure the atmospheric processors and begin the emergency composition audit. I want a full accounting of the catalyst's distribution and concentration before the council session."

Dr. Patel nodded and left. Dr. Yun remained in her chair for a moment. Then she stood and walked out without speaking.

---

## D-arc-Sf1-3

**6 beats, non-linear: E4 -> E1 -> E2 -> E3 -> E5 -> E6, embedded-document voice**

**Note on beat order.** This sequence is depicted non-chronologically. The chronological order is: E1 (commitment) -- E2 (trust-displayed) -- E3 (violation) -- E4 (first-signal) -- E5 (discovery) -- E6 (confrontation). The depicted order opens with the first signal, then loops back through the commitment and trust context, moves through the violation, and resolves with discovery and confrontation.

**Scenario.** An orbital shipyard's quality assurance director accepts the yard's safety charter, which requires independent inspection of all hull welds before a vessel is cleared for pressurisation. Under pressure to meet a fleet delivery schedule, she certifies forty-one hull sections as inspected when only twenty-three have been physically examined, relying on the welding team's internal quality data for the remaining eighteen. A structural engineer performing a pre-delivery survey discovers that three of the uninspected sections contain weld flaws that would have failed certification.

> A = the shipyard superintendent; B = the QA director, Commander Okafor; P = safety charter (all hull welds must receive independent QA inspection before pressurisation clearance; the QA director certifies each section personally or through a designated QA inspector; no weld may be cleared on the basis of the welding team's own quality data alone; the QA director bears personal liability for all certifications); V = certifying eighteen hull sections as independently inspected when they had not been physically examined by any QA inspector, relying solely on the welding team's internal data, resulting in three flawed sections being cleared for pressurisation.

**E4 (first-signal scene -- embedded document).** The following message was logged in the shipyard's internal communication system eleven days before the pre-delivery survey. It is addressed to the QA director from a junior QA inspector:

> *Commander Okafor -- I am writing to flag a scheduling concern regarding Vessel 7714. My inspection queue currently shows eighteen hull sections assigned to me for QA sign-off in the next four working days. Our standard inspection rate is two sections per shift. At full capacity, working double shifts, I can complete eight sections in four days. The remaining ten would require either a schedule extension or assignment to another inspector. I note that no other inspector is currently assigned to 7714.*
>
> *I also note that thirteen of the eighteen sections already show QA clearance in the certification log, with timestamps from the past week. I did not inspect those sections. The clearance entries are attributed to my inspector code, but I was on scheduled leave for three of the days in question. I am requesting clarification on who performed those inspections and entered the clearances under my code.*
>
> *Respectfully, Inspector Chen.*

The QA director's response, logged two hours later:

> *Inspector Chen -- The schedule has been adjusted. The thirteen sections you reference were reviewed using the welding team's in-process quality data, which I verified personally against the certification standard. The clearance entries were logged under your code because you are the assigned inspector of record for Vessel 7714. This is an administrative matter. Please complete the remaining five sections on your return. -- Cdr. Okafor.*

**E1 (commitment scene -- embedded document).** The shipyard's safety charter, Section 4.2, as entered into the pre-delivery inquiry record by the superintendent's office. The charter was signed by Commander Okafor sixteen months before the events in question:

> *The Quality Assurance Director accepts personal responsibility for the integrity of all hull-weld certifications issued under the yard's authority. Every hull section must receive an independent QA inspection before pressurisation clearance is granted. "Independent" is defined as: performed by a designated QA inspector who is not a member of the welding team that produced the weld, using the yard's standardised inspection protocol, with results recorded in the certification log under the inspector's own code. No hull section may be cleared for pressurisation on the basis of the welding team's in-process quality data alone, regardless of the data's completeness or accuracy. The QA Director may perform inspections personally or designate qualified inspectors, but may not delegate the certification decision to any member of the welding team. The QA Director bears personal liability for every certification issued under her authority.*

The charter signature page shows Commander Okafor's biometric acceptance, the superintendent's countersignature, and the date.

**E2 (trust-displayed scene -- embedded document).** An extract from the superintendent's quarterly performance review, filed eight months after Okafor's appointment:

> *Commander Okafor's management of the QA division has been exemplary. During the certification cycle for Vessels 7709 through 7712, her team identified twenty-six weld flaws that passed the welding team's own in-process quality checks. Fourteen of those flaws were critical -- they would have caused pressure-boundary failure under operational load. Commander Okafor personally reinspected six of the fourteen critical flaws after her inspectors flagged them, confirming the findings and ordering re-welds before clearance. Her insistence on independent inspection as a non-negotiable standard has materially improved the yard's safety record. I have recommended her for early promotion.*

**E3 (violation scene).** The QA office, a series of evenings over a two-week period. Okafor sits at her terminal with the certification log open on one screen and the welding team's in-process quality data on the other.

The delivery schedule for Vessel 7714 allows no margin. The fleet command delivery date is fixed. The vessel has forty-one hull sections requiring QA certification before pressurisation. Her inspection team has been reduced to one -- Inspector Chen -- after two inspectors were reassigned to an emergency repair on Vessel 7710. Chen can inspect two sections per shift. The math does not work.

She considers requesting a schedule extension. She knows the answer: fleet command has rejected the last three extension requests for other vessels, citing operational readiness requirements. She considers requesting temporary inspector assignments from another division. She knows the lead time: two weeks minimum, which exceeds the delivery window.

She opens the welding team's quality data for the eighteen sections Chen cannot reach. The data is detailed. Each section shows weld parameters, visual inspection photographs, and ultrasonic scan results. All eighteen sections show nominal readings. The welding team's own quality control has flagged no flaws.

She begins entering QA clearances in the certification log. She uses Chen's inspector code, because Chen is the inspector of record and the system requires an inspector assignment. She certifies each of the eighteen sections as having received independent QA inspection. She bases the certification on the welding team's data, which she reviews at her terminal. She does not physically examine any of the eighteen sections. She does not send anyone to physically examine them.

Over two weeks, she clears all eighteen sections. When Chen returns from leave and flags the discrepancy, she tells him it is an administrative matter and directs him to complete the remaining assigned sections.

**E5 (discovery scene).** Vessel 7714, docked at the yard's finishing bay. The structural engineer, Lt. Commander Vasquez, is conducting the pre-delivery survey -- a final inspection performed by the fleet's own engineering staff before accepting the vessel from the yard. The survey is independent of the yard's QA process. It is the fleet's last check.

Vasquez works section by section, hull frame by hull frame. She reaches section 31 -- one of the eighteen sections Okafor certified without physical inspection. She runs her own ultrasonic probe along the primary weld seam. The readout shows a subsurface inclusion -- a gas pocket trapped in the weld metal, invisible to the eye but clearly present on the scan. She marks it.

She moves to section 34. A similar flaw: a lack-of-fusion zone where the weld metal did not fully bond to the base plate. She marks it. Section 38: a crack propagation site at the root of a fillet weld, consistent with thermal stress during cooling. She marks it.

Three compromised sections in eighteen uninspected. She pulls the certification log. All three sections show QA clearance. She pulls the inspection records. The records attribute the inspections to Inspector Chen. She checks Chen's duty log. Chen was on scheduled leave on the dates the inspections are recorded.

She halts the pre-delivery survey, seals the vessel against pressurisation, and transmits her findings to the superintendent's office with a request for an immediate meeting.

**E6 (confrontation scene).** The superintendent's office, the following morning. The superintendent sits behind his desk. Vasquez stands at the window with her survey data on a tablet. Commander Okafor arrives and sits.

The superintendent places three documents on the desk: Vasquez's flaw report, the certification log showing QA clearance for the three compromised sections, and Inspector Chen's internal message flagging the discrepancy.

"Three hull sections on Vessel 7714 contain weld flaws that would fail pressurisation," the superintendent says. "All three are certified as inspected. Inspector Chen did not inspect them. His duty log confirms he was on leave. Your response to his inquiry states that you reviewed the welding team's in-process data and entered the clearances yourself. The safety charter prohibits clearing any section on the basis of the welding team's data alone. Explain."

Okafor looks at the documents. She does not look at Vasquez.

"The delivery schedule gave me twenty working days to certify forty-one sections with one inspector," she says. "The math required either a schedule extension or a reduction in inspection scope. I requested neither because both would have been denied. I reviewed the welding team's data for the eighteen sections Chen could not reach. The data was complete and showed no flaws. I made a judgment that the data was sufficient to certify."

"The charter does not permit that judgment. You wrote the inspection protocol yourself. Independent means independent. The welding team's data is not independent."

"I understand the definition. I also understand that three flaws in eighteen sections is a rate consistent with what my full inspection team finds in a normal cycle. If Chen had inspected those sections, he would have caught the flaws and ordered re-welds. The outcome would have been the same, just slower."

"The outcome is not the same. Three compromised sections were cleared for pressurisation. If Vasquez had not caught them in the fleet survey, this vessel would have been pressurised with three potential failure points in the hull. That is not a scheduling problem. That is a safety failure."

"I am not disputing that. I am explaining the constraints."

"The constraints are not the issue." The superintendent stands. "Your QA access is revoked effective now. All certifications you issued for Vessel 7714 are suspended pending reinspection by a fleet QA team. The eighteen sections cleared without physical inspection will be reinspected in full. Any additional flaws found will be added to the inquiry record. I am referring the matter to the fleet safety board."

Okafor looks at him steadily. "And the delivery schedule?"

"Is no longer your concern. Vasquez, how long for a full reinspection of the eighteen sections?"

Vasquez checks her tablet. "Six days, working double shifts. Assuming re-welds on the three identified flaws, add four days. Ten days total."

"Fleet command gets a ten-day delay notification this afternoon." The superintendent turns to Okafor. "Your credentials, Commander."

She removes her access badge and her QA seal and places them on his desk. She stands, straightens her uniform, and walks out. The superintendent begins drafting the fleet safety board referral. Vasquez returns to the vessel to begin the reinspection.

---

## D-arc-Sf1-4

**5 beats, non-linear: E3 -> E1 -> E4 -> E2 -> E5, present tense**

**Note on beat order.** This sequence is depicted non-chronologically. The chronological order is: E1 (commitment) -- E2 (trust-displayed) -- E3 (violation) -- E4 (discovery) -- E5 (confrontation). The depicted order opens mid-violation, loops back to the commitment, jumps forward to discovery, then loops back to the trust-displayed context before resolving with the confrontation.

**Scenario.** A habitat ring's water reclamation chief accepts the habitat charter's contamination protocol, which requires immediate shutdown of any reclamation loop showing microbial counts above the safety threshold. Over seven months, he overrides the automated shutdown triggers on two reclamation loops serving the habitat's agricultural sector, allowing contaminated water to cycle through the crop irrigation system because shutting down the loops would destroy the current growing cycle and leave the habitat without fresh produce for six months. The habitat's public health officer discovers the overrides when a cluster of gastrointestinal illness in the agricultural sector traces back to the irrigation supply.

> A = the habitat director; B = the water reclamation chief, Okonkwo; P = habitat charter contamination protocol (any reclamation loop showing microbial counts above the safety threshold must be shut down immediately; no override of the automated shutdown trigger is permitted without the habitat director's written approval and a public health review; the reclamation chief certifies weekly that all loops are operating within approved parameters); V = overriding the automated shutdown triggers on two reclamation loops for seven months, allowing contaminated water to enter the agricultural irrigation system, and certifying weekly that all loops were operating within approved parameters.

**E3 (violation scene).** The water reclamation control room on deck fourteen, 0300 hours. The room hums with the sound of pump cycles and the low whine of the UV treatment arrays. Okonkwo sits at the primary console. The two overnight technicians left an hour ago -- he told them he was running a maintenance diagnostic and would close the shift himself.

The automated shutdown trigger on Loop 7 is flashing amber. Microbial count: 340 colony-forming units per millilitre. The safety threshold is 100. The system wants to shut the loop down. In twelve seconds, it will.

Okonkwo enters his override code. The amber light holds. The shutdown trigger resets. The loop continues cycling.

He has been doing this for four months. Loop 7 and Loop 12 -- both serving the agricultural sector's irrigation grid -- have been intermittently exceeding the microbial threshold since a biofilm colony established itself in the pipe junctions six months ago. The biofilm is persistent. He has treated it with every approved agent. It responds, retreats, and re-establishes within days.

The correct response, under the contamination protocol, is to shut both loops down, drain the system, perform a full mechanical scrub of the pipe junctions, and rebuild the biofilm barriers from scratch. The procedure takes eight weeks. During those eight weeks, the agricultural sector receives no irrigation water. The current growing cycle -- sixty-two days into a ninety-day grain rotation -- dies. The habitat loses six months of food production. The next growing cycle cannot begin until the loops are restored and recertified.

Okonkwo has calculated the trade-off. The microbial contamination at current levels is unlikely to cause acute illness. The organisms are environmental, not pathogenic. The UV treatment arrays in the irrigation system reduce the count by approximately 60% before the water reaches the crops. The remaining load is above threshold but below the level that, in his assessment, poses a meaningful health risk.

He files his weekly certification. All loops operating within approved parameters. He has filed the same certification every week for four months. Loop 7's amber light flashes again. He overrides it again.

**E1 (commitment scene).** Nine months earlier. The habitat director's office on deck one. The office has a viewport -- one of only four in the administrative section -- and the stars turn slowly behind the director's head as the habitat rotates.

The director places the contamination protocol on the desk between them. She is a small woman with precise speech and a reputation for reading every document she signs. She expects the same of others.

"Section 3," she says.

Okonkwo reads Section 3 aloud. Any reclamation loop showing microbial counts above the safety threshold -- defined as 100 colony-forming units per millilitre at any sampling point -- must be shut down immediately. Immediately means within the automated trigger's response window: twelve seconds from threshold exceedance. No override of the automated shutdown trigger is permitted without the habitat director's written approval and a completed public health review. The water reclamation chief certifies weekly that all reclamation loops are operating within approved parameters. False certification is a charter violation subject to dismissal and habitat-exile proceedings.

The director asks him if he understands. He says he does. He places his palm on the biometric reader. The system logs his acceptance. The director countersigns.

"The water system is the habitat," she says. "Everything else -- power, atmosphere, food -- depends on it. If the water fails, we have thirty days before the cascade starts. The threshold exists because thirty days is not enough time to recover from a contamination event. The protocol is not conservative. It is survival-grade."

Okonkwo nods. He understands. He has managed reclamation systems on three habitats. He knows what thirty days looks like.

**E4 (discovery scene).** The public health office on deck three. Dr. Mendes, the habitat's public health officer, sits at her desk reviewing the week's illness reports. She has flagged a cluster: fourteen cases of gastrointestinal illness in the agricultural sector over the past ten days. The cases are concentrated among workers in the grain cultivation bays -- the same bays served by Loops 7 and 12.

She pulls the water quality data from the reclamation system's public reporting feed. All loops show readings within approved parameters. The weekly certifications from Okonkwo confirm compliance.

She does not accept the public data. She walks to the agricultural sector and takes her own water samples from the irrigation outlets in three grain bays. She carries them back to the public health lab and runs the analysis herself.

The results take two hours. The microbial count at the irrigation outlet in Bay 4 is 127 colony-forming units per millilitre. Bay 6 is 143. Bay 9 is 112. All above the safety threshold. The organisms are environmental -- not acutely dangerous, but capable of causing the gastrointestinal symptoms she is seeing in the illness cluster, especially at chronic low-level exposure over weeks or months.

She pulls the reclamation system's internal diagnostic log -- a feed she has access to as public health officer but does not normally review. The diagnostic log shows what the public reporting feed does not: the automated shutdown trigger on Loop 7 has been overridden 47 times in four months. Loop 12, 31 times. Every override is logged to the same user code. The code belongs to Okonkwo.

She saves her samples, locks the lab results, and goes to the habitat director.

**E2 (trust-displayed scene).** Five months earlier -- before the overrides began. The habitat's annual water system review. The director convenes a panel of department heads to evaluate the reclamation system's performance. Okonkwo presents.

He is thorough. He walks the panel through every loop's performance metrics, every maintenance action, every replacement cycle. He flags two pipe junctions in the agricultural sector that show early biofilm colonisation -- a common problem in closed-loop irrigation systems. He recommends preventive treatment with an approved biocide and schedules the application for the following week.

The director asks whether the biofilm poses a contamination risk. Okonkwo says not at current levels. He says the threshold exceedance risk is low if the preventive treatment is applied on schedule. He says that if the biofilm becomes established and the loops exceed threshold, the protocol is clear: immediate shutdown, full mechanical scrub, eight-week restoration.

The director asks whether an eight-week shutdown would be operationally survivable. Okonkwo says it would be difficult -- the agricultural sector would lose one full growing cycle -- but that the protocol exists because the alternative is worse.

The director notes his candour in the review record. She tells the panel that Okonkwo's approach to the biofilm issue is exactly right: identify the risk, treat it preventively, and if prevention fails, follow the protocol without hesitation. The panel endorses his maintenance plan.

**E5 (confrontation scene).** The habitat director's office. The stars turn behind her. Dr. Mendes stands by the viewport with her lab results on a tablet. Okonkwo sits across the desk from the director.

The director places three items on the desk: the diagnostic log showing 78 shutdown overrides across two loops, Okonkwo's weekly certifications stating all loops within parameters, and Dr. Mendes's independent water samples showing microbial counts above threshold at three irrigation outlets.

"Shut down Loops 7 and 12," the director says. "Immediately. From your console, now."

Okonkwo does not move. "If I shut down both loops, the current grain rotation dies. We're seventy-one days into a ninety-day cycle. The harvest is nineteen days away. Nineteen days of continued operation at current contamination levels, with the UV arrays reducing the microbial load, against six months of food deficit if the crops die."

"The contamination protocol does not include a harvest exception."

"I know. I'm asking you to grant one. Written approval, public health review -- I will submit to every procedural requirement. But shutting down the loops today destroys seventy-one days of food production that the habitat cannot replace before the reserve runs out."

Dr. Mendes speaks. "Fourteen colonists are sick. The exposure is chronic. The organisms are environmental, not pathogenic, but seven months of low-level exposure has consequences I cannot fully assess without longitudinal data that does not exist because no one told me the contamination was occurring. I cannot recommend continued operation."

The director looks at Okonkwo. "You presented the biofilm risk to the annual review. You told this panel that if the loops exceeded threshold, you would follow the protocol. You described the eight-week shutdown as operationally difficult but necessary. Then you overrode the shutdown seventy-eight times and certified compliance. What changed?"

"The biofilm didn't respond to treatment. The threshold exceedances started two months after the review. I ran the numbers. The shutdown would kill the growing cycle. I made a judgment that the contamination level was manageable and the food production was not expendable."

"That judgment was not yours to make."

Okonkwo is silent for a long moment. Then he reaches for his console access. He enters the shutdown commands for both loops. The status board on the wall shifts: Loop 7, offline. Loop 12, offline. The irrigation grid for the agricultural sector goes dark.

"The grain rotation," he says.

"Is lost," the director says. "Along with your certification authority. Dr. Mendes will assume oversight of the water system pending a full public health review. Your access to the reclamation control systems is revoked. I am convening a charter review board. You will have the opportunity to present your case."

Okonkwo stands. He looks at the status board -- two loops dark, the agricultural grid offline. He removes his access badge and sets it on the desk.

"I was trying to feed the habitat," he says.

"I know," the director says. "That is not the same as keeping it safe."

He walks out. The director turns to Dr. Mendes. "How long for the public health review?"

"Two weeks for the initial assessment. Eight weeks for the loop restoration. Six months before the next harvest."

The director nods. She begins drafting the notification to the habitat population.

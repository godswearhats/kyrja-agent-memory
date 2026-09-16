# Rescue arc × Sci-fi — Batch 2 (Tier B)

## Re-arc-Sf2-1

**5 beats, chronological, dialogue-driven**

**Scenario.** A communications officer on a deep-space relay station intercepts a distress signal from a colony transport that has lost navigation and is drifting toward a stellar debris field. The station commander refuses to divert the relay's power to boost a navigation patch to the transport, because doing so would disrupt the corporate data stream for six hours. The comms officer must find another way to get the navigation data to the transport before it enters the debris field.

> A = communications officer (Esen Bakir); B = colony transport *Avalon* (two thousand colonists in cryo, forty crew awake); T = stellar debris field (Kessler-class remnant of a brown dwarf collision), intercept in eleven hours at current drift.

**E1 (danger present scene).** Relay Station Tessera, comms bay, 0340 station time. Esen's console chimed with an automated distress header on the emergency band -- a compressed burst, repeating every ninety seconds, originating from a point fourteen light-minutes away. She decoded the header: colony transport *Avalon*, registry Heliodyne Corp, outbound to Kepler-442b. Navigation array failure. Main and backup stellar-fix processors offline. Vessel under inertial drift, unable to determine position or correct course.

She pulled the *Avalon's* last registered trajectory from the relay's traffic log and overlaid it on the sector chart. The drift vector put the transport on a course that would carry it into the outer margin of a Kessler-class debris field -- the remnant of a brown dwarf collision that had seeded a volume of space two AU across with rock fragments ranging from gravel to objects the size of small moons. At the *Avalon's* current velocity, the leading edge of the field was eleven hours away.

The *Avalon* had no way to know this. Without navigation, they could not see the field. Without navigation, they could not correct course. They were flying blind into a wall of rock.

Esen opened a channel and sent a reply on the emergency band: *Tessera relay copies your distress. Debris field on your current vector, eleven hours. Stand by for navigation assistance.* She set the message to repeat and went to find the station commander.

**E2 (failed initial response scene).** The station commander's office, 0355. Commander Dietrich was already awake -- he monitored the emergency band on a secondary display, though he hadn't acted on the alert. Esen told him what she'd found: the *Avalon's* situation, the debris field, the eleven-hour window.

"I need to send them a navigation patch," she said. "A stellar-fix calibration set and the debris-field coordinates. But the *Avalon's* antenna is low-gain -- their high-gain array probably went down with the nav system. I'd need to boost our transmission power to reach them, which means pulling capacity from the primary data stream."

"For how long?"

"Six hours. I need the full relay aperture to push enough signal through their low-gain antenna at this distance. The corporate data stream goes dark for that window."

Dietrich leaned back. "The Heliodyne data stream carries financial settlement packets for the entire outer-system clearing house. Six hours of interruption triggers penalty clauses in our contract. The last time this station interrupted the stream for four hours, Heliodyne docked our operating budget by twelve percent."

"There are two thousand people in cryo on that ship. Forty crew awake. Eleven hours."

"Send the patch on our secondary antenna. Half power, narrow beam."

"The secondary doesn't have the gain. At fourteen light-minutes, with their low-gain receiver, the signal-to-noise ratio won't be high enough for them to decode the navigation data. I've already run the link budget. It doesn't close."

"Then send it on the primary at reduced power. Sixty percent. Keep forty percent on the data stream."

"Sixty percent won't close the link either. I need the full aperture, Commander."

Dietrich was quiet for a moment. "Find another way. I'm not authorising a full-stream interruption."

**E3 (preparation for intervention scene).** The comms bay, 0415. Esen ran the numbers again. Dietrich was right that the secondary antenna couldn't close the link. He was wrong that sixty percent on the primary would work -- she had already shown him the link budget. The *Avalon's* low-gain antenna was a small dish, designed for short-range communication with orbital infrastructure. At fourteen light-minutes, the signal attenuation was too great for anything less than full relay power.

She pulled up the sector traffic log. Three other vessels were within communications range of Tessera: a mining tug eighteen light-minutes out, an automated freighter twenty-two light-minutes out, and a survey ship -- the *Calloway* -- nine light-minutes out on the far side of the debris field.

The *Calloway* was a research vessel. Research vessels carried high-gain directional antennas for deep-space data collection. If Esen could reach the *Calloway* on the secondary antenna -- which had enough gain for a ship with a proper receiver at nine light-minutes -- she could relay the navigation patch through the *Calloway's* high-gain transmitter, which would have enough power to reach the *Avalon's* low-gain antenna from the other side.

The geometry was awkward. The *Calloway* was on the far side of the debris field, so the signal path would go around, not through. But light doesn't care about debris fields. The signal would travel in a straight line from the *Calloway* to the *Avalon*, and the line was clear.

She began composing the relay chain: Tessera secondary to *Calloway*, *Calloway* high-gain to *Avalon*. She ran the link budget for each leg. Both closed. She drafted the navigation patch -- stellar-fix calibration data, debris-field coordinates, and a recommended course correction -- and packaged it for relay.

**E4 (intervention scene).** The comms bay, 0430. Esen opened a channel to the *Calloway* on the secondary antenna.

"Survey vessel *Calloway*, this is Tessera relay, emergency traffic. I need you to relay a navigation patch to the colony transport *Avalon*, currently drifting toward the Kessler debris field on your station-side perimeter. The *Avalon* has lost its nav array and cannot receive from us directly. I'm sending you the patch and the *Avalon's* estimated position. I need you to retransmit on your high-gain antenna, full power, aimed at the coordinates I'm providing. Confirm receipt and willingness to relay."

The round-trip light delay was eighteen minutes. She waited. At 0448, the *Calloway's* reply came through.

"Tessera, *Calloway* copies. We have your patch and the *Avalon's* coordinates. Retransmitting on high-gain now. We'll hold the beam until we get confirmation from the *Avalon* that they've received. Be advised, we can see the debris field from here on lidar. Your drift estimate is conservative -- the outer margin extends further station-ward than your chart shows. Recommend you update the *Avalon's* correction vector by three degrees port. Sending revised coordinates."

Esen received the *Calloway's* updated coordinates, verified them against her own data, and repackaged the navigation patch with the correction. She sent the update back to the *Calloway* for retransmission.

At 0511, the *Calloway* confirmed: the *Avalon* had received the navigation patch. The *Avalon's* crew was inputting the stellar-fix calibration manually.

**E5 (outcome scene).** The comms bay, 0600. The *Avalon's* next distress burst was different. The automated header was gone, replaced by a directed transmission on the emergency band, addressed to Tessera relay:

*Tessera, Avalon. Navigation patch received via Calloway relay. Stellar-fix calibration complete. We have position and we can see the debris field. Executing course correction now. New heading clears the field margin by point-four AU. Estimated time to clear the field's gravitational influence: nine hours. All crew and colonists accounted for. Request you notify Heliodyne dispatch of our revised trajectory.*

Esen logged the message, forwarded the revised trajectory to Heliodyne's dispatch office through the primary data stream -- which had not been interrupted for a single second -- and filed the incident report.

Dietrich came into the comms bay at 0620. He read the incident report on her screen. He did not comment on the method she had used. He asked whether the *Calloway* had charged a relay fee. Esen said the *Calloway* had not mentioned one. Dietrich nodded and returned to his office.

Esen watched the *Avalon's* updated position on the sector chart. The transport was turning, slowly -- two thousand tonnes of hull and cargo and two thousand sleeping colonists, pivoting on manoeuvring thrusters, the debris field sliding from ahead to abeam to astern. She watched until the course correction was complete and the *Avalon's* track showed clear space ahead. Then she closed the chart and returned to her watch.

---

## Re-arc-Sf2-2

**4 beats, chronological, free indirect style**

**Scenario.** An atmospheric processor technician on a terraforming colony discovers that the colony's main oxygen generator is about to vent its entire reserve into space through a cracked thermal coupling, which will leave the colony without breathable air within six hours. The colony administrator has locked down the processor complex for a scheduled firmware update and refuses to interrupt it.

> A = atmospheric processor technician (Davi Souza); B = twelve hundred colonists in the surface settlement; T = cracked thermal coupling on the main oxygen generator, venting reserve oxygen into vacuum, six hours to atmosphere failure.

**E1 (danger present scene).** Atmospheric Processing Complex Seven, the maintenance level, 1400 local time. Davi had come down to the maintenance level to replace a filter cartridge on one of the secondary scrubbers -- routine work, the kind that filled the gaps between firmware updates and kept the colony breathing without anyone noticing. The maintenance level was a concrete corridor lined with pipes and sensor nodes, lit by strips that flickered when the processor cycled.

He noticed the frost first. A line of white crystals along the base of the main oxygen conduit, running from the thermal coupling housing toward the exterior wall. Frost on an oxygen line meant a leak -- gas expanding as it escaped, dropping in temperature, condensing moisture from the corridor air. He followed the frost line to the coupling housing and found the crack: a hairline fracture in the ceramic sleeve, running three-quarters of the way around the circumference. Gas was hissing through it, a thin, steady whistle that he could hear only because the maintenance level was quiet.

He pulled up the oxygen reserve reading on his diagnostic pad. The main reserve tank should have read ninety-two percent. It read seventy-eight. It had been ninety-two at his last check, eight hours ago. Fourteen percent in eight hours. The colony's atmosphere system could sustain operations down to about twenty percent reserve before the air quality in the settlement began to degrade. At the current leak rate, they would hit twenty percent in approximately six hours.

Davi looked at the crack and thought about what it would take to replace the coupling. The replacement part was in the parts locker on the level above. The work itself was a two-hour job. But the coupling was in the main oxygen line, and replacing it required shutting down the line, which required shutting down the atmospheric processor, which was currently in the middle of a firmware update that the colony administrator had scheduled three weeks ago and locked behind an administrative override.

**E2 (failed initial response / danger escalation scene).** The colony administrator's office, operations module, 1430. Administrator Chen listened to Davi's report with the expression of a person who was already thinking about the firmware update. Davi had seen the expression before. Chen was an administrator, not an engineer. He understood firmware schedules and colony budgets. He did not understand thermal couplings.

Davi told him the reserve was dropping. He told him the coupling needed to be replaced. He told him the replacement required a processor shutdown. Chen told him the firmware update was a corporate-mandated security patch that had to be installed within a contractual compliance window, and that the window closed at midnight. If the update was interrupted, it would need to be restarted from the beginning, and the next compliance window was thirty days away. The corporate penalty for missing a compliance window was a reduction in the colony's supply allocation.

Davi told him the colony would not need a supply allocation if the reserve hit zero. Chen told him to find a temporary fix that did not require a processor shutdown. He said he would authorise a shutdown if the reserve dropped below forty percent, and not before.

Davi left the office and returned to the maintenance level. Forty percent was a number Chen had chosen because it sounded like a reasonable margin. It was not. Below forty percent, the scrubbers would begin to strain. Below thirty, the settlement's interior air would become noticeably thin. Below twenty, people would start to feel it -- headaches, confusion, shortness of breath. Chen's threshold left a margin of twenty percentage points between his authorised shutdown and the onset of symptoms. At the current leak rate, that margin was less than two hours.

**E3 (preparation for intervention scene).** The maintenance level, 1500. Davi could not replace the coupling without a shutdown. But he could slow the leak. He opened the parts locker and found what he needed: a ceramic patch compound rated for oxygen-line pressures, a clamping sleeve from a decommissioned secondary line, and a roll of thermal wrapping.

The patch would not hold permanently. The crack was too long and the internal pressure too high. But if he could reduce the leak rate by even half, he would buy the colony another six hours -- enough time for the firmware update to complete, for Chen to authorise the shutdown, and for Davi to replace the coupling properly.

He carried the materials to the coupling housing and began working. The oxygen hissing through the crack was cold enough to numb his fingers within minutes. He applied the patch compound in layers, building up thickness along the fracture, then wrapped the clamping sleeve over the patch and tightened it. The thermal wrapping went over everything, insulating the repair from the corridor air.

The hissing diminished. It did not stop. He checked his diagnostic pad. The leak rate had dropped by roughly sixty percent. The reserve was now at seventy-one percent and falling, but falling more slowly. His revised estimate: the reserve would reach Chen's forty-percent threshold in approximately nine hours. The firmware update would complete in seven.

**E4 (outcome scene).** The maintenance level, 2230. The firmware update completed at 2147. Davi had been sitting on the corridor floor beside the coupling housing for the past seven hours, monitoring the patch. The leak rate had increased twice as the patch compound settled under pressure -- each time, he had added another layer and retightened the clamping sleeve. The reserve stood at fifty-one percent. His margin had held.

At 2200, Chen's authorisation for the processor shutdown came through on Davi's diagnostic pad -- a one-line message: *Firmware complete. Shutdown authorised. Proceed with repair.* Davi initiated the shutdown sequence. The processor wound down over twenty minutes, the deep hum of the complex fading to silence. He removed the cracked coupling, fitted the replacement, and brought the system back online.

The processor restarted at 2315. The oxygen line pressurised. The replacement coupling held. Davi watched the reserve reading on his pad: fifty-one percent and climbing. The main generator was replenishing the reserve at its standard rate. Full capacity would be restored by morning.

He cleaned his tools, stowed the materials, and climbed the stairs to the surface level. The settlement corridor was quiet. The air tasted the same as it always had. Twelve hundred people had spent the day in that air, breathing it without thinking about it, unaware that the margin between normal and not-normal had been a ceramic patch and a clamping sleeve held in place by a technician sitting on a concrete floor.

Davi walked to the canteen, poured a cup of coffee, and sat at a table by the window. Through the glass, the atmospheric processor's exhaust plume was visible against the dark sky -- a faint shimmer of heat and gas, steady, uninterrupted. He drank his coffee and went to bed.

---

## Re-arc-Sf2-3

**6 beats, non-linear: E1 (embedded document/aftermath) -> E2 (danger present) -> E3 (danger escalation) -> E4 (failed initial response) -> E5 (intervention) -> E6 (outcome), present tense**

**Scenario.** A dock controller at an orbital station detects that a passenger shuttle's docking clamps have failed to disengage after departure, and the shuttle is dragging the station's docking arm into a structural-failure trajectory. One hundred and twelve passengers are aboard the shuttle, and the station's automated systems are about to sever the arm -- with the shuttle still attached -- to protect the station.

> A = dock controller (Yuki Tanabe); B = one hundred and twelve passengers aboard shuttle *Larkspur*; T = station automated severance protocol, which will sever the docking arm (and the shuttle's hull where it is clamped) in eight minutes to prevent station structural failure.

**E1 (aftermath -- embedded document, depicted first).** From the station incident log, entered by the operations director six hours after the event:

> *At 1407 station time, Dock Controller Tanabe identified a clamp-retention fault on Berth 9 during the departure of passenger shuttle Larkspur. The shuttle's main engines had fired with the docking clamps still engaged, placing torsional load on the station's Arm 3. The station's structural-protection system initiated an automated severance countdown -- eight minutes to emergency detachment of Arm 3 at the shoulder joint. Severance at the shoulder would have bisected the shuttle's forward cabin, which was pressurised and occupied by one hundred and twelve passengers. Controller Tanabe disabled the automated severance, manually overrode the clamp-retention circuit, and released the shuttle from Berth 9 with four minutes remaining on the severance clock. The shuttle departed with minor hull scoring at the clamp contact points. No casualties. No decompression. Arm 3 sustained torsional deformation rated at twelve percent of failure threshold. The arm is offline pending structural assessment. Controller Tanabe has been referred to the operations review board for the unauthorised disabling of an automated safety system.*

**E2 (danger present scene).** Dock control, Berth 9 monitoring station, 1407. Yuki's board lights up red. The departure sequence for the *Larkspur* has proceeded normally through steps one through six -- passenger seal confirmed, umbilicals retracted, clearance issued -- but step seven, clamp release, has not completed. The status indicator for the four docking clamps reads ENGAGED. The shuttle's main engines have already fired. The *Larkspur* is pulling away from the berth at departure thrust, and the clamps are holding it to the station's docking arm like a leash.

The arm's stress telemetry spikes. Torsional load on the shoulder joint climbs past forty percent of rated capacity in the first ten seconds. The station's structural-protection system registers the anomaly and begins its assessment. Yuki watches the system's logic cascade on her secondary display: load exceeding threshold, rate of increase exceeding threshold, projected time to structural failure of Arm 3 -- fourteen minutes. The system's response is automatic: initiate emergency severance of Arm 3 at the shoulder joint. Countdown: eight minutes.

Yuki knows what severance means. The shoulder joint is a controlled explosive separation -- pyrotechnic bolts that blow the arm free from the station hull. The arm detaches cleanly. The station is protected. But the shuttle is still clamped to the end of the arm. The severance plane cuts through the docking interface, which means it cuts through the shuttle's forward hull section at the clamp contact points. Forward cabin. One hundred and twelve passengers.

**E3 (danger escalation scene).** Dock control, 1409. The *Larkspur's* pilot has felt the resistance. The shuttle's thrust telemetry shows the engines throttling up -- the autopilot is compensating for what it interprets as unexpected drag. More thrust means more torsional load on the arm. The stress reading climbs past fifty-five percent.

Yuki opens a channel to the shuttle. "Larkspur, dock control. Cut your engines. You are still clamped to the berth. Cut your engines immediately."

The pilot's response comes three seconds later. "Dock control, Larkspur. Engines to idle. What happened to the clamp release?"

"Clamp-retention fault. Your clamps did not disengage. We are working the problem. Keep your engines at idle and do not -- repeat, do not -- attempt to reverse thrust. Any lateral load will accelerate the arm failure."

The stress reading drops to forty-eight percent with the engines at idle, but it does not drop further. The shuttle's inertial drift, even without thrust, is maintaining load on the arm. The severance countdown continues: six minutes, forty seconds.

**E4 (failed initial response scene).** Dock control, 1410. Yuki sends the clamp-release command again through the standard control pathway. No response. The clamps remain engaged. She cycles the circuit. No response. She queries the clamp controller's diagnostic and gets the answer: a firmware fault in the clamp-retention module has locked the clamps in the engaged position. The module is not responding to release commands. The standard release pathway is dead.

She calls the station's systems engineer on the emergency line. He answers from the maintenance bay, four decks below.

"I need a manual release on the Berth 9 clamps. The firmware module is locked."

"Manual release requires someone at the berth. That's a hard-vacuum EVA -- the berth is on the exterior hull. I can suit up, but I need twenty minutes to get out there."

"I don't have twenty minutes. I have five and a half."

"Then I can't reach it."

**E5 (intervention scene).** Dock control, 1411. Yuki looks at the severance countdown: five minutes, ten seconds. She looks at the clamp-retention circuit on her board. She looks at the structural-protection system's logic cascade.

The automated severance is a safety system. It exists to protect the station from structural failure. It is triggered by the stress readings on the arm, and it will execute when the countdown reaches zero unless the stress readings drop below threshold or the system is manually overridden. The override requires a dock controller's authentication code and a physical keyswitch on the control board. The override has never been used. It exists because the station's designers understood that automated systems cannot account for every scenario.

Yuki considers. If she overrides the severance, the arm continues to take load. If the stress exceeds the arm's structural capacity, the arm fails on its own -- an uncontrolled failure, which is worse than a controlled severance because it produces debris. But the stress reading is at forty-eight percent and holding. The shuttle is at idle. The arm can sustain forty-eight percent indefinitely. The risk is not the current load. The risk is that the clamps remain engaged while the severance is the only thing on a timer.

She needs to release the clamps. The standard pathway is dead. The manual pathway requires an EVA she doesn't have time for. But there is a third pathway -- one that is not in the operating manual because it was never intended for operational use. The clamp-retention module has a hardware reset line, a physical circuit that bypasses the firmware entirely and returns the clamps to their default state. The default state is disengaged. The reset line is accessible from her console -- it is one of the emergency maintenance circuits that dock controllers are trained on but instructed never to use without engineering approval, because a firmware-bypassed reset clears all clamp state, including the safety interlocks that prevent premature release during docking.

There is no docking in progress. There is only a shuttle that needs to be let go.

Yuki enters her authentication code, turns the physical keyswitch, and disables the automated severance. The countdown stops at three minutes, fifty-two seconds. Then she opens the emergency maintenance panel on her console, locates the hardware reset line for Berth 9's clamp-retention circuit, and triggers it.

The clamp status indicators flicker from ENGAGED to FAULT to DISENGAGED. All four clamps release simultaneously.

**E6 (outcome scene).** Dock control, 1412. The *Larkspur* drifts free. The stress reading on Arm 3 drops from forty-eight percent to zero in two seconds. The shuttle's pilot, feeling the release, comes back on the channel.

"Dock control, *Larkspur*. We're free. Clamps released. Confirm we are clear to manoeuvre?"

"*Larkspur*, confirmed. You are clear of Berth 9. Proceed to holding pattern alpha and stand by for hull inspection before onward transit. You may have scoring at the clamp contact points."

"Copy, dock control. Proceeding to holding alpha."

Yuki watches the *Larkspur* pull away from the arm -- slowly, on thrusters, the pilot taking no chances. The shuttle's hull is intact. The forward cabin is intact. One hundred and twelve passengers are sitting in their seats, most of them unaware that anything unusual happened during their departure.

The operations director arrives in dock control fourteen minutes later. He has reviewed the telemetry. He asks Yuki to explain, in order, why she disabled the station's automated structural-protection system without authorisation from the operations office. Yuki walks him through the sequence: the clamp fault, the severance geometry, the hull bisection, the stress margins, the hardware reset. The operations director listens. He makes notes. He tells her the review board will convene within the week and that she should prepare a written account.

He does not tell her she was wrong. He does not tell her she was right. He tells her the severance system exists for a reason and that disabling it was a decision with consequences regardless of outcome.

Yuki returns to her console. The *Larkspur* is in the holding pattern, awaiting hull inspection. Arm 3 is offline, flagged for structural assessment. Her board is quiet. She resets the severance system, re-enables the automated protocol, and logs the reset. The countdown timer returns to standby. She watches it for a long time before she looks away.

---

## Re-arc-Sf2-4

**5 beats, non-linear: E1 (outcome, depicted first) -> E2 (danger present) -> E3 (danger escalation) -> E4 (preparation for intervention) -> E5 (intervention / cost), free indirect style**

**Scenario.** A habitat maintenance engineer on a Jovian-orbit station discovers that the station's radiation shielding has developed a gap during a routine reconfiguration, and a solar-particle event is twelve hours away. The shielded section can hold only three-quarters of the station's population. The engineer must extend the shielding to cover the exposed module before the particle wavefront arrives.

> A = habitat maintenance engineer (Reva Okafor); B = three hundred and twenty residents of Module 7 (the exposed section); T = incoming solar-particle event, wavefront arrival in twelve hours, lethal radiation dose within ninety minutes of exposure for unshielded personnel.

**E1 (outcome -- depicted first).** Module 7's observation gallery, twenty hours after the particle wavefront passed. Reva sits against the bulkhead with her dosimeter clipped to her collar. The reading is elevated -- 340 millisieverts, accumulated over the six hours she spent working in the partially shielded gap between Modules 6 and 7. The station physician has told her this is below the threshold for acute symptoms but above the threshold for long-term risk. She will be monitored. Her lifetime dose record has been updated.

Through the gallery window, the Jovian cloud bands turn in their ancient pattern. The particle event has passed. Module 7's three hundred and twenty residents are in their quarters, behind shielding that was not there twenty-four hours ago. None of them received a measurable dose. The shielding extension -- twelve panels of borated polyethylene, bolted to a frame that Reva fabricated from cargo-rack components -- is visible from the gallery as a rough addition to the station's exterior, ugly against the station's machined hull. It will be replaced with a proper installation during the next maintenance window. For now, it holds.

Reva looks at her dosimeter and thinks about the number. Then she closes her eyes and listens to the station's hum -- the life-support fans, the coolant pumps, the three hundred and twenty people breathing on the other side of the bulkhead.

**E2 (danger present scene).** The maintenance office, Module 4, twenty-two hours earlier. Reva had been reviewing the shielding-reconfiguration log from the previous week's maintenance cycle when she found the discrepancy. During the reconfiguration, a section of the station's magnetic shielding array had been repositioned to accommodate a new antenna mount on Module 5. The repositioning was logged, approved, and completed. But the coverage map generated after the reconfiguration showed a gap -- a cone-shaped region of reduced shielding effectiveness that extended from the array's new position to the hull of Module 7.

The gap was small in angular terms. In practical terms, it left the entirety of Module 7's residential section -- three hundred and twenty people, their quarters, the school, the medical annex -- with shielding rated at twelve percent of the station's standard. Twelve percent was adequate for normal background radiation. It was not adequate for a solar-particle event.

Reva checked the solar-weather bulletin from the deep-space monitoring network. A coronal mass ejection had been detected nine hours ago, originating from a sunspot cluster on the solar limb. The projected particle wavefront would reach Jovian orbit in approximately twelve hours. The bulletin rated the event as severe.

**E3 (danger escalation scene).** The station commander's office, Module 1, one hour later. Reva presented the shielding gap and the solar-weather bulletin. Commander Vasquez understood the problem immediately. She asked how many people Module 7 housed. Reva said three hundred and twenty. Vasquez asked whether they could be relocated to the shielded modules.

Reva had already run the numbers. The shielded modules -- 1 through 6 -- had a combined emergency capacity of nine hundred. The station's total population was twelve hundred. Modules 1 through 6 were already housing eight hundred and eighty people under normal allocation. Three hundred and twenty additional residents could be accommodated physically, but the life-support load -- oxygen generation, CO2 scrubbing, thermal regulation -- would exceed the rated capacity of Modules 1 through 6 within eight hours. The particle event was projected to last fourteen hours. The last six hours would see degrading air quality, rising temperatures, and CO2 levels approaching the threshold for cognitive impairment.

Vasquez asked about the alternative. Reva said the alternative was to extend the shielding to cover Module 7. The station carried spare shielding panels in cargo storage -- borated polyethylene sheets intended for the next scheduled maintenance. The panels existed. The question was whether they could be installed in twelve hours.

Vasquez asked whether Reva could do it. Reva said she could, but not from inside the station. The panels needed to be mounted on the exterior hull, in the gap between the magnetic array's coverage zone and Module 7. That meant an EVA in a maintenance suit, working on the hull, with the particle wavefront twelve hours away and closing.

**E4 (preparation for intervention scene).** Cargo storage, Module 3, and the EVA prep bay, Module 2. Reva and two maintenance technicians spent three hours preparing. They pulled twelve shielding panels from cargo storage -- each one a two-metre square of borated polyethylene, thirty kilograms, awkward to handle in zero gravity. They fabricated a mounting frame from cargo-rack components, using the machine shop's cutting and welding tools to build a structure that could be bolted to the station's exterior hull using the existing attachment points for the antenna mounts.

Reva calculated the geometry. The gap was cone-shaped, widening from the array to the hull. Twelve panels, arranged in an overlapping pattern on the frame, would close the gap to an acceptable level -- not full standard shielding, but enough to reduce the radiation dose in Module 7 from lethal to negligible during the event.

The EVA would be the problem. The mounting points were on the hull between Modules 6 and 7, in a section with no lighting and no handholds. She would be working in a maintenance suit -- not a full EVA suit but a lighter rig designed for hull inspections, with six hours of life support and limited radiation protection. The suit's own shielding was rated for normal background, not for particle events. If the wavefront arrived early, or if the installation took longer than estimated, she would be exposed.

She suited up at hour eight of the twelve-hour window. Four hours to install.

**E5 (intervention / cost scene).** The station's exterior hull, between Modules 6 and 7. Reva works in the dark, by helmet lamp, with the frame tethered to the hull and the panels stacked on a cargo sled beside her. Jupiter fills the sky to her left, banded and enormous, casting enough reflected sunlight to see the hull's surface but not enough to work by.

She bolts the frame to the first mounting point. The bolts are designed for gloved hands, but the maintenance suit's gloves are thicker than workshop gloves, and the bolt heads are small. Each bolt takes twice as long as it would inside. She finishes the first mounting point and moves to the second. The sled follows on its tether, bumping against the hull.

By the third hour, she has the frame in place and six of the twelve panels mounted. The work has a rhythm now -- position the panel, align the bolt holes, drive the bolts, check the overlap with the adjacent panel. The temperature inside her suit is rising. The suit's cooling system is working, but the exertion is generating more heat than the system can remove.

At hour three and a half, the solar-weather bulletin updates on her helmet display. The wavefront is accelerating. Revised arrival: nine hours from original detection, not twelve. She has been outside for three and a half hours. The revised arrival is thirty minutes away.

She does not go inside. She mounts the seventh panel. The eighth. The ninth. Her dosimeter begins to tick -- not from the wavefront, which has not arrived, but from the increased pre-event particle flux that precedes a major event, the radiation equivalent of wind before a storm.

The tenth panel. The eleventh. The dosimeter is climbing. She can feel the fatigue in her arms and the heat in her suit and the particular lightheadedness that might be exertion or might be the early edge of radiation exposure.

The twelfth panel goes on crooked. She adjusts it, drives the last two bolts, and checks the overlap. The gap is closed. The shielding is not elegant -- the panels are uneven, the frame is improvised, the bolts are torqued by feel rather than by spec. But the coverage map on her helmet display updates: Module 7's shielding rating climbs from twelve percent to eighty-one percent.

She triggers the cargo sled's return to the airlock, clips her tether to the guide rail, and pulls herself along the hull toward the EVA hatch. She is inside and through the decontamination lock when the wavefront arrives. She feels nothing. The instruments in the maintenance office, which she checks twenty minutes later, show the particle flux spiking to levels that would have delivered a lethal dose in ninety minutes to anyone on the unshielded hull.

She was inside with eleven minutes to spare. Her dosimeter reads 340 millisieverts. She files the installation report, removes her suit, and walks to the medical annex for assessment. The station physician looks at the dosimeter, looks at her, and tells her to sit down.

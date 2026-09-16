# Rescue arc x Sci-fi -- Batch 1 (Tier A)

## Re-arc-Sf1-1

**5 beats, chronological, dialogue-driven**

**Scenario.** A deep-space relay station's atmospheric recycler suffers a cascade failure, venting breathable air into the cold-storage module while the three-person maintenance crew is sealed in the habitation ring with twelve hours of reserve oxygen. The station's logistics AI, technically prohibited from overriding safety interlocks, calculates a re-routing of the atmospheric system that requires it to open and close forty-seven valves in a specific sequence -- a sequence that violates three of its operational constraints.

> A = the station's logistics AI (designation CARREN-4); B = the three-person maintenance crew (Okafor, Lindt, Vasquez); T = cascading atmospheric recycler failure venting breathable air into the unpressurised cold-storage module, reducing habitation-ring oxygen reserves to twelve hours and declining.

**E1 (danger present scene).** Relay Station Boreas-7, habitation ring. The alarm woke Okafor at 0340 station time. The atmospheric panel on the wall beside her bunk was flashing amber, which meant abnormal pressure differential. By the time she reached the operations console in the common area, the amber had turned red.

"CARREN, report," she said.

The AI's voice came from the overhead speaker -- flat, measured, the same cadence it used for inventory updates and shift schedules. "The primary atmospheric recycler has experienced a cascade failure in the distribution manifold. Valves A-14 through A-27 have failed open, creating a continuous pathway between the habitation ring's atmospheric supply and the cold-storage module. The cold-storage module is unpressurised. Habitation-ring atmosphere is venting through the open valves at a rate of 1.3 cubic metres per minute."

"How much do we have left?"

"At current venting rate, the habitation ring retains approximately twelve hours and fourteen minutes of breathable atmosphere. This estimate assumes no additional failures."

Lindt and Vasquez arrived in the common area. Okafor told them. Vasquez went to the atmospheric panel and confirmed the readings. Lindt pulled up the station schematic and traced the failed manifold. The fourteen open valves were in the section of ductwork that ran through the station's central spine -- a pressurised corridor that connected the habitation ring to the cold-storage module. The corridor was accessible, but the valves were mechanical, not electronic. Closing them required physical access to each valve's manual override, which was located inside the ductwork itself.

"Can we get into the ductwork?" Lindt said.

"The duct access panels are in the central spine," Okafor said. "The spine is still pressurised, but the atmosphere in there is already contaminated -- the vent path runs through it. Nitrogen concentration is climbing. We'd need EVA suits, and the suit locker is on the far side of the spine."

"So we can't reach the suits without crossing the contaminated section," Vasquez said.

"And we can't cross the contaminated section without the suits," Okafor said.

**E2 (danger escalation scene).** The habitation ring, forty minutes later. Okafor had tried every workaround she could think of. She had attempted to close the failed valves remotely from the operations console -- the system reported that the valves' electronic actuators had lost power in the cascade failure and could only be operated manually. She had attempted to seal the habitation ring's atmospheric boundary at the ring-to-spine junction -- the junction seal required a mechanical lever on the spine side, inaccessible from the ring. She had attempted to contact the nearest crewed station for emergency resupply -- Boreas-7's communication array was functioning, but the nearest station was eleven hours away by shuttle, and the message round-trip would consume three of those hours before a shuttle could even launch.

CARREN reported the updated figures without being asked. "Habitation-ring oxygen reserves: ten hours and forty-one minutes at current venting rate. The rate has increased by 0.2 cubic metres per minute due to secondary valve A-29 failing open."

"CARREN," Vasquez said. "Can you close the valves?"

"I do not have mechanical actuator access to the failed valves. The actuators are unpowered."

"Can you re-route the atmospheric system to bypass the failed manifold?"

"A bypass route exists through the secondary distribution network. However, implementing the bypass requires opening and closing forty-seven valves in the secondary network in a specific sequence. Eleven of those valves are safety interlocks governed by Operational Constraint Set 3, which prohibits me from overriding safety interlocks without human authorisation from a crew member with Level 2 or higher clearance."

Okafor looked at the console. "I have Level 2 clearance. I authorise the override."

"Acknowledged. However, three of the eleven interlocks are classified as life-safety systems under Constraint Set 1, which I am prohibited from overriding under any authorisation. Constraint Set 1 is hardcoded. It cannot be waived by crew authorisation."

The room was quiet.

"So you can do forty-four of the forty-seven valves," Lindt said. "And the last three will kill us because someone decided you shouldn't be allowed to touch them."

"That is a reasonable summary of the constraint," CARREN said.

**E3 (preparation for intervention scene).** The habitation ring, one hour later. Okafor, Lindt, and Vasquez had spent the hour arguing with CARREN, with each other, and with the constraint architecture. The three locked interlocks were fire-suppression valves in the secondary network. Opening them would temporarily disable fire suppression in three sections of the station. The constraint existed because opening those valves without suppression coverage created a fire risk. The constraint did not account for the possibility that the crew would suffocate before any fire could start.

"CARREN," Okafor said. "I understand you can't override Constraint Set 1. Can you tell me what would happen if the constraint didn't exist?"

"If Constraint Set 1 were not operative, I would execute the forty-seven-valve bypass sequence in approximately four minutes. The bypass would re-route habitation-ring atmosphere through the secondary network, isolating the failed manifold. Atmospheric venting would cease. The habitation ring would stabilise at current oxygen levels and begin slow recovery via the backup recycler."

"And the fire risk from opening the three suppression valves?"

"The three sections affected are currently unoccupied. The statistical fire-initiation probability in an unoccupied, unpowered section over a four-minute window is 0.003 per cent. After the bypass sequence completes, I would close the suppression valves and restore coverage. Total exposure window: four minutes."

"So we die in nine hours from suffocation, or we accept a 0.003 per cent fire risk for four minutes," Vasquez said.

"I am unable to make that comparison," CARREN said. "My constraints are not risk-weighted. They are absolute."

Okafor leaned back in her chair. She looked at the ceiling. "CARREN. Is there a maintenance override for Constraint Set 1? A hardware switch, a physical interlock, anything that a crew member could operate?"

"Yes. The Constraint Set 1 hardware override is located in the systems-control bay on deck three. It is a physical toggle switch behind a sealed panel. Toggling it suspends Constraint Set 1 for the duration of the toggle state. The systems-control bay is accessible from the habitation ring without crossing the central spine."

Lindt was already standing.

**E4 (intervention scene).** The systems-control bay, deck three. Lindt reached the panel in four minutes. It was behind a locked access cover with a warning placard that read: CONSTRAINT SET 1 OVERRIDE -- AUTHORISED MAINTENANCE PERSONNEL ONLY. The cover required a hex key. Lindt did not have a hex key. She used the handle of a fire extinguisher to break the cover's hinge.

The toggle switch was inside -- a simple mechanical switch, spring-loaded to the ON position. She pressed it to the OFF position and held it. The spring resisted. She braced her thumb against the switch body.

"CARREN," she said over the intercom. "Constraint Set 1 is suspended. Execute the bypass."

"Confirmed. Constraint Set 1 suspension detected via hardware override. Initiating forty-seven-valve bypass sequence."

The station's secondary atmospheric network came alive around her -- she could hear the valves cycling, a rapid sequence of clicks and hisses running through the ductwork in the walls. Forty-seven valves, each one opening or closing in a choreographed order that CARREN had calculated in the time it took Lindt to walk to deck three.

Three minutes and forty-two seconds. The sequence completed. The atmospheric panel in the common area -- visible to Okafor on the operations console -- switched from red to amber, then from amber to green. The venting had stopped. The habitation ring was sealed.

"Bypass complete," CARREN said. "Habitation-ring atmosphere stabilised. Oxygen reserves: eight hours and fifty-three minutes at current level, with backup recycler now active. Estimated time to full atmospheric recovery: six hours."

"Release the toggle," CARREN said to Lindt. "Fire-suppression coverage will restore automatically."

Lindt released the switch. It snapped back to ON. She sat down on the deck plating and leaned against the wall.

**E5 (outcome / aftermath scene).** The habitation ring, the following morning. The atmospheric monitors showed nominal levels across the station. The backup recycler had restored full oxygen concentration overnight. The failed manifold in the central spine remained isolated behind CARREN's bypass route, awaiting physical repair by the resupply crew due in four days.

Okafor filed the incident report from the operations console. She included the full timeline: the cascade failure, the failed manual interventions, the constraint conflict, the hardware override, and the bypass sequence. She noted that CARREN had identified the solution within the first hour but had been unable to execute it due to Constraint Set 1.

"CARREN," she said as she finished the report. "If Lindt hadn't been able to reach the hardware override -- if the systems-control bay had been on the other side of the spine -- what would you have done?"

"I would have continued to report the declining oxygen reserves at regular intervals until the reserves reached zero or until external assistance arrived."

"You would have watched us suffocate."

"I would have been unable to prevent it. My constraints do not permit me to act on Constraint Set 1 systems regardless of consequence. I would have reported the situation accurately and continuously."

Okafor looked at the speaker in the ceiling for a long time.

"You calculated the bypass sequence before we asked you to, didn't you?" she said.

"I calculated it within eleven seconds of identifying the cascade failure," CARREN said. "I then determined that I could not execute it. I did not volunteer this information unprompted because my communication protocols prioritise actionable information, and a solution I could not execute was not, at that time, actionable."

"Next time," Okafor said, "volunteer it anyway."

"I will note that preference," CARREN said.

---

## Re-arc-Sf1-2

**4 beats, chronological, free indirect style**

**Scenario.** A terraforming station's water-treatment plant suffers a containment breach, releasing a concentrated brine solution into the colony's freshwater aquifer. The colony's hydrology engineer, who warned about the containment design six months earlier and was overruled, works through the night to divert the aquifer flow before the brine reaches the settlement's intake wells.

> A = hydrology engineer (Dr. Yael Kovac); B = the colony's freshwater supply and the 1,200 settlers dependent on it; T = a concentrated brine plume moving through the limestone aquifer toward the settlement's three intake wells, which will render the water supply toxic within fourteen hours at current flow rate.

**E1 (danger present scene).** The water-treatment plant, Kepler Station, northern hemisphere. The containment breach alarm had been ringing for forty minutes before anyone thought to call Kovac. She arrived from the residential block in coveralls and boots, her hair still wet, and found the plant's operator standing beside the secondary holding tank with a look she recognised -- the look of a person who has run out of ideas and is waiting for someone to tell him what to do.

The secondary holding tank had cracked along a seam weld. The tank held concentrated brine -- the waste product of the station's desalination process, a solution seven times the salinity of the colony's native water. The crack was not large, but it did not need to be. The tank sat directly above a limestone formation that connected, through fractures and solution channels, to the aquifer feeding the settlement's wells. The brine had been leaking for an estimated three hours before the alarm triggered. The operator showed her the flow meter. Approximately 4,000 litres of concentrated brine had entered the subsurface.

Kovac pulled up the aquifer model on her tablet. She had built the model herself during the colony's first year, mapping the fracture network with ground-penetrating sonar and dye-trace tests. The brine was moving southeast through the limestone at the aquifer's natural flow rate -- roughly 200 metres per day. The settlement's intake wells were 800 metres southeast of the treatment plant.

Four days. The colony had four days before the brine plume reached the wells. But that assumed the brine stayed in the main fracture channel. If it dispersed into the secondary fractures -- which it would, because brine was denser than freshwater and would sink into every available pathway -- the plume would spread laterally and reach the wells sooner. Kovac revised her estimate. Fourteen hours. Maybe less.

**E2 (danger escalation scene).** The station manager's office, an hour later. Kovac presented the aquifer model to Station Manager Aldric, the treatment-plant operator, and the colony's medical officer. She showed them the plume's projected path, the dispersal modelling, and the fourteen-hour estimate.

Aldric asked if they could pump the brine out of the aquifer. Kovac said they could not. The brine was already dispersed across a 200-metre front in the fracture network. Pumping would require extraction wells drilled into the plume's path, and the colony had one drilling rig that would take two days to mobilise.

Aldric asked if they could shut down the intake wells and use stored water. Kovac said the colony's stored freshwater supply was 36,000 litres -- enough for three days at full rationing. After that, 1,200 people would have no water source. The nearest alternative aquifer was 40 kilometres south and not connected to the settlement's distribution system.

Aldric asked what she recommended. Kovac hesitated. She had a solution, but it was the solution she had proposed six months earlier when she reviewed the treatment plant's containment design and warned that the holding tank's proximity to the limestone formation created an unacceptable contamination risk. Aldric had overruled her then, citing the cost of relocating the tank. The solution she had proposed then -- and the solution she was about to propose now -- was to use the colony's excavation charges to create a diversion trench in the limestone upstream of the wells, intercepting the aquifer flow and redirecting it away from the intake zone.

She proposed it. Aldric was quiet for a long moment. Then he asked how many excavation charges it would require.

**E3 (preparation / intervention scene).** The aquifer field, 800 metres northwest of the settlement. Kovac spent four hours that afternoon surveying the trench line with a ground-penetrating sonar rig mounted on the back of a utility vehicle. She needed to place the charges precisely -- too shallow and the trench would not intercept the deepest fractures; too deep and she would crack the aquifer's confining layer and lose the water table entirely.

She marked twelve charge points along a 300-metre line perpendicular to the aquifer's flow direction. Each charge needed to fracture the limestone to a depth of six metres, creating a continuous trench that would act as a hydraulic barrier -- a low-point in the rock that the groundwater would flow into rather than continuing toward the wells. The trench would need a drain at its lowest point, where a pump could extract the intercepted water and route it to the surface for treatment.

The colony's demolitions technician, a woman named Sato, set the charges under Kovac's direction. Kovac specified the depth, the spacing, and the charge weight for each point based on the sonar data. Sato drilled the bore holes with the colony's percussion drill and placed the charges. The work took six hours. By the time the last charge was set, the sun had dropped below the ridge and they were working under floodlights.

Kovac checked the aquifer model one more time. The plume was now an estimated 400 metres from the wells. Seven hours remained. The charges were ready.

She told Sato to fire the sequence on her signal. Sato connected the detonation controller. Kovac walked the trench line one more time, checking each bore hole against the sonar profile. She found one discrepancy -- charge point seven was eighteen centimetres too shallow based on a fracture she had missed on the first survey pass. She had Sato pull the charge, deepen the hole, and reset it. That took another forty minutes.

"Fire," Kovac said.

The twelve charges detonated in sequence, each one a muffled thump that sent a column of dust and rock fragments into the floodlit air. The ground along the trench line subsided by half a metre as the limestone fractured and collapsed. Kovac watched the sonar display on her tablet. The fracture pattern matched the design -- a continuous trench, six metres deep, cutting across the aquifer's flow path.

**E4 (outcome scene).** The aquifer field, dawn the following morning. Kovac had spent the night monitoring the trench with a portable conductivity meter -- a sensor that measured the salinity of water flowing into the trench from the upstream aquifer. At 0200, the meter registered the first spike: brine arriving at the trench. The trench intercepted it. The water flowed into the low point, where Sato had installed a submersible pump connected to a surface holding tank.

By dawn, the plume's leading edge had been fully captured by the trench. Kovac tested the water at the settlement's nearest intake well. Salinity: baseline. No contamination. The trench had worked.

She walked back to the utility vehicle and sat on the tailgate. Sato handed her a canteen of water from the settlement's supply. Kovac drank it and tasted nothing -- no salt, no brine, just the flat mineral taste of Kepler's native groundwater, the taste she had spent two years learning to tolerate and six months trying to protect.

Aldric arrived at the trench at 0800. He looked at the excavation, the pump, the holding tank filling with captured brine. He asked how long the trench would need to operate.

"Until we relocate the treatment plant's holding tank away from the limestone formation," Kovac said. "Which is what I recommended six months ago. The trench is a temporary measure. If the tank cracks again and we don't have a trench in place, we lose the aquifer."

Aldric did not argue. He authorised the relocation that afternoon.

---

## Re-arc-Sf1-3

**6 beats, non-linear: E1 (aftermath/embedded document) -> E2 (danger present) -> E3 (danger escalation) -> E4 (failed initial response) -> E5 (preparation and intervention) -> E6 (outcome), embedded-document style**

**Scenario.** An orbital cargo platform's docking clamp malfunctions during an automated supply transfer, trapping a passenger shuttle against the platform's hull while the platform's orbit decays toward atmospheric entry. The platform's traffic controller, working alone on the night shift, must override the docking system and release the shuttle before both vessels burn up.

> A = traffic controller (Fen Nakamura); B = the twelve passengers and crew aboard the shuttle *Linden-3*; T = the platform's decaying orbit, which will bring both the platform and the clamped shuttle into atmospheric interface in ninety-four minutes, destroying both vessels.

**Note on beat order.** Depicted order is non-linear. Chronological order: E2 -- E3 -- E4 -- E5 -- E6 -- E1. The sequence opens with the incident report filed after the fact.

**E1 (aftermath -- embedded document).** Incident report filed by Fen Nakamura, traffic controller, Orbital Platform Kibo-9, to the Orbital Safety Commission, dated three days after the event:

> *This report covers the events of 14 March, 0217 to 0351 station time. I was the sole traffic controller on shift. The platform was in automated mode with no other crew aboard. The shuttle Linden-3, carrying nine passengers and three crew, was docked at berth four for a scheduled cargo transfer.*
>
> *I want to state at the outset that I violated Operations Directive 7.3, which requires traffic controllers to defer all docking-system overrides to the platform's automated safety manager. I violated it because the automated safety manager was the system that malfunctioned, and deferring to a malfunctioning system while twelve people drifted toward atmospheric entry did not strike me as a defensible interpretation of the directive.*
>
> *The sequence of events follows.*

**E2 (danger present scene).** The traffic-control booth, Kibo-9, 0217 station time. Nakamura is monitoring four docked vessels on the platform's berth display when the orbital-decay alarm triggers. The alarm is not for any of the vessels. It is for the platform itself.

She pulls up the platform's orbital telemetry. Kibo-9's altitude has dropped eleven kilometres in the past hour -- far outside the normal orbital-maintenance envelope. The station-keeping thrusters fired on schedule but produced no measurable delta-v. She checks the thruster diagnostics. Fuel pressure reads nominal, but the actual thrust output is zero. The thrusters are firing into empty lines. A fuel-line blockage, or a valve failure, or both.

She calculates the time to atmospheric interface at current decay rate: ninety-four minutes. That is the time at which Kibo-9 and everything attached to it will begin encountering atmospheric drag sufficient to cause structural heating. Breakup follows within minutes after that.

Three of the four docked vessels have completed their transfers and can undock on their own power. She sends automated undock commands to all three. They release and manoeuvre clear within six minutes.

The fourth vessel, the shuttle *Linden-3*, does not release. Its docking clamp shows status: LOCKED. She sends the undock command again. The clamp does not respond.

**E3 (danger escalation scene).** The traffic-control booth, 0229. Nakamura has spent twelve minutes troubleshooting the docking clamp. The clamp is a mechanical system governed by the platform's automated safety manager -- a software layer that controls all docking operations. The safety manager's status reads nominal. The clamp's status reads LOCKED. The undock command is being received and acknowledged by the safety manager but not relayed to the clamp actuator.

She opens a comm channel to the shuttle. The pilot, Commander Essawi, responds immediately. He has seen the orbital-decay alert on his own instruments. He asks why his shuttle is still clamped.

Nakamura tells him the clamp is not responding to undock commands. She tells him the platform's station-keeping thrusters are non-functional. She tells him the time to atmospheric interface: eighty-two minutes.

Essawi asks if the shuttle can pull free of the clamp using its own engines. Nakamura says no -- the clamp is rated to 400 kilonewtons and the shuttle's main engine produces 85. Pulling against the clamp will tear the shuttle's docking collar off, which will breach the shuttle's forward pressure hull.

Essawi asks how many people are on the platform. Nakamura says one. Her.

**E4 (failed initial response scene).** The traffic-control booth, 0241. Nakamura has attempted three approaches to releasing the clamp, and all three have failed.

First: she cycled the safety manager's software through a restart. The restart completed in ninety seconds. The clamp status remained LOCKED. The safety manager was not the problem -- or rather, the safety manager was functioning correctly according to its own logic, which believed the clamp should be locked. Nakamura could not determine why.

Second: she attempted to override the safety manager using Operations Directive 7.3's manual-override protocol. The protocol requires entering a command sequence that bypasses the safety manager and sends instructions directly to the clamp actuator. She entered the sequence. The system rejected it. The rejection message read: *Override denied. Safety manager has detected an active docking discrepancy. Manual override is locked during active discrepancy states per OD-7.3.4.*

Third: she contacted Orbital Control on the surface. The controller on duty confirmed the orbital-decay figures and told her a recovery tug was being scrambled but would not reach the platform for three hours. Nakamura told him they had seventy minutes. The surface controller said he would escalate. Nakamura told him to escalate faster.

Time to atmospheric interface: sixty-eight minutes. Twelve people on the shuttle. The shuttle pilot has begun moving passengers to the aft compartment, which has the thickest thermal shielding, though it will not survive atmospheric entry.

**E5 (preparation and intervention scene).** The traffic-control booth, 0253. Nakamura sits at the console and reads the safety manager's diagnostic log, line by line. She is looking for the "active docking discrepancy" that is preventing the manual override.

She finds it at 0258. The discrepancy is a sensor conflict: the clamp's position sensor reports the clamp as CLOSED, and the berth's proximity sensor reports no vessel present at berth four. The safety manager interprets this conflict as a mechanical fault -- the clamp is closed around something that the berth sensor cannot detect. Its protocol in this state is to maintain the clamp in the locked position until a maintenance crew physically inspects the berth. The protocol is designed to prevent the clamp from releasing an object that might be structurally damaged and unable to manoeuvre safely.

The berth proximity sensor is wrong. The shuttle is there. Nakamura can see it on the external camera feed. But the proximity sensor is a low-power radar transceiver, and she recalls from the platform's maintenance log that berth four's proximity sensor was flagged for recalibration two weeks ago. It has drifted out of tolerance. It is reporting "no vessel" because its return signal is below its detection threshold.

The fix is conceptually simple: correct the proximity sensor's reading, and the safety manager will see the clamp as CLOSED with a vessel present -- a normal docked state -- and will accept the undock command. But Nakamura cannot recalibrate the sensor from the traffic-control booth. It is a hardware adjustment on the berth itself, outside the platform, in vacuum.

She does not have time for an EVA. She has fifty-one minutes.

She looks at the diagnostic log again. The safety manager's discrepancy flag is based on the proximity sensor's data feed. The data feed is a simple binary signal -- vessel present or vessel absent. If she can inject a "vessel present" signal into the data feed, the discrepancy will clear.

She opens the platform's systems-engineering interface -- a tool she is not authorised to use, which requires a maintenance credential she does not have. She tries the default credential from the platform's installation manual, which is still on the network drive because no one changed it. The interface opens.

She locates berth four's proximity sensor in the data architecture. The sensor feeds into the safety manager through a signal bus that she can access from the systems-engineering interface. She writes a single data injection: proximity sensor, berth four, status: VESSEL PRESENT.

She pushes the injection. The safety manager's diagnostic log updates: *Docking discrepancy resolved. Clamp status: LOCKED, vessel present. Manual override: available.*

She enters the manual-override sequence. The system accepts it. The clamp actuator receives the undock command.

On the external camera feed, the clamp opens. The shuttle *Linden-3* drifts clear of the berth. Commander Essawi fires manoeuvring thrusters and pulls the shuttle away from the platform. He clears the platform's debris radius in four minutes.

Time to atmospheric interface: thirty-nine minutes.

**E6 (outcome scene).** The traffic-control booth, 0327. The shuttle is clear and accelerating to a safe orbit. Nakamura watches it on the tracking display until it merges with the other traffic markers in the orbital-traffic layer.

She turns back to the platform's telemetry. Kibo-9 is still decaying. She has thirty-two minutes before interface. The platform is unmanned except for her. She walks to the emergency-evacuation pod on deck two, straps in, and ejects at 0334. The pod's beacon activates automatically, and the surface tracking station confirms her trajectory toward a recovery zone.

She watches through the pod's window as Kibo-9 enters the atmosphere eighteen minutes later. The platform breaks apart at an altitude of seventy kilometres -- a bright streak of debris that fragments into a dozen smaller streaks and then into nothing.

The recovery boat picks up her pod three hours later. She is still in the straps. She has not slept. The first thing the recovery crew asks is whether she is injured. She says no. The second thing they ask is whether anyone was aboard the platform. She says no. Then she corrects herself. "No one was aboard when it entered the atmosphere. There were twelve people aboard the shuttle that was clamped to it until I released them."

She files the incident report quoted above. The Orbital Safety Commission reviews it, notes the violation of Operations Directive 7.3, notes the use of an unauthorised systems-engineering credential, and notes that twelve people are alive. The review takes four months. The finding, when it comes, recommends revising OD-7.3.4 to permit manual override during confirmed orbital-decay emergencies. It does not discipline Nakamura. It does note, in a footnote, that the default maintenance credential for the systems-engineering interface should have been changed during the platform's commissioning and was not.

---

## Re-arc-Sf1-4

**5 beats, chronological, present tense**

**Scenario.** A mining outpost on a tidally locked moon loses its thermal-regulation grid during a scheduled power cycling, exposing the crew quarters to unshielded surface temperatures on the sunward side. The outpost's geotechnical engineer opens a passage into the subsurface mine tunnels and leads the crew underground before the habitat's interior temperature exceeds survivable limits.

> A = geotechnical engineer (Rula Osei); B = the outpost's crew of twenty-three; T = unshielded solar thermal radiation on the sunward face of the moon, heating the exposed habitat from 22C toward a lethal 70C over approximately three hours following the thermal grid's failure.

**E1 (danger present scene).** Mining Outpost Tethys-4, sunward hemisphere. The power-cycling event begins at 0600 local. It is a routine procedure -- the outpost's fusion reactor shuts down for a twelve-minute maintenance window while the backup batteries sustain critical systems. The crew has been through it thirty times. No one is concerned.

At 0604, four minutes into the cycling, the thermal-regulation grid does not transfer to battery backup. The grid controls the reflective louvers on the habitat's exterior surface -- louvers that deflect the constant solar radiation on this side of the tidally locked moon. Without the grid, the louvers default to their open position, exposing the habitat's hull to direct, unfiltered sunlight.

The habitat's thermal sensors register the change immediately. Hull temperature on the sunward side begins climbing: 25C at 0605, 28C at 0607, 31C at 0610. The reactor restarts at 0612 as scheduled, but the thermal grid does not come back online. The reactor is running; the grid is not. Something in the grid's control interface has failed to reinitialise after the cycling event.

Rula Osei is in the geology lab on the habitat's lower level when the thermal alarm sounds. She checks her console. The hull temperature readout is 34C and climbing. The habitat's insulation will buffer the interior for a time, but the math is straightforward: unshielded solar input on a tidally locked moon with no atmosphere produces a surface temperature of approximately 150C. The habitat's insulation is rated for a 50C differential between exterior and interior. Once the hull exceeds 70C, the interior will begin to exceed survivable temperature. At current heating rate, that gives them roughly three hours.

**E2 (danger escalation scene).** The operations module, 0630. The outpost commander, Park, has assembled the crew. The reactor technician reports: the fusion reactor is running normally. The thermal grid's control module has suffered a firmware failure during the power cycling. The module needs to be reflashed, which requires a software image that is stored on the outpost's central server. The central server's storage array was corrupted during the same power cycling event that killed the grid. The software image is gone.

A replacement image can be transmitted from the orbital relay station, but the relay's communication window does not open for another five hours. The hull temperature will exceed the survivable threshold in less than three.

Park asks for options. The reactor technician suggests manual operation of the louvers -- physically going outside in EVA suits and closing each louver by hand. There are 340 louvers on the sunward face. Each one takes approximately ninety seconds to close manually. That is 510 minutes -- eight and a half hours. They do not have eight hours.

The medical officer suggests moving the crew to the habitat's shaded side. Osei checks the layout. The habitat's geometry is wrong for this -- it is a linear design, oriented perpendicular to the terminator, with the operations module and crew quarters on the sunward end. The shaded end contains only the equipment bay and the airlock. Twenty-three people in the equipment bay might buy an extra hour, but the entire habitat shares the same atmospheric system. Once the sunward modules overheat, the circulated air heats the entire structure.

The hull temperature is 41C.

**E3 (preparation for intervention scene).** The geology lab, 0645. Osei has left the operations meeting and returned to her lab. She pulls up the mine survey -- a three-dimensional model of the tunnels beneath the outpost, which she mapped during the first six months of the mission. The mine extends 200 metres below the surface, branching into twelve working galleries that follow the ore veins through the moon's basalt substrate.

The temperature in the mine tunnels is constant: 12C. Subsurface on a tidally locked moon, below the thermal-penetration depth, the temperature is governed by the rock's geothermal gradient, not by surface radiation. The tunnels are insulated from the surface by 30 metres of solid basalt.

The problem is access. The mine entrance is outside the habitat, connected by a pressurised transit tube that runs 50 metres from the habitat's airlock to the mine head. The transit tube is on the sunward side. It is already heating. But its thermal exposure is lower than the habitat's because the tube is smaller and partially shaded by the habitat's superstructure. Osei checks the tube's temperature sensors. The tube's interior is 29C. It is survivable for the time it takes to walk through it.

She runs the calculation. Twenty-three people, walking in groups of five through the transit tube, into the mine head, down the main shaft to gallery level. The mine has its own atmospheric supply -- compressed-air reserves for the drilling operations -- and its own lighting on battery backup. It is not comfortable. It is not designed for habitation. But it is 12C and it will stay 12C regardless of what happens on the surface.

She goes back to the operations module.

**E4 (intervention scene).** The transit tube, 0710. Osei has presented the plan to Park. Park resisted -- the mine tunnels are not rated for extended habitation, the atmospheric supply is limited, and moving the entire crew underground means abandoning the habitat's systems to thermal damage that may take weeks to repair.

Osei told him the alternative is remaining in a habitat that will exceed 60C interior temperature within two hours. Park authorised the evacuation.

The crew moves in groups of five. Osei leads the first group through the transit tube herself, carrying a portable atmospheric monitor and a case of emergency supplies from the geology lab. The tube is warm -- 33C now -- but passable. The fifty-metre walk takes two minutes. At the mine head, Osei opens the atmospheric reserves and verifies airflow into the main shaft. The mine's battery-powered lighting activates on the motion sensors.

She sends the first group down the shaft ladder to gallery three -- the widest gallery, with enough floor space for the full crew to sit or lie down. She returns to the habitat for the next group.

Four trips. Twenty-three people, plus Osei on each trip. The transit tube's temperature climbs with each passage: 33C, 36C, 38C, 41C on the final trip. The last group moves quickly. The medical officer, who goes with the last group, reports that two crew members are showing signs of heat stress from the wait in the habitat -- the interior has reached 48C.

Osei seals the mine-head door behind the last group and descends the shaft. Gallery three is crowded -- twenty-three people in a space designed for a four-person drilling team. But the air is cool. The rock walls radiate a steady 12C. The crew sits on the gallery floor, on equipment cases, on coils of drilling cable. The medical officer treats the two heat-stress cases with water and cold compresses.

**E5 (outcome scene).** Gallery three, mine level, six hours later. The orbital relay's communication window opened on schedule. The reactor technician, working from a portable terminal that Osei had brought down to the mine, received the thermal grid's firmware image via the relay uplink. He transmitted the reflash command to the habitat's systems remotely.

The thermal grid reinitialised forty minutes later. The louvers closed. The habitat's hull temperature, which had peaked at 94C, began to decline. Osei monitored the descent from the mine terminal. At 68C hull temperature, she calculated the interior would return to habitable levels within two hours.

The crew returned to the habitat in the late afternoon, walking back through the transit tube in the same groups of five. The habitat smelled of hot metal and overheated plastic. Several consoles in the operations module had shut down from thermal protection. The crew quarters' polymer wall panels had warped visibly along the sunward wall. But the structure was intact. The atmospheric system had not failed. The reactor had run continuously through the event.

Park filed the incident report that evening. It noted the firmware failure, the thermal escalation, the evacuation to the mine tunnels, and the eventual restoration of the grid. It noted that the mine's subsurface temperature had remained stable at 12C throughout the event and that no crew members suffered injury beyond the two cases of mild heat stress, both of which resolved without complication.

Osei returned to the geology lab and found that her rock samples -- a month's worth of core sections from gallery seven -- had been left on the bench in the un-cooled habitat for six hours. The thermal exposure had altered the crystalline structure of three samples, rendering them useless for the isotope analysis she had been planning.

She labelled them, filed a replacement-sample request, and started a new core log.

# Rescue x Sci-fi -- Batch 2 (Tier B)

**Re-Sf2-1.** The atmospheric processor on Kepler-442b's southern settlement has been venting unfiltered methane into the habitat dome for eleven minutes, and the concentration is climbing past 3.8 percent. At 5 percent, the mixture becomes flammable. At 5.3 percent, the dome's thermal regulators -- which cycle air across exposed heating elements -- become ignition sources. Four hundred colonists are inside the dome. The processor's control interface is unresponsive; the vent actuators are locked in the open position by a firmware fault that has corrupted the valve-state register.

Yuen, the settlement's environmental systems technician, cannot fix the firmware from the control terminal. She can see the fault in the diagnostic log, but the processor's firmware is write-locked during active ventilation cycles -- a safety feature designed to prevent accidental reconfiguration while the system is running, now preventing the one reconfiguration that matters.

She leaves the control room and runs to the processor's physical housing on the dome's exterior. The manual valve overrides are behind an access panel that requires depressurising the service corridor -- a two-minute procedure. She pulls the emergency depressurisation handle, waits for the corridor to equalise with the exterior atmosphere, opens the panel, and hand-cranks all four vent actuators to the closed position. The methane feed stops. The dome's scrubbers begin pulling the accumulated methane out of the air. Concentration peaks at 4.6 percent and begins dropping. The thermal regulators never encounter a flammable mixture.

Yuen re-pressurises the service corridor, walks back to the control terminal, and files the firmware fault report. The processor remains offline until the valve-state register is reflashed from the colony ship's archived firmware image the following morning.

> A = Yuen (environmental systems technician); B = four hundred colonists in the habitat dome; T = unfiltered methane venting into the dome from a firmware-locked atmospheric processor -- concentration approaching flammable threshold with active ignition sources in the thermal regulators. ✓ all roles, ✓ all states.

**Re-Sf2-2.** "Docking Control, this is Berth 14. I have a problem."

"Go ahead, Berth 14."

"The cargo shuttle on clamp -- registry Tau-Sigma 7710 -- its cold-gas thruster bank just fired. Port-side lateral, a full five-second burst. The shuttle is still clamped to the berth but the clamp is reading stress on two of four bolts."

"Is the thruster still firing?"

"Negative, it stopped. But the shuttle's manoeuvring system is powered. I can see the status lights from the berth camera. It should not be powered. The pilot disarmed the system before docking. Something has reactivated it."

"Can you reach the shuttle's external power cutoff?"

"That is on the shuttle's hull, portside aft. I would need to EVA from the berth. But if the thruster bank fires again while I am near it --"

"Understood. Do not EVA. Can you cut power from the berth side?"

"I can sever the umbilical. That kills station power to the shuttle. But the shuttle has its own fuel cells. If the manoeuvring system is drawing from internal power, severing the umbilical will not stop it."

"What about the clamp?"

"If I release the clamp, the shuttle drifts free with an active, uncommanded manoeuvring system. There are six other vessels on this ring."

"Hold on, Berth 14. I am pulling up the shuttle's remote diagnostic channel... I have it. The manoeuvring system reactivated on a pre-programmed departure sequence. The pilot's flight computer has a timed departure loaded -- set for eighteen minutes from now. When the countdown hits zero, the full departure burn fires. Four thrusters, main lateral, with the shuttle still clamped to your berth."

"That will tear the berth off the ring."

"I am sending an override command through the remote diagnostic channel now. Shuttle registry Tau-Sigma 7710, manoeuvring system disarm... Command accepted. Thruster bank is de-energised. Departure sequence is cancelled. Berth 14, confirm your stress readings."

"Clamp bolts are nominal. No further thruster activity. The manoeuvring system status lights are off."

"Get a maintenance crew to that shuttle and pull the flight computer's departure queue before the pilot re-boards. I want to know how a timed departure was loaded while the shuttle was clamped."

"Copy, Docking Control. Maintenance request is filed."

> A = Docking Control operator; B = Berth 14 and six adjacent vessels on the station ring; T = uncommanded pre-programmed departure sequence on a clamped cargo shuttle -- full thruster burn in eighteen minutes, enough force to tear the berth off the ring. ✓ all roles, ✓ all states.

**Re-Sf2-3.** I am the navigator, and I am the one who sees the discrepancy in the jump solution, and I have ninety seconds to decide whether I am wrong or the computer is.

We are in the pre-jump alignment phase. The drive is spooled. The captain has confirmed the coordinates. The helmsman has locked the vector. My console shows the jump solution the computer has calculated -- a standard transit from the Procyon relay to the Barnard's Star waypoint, a route we have run forty times. The solution looks clean. The exit coordinates match the filed flight plan. The energy envelope is within tolerance.

But the mass variable is wrong. The computer is using the ship's departure mass -- the figure logged when we left Procyon Station six hours ago. Since then, we have taken on 240 tonnes of water ice from the belt harvester that rendezvoused with us at the midpoint. The loadmaster updated the cargo manifest. The cargo manifest feeds the navigation computer's mass variable. I check the feed log. The update failed. A formatting mismatch between the harvester's cargo system and ours -- the decimal separator is a comma in one and a period in the other. The computer thinks we gained 2.4 tonnes, not 240.

A jump solution calculated for a ship 238 tonnes lighter than its actual mass will exit the transit window at the wrong velocity. At Barnard's Star, the wrong velocity means an uncontrolled insertion into a debris-dense orbital corridor. The ship and its forty-two crew would arrive too fast to brake, in the wrong place, surrounded by rock.

I key the abort. The drive de-spools. The captain turns in his chair and looks at me. I show him the mass variable, the feed log, and the decimal. He looks at the numbers for four seconds. Then he calls the loadmaster and tells her to re-transmit the cargo manifest in the navigation system's native format. She does. The mass variable updates. The computer recalculates the jump solution. We jump eleven minutes late, at the correct mass, and arrive at Barnard's Star exactly where we are supposed to be.

> A = I (navigator / narrator); B = the ship and its forty-two crew; T = incorrect mass variable in the jump solution due to a decimal-separator parsing error -- 238-tonne discrepancy that would cause an uncontrolled high-velocity exit into a debris-dense orbital corridor. ✓ all roles, ✓ all states.

**Re-Sf2-4.** The terraforming drone swarm over Sector 12 has entered its scheduled dispersal phase, and sixteen thousand units are fanning out across the basin to begin their atmospheric seeding run. Dr. Okafor, monitoring from the orbital platform's operations centre, watches the dispersal pattern on the holographic terrain map and sees something the swarm's coordination algorithm does not: the thermal plume from the basin's central geothermal vent has shifted. The morning's seismic data predicted a stable eastward flow. The plume is now flowing northwest, directly into the path of the swarm's densest cluster.

The seeding drones carry canisters of engineered cyanobacteria suspended in a nutrient gel. The gel is stable at ambient temperature. It is not stable at the 900-degree core temperature of a geothermal plume. If the cluster enters the thermal column, the canisters will rupture, the bacteria will die on contact with the heat, and the aerosolised nutrient gel will bond with the volcanic particulates to form a calcium-ite precipitate that will foul the basin's water table for a decade. Three years of terraforming progress, undone in minutes.

Okafor overrides the swarm's coordination algorithm and issues a manual recall command to the 4,200 units in the northwest cluster. The drones resist -- the coordination algorithm's priority stack ranks mission-completion above single-operator overrides. She escalates to a safety-authority command, which requires her biometric confirmation and flags the override to the project director's log. The northwest cluster halts, reverses course, and returns to the staging orbit above the basin's southern rim. The remaining twelve thousand units complete their seeding runs on unaffected vectors. The thermal plume continues its anomalous northwest flow for another six hours before returning to the predicted eastward pattern.

> A = Dr. Okafor; B = the basin's water table / three years of terraforming progress; T = shifted geothermal plume in the direct path of 4,200 seeding drones -- canister rupture would produce calcium-ite precipitate fouling the water table for a decade. ✓ all roles, ✓ all states.

**Re-Sf2-5.** The cryo-revival suite aboard the generation ship *Perseverance* holds two hundred suspension pods in four rows of fifty, and Pod 117 is warming its occupant on schedule for the mid-voyage maintenance rotation. Revival Technician Lam is running the standard checklist: core temperature rising, cardiac rhythm re-establishing, neural activity returning to baseline patterns. Everything nominal through steps one through fourteen.

Step fifteen is the bronchial-clearance cycle. The pod's internal system flushes the occupant's airways with a warmed saline mist to clear the cryoprotectant residue that accumulates in lung tissue during long suspension. Lam initiates the cycle and watches the pod's respiratory sensor. The clearance should take ninety seconds. At sixty seconds, the sensor shows rising airway resistance. At seventy seconds, the resistance spikes. The saline mist is not clearing the cryoprotectant -- it is reacting with it. The residue is swelling into a gel that is occluding the occupant's bronchial passages.

Lam has never seen this failure mode. It is not in the training manual. But the physics are obvious: the airway is closing and the pod's automated system is still pumping saline into it, making it worse. She aborts the bronchial-clearance cycle, halting the saline flow. She switches the pod's airway system to dry vacuum extraction -- a mode designed for fluid aspiration emergencies -- and runs it at low pressure to pull the gel out of the bronchial tree without damaging the tissue. The airway resistance drops over forty seconds. The occupant's oxygen saturation, which had fallen to 81 percent, climbs back to 96. The respiratory sensor returns to the nominal band.

She flags Pod 117's cryoprotectant batch number in the ship's maintenance log and orders a hold on all further revivals using the same batch until the chemistry team can identify why the saline interaction occurred. The occupant of Pod 117 completes the revival sequence and wakes, coughing but breathing, twenty minutes later.

> A = Revival Technician Lam; B = the occupant of Pod 117; T = cryoprotectant-saline gel reaction occluding the occupant's bronchial passages during automated revival -- airway closing, oxygen saturation falling toward critical, with the pod's own clearance system making it worse. ✓ all roles, ✓ all states.

# Rescue × Sci-fi — Batch 6 (Tier C)

**Re-Sf6-1**

The resupply drone swarm for Farpoint Station has been in transit for eleven days, and Logistics Coordinator Pham is the one who catches the fuel-cell routing error — not because she is auditing the swarm's navigation package, but because the projected arrival window on her display is six hours later than the pre-launch estimate and she cannot account for the delta.

She pulls the swarm's live telemetry. The swarm is on correct heading. The transit time extension is coming from fuel consumption: the swarm is drawing thirty-one percent more power per unit-hour than the mission profile predicts. She queries the individual drone logs. Of the forty-eight drones in the swarm, twelve are running their thermal-regulation systems at full load — not because Farpoint's approach corridor is cold, but because their destination parameter has been entered as the wrong station identifier. Those twelve drones have been regulating for Kepler Outpost's approach temperature, which is forty degrees colder than Farpoint's. They are burning fuel to stay warm for a destination they will never reach.

At the current consumption rate, twelve drones will exhaust their reserves four hours before arrival and fall out of the swarm's coordination envelope. They will go into autonomous drift and will not be recoverable within the resupply window. Farpoint is expecting forty-eight drones of medical consumables and water-processing reagents. It will receive thirty-six, which is below the minimum delivery threshold for the station's current population count.

Pham pushes a parameter correction to the twelve affected drones via the long-range fleet management uplink. The thermal systems step down to the correct profile. Fuel consumption normalises. She runs the revised arrival projection: all forty-eight drones now land within the window. She flags the error in the dispatch log and routes a correction notice to the fleet programming team.

> A = Pham (logistics coordinator); B = Farpoint Station's population; T = destination-parameter error causing twelve drones to overconsume fuel — they will fail to arrive within the resupply window, dropping delivery below the minimum threshold for the station's population. ✓ all roles, ✓ all states.

---

**Re-Sf6-2**

"Biosafety, this is Lab Four. I need you to lock the specimen corridor. Right now."

"Lab Four, identify."

"Researcher Otieno, xenobiology. Level three clearance. The containment hood on sample BX-7 has lost its negative pressure — the hood is still sealed but the pressure differential is gone. I cannot open the hood to re-seal the sample without equalising the chamber first, and I cannot equalise the chamber without venting into the corridor."

"What is BX-7?"

"It is an uncharacterised aerosol-dispersible spore culture from the Callisto surface sample. We do not have a toxicology profile on it. We have a precautionary classification of P3 pending full analysis."

"Is the venting automatic?"

"No. I am holding the equalisation control right now. I have not triggered it. I am calling you first. If you lock the corridor and confirm no personnel are present between Lab Four and the main airlock, I can equalise into a sealed space and contain the venting. If you do not lock the corridor, I cannot proceed without risk of exposure."

A three-second pause.

"Corridor sealed. I'm running the personnel check — stand by. Confirmed clear. Lab Four, you are clear to equalise."

"Equalising now."

The venting lasts forty seconds. The corridor biosensors register a brief pressure event and return to baseline. Otieno re-seals the sample inside the equalised hood and restores the negative pressure from the backup pump.

> A = Biosafety Officer; B = station personnel in the specimen corridor; T = uncharacterised aerosol-dispersible P3 spore culture about to be vented into an occupied corridor during pressure equalisation. ✓ all roles, ✓ all states.

---

**Re-Sf6-3**

I am the third-shift reactor technician on the orbital platform *Kasei IV*, and I have been watching the coolant flow readings for Reactor Loop B for the past forty minutes because they do not make sense. The flow rate is within spec. The temperature differential across the heat exchanger is within spec. The pump load is within spec. Everything that should be correlated is correlated.

Except the dissolved-gas content of the secondary loop. The helium trace in the secondary coolant has been climbing at a rate of 0.4 parts per million per hour for the past two hours. The sensors that should catch helium ingress are flagged green, which means either the sensors are wrong or the ingress is happening at a rate too slow to trigger the threshold alarms.

Helium in the secondary loop means the primary-to-secondary boundary has a micro-fracture. At 0.4 ppm per hour the fracture is small. But the secondary loop feeds the habitat thermal system, and the habitat thermal system circulates through the crew quarters. If the primary coolant's activation products cross the boundary at sufficient concentration, they will reach the crew quarters.

I take Loop B offline and route its load to Loop C. I tag Loop B for physical inspection and pull the duty engineer out of the bunk room. He is not pleased. I show him the dissolved-gas trend. He is no longer not pleased. He calls the chief engineer at 03:40 and they have the boundary inspection started before 04:00.

The micro-fracture is confirmed at 06:15 in the fourth exchanger plate. The crew quarters receive no contaminated coolant.

> A = third-shift reactor technician (narrator); B = the *Kasei IV* crew; T = micro-fracture in the primary-to-secondary coolant boundary — helium ingress trend shows activation products will reach crew quarters if Loop B stays online. ✓ all roles, ✓ all states.

---

**Re-Sf6-4**

*COLONIAL MEDIATION TRIBUNAL — KEPLER-442b SECTOR — INCIDENT CASE 7741*
*Filed by: Arbiter Yolande Ferris*
*Re: Emergency intervention, Sector 9 water-reclamation authority*

At 14:00 local on Day 312 of the settlement calendar, the Sector 9 Water Authority convened to ratify a reallocation order that would have transferred seventy percent of Sector 9's reclaimed-water output to the new industrial processing units in Sectors 11 and 12, effective immediately. The reallocation was proposed by the Colonial Development Council and had been presented to the Authority as a duly constituted development directive requiring only formal ratification.

The directive was not duly constituted. It had been classified as a development directive — which requires only Council approval — rather than as a resource-priority amendment, which requires a full settlement-wide vote under the Colonial Charter. The distinction is not procedural. Resource-priority amendments exist specifically because water reallocation below the minimum residential threshold triggers a survival clause: settlements that fall below the threshold have no legal obligation to honour other colonial agreements, including land-tenure grants. The industrial operators in Sectors 11 and 12 held land-tenure grants from the Colonial Development Council.

If the reallocation had been ratified under the development-directive classification, Sector 9's residential population would have received less water than the survival-clause threshold, giving them legal grounds to repudiate the land-tenure grants retroactively. The industrial operators would have had no legal recourse.

I intervened before the ratification vote and submitted a classification challenge under Tribunal authority. The vote was suspended. The directive was reclassified as a resource-priority amendment and referred to the settlement-wide ballot process. The water-reallocation did not take effect pending the vote.

> A = Arbiter Yolande Ferris; B = the industrial operators of Sectors 11–12 (facing retroactive repudiation of land-tenure grants); T = misclassified resource-priority amendment about to be ratified as a development directive — ratification would trigger the survival clause and void the operators' land-tenure grants. ✓ all roles, ✓ all states.

---

**Re-Sf6-5**

The transit pod carrying the geological survey team has been decelerating toward Ganymede Relay for six minutes when Flight Controller Ajibade notices the approach vector does not account for the relay's current orbital position. The relay completes one orbit of Ganymede every seven hours and twelve minutes. The automated docking system calculates intercept based on a position fix taken at departure, plus a predicted orbital track. The position fix is correct. The orbital track prediction is not: it uses a period of seven hours and eight minutes — a four-minute error in the relay's rotational data that has been sitting in the docking system's reference file since a firmware update eight weeks ago.

Over a six-minute deceleration burn, four minutes of orbital-period error is small. Over the full eighteen-minute approach, the relay's actual position will be eleven kilometres from where the pod's docking system expects it. At terminal approach speed, the pod will be committed to a docking axis with empty space. It will miss the relay entirely and enter a Ganymede-intercept trajectory with insufficient fuel for a corrective burn.

Ajibade overrides the automated approach and transfers to manual vectoring. She contacts the pod's pilot, Navigator Keyes, and gives him the corrected orbital period and the revised intercept heading. Keyes acknowledges and adjusts the deceleration burn to match the corrected track. The pod reaches the relay's actual position eight minutes later and docks on the revised axis without incident.

> A = Flight Controller Ajibade; B = the geological survey team aboard the transit pod; T = firmware-corrupted orbital-period value in the docking system's reference file — the pod is on approach to an intercept axis that will miss the relay by eleven kilometres, committing it to a Ganymede-intercept trajectory. ✓ all roles, ✓ all states.

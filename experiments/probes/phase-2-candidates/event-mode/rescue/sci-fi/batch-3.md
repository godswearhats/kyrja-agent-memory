# Rescue × Sci-fi — Batch 3 (Tier C)

**Re-Sf3-1**

The pressure log for Habitat Ring C shows nominal. It has shown nominal for the past four hours because the Ring C pressure sensor array went offline at 14:32 and the monitoring system defaulted to the last valid reading, as designed. The design assumption was that the array would never be offline for more than fifteen minutes.

Ysolde is the habitat's systems integration technician. She is not on shift. She is eating in the common bay when the display on the wall cycles through its dashboard loop and she catches, for half a second, the sensor-array status icon on the environmental tab — grey, not green. She stands up and crosses to the display. The array has been grey since 14:32. It is now 18:41.

She pulls the physical gauge readout for Ring C from the maintenance console — a direct line, not routed through the array. The physical gauge reads 87 kPa. Nominal is 101 kPa. The threshold for suit-mandatory evacuation is 90 kPa. Ring C has forty-one people in it, none of them in suits, all of them breathing air that is currently below the evacuation threshold, and the monitoring system has been telling the duty officer it is fine for four hours and six minutes.

She trips the Ring C evacuation alarm from the maintenance console, overriding the duty officer's board. The alarm sounds through the ring. She gets the duty officer on comms and tells him what the physical gauge reads and how long the array has been offline. He authorises the evacuation. All forty-one personnel are clear of Ring C in eleven minutes.

> A = Ysolde (systems integration technician, off-shift); B = 41 personnel in Habitat Ring C; T = slow pressure loss in Ring C, undetected for 4+ hours due to a failed sensor array defaulting to the last nominal reading — habitat already below evacuation threshold with no suits deployed. ✓ all roles, ✓ all states.

---

**Re-Sf3-2**

"Docking authority, this is the *Manche Libre*, requesting emergency contact with your medical station."

"*Manche Libre*, docking authority. Go ahead. What is your situation?"

"We have a passenger in cryo bay two. She came out of suspension during transit. Spontaneous wake — her vitals monitor flagged it about forty minutes ago. Her core temperature is fourteen degrees and dropping. Cryo systems are showing a heater-coil fault on bay two. She is alive. She will not stay alive at this temperature."

"What is your current distance from dock?"

"Thirty-one minutes at current burn. We cannot increase burn — we have seventeen other passengers in active suspension and a hard burn will trigger a cascade alert in the cryo management system."

"Stand by, *Manche Libre*."

A longer pause.

"*Manche Libre*, medical station is patching to your cryo management system directly. They need access to manually override the bay two heater from our end and run heat from the bay-three coil in parallel. Can you authorise remote access?"

"Yes. Authorising now. Access code seven-seven-delta-four."

"We have access. Starting the parallel heat protocol. Your cryo tech needs to watch bay two temperature and ping us every four minutes."

"Understood. She's at thirteen-point-eight now."

"She'll be at fifteen before you dock. Medical team will be at the airlock."

> A = docking authority medical station; B = the spontaneously revived passenger in bay two; T = heater-coil fault in cryo bay two dropping core temperature toward fatal hypothermia, 31 minutes from dock. ✓ all roles, ✓ all states.

---

**Re-Sf3-3**

What I knew, sitting at the relay desk on Meridian Station, was this: the *Takahe* had filed a standard approach vector two hours ago, her nav transponder was transmitting normally, and she was eleven minutes from the docking corridor. What the *Takahe*'s crew did not know, and could not know, because the notification had come in on an admincast frequency they would not have been monitoring on final approach, was that docking corridor seven had been partially sealed following a microfracture event forty minutes ago. The corridor appeared open on approach radar because the inner seal was intact and the fracture was in the outer wall segment. If the *Takahe* extended her docking collar and pressurised the corridor to equalise before boarding, the pressure differential would propagate the fracture and breach the outer seal with the collar locked.

I switched to the *Takahe*'s hailing frequency and raised them. They answered on the third ping, sounding mildly irritated — ships on final approach don't love unscheduled comms. I told them to divert to corridor four. Their pilot asked why. I gave her the fracture reference number from the maintenance log and told her corridor four was clear and waiting. She was quiet for about four seconds. Then she said "diverting to four" and read back the corridor number.

The *Takahe* docked in corridor four without incident. The fracture in corridor seven was visible to the naked eye when the maintenance team went in with suits.

> A = I (relay desk operator, Meridian Station); B = the crew and passengers of the *Takahe*; T = a propagating microfracture in the outer wall of docking corridor seven — would have breached under docking-collar pressurisation, with the collar locked. ✓ all roles, ✓ all states.

---

**Re-Sf3-4**

The colony ship *Erqui* carries eleven thousand people in managed suspension across a transit lasting nineteen years. Its crew of thirty-two rotates through four-year active cycles. In Year Fourteen, during the third crew rotation, the agronomist Benedikt Osei reads through the archived decision logs from Year Eight and finds an entry that should not be there.

The Year Eight crew authorised a resource reallocation — standard procedure during a transit-efficiency review — that shifted sixteen percent of the atmospheric processing capacity from the suspension bays to the ship's active zones. The reallocation was logged as temporary, pending reversal at the Year Twelve checkpoint. The Year Twelve crew reversed it partially. The suspension bays are currently operating at ninety-one percent of the atmospheric processing capacity the eleven thousand sleeping passengers require for their current metabolic suppression depth. At ninety-one percent, the metabolic suppression holds. At any lower rate, it begins to fail.

The Year Fourteen crew does not know this because the Year Twelve checkpoint log shows the reallocation as "resolved," which is the status the Year Twelve crew entered when they made the partial reversal and considered the variance acceptable. The variance is not acceptable. It has no margin.

Osei brings the full allocation history to the ship's primary systems engineer with the metabolic requirement tables from the suspension bay specification. The engineer verifies the numbers. She restores the suspension bay processing capacity to full specification within the hour, drawing power from the active-zone recreational systems and the secondary thermal circulation loop.

> A = Benedikt Osei (agronomist); B = 11,000 passengers in suspension; T = an unresolved atmospheric processing shortfall in the suspension bays — logged as "resolved" at the Year Twelve checkpoint, leaving suspension metabolism with no safety margin. ✓ all roles, ✓ all states.

---

**Re-Sf3-5**

> **INCIDENT RECORD — THARSIS RELAY NODE 7**
> **Logged by:** Automated systems; Narrative annotation by Ops Specialist Chiara Dembélé
> **Event timestamp:** Sol 412, 06:14 local
>
> At 06:02, the outbound packet queue for the Tharsis–Phobos relay link began processing a firmware update bundle destined for the Phobos navigation beacon array. The bundle had been queued by ground control at Hellas Base and was scheduled to transmit during the standard 06:00 low-traffic window.
>
> At 06:07, I flagged the bundle for manual hold. Reason: the version identifier in the bundle header — FW-NAV-4.1.2 — does not match the version currently installed on the Phobos array (FW-NAV-4.2.0). The bundle is a downgrade. The 4.1.2 firmware does not include the orbital drift compensation patch added in 4.1.7 and carried forward. Phobos array is currently tracking seventeen active approach vectors, including the *Sundarbans* transit inbound with 340 passengers. Downgrading the beacon array firmware during an active multi-vessel tracking window would remove the drift compensation function mid-track.
>
> At 06:09, I contacted Hellas Base on the operations channel and reported the version mismatch. Hellas Base confirmed the bundle had been queued in error — a version-rollback package from a testing environment had been promoted to the production queue by a scripting mistake.
>
> Hold confirmed. Bundle pulled from queue at 06:12. Correct bundle queued for Sol 413 low-traffic window. All seventeen approach vectors remained under continuous tracking. No navigational interruption.

> A = Ops Specialist Chiara Dembélé; B = 17 vessels under active approach tracking, including the *Sundarbans* (340 passengers); T = a firmware downgrade bundle queued in error for the Phobos navigation beacon array — would have removed orbital drift compensation mid-track during an active approach window. ✓ all roles, ✓ all states.

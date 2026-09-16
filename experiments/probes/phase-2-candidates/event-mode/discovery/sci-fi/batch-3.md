# Discovery × Sci-fi — Batch 3 (Tier C)

**Di-Sf3-1**

The atmospheric processor on Kepler Station Outpost 7 has been returning nominal oxygen-partial-pressure readings for the eleven months since Station Commander Reyes signed off on the maintenance certification. She has routed all safety reviews through the certification on that basis — the processor is certified, the air is within tolerance, no priority inspection queue. On the morning of the quarterly physical, the station medic flags three crew members for elevated erythrocyte counts. Reyes is in the infirmary when the medic runs the differential. Elevated red cell count is a hypoxia response — the body making more oxygen-carriers because there is not enough oxygen to carry. She looks at the atmospheric panel on the infirmary wall. It reads 20.9 kilopascal partial pressure: nominal. The medic pulls the raw sensor log from the environmental subsystem, not the processed output. The raw log shows a consistent seven-month drift to 17.1 kilopascal. The processor's reporting module had been applying a correction offset — a calibration constant entered during the maintenance cycle — that was adding 3.8 kilopascal to every outgoing reading without altering the actual atmosphere. The crew had been breathing sub-threshold air for seven months. The certification had verified the reporting module, not the air.

> A = Station Commander Reyes; B = the atmospheric processor is operating within tolerance and the station air is at nominal oxygen partial pressure (per certified maintenance records); E = crew medic's raw environmental sensor log showing seven-month drift to 17.1 kPa, versus processed output reading 20.9 kPa — a calibration offset added to readings without changing actual atmosphere; corroborated by three crew members' hypoxia-response erythrocyte counts; B′ = the certification verified the reporting module only; actual atmospheric oxygen has been sub-threshold for seven months. ✓ all roles, ✓ all states

---

**Di-Sf3-2**

"How many active relay nodes are we showing on the network map?" the comms engineer asks.

"Forty-seven," says her apprentice. He has the topology display up on the central screen. "Same as last quarter. Same as the quarter before."

"Pull the individual handshake logs. Not the aggregate map — the per-node logs."

He pulls them. She leans over his shoulder and counts the nodes with successful handshakes in the past seventy-two hours. Thirty-one. She counts again. Thirty-one.

"Where are the other sixteen?"

He cross-checks. Sixteen nodes on the map are flagged as active in the aggregate topology model, but their individual handshake logs show no successful contact in between four and nine months. The network mapping algorithm propagates the last-known-active status forward until a node reports failure. None of the sixteen had reported failure — they had simply stopped responding, and a non-response was not, in the algorithm's logic, a failure state.

She had been routing high-priority transmissions across a network she believed to have forty-seven reliable nodes. Thirty-one of them were actually reachable.

> A = comms engineer; B = the relay network has forty-seven active, reachable nodes (per the aggregate network topology map); E = per-node handshake logs showing only thirty-one nodes with successful contact in the past seventy-two hours; sixteen mapped-as-active nodes have had no successful handshake for four to nine months; B′ = the reachable network has thirty-one nodes, not forty-seven; the topology algorithm propagates last-known-active status and does not register silent failure as a failure state. ✓ all roles, ✓ all states

---

**Di-Sf3-3**

I had been the colony ship *Perihelion*'s demographic officer for the full fourteen-year transit, and I had signed every population report that went to the colonial authority. My projections for the Kepler-442b settlement were built on a founding cohort of 1,204 adults and the actuarial tables we carried in the ship's charter: expected mortality, expected birth rate, expected age distribution at landfall. When we entered final approach and I ran the pre-landing census — mandatory under Colonial Compact Article 9, physical headcount by section — I got to Section F, the aft residential block, and the physical count stopped matching. I counted Section F twice. The section manifest listed 186 occupants. I counted 219. I went to the section supervisors. They had been logging births to the Section F cohort in the shipboard civil register, but the civil-register feed had not been connected to my demographic database since a system migration in transit year six. Every birth, every death, every age-status change logged in the civil register for the past eight years had not propagated to the population model I had been reporting to the colonial authority. The settlement I had planned for was calibrated to a population profile eight years out of date.

> A = demographic officer aboard *Perihelion*; B = the founding population at landfall consists of 1,204 adults distributed per the actuarial projections, accurately reflected in the demographic database; E = physical headcount of Section F yielding 219 versus manifest figure of 186, traced to a system migration in transit year six that severed the civil-register feed from the demographic database — eight years of births, deaths, and age changes not propagated; B′ = the demographic database is eight years out of date; the actual population profile at landfall is unknown, and settlement planning based on it is unreliable. ✓ all roles, ✓ all states

---

**Di-Sf3-4**

The orbital survey chief has modelled the asteroid's trajectory for six weeks. The mass estimate came from the radar cross-section team: 4.2 × 10¹² kilograms, consistent with a mid-grade S-type body at that albedo. The trajectory model, built on that mass, puts the object in a stable resonance orbit that will carry it clear of the inner system. She has signed three status reports on that basis and briefed the Planetary Defence Council twice. On the day the mining consortium's prospector drone makes its closest approach, it transmits a density profile. The surface albedo is S-type. The interior is not. The drone's gravimetric sensor shows a mean bulk density of 7.8 grams per cubic centimetre — iron-nickel throughout, not the silicate mix the albedo implied. The actual mass is 1.1 × 10¹³ kilograms: 2.6 times her estimate. She sits at her terminal and reruns the trajectory model with the corrected mass. The resonance that kept the body clear of the inner system was mass-dependent. At 1.1 × 10¹³, the resonance does not hold.

> A = orbital survey chief; B = the asteroid's mass is 4.2 × 10¹² kg (S-type silicate composition inferred from albedo), placing it in a stable resonance orbit clear of the inner system; E = mining prospector drone's gravimetric density profile showing iron-nickel interior at 7.8 g/cm³ — actual mass 1.1 × 10¹³ kg, 2.6× the radar-derived estimate; B′ = the asteroid's mass is 1.1 × 10¹³ kg; at this mass the resonance orbit does not hold, and prior trajectory clearance assessments are invalid. ✓ all roles, ✓ all states

---

**Di-Sf3-5**

TO: Oversight Committee, Meridian Terraforming Authority
FROM: Senior Soil Chemist Davorka Ilic
RE: Bacterial assay results, Southern Lowlands transect, Day 2,847

The attached assay was run as a routine protocol check, not as an investigation. I am submitting it to the Committee because its results contradict the foundational parameter of the current phase-three timeline.

The introduced *Acidithiobacillus*-variant strains have been the backbone of the sulphur-oxidation cycle since Phase One. Authority projections assume a viable colony density of 10⁸ CFU per gram of regolith at the Phase Three transect depth. This assumption underlies the projected pH reduction timeline of fourteen years to target threshold, which in turn underpins the atmospheric seeding schedule, the settlement infrastructure bond issuance, and the current colonist-intake contracts.

The Day 2,847 assay returned 3.1 × 10⁴ CFU per gram at target depth across eleven of fourteen sample sites. The viable density is approximately three thousand times below projection. Follow-on culture indicates the strain has not died but has entered a low-activity persistence state under regolith pressure and temperature conditions at depth that were not present in the Phase One surface trials.

The fourteen-year pH timeline was derived from surface-trial performance data. It does not describe what the bacteria do at depth. I do not have a revised timeline to offer. I have only the assay.

> A = Senior Soil Chemist Davorka Ilic (and by extension the Meridian Terraforming Authority's planning basis); B = *Acidithiobacillus*-variant colonies maintain viable density of 10⁸ CFU/g at Phase Three transect depth, supporting a fourteen-year pH reduction timeline; E = Day 2,847 assay returning 3.1 × 10⁴ CFU/g at depth across eleven of fourteen sites — ~3,000× below projection, traced to a low-activity persistence state under depth conditions absent from surface trials; B′ = the bacterial strains do not maintain projected density at depth; the fourteen-year timeline is based on surface-trial data that does not describe below-surface performance. ✓ all roles, ✓ all states

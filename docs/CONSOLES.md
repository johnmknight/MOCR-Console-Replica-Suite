# MOCR Console Replica Suite — Console Reference

Master research document for all 16 Apollo MOCR flight controller positions. Each section
covers the historical role, known display data, current stub status, planned KSA telemetry
mapping, and open research questions.

**Primary source:** Lee Hutchinson, "Apollo Flight Controller 101: Every console explained,"
Ars Technica, December 24, 2019. Local copy at
`C:\Users\john_\Downloads\Apollo Flight Controller 101_ Every console explained - Ars Technica.pdf`

**Secondary sources:** NASA Technical Reports, oral histories, Apollo Operations Handbook,
MOCR photographs, spaceflight history community knowledge.

**Convention:** Items marked **[UNKNOWN]** are gaps in the public record that primary source
access (NASA JSC History Collection at UHCL Archives) could fill. Items marked **[INFERRED]**
are reasonable assumptions based on the position's responsibilities but not confirmed by
documentation.

---

## Table of Contents

1. [Row 1 — The Trench](#row-1--the-trench)
   - [BOOSTER — Booster Systems Engineer](#booster--booster-systems-engineer)
   - [RETRO — Retrofire Officer](#retro--retrofire-officer)
   - [FDO — Flight Dynamics Officer](#fdo--flight-dynamics-officer)
   - [GUIDO — Guidance Officer](#guido--guidance-officer)2. [Row 2 — Spacecraft Systems](#row-2--spacecraft-systems)
   - [SURGEON — Flight Surgeon](#surgeon--flight-surgeon)
   - [CAPCOM — Capsule Communicator](#capcom--capsule-communicator)
   - [EECOM — Electrical, Environmental & Consumables](#eecom--electrical-environmental--consumables)
   - [GNC — Guidance, Navigation & Control (CM)](#gnc--guidance-navigation--control-cm)
   - [TELMU — Telemetry, Electrical & EVA Mobility Unit](#telmu--telemetry-electrical--eva-mobility-unit)
   - [CONTROL — LM Guidance, Navigation & Control](#control--lm-guidance-navigation--control)
3. [Row 3 — Support & Command](#row-3--support--command)
   - [INCO — Instrumentation & Communications](#inco--instrumentation--communications)
   - [O&P — Operations & Procedures](#op--operations--procedures)
   - [FLIGHT — Flight Director](#flight--flight-director)
   - [FAO — Flight Activities Officer](#fao--flight-activities-officer)
   - [NETWORK — Network Controller](#network--network-controller)
4. [Row 4 — Management](#row-4--management)
   - [PAO — Public Affairs Officer](#pao--public-affairs-officer)

---

## Row 1 — The Trench

The front row of the MOCR — lowest elevation, closest to the projection screens. These four
positions were responsible for spacecraft trajectory, flight dynamics, and guidance. Known
collectively as "the trench," this row handled the physics of getting there and getting back.

---

### BOOSTER — Booster Systems Engineer

**Position:** Far left, Row 1**Staffing:** Three controllers during launch (one per Saturn V stage). After TLI, the
console was reassigned to mission-specific scientific experiment personnel.
**Employer:** Marshall Space Flight Center (reported to JSC for launches).

#### Historical Role

BOOSTER monitored all three Saturn V stages during the approximately 9-minute ride to orbit,
plus the S-IVB's Trans-Lunar Injection burn. BOOSTER had authority to send an abort command
during the launch phase. After TLI, the position's primary mission was complete.

#### Known Display Data

- Per-stage thrust levels
- Chamber pressures
- Propellant flow rates (LOX, RP-1 for S-IC; LOX, LH2 for S-II and S-IVB)
- Burn duration / time remaining
- Stage separation sequence status
- **[UNKNOWN]** Exact display layout and formatting
- **[UNKNOWN]** Specific alarm thresholds and redline values
- **[UNKNOWN]** Hazeltine display format specifications

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| First Stage | S-IC | THRUST, CHAMB P, LOX FLOW, RP-1 FLOW, BURN T |
| Second Stage | S-II | THRUST, CHAMB P, LH2 FLOW, LOX FLOW, BURN T |
| Third Stage | S-IVB | THRUST, CHAMB P, LH2 FLOW, LOX FLOW, BURN T |
| Sequence Events | SEQ | STAGE, SEP ARM, IGN CMD |
#### KSA Telemetry Mapping

KSA-Bridge does not currently publish per-stage propulsion data. BOOSTER will require either:
- New KSA-Bridge telemetry topics for staged propulsion
- Synthetic/simulated data derived from existing vehicle telemetry
- **[INFERRED]** Could map to `ksa/telemetry/resources` thrust values during ascent phase

#### Open Research Questions

1. What were the specific Hazeltine display formats for each stage?
2. What abort criteria did BOOSTER monitor (specific threshold values)?
3. How was the console reconfigured for experiment monitoring after TLI?
4. What was the data refresh rate for propulsion telemetry?

---

### RETRO — Retrofire Officer

**Position:** Second from left, Row 1
**Authority:** Could call for mission abort.

#### Historical Role

RETRO's entire job was getting the crew home. Maintained continuously updated abort option
lists — procedures for returning the crew to Earth from any point in the mission. Tracked
the Service Module main engine for lunar orbit departure. Planned Trans-Earth Injection
burns. Monitored retrofire systems and safe return trajectories.
#### Known Display Data

- Abort option lists (mode, TIG, delta-V required, landing zone)
- Trans-Earth Injection burn parameters
- Reentry corridor tracking (entry angle, range, g-loading)
- Recovery zone identification and weather
- **[INFERRED]** Entry interface altitude and deceleration profile
- **[UNKNOWN]** Exact display layout for abort option lists
- **[UNKNOWN]** How abort options were ranked and prioritized on-screen

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| Abort Options | ABT | MODE, TIG, DV REQ, IMPACT |
| Trans-Earth Injection | TEI | TIG, DV REQ, BURN DUR, ENTRY ANG |
| Reentry Tracking | RET | RANGE, ENTRY I/F, GAMMADOT, GLOAD |
| Recovery Zone | RCV | ZONE, SPLASH, WEATHER |

#### KSA Telemetry Mapping

- Abort calculations can be derived from `ksa/telemetry/orbit` and `ksa/telemetry/velocity`
- Recovery zone estimation from orbital elements
- **[INFERRED]** Entry interface calculations from periapsis and trajectory data

#### Open Research Questions

1. How were abort options displayed — tabular list? Scrolling? Fixed slots?
2. What reentry corridor parameters were shown in real time vs. computed on demand?3. Did RETRO have a graphical trajectory display or purely numerical?
4. What was the format of the abort option "card" — how many fields per option?

---

### FDO — Flight Dynamics Officer

**Position:** Second from right, Row 1
**Pronunciation:** "FEE-doe"
**Authority:** One of only two positions (with FLIGHT) that had direct abort authority during
launch, via dedicated abort toggle switches.

#### Historical Role

FDO tracked the vehicle's trajectory at all mission stages. Calculated maneuver times.
Monitored spacecraft position via ground tracking stations. Coordinated with the Manned
Space Flight Network. Trajectory deviations could be catastrophic — fractions of a degree
could mean life or death.

#### Known Display Data

- Orbital elements (apoapsis, periapsis, inclination, eccentricity, SMA, LAN, AOP, period)
- Velocity (orbital, surface, vertical)
- Altitude and geographic position (latitude, longitude)
- Attitude (heading, pitch, roll)
- Maneuver parameters (TIG, burn duration, delta-V)
- Mission elapsed time

#### Current Implementation

**Two working consoles exist:**
1. **Apollo FDO Console** (`consoles/fdo/fdo-console.html`) — Faithful period recreation.
   Dense columnar layout with blue text on dark background, CRT scanlines, responsive
   scaling. Sections: ODO, VEL, ALT, ATT, VEH, RES, MAN, MET.

2. **Hard Sci-Fi FDO Console** (`consoles/fdo-hardscifi/hardscifi-fdo-console.html`) —
   Modern variant with Three.js globe, real-time orbit rendering, orbital element markers,
   trajectory sparklines, multi-body surface data, light/dark themes, event logging.

#### KSA Telemetry Mapping

Fully mapped. Subscribes to all `ksa/telemetry/#` topics. Unit conversions: radians to
degrees for angles, seconds to minutes for period, meters to km for SMA.

---

### GUIDO — Guidance Officer

**Position:** Far right, Row 1
**Pronunciation:** "GUIDE-oh"

#### Historical Role

GUIDO monitored the Primary Guidance, Navigation, and Control Systems (PGNCS, pronounced
"pings") — the onboard computers in both the Command Module and Lunar Module. Tracked
velocity and vector reporting. Ensured spacecraft computers' calculated position matched
reality. Also monitored the Lunar Module Abort Guidance System (AGS, "aggs").

Software and computer focused — the counterpart to GNC's hardware focus.
**Famous moment:** Apollo 11 landing — LM computer overwhelmed with 1202/1201 alarms.
GUIDO Steve Bales and backroom staff determined it was safe to proceed, saving the first
moon landing. Decision made in approximately 30 seconds.

#### Known Display Data

- CM Computer (CMC) state: program, verb, noun, registers R1-R3
- LM Computer (LGC) state: program, verb, noun, registers R1-R3
- Navigation state vector accuracy (position error, velocity error)
- AGS status and deviation from primary guidance
- Computer program alarms (1202, 1201, etc.)
- **[UNKNOWN]** How computer state was displayed — DSKY mirror? Separate format?
- **[UNKNOWN]** What "velocity and vector reporting" looked like on the display

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| CM Computer (PGNCS) | CMC | PROG, VERB, NOUN, R1, R2, R3 |
| LM Computer | LGC | PROG, VERB, NOUN, R1, R2, R3 |
| Navigation State | NAV | POS ERR, VEL ERR, STATE |
| Abort Guidance | AGS | STATUS, POS DEV, VEL DEV |

#### KSA Telemetry Mapping

KSA-Bridge does not currently publish computer state or guidance system data. Would require:
- New topics for onboard computer program state
- Navigation accuracy / state vector comparison data
- **[INFERRED]** Could partially derive from orbit/position data discrepancies
#### Open Research Questions

1. Did GUIDO see a mirror of the DSKY display, or a reformatted ground version?
2. How was the AGS deviation from PGNCS displayed — numerical delta? Side-by-side?
3. What program alarm codes were displayed and how were they formatted?
4. How did GUIDO's display change between CM-active and LM-active mission phases?

---

## Row 2 — Spacecraft Systems

Second row, elevated approximately 2 feet above the trench. Six positions focused on
spacecraft hardware systems and crew health. The left side (SURGEON, CAPCOM) handled crew
interface; the center (EECOM) handled CM systems; the right side (GNC, TELMU, CONTROL)
handled hardware and the Lunar Module.

---

### SURGEON — Flight Surgeon

**Position:** Far left, Row 2
**Staffing:** Medical doctor.

#### Historical Role

Monitored crew health via biomedical telemetry. Displayed ECG (electrocardiogram) and
electropneumogram data. Tracked heart rates and breathing rates. Had authority to
recommend crew grounding.
**Reputation:** Often adversarial relationship with astronaut corps — "pilots can leave
doctor's office in one of two conditions: fine, or grounded." Apollo 13: Flight Surgeon
Chuck Berry grounded Ken Mattingly over measles exposure.

**Anecdote:** Chris Kraft once played a heart attack ECG tape through the telemetry link.
SURGEON said crew was "looking just fine."

#### Known Display Data

- Per-crewmember ECG waveforms
- Heart rate (beats per minute)
- Respiration rate (breaths per minute)
- **[INFERRED]** Body temperature, blood pressure
- **[INFERRED]** EVA suit biometrics (suit pressure, O2 flow, metabolic rate)
- **[UNKNOWN]** Exact biomedical display format
- **[UNKNOWN]** Whether ECG was waveform display or numerical summary
- **[UNKNOWN]** What "electropneumogram" display looked like

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| Commander | CDR | HR, RESP, ECG, TEMP, BP |
| CM Pilot | CMP | HR, RESP, ECG, TEMP, BP |
| LM Pilot | LMP | HR, RESP, ECG, TEMP, BP |
| EVA Biomedical | EVA | SUIT P, O2 FLOW, METAB |

#### KSA Telemetry Mapping
KSA does not simulate crew biomedical data. SURGEON will require synthetic/simulated data
or a separate data source entirely. Could be an interesting creative opportunity — generate
plausible biomedical telemetry based on mission phase and g-loading.

#### Open Research Questions

1. Was ECG displayed as a live waveform trace or numerical heart rate only?
2. What biomedical parameters were available per crewmember?
3. Did the display change format during EVA vs. cabin operations?
4. What alarm thresholds existed for heart rate, respiration?

---

### CAPCOM — Capsule Communicator

**Position:** Second from left, Row 2
**Staffing:** Always an astronaut.

#### Historical Role

The ONLY voice authorized to speak directly to the crew. Single point of contact between
Mission Control and the spacecraft. Translated controller recommendations into crew
instructions in "astronaut terms." Provided a "friendly, well-known voice."

**Rationale:** Resource management (track all transmissions), crew safety (single
instruction source), familiarity with spacecraft systems.

**Exception:** Gemini 4 — Chris Kraft directly ordered Ed White to end his EVA (safety
and time constraints).
#### Known Display Data

- Voice communication status (uplink/downlink)
- Signal quality indicators
- Message log / pending items
- Go/No-Go poll status and crew acknowledgment
- **[UNKNOWN]** Whether CAPCOM had a dedicated text display or primarily used voice
- **[UNKNOWN]** Message pad format for reading up data to crew
- **[INFERRED]** Voice PAD readback tracking

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| Voice Communications | COM | UPLINK, DOWNLINK, QUALITY, MODE |
| Message Log | MSG | LAST TX, LAST RX, PENDING |
| Voice Pad | PAD | READBACK, CONFIRM |
| Go/No-Go Status | GNG | POLL, RESULT, CREW ACK |

#### KSA Telemetry Mapping

CAPCOM is primarily a voice/communications position. In the KSA context, this console could:
- Display MQTT connection status as proxy for comm link status
- Show message log of telemetry events
- Implement a go/no-go polling interface for multi-user sessions
- **[INFERRED]** Could integrate with KSA-PAO for commentary status

#### Open Research Questions
1. What did CAPCOM's display actually show — was it primarily a comm status panel?
2. Did CAPCOM have telemetry displays or rely on verbal reports from other positions?
3. What was the format of the PAD (voice data uplink) that CAPCOM read to crew?
4. How was the go/no-go poll displayed and tracked?

---

### EECOM — Electrical, Environmental & Consumables

**Position:** Center, Row 2
**Original name:** Electrical, Environmental, and COMmunications.
**After Apollo 10:** Communications responsibility moved to INCO.

#### Historical Role

Monitored all Command/Service Module electrical and environmental systems. Power generation
and distribution (three fuel cells). Cryogenic levels (O2 and H2 tanks). Cabin cooling,
pressure, and life support. Vehicle lighting.

**Famous EECOMs:**
- Sy Liebergot — on duty during Apollo 13 O2 tank explosion
- John Aaron — "steely-eyed missile man." Apollo 12: lightning strike recovery (switched to
  backup power filter). Apollo 13: led power-up checklist development that saved the crew.

#### Known Display Data

- Fuel cell output (amps, volts) per cell (FC1, FC2, FC3)
- Main bus voltage (Bus A, Bus B)
- Total power consumption
- Cryogenic tank quantities (O2 Tank 1 & 2, H2 Tank 1 & 2)- Cryogenic flow rates
- Cabin pressure, temperature, humidity
- Partial pressure of O2 (ppO2)
- CO2 partial pressure
- Water and consumables remaining
- Consumables margin (hours of remaining life support)
- **[UNKNOWN]** Exact alarm thresholds and redline values for each parameter
- **[UNKNOWN]** Display layout — which parameters were grouped together

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| Electrical Power | EPS | FC1, FC2, FC3, BUS A, BUS B, TOTAL W |
| Cryogenics | CRY | O2 TK1, O2 TK2, H2 TK1, H2 TK2, O2 FLOW, H2 FLOW |
| Environmental Control | ECS | CABIN P, CABIN T, PPO2, CO2 PP, HUMIDITY |
| Consumables | CON | O2 RMNG, H2 RMNG, H2O RMNG, MARGIN |

#### KSA Telemetry Mapping

- `ksa/telemetry/resources` provides fuel, oxidizer, monopropellant, electric
- Could map electric → fuel cell proxy, fuel/oxidizer → consumables
- Environmental data would need new telemetry topics or synthetic generation
- **[INFERRED]** Consumables margin could be calculated from resource depletion rate

#### Open Research Questions

1. How were the three fuel cells displayed — side by side? Stacked?
2. What was the cryogenic tank display format — gauge? Numerical? Both?
3. How did EECOM track consumables margin — spreadsheet-style timeline?4. What were the specific redline values that triggered alarms?
5. How did the display change during the Apollo 13 crisis (loss of FC1, FC3)?

---

### GNC — Guidance, Navigation & Control (CM)

**Position:** Fourth from left, Row 2

#### Historical Role

Hardware counterpart to GUIDO's software focus. Monitored reaction control system (RCS)
hardware, Service Module main engine hardware, and guidance system hardware components
(gyroscopes, accelerometers, optics). The distinction: GUIDO watched the computers and
software; GNC watched the physical hardware those computers controlled.

#### Known Display Data

- RCS quad propellant levels (Quad A, B, C, D)
- RCS thruster status
- SPS (Service Propulsion System) engine status, fuel, oxidizer, chamber pressure
- SPS gimbal position (pitch, yaw)
- IMU (Inertial Measurement Unit) status and drift rates
- Attitude (heading, pitch, roll) and attitude rates
- **[UNKNOWN]** Specific RCS thruster firing indicators
- **[UNKNOWN]** IMU drift rate display format
- **[UNKNOWN]** How SPS gimbal was displayed — numerical or graphical

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|| Reaction Control | RCS | QUAD A-D, THRST |
| Service Propulsion | SPS | STATUS, FUEL, OXID, CHAMB P, GIMBAL P, GIMBAL Y |
| Inertial Measurement Unit | IMU | STATUS, DRIFT X/Y/Z |
| Attitude | ATT | HDG, PITCH, ROLL, RATE P/Y/R |

#### KSA Telemetry Mapping

- `ksa/telemetry/attitude` provides heading, pitch, roll
- `ksa/telemetry/resources` provides fuel, oxidizer, monopropellant
- Attitude rates would need new telemetry or derivation from attitude changes
- RCS and SPS detail would need new KSA-Bridge topics

#### Open Research Questions

1. How were the four RCS quads displayed — diagram? Table?
2. What IMU drift rate thresholds triggered realignment requests?
3. How was SPS gimbal position displayed — cross-hair graphic or numbers?
4. Did GNC see individual thruster firings or only aggregate quad status?

---

### TELMU — Telemetry, Electrical & EVA Mobility Unit

**Position:** Fifth from left, Row 2

#### Historical Role

EECOM's counterpart for the Lunar Module. Monitored LM life-support, LM power systems
(batteries — no fuel cells due to weight constraints), and EVA spacesuit (PLSS) systems.
**Famous moment:** Apollo 13 — solved the LM lifeboat power-up chicken-and-egg problem
(needed power to activate systems, but activating systems required power from systems
not yet powered).

#### Known Display Data

- LM battery voltages (Descent batteries 1-4, Ascent batteries)
- LM bus voltage and current draw
- LM cabin pressure, temperature, ppO2, CO2 levels
- LM suit circuit pressure
- PLSS (Portable Life Support System) status during EVA
- PLSS oxygen remaining, battery charge, cooling water, feedwater
- LM consumables remaining with margin
- **[UNKNOWN]** Exact battery display format
- **[UNKNOWN]** How EVA and cabin modes were displayed simultaneously
- **[UNKNOWN]** PLSS telemetry data rate and display refresh

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| LM Power Systems | LPS | BATT 1-4, ASC BATT, BUS V, AMPS |
| LM Environmental | LEC | CABIN P, CABIN T, PPO2, CO2 PP, SUIT P |
| EVA Suit Systems | EMU | PLSS O2, PLSS BAT, SUIT P, COOL H2O, FEEDH2O |
| LM Consumables | LCN | O2 ASC, O2 DES, H2O ASC, H2O DES, MARGIN |

#### KSA Telemetry Mapping
KSA-Bridge does not distinguish CM vs. LM systems. TELMU would require:
- New telemetry topics for LM-specific systems
- Or synthetic data generation for LM subsystems
- EVA data would need a completely new data source

#### Open Research Questions

1. How did TELMU's display differ from EECOM's — same format, different data?
2. What was the PLSS telemetry display during EVA — real-time or summary?
3. How were ascent/descent stage consumables separated on-screen?
4. What was the Apollo 13 LM power-up sequence display?

---

### CONTROL — LM Guidance, Navigation & Control

**Position:** Far right, Row 2

#### Historical Role

GNC's counterpart for the Lunar Module. Monitored landing radar, attitude thrusters, and
ascent/descent rocket hardware. Software was handled by GUIDO (LM and CM used the same
computer architecture).

#### Known Display Data

- Descent Propulsion System status, thrust level, fuel/oxidizer, chamber pressure
- Ascent Propulsion System status, fuel/oxidizer, chamber pressure
- Landing radar altitude and velocity readings, radar lock status
- LM RCS system propellant levels (System A, System B)- LM RCS thruster status and attitude hold mode
- **[UNKNOWN]** Landing radar display format — numerical or graphical altitude
- **[UNKNOWN]** How descent engine throttle was displayed (it was throttleable)
- **[UNKNOWN]** Fuel quantity warning display format ("60 seconds" call)

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| Descent Propulsion | DPS | STATUS, THRUST, FUEL, OXID, CHAMB P |
| Ascent Propulsion | APS | STATUS, FUEL, OXID, CHAMB P |
| Landing Radar | LRR | ALT, VEL X/Y/Z, LOCK |
| LM Reaction Control | RCS | SYS A, SYS B, THRST, ATT HOLD |

#### KSA Telemetry Mapping

Similar challenges to TELMU — KSA-Bridge doesn't separate CM/LM systems. Would need:
- LM-specific propulsion telemetry topics
- Landing radar simulation data
- **[INFERRED]** Could use altitude + vertical velocity as landing radar proxy

#### Open Research Questions

1. How was DPS throttle displayed — percentage? Bar? Absolute thrust?
2. What did the landing radar display look like during powered descent?
3. How were the "60 seconds" and "30 seconds" fuel warnings displayed?
4. Did CONTROL see the same attitude data as GNC or LM-specific data?

---
## Row 3 — Support & Command

Third row, another approximately 2 feet of elevation above Row 2. Five positions handling
communications infrastructure, procedures, mission timeline, network operations, and — at
center — the Flight Director's command position.

---

### INCO — Instrumentation & Communications

**Position:** Far left, Row 3
**Created:** After Apollo 10 (responsibilities taken from EECOM and TELMU).

#### Historical Role

Managed all data, voice, and video communications between the spacecraft and ground.
Monitored CM and LM communication systems. Managed the telemetry link. Handled all data
transmission including TV video.

#### Known Display Data

- Uplink command rate, signal strength, lock status, error rates
- Downlink telemetry rate, signal strength, bit error rate, format
- Video feed status, source selection, quality
- Antenna tracking (station, azimuth, elevation, range, handover scheduling)
- **[UNKNOWN]** Specific signal strength thresholds and display format
- **[UNKNOWN]** How tracking station handovers were displayed
- **[INFERRED]** Doppler tracking data for trajectory support
#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| Uplink | UPL | CMD RATE, SIGNAL, LOCK, ERRORS |
| Downlink | DNL | TLM RATE, SIGNAL, BER, FORMAT |
| Video | VID | STATUS, SOURCE, QUALITY |
| Antenna / Tracking | ANT | STATION, AZ, EL, RANGE, HANDOVER |

#### KSA Telemetry Mapping

- MQTT connection status maps naturally to comm link status
- `ksa/bridge/status` provides bridge health as proxy for telemetry link
- Signal strength and data rates would be synthetic
- Could display MQTT message rates as telemetry throughput proxy

#### Open Research Questions

1. What was the tracking station display format — map? Table? Both?
2. How was handover between stations displayed and managed?
3. What video/TV controls did INCO have?
4. How were communication blackouts (reentry) displayed?

---

### O&P — Operations & Procedures

**Position:** Second from left, Row 3

#### Historical Role
Procedural compliance gatekeeper. Ensured all controllers followed the flight control
operations handbook. Processed data printout requests and voice playback requests.
Verified proper forms and GMT timestamps on all documentation.

#### Known Display Data

- Current flight plan step and status
- Flight plan change tracking (pending, approved, rejected)
- Operations log (entries, shift info, GMT timestamps)
- Data requests (printout queue, playback requests, status)
- **[UNKNOWN]** Almost everything about this display — O&P is one of the
  least-documented positions
- **[UNKNOWN]** Whether O&P had a telemetry display at all or was primarily
  paper/procedure-based

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| Flight Plan | FLT | STEP, STATUS, REF DOC |
| Flight Plan Changes | CHG | PENDING, APPROVED, REJECTED |
| Operations Log | LOG | LAST ENTRY, SHIFT, GMT |
| Data Requests | REQ | PRINTOUT, PLAYBACK, STATUS |

#### KSA Telemetry Mapping

O&P is procedural, not telemetry-driven. In the KSA context, this console could:
- Display mission timeline/phase tracking- Log all MQTT messages as an operations record
- Track procedure checklists for multi-user sessions

#### Open Research Questions

1. Did O&P have any real-time telemetry displays?
2. What did the console screen actually show — was it purely administrative?
3. How were flight plan changes tracked and displayed?
4. What was the pneumatic tube (p-tube) system used for at this position?

---

### FLIGHT — Flight Director

**Position:** Center, Row 3 (elevated above the trench)
**Authority:** Ultimate authority over mission success and crew safety. Only way to
countermand: fire the flight director.

#### Historical Role

The "orchestra leader." Passive monitoring — no direct spacecraft control. Watched the
aggregate status of all other positions via the event indicator panel. Could override
anyone to ensure crew safety. One of only two positions with direct abort authority
during launch.

**Famous directors:** Gene Kranz (White), Glynn Lunney (Black), Gerry Griffin (Gold),
Milt Windler (Maroon), Cliff Charlesworth (Green).

#### Known Display Data
- Go/No-Go status board showing all controller positions (green/amber/red indicators)
- Mission phase and status
- Abort status (armed, mode, authority)
- Shift management (team ID, on-duty time, handover status)
- Mission logbooks
- **[UNKNOWN]** What other telemetry FLIGHT could see — aggregate summary? Selectable?
- **[UNKNOWN]** Exact format of the event indicator panel on the console vs. the wall display

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| Go/No-Go Board | GNG | All 13 controller positions |
| Mission Status | MIS | PHASE, RULE, DECISION |
| Abort Status | ABT | ARM, MODE, AUTHORITY |
| Shift Management | SHF | FLIGHT ID, TEAM, HANDOVER, ON DUTY |

#### KSA Telemetry Mapping

FLIGHT is a meta-console — it monitors the status of other consoles, not raw telemetry.
In the KSA context:
- Go/No-Go board could show MQTT connection status of each console
- Could aggregate critical alerts from all telemetry topics
- Mission phase derived from telemetry state (pre-launch, ascent, orbit, etc.)

#### Open Research Questions

1. What telemetry did FLIGHT see directly vs. receiving verbal reports?
2. How did the event indicator panel work — manual toggle by each controller?3. Did FLIGHT have a selectable display that could show any position's data?
4. What was the abort toggle panel layout?

---

### FAO — Flight Activities Officer

**Position:** Right of Flight Director, Row 3

#### Historical Role

Mission timeline manager. Ensured preplanned activities occurred on schedule. Knew all
mission checklists and understood time requirements for each step. Required comprehensive
spacecraft systems knowledge.

#### Known Display Data

- Mission timeline (current activity, next activity, time offset)
- Upcoming events schedule
- Active checklists and current step
- Crew schedule (wake, sleep, meal, EVA windows)
- **[UNKNOWN]** Timeline display format — scrolling list? Gantt-like?
- **[UNKNOWN]** How much of the mission timeline was visible at once
- **[INFERRED]** Time deltas showing ahead/behind schedule

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| Mission Timeline | TLN | CURRENT, NEXT, T+, DELTA |
| Upcoming Events | EVT | EVENT 1, T-, EVENT 2, T- || Checklists | CKL | ACTIVE, STEP, CREW ACK |
| Crew Schedule | SLP | WAKE, SLEEP, MEAL, EVA WIN |

#### KSA Telemetry Mapping

FAO is timeline-driven, not directly telemetry-driven. Could:
- Use mission elapsed time to drive timeline position
- Maintain an editable event schedule
- Track phase transitions based on telemetry state changes

#### Open Research Questions

1. What did FAO's display actually look like — was it a timeline or a checklist view?
2. How far ahead could FAO see on the timeline?
3. How were schedule deviations displayed?
4. Did FAO have any direct telemetry or only derived timing data?

---

### NETWORK — Network Controller

**Position:** Far right, Row 3

#### Historical Role

Interface with the global Manned Space Flight Network (MSFN). Ensured Mission Control
received all needed tracking data. Responsible for fixing downed computers at remote
tracking stations. Managed data transmission inside the MCC itself. First-line tech
support for console hardware problems.

"Had a really pressured job" — when a remote station went down, it was NETWORK's problem.
#### Known Display Data

- Tracking station status (active, next AOS, LOS countdown, coverage percentage)
- Data link status (uplink, downlink, backup link, latency)
- MCC systems status (mainframe, backup, displays, communications)
- Open issues tracking
- **[UNKNOWN]** Tracking station map display format
- **[UNKNOWN]** How AOS/LOS scheduling was displayed
- **[INFERRED]** Global MSFN map with station status indicators

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| Tracking Stations | STA | ACTIVE, NEXT AOS, LOS IN, COVERAGE |
| Data Links | LNK | UPLINK, DOWNLINK, BACKUP, LATENCY |
| MCC Systems | MCC | MAINFRAME, BACKUP, DISPLAYS, COMMS |
| Issues | ISS | OPEN, PRIORITY, LAST FIX |

#### KSA Telemetry Mapping

- MQTT broker status maps to data link health
- Could monitor actual network latency and message throughput
- MCC systems status could reflect actual console connectivity
- **[INFERRED]** Could show MSFN-equivalent tracking coverage based on orbital position

#### Open Research Questions

1. Did NETWORK have a world map showing tracking station status?2. How was AOS/LOS predicted and displayed?
3. What MCC internal systems did NETWORK monitor?
4. How were remote station problems reported and tracked on the display?

---

## Row 4 — Management

Top row — management oversight and public interface. During Apollo, Row 4 also included
the Flight Operations Director, NASA HQ liaison, and Department of Defense liaison. Only
PAO is planned for the console suite, as the other positions were primarily observational.

---

### PAO — Public Affairs Officer

**Position:** Far left, Row 4

#### Historical Role

"Voice of Mission Control" to the public. Provided audio narration for radio and
television broadcasts. Explained mission events to the public in accessible language.
Gave media commentary its foundation.

**Note:** See also [KSA-PAO](https://github.com/johnmknight/KSA-PAO), the AI-powered
Public Affairs Officer commentary system that subscribes to the same KSA-Bridge
telemetry and generates NASA-style mission commentary with neural text-to-speech.

#### Known Display Data

- Narration status (on-air, standby)
- Current broadcast mode (TV, radio)- Mission event summary for public consumption
- Commentary log (timestamped entries)
- **[UNKNOWN]** What telemetry PAO could see — did they have their own display?
- **[UNKNOWN]** Whether PAO had access to internal loop audio on their console
- **[INFERRED]** PAO likely had a simplified mission status summary display

#### Current Stub Sections

| Section | Code | Fields |
|---------|------|--------|
| Narration | NAR | STATUS, BROADCAST, AUDIENCE |
| Mission Events | EVT | LAST, CURRENT, NEXT |
| Media | MED | TV FEED, RADIO, PRESS |
| Commentary Log | LOG | ENTRIES, LAST TX |

#### KSA Telemetry Mapping

PAO ties directly into the existing KSA-PAO system:
- Could display KSA-PAO commentary output in real time
- Mission event log from telemetry state changes
- Could subscribe to `ksa/pao/#` topics from KSA-PAO
- Broadcast status could reflect KSA-PAO TTS output state

#### Open Research Questions

1. What did PAO's console display actually show?
2. Did PAO have access to all controller voice loops?
3. Was there a mission event summary display tailored for public communication?
4. How did PAO coordinate with the TV camera and broadcast systems?
---

## Positions Not Included in the Console Suite

The following Row 4 positions are documented for historical completeness but are not
planned as console displays, as they were primarily observational/liaison roles:

- **Assistant Flight Director** — Duplicated FLIGHT duties as backup. Row 3.
- **Flight Operations Director** — Senior MSC director (often Chris Kraft). Management
  liaison, not operational control. Row 4.
- **NASA HQ Liaison** — Representative from NASA Washington DC. "Rarely had anything to
  do, but usually someone there watching." Row 4.
- **Department of Defense Liaison** — Usually a general. Coordinated spacecraft recovery
  after splashdown. Had a "really cool red phone." Row 4.

---

## Console Technology Notes

### Hazeltine & Philco Displays

The original MOCR used Hazeltine and Philco CRT displays. These were character-based
monochrome displays — not graphical terminals. Data was presented in fixed-format text
layouts with specific character positions for each data field.

**[UNKNOWN]** Exact character dimensions, refresh rates, and color specifications for
both Hazeltine and Philco displays. This is primary source material likely in the
UHCL Archives collection.

### Projection Screens
Five large rear-projection Eidophor displays at the front of the room:
- Center "Ten by Twenty" (10ft x 20ft) — vehicle position and status
- Two left screens — vehicle command history, current flight plan page
- Two right screens — TV images from mission cameras or network television
- Nine smaller chronographic displays above — time and mission clocks

### Event Indicator Panels

Color-coded status displays: Green (ready), Amber (standby), Red (no-go). Used for the
go/no-go poll before launch and critical events. Also used during shift changes. Provided
immediate visual status to FLIGHT.

### Pneumatic Tube System

P-tube system for physical document delivery between positions. Used for flight plan
change requests, printed data, and other paper documents.

---

## Sources

1. **Primary:** Hutchinson, Lee. "Apollo Flight Controller 101: Every console explained."
   Ars Technica, December 24, 2019.
2. **Local reference:** `docs/apollo-mission-control-reference.md` (structured extract)
3. **NASA Technical Reports:** Various Apollo Operations Handbooks, Mission Rules documents
4. **Oral Histories:** NASA Johnson Space Center Oral History Project
5. **Photographs:** NASA image archive, Apollo-era MOCR photographs
6. **Access advocacy:** [NASA-Policy-Work](https://github.com/johnmknight/NASA-Policy-Work)
   — ongoing effort to access the NASA JSC History Collection at UHCL Archives
# MOCR Projection Screen Displays — Design Document

Design reference for implementing the five large front-wall projection displays and nine
chronographic displays from the Apollo-era Mission Operations Control Room (MOCR 2).

**Status:** Stretch goal. These are the "big boards" that dominated the front wall of Mission
Control — the screens every flight controller looked up at. Adding them to the suite would
complete the room.

---

## Physical Layout

The front (west) wall of MOCR 2 had three tiers of displays:

### Tier 1: Chronographic Displays (top)
Nine smaller displays mounted above the main screens, showing timing data:
- GMT (Greenwich Mean Time)
- MET / GET (Mission/Ground Elapsed Time)
- TIG (Time of Ignition — countdown to next burn)
- Event timers
- REV (Revolution/orbit counter)
- AOS / LOS (Acquisition/Loss of Signal countdowns)
- Range to target
- Retrofire countdown
### Tier 2: Five Large Rear-Projection Screens (main)

Viewed left to right from the controllers' perspective:

| Position | Name / Role | Projection Type | Typical Content |
|----------|-------------|-----------------|-----------------|
| Screen 1 (far left) | Command History | Plotting / Eidophor | Vehicle command history, telemetry summary |
| Screen 2 (left) | Flight Plan | Plotting / Eidophor | Current flight plan page, procedures |
| Screen 3 (center) | "Ten by Twenty" | 7-projector plotting | Vehicle position, ground track, trajectory |
| Screen 4 (right) | Television | Eidophor TV | Mission camera feeds, onboard TV |
| Screen 5 (far right) | Television | Eidophor TV | Network TV, recovery ops, alternate feeds |

The center screen measured 10 feet tall by 20 feet wide. The four flanking screens were
smaller. All five were rear-projected from the "Bat Cave" — a blacked-out projection room
(36 ft wide × 65 ft long × 15 ft high) behind the screens.

### Tier 3: Summary Display Projection Room ("Bat Cave")

Not visible to controllers. Housed the projection hardware:
- 5 seven-projector Xenon plotting display systems
- 7 large-screen Eidophor television projectors
- Optical mirrors, cooling systems, slide changers
- Manned by display operators who swapped slides and monitored equipment
---

## Projection Technology

### Seven-Projector Plotting Display (Center Screen)

Each plotting display comprised seven projectors working in overlay:

1. **Background projector** — Displayed the base map (world map, lunar surface, etc.)
   from a 1-inch-square glass slide with metal film etching. Swapped between mission phases.

2. **Two spotting projectors** — Imposed symbols (spacecraft icon, target markers) on the
   map. Position driven by real-time trajectory data from the RTCC (Real-Time Computer
   Complex). Symbols physically moved across the slide via servo mechanisms.

3. **Four scribing projectors** — Used diamond-tipped styli to scratch through metalized
   coating on glass slides, creating:
   - Ground track lines (the spacecraft's path over Earth)
   - Trajectory plots (ascent, descent, orbital paths)
   - Alphanumeric data (velocity, altitude, range annotations)
   - X-Y plots (altitude vs. range, etc.)

All illuminated by 2500-watt Xenon lamps. The scribed lines appeared as light projected
through the scratched-away metal coating — like an Etch-a-Sketch driven by IBM mainframes.

Slides were built up in layers with colors obtained through dichroic filters. The composite
image was far sharper than any video technology of the era.
### Eidophor Television Projectors (Side Screens)

Quartz-lamp video projectors that bounced images off mirrors onto the screens.
Used for:
- Live television from spacecraft cameras
- Network television coverage (launch, recovery)
- CRT-generated telemetry displays (composite image: CRT numbers + slide overlay labels,
  captured by CCTV camera and projected)
- Any of the 350+ group display channels available to individual consoles

The side screens were flexible — controllers could request specific display channels
be put up on the big screens via the Display Operations Room.

---

## Display Modes by Mission Phase

The center screen's content changed as the mission progressed. Each phase had a
characteristic display. The side screens adapted as well, typically showing the most
relevant telemetry, flight plan page, or television feed for the current phase.

### Mode 1: Pre-Launch / Countdown

**Center screen:** Launch vehicle status display — Saturn V systems summary,
countdown clock, hold status, weather data.

**Left screens:** Flight plan page for launch phase, abort mode summary.

**Right screens:** Television — pad camera views of the vehicle on the launch pad.
**Clocks:** GMT, countdown to T-0, hold time if applicable.

### Mode 2: Launch / Ascent

**Center screen:** Ascent trajectory plot — altitude vs. downrange distance. The
scribing projectors traced the actual ascent path in real time against a pre-plotted
nominal trajectory. Abort mode boundaries (Mode I, Mode II, Mode III, Mode IV) were
shown as regions on the plot. The spotting projector tracked the vehicle icon.

**Left screens:** Vehicle command history, abort option summary.

**Right screens:** Television — tracking camera views of the ascending vehicle.

**Clocks:** GET counting up from T-0, time to MECO, time to staging events.

### Mode 3: Earth Orbit

**Center screen:** Mercator projection world map with:
- Ground track — a sine-wave pattern showing the orbital path over Earth
- Three orbits visible (current + two future passes)
- Tracking station locations marked (MSFN ground stations)
- Spacecraft position icon moving along the track in real time
- AOS/LOS markers for each station pass
- Orbital parameters annotated (apogee, perigee, period, inclination)

This was the iconic "sine wave over the world map" display seen in most Apollo-era
Mission Control photographs.
**Left screens:** Flight plan, upcoming maneuver parameters, systems status summary.

**Right screens:** Television — onboard camera when available, otherwise network coverage.

**Clocks:** GET, REV counter, AOS/LOS for current station, TIG for next burn.

### Mode 4: Trans-Lunar Injection (TLI) Burn

**Center screen:** Burn monitoring display — trajectory plot showing departure from
Earth orbit. Plotted parameters likely included velocity gained, remaining delta-V,
cutoff predictions. Vehicle icon tracked along the planned trajectory.

**Left screens:** TLI burn parameters, abort options (free-return trajectory data).

**Right screens:** Television if available, otherwise telemetry summary.

**Clocks:** GET, TIG countdown, burn duration timer.

### Mode 5: Translunar Coast

**Center screen:** Earth-Moon trajectory plot — a schematic showing the spacecraft's
position along the translunar path, with Earth at one end and Moon at the other.
Distance markers, velocity annotations, midcourse correction opportunities marked.
**[INFERRED]** — specific layout unknown, but the display had to convey position
between two bodies rather than over Earth's surface.

**Left screens:** Flight plan, consumables timeline, midcourse correction planning.

**Right screens:** Television — onboard TV broadcasts when scheduled.
**Clocks:** GET, time to LOI (Lunar Orbit Insertion), distance to Moon.

### Mode 6: Lunar Orbit Insertion (LOI)

**Center screen:** Burn monitoring display — LOI trajectory showing approach to Moon,
capture into lunar orbit. Plotted against nominal trajectory.

**Left screens:** LOI burn parameters, abort options.

**Right screens:** Telemetry summary or television.

**Clocks:** GET, TIG countdown, burn duration, time to AOS after far-side pass.

### Mode 7: Lunar Orbit

**Center screen:** Lunar ground track — **[INFERRED]** Mercator or polar projection
of the lunar surface with the orbital path shown, landing site marked, AOS/LOS markers
for communications (far side of Moon = loss of signal). This is where the display
departed from the standard Earth Mercator map. Orbital parameters annotated.

**Left screens:** Flight plan, undocking/separation checklist, DOI parameters.

**Right screens:** Television — lunar surface views when available.

**Clocks:** GET, REV counter, AOS/LOS (lunar far-side passes), TIG for DOI/PDI.

### Mode 8: Powered Descent / Landing

**Center screen:** Descent trajectory plot — altitude vs. downrange distance to thelanding site. The Eidophor projections are confirmed to have shown the Apollo 11 LM
descent stage trajectory during the first manned lunar landing. The scribing projectors
traced the actual descent path against a pre-plotted nominal profile. Vehicle icon
tracked in real time. Altitude, velocity, fuel remaining annotations updated every
2 seconds by display operators.

This was the display visible in the famous "landing" photographs and footage.

**Left screens:** LM systems status, abort staging parameters.

**Right screens:** Television — LM cabin camera if available (Apollo 11 had no
landing camera; later missions did).

**Clocks:** GET, altitude, descent rate, fuel remaining time.

### Mode 9: Lunar Surface / EVA

**Center screen:** **[INFERRED]** Lunar surface map showing EVA traverse, or
mission timeline display. The center screen's content during surface operations is
poorly documented. It may have shown a surface map with planned EVA routes and
the astronauts' position, or it may have reverted to a mission timeline view.

**Left screens:** EVA checklist, timeline, consumables.

**Right screens:** Television — the lunar surface TV camera (the iconic live
footage seen worldwide was also displayed here for controllers).

**Clocks:** GET, EVA elapsed time, PLSS consumables time remaining.
### Mode 10: Ascent / Rendezvous

**Center screen:** Rendezvous trajectory plot — LM ascent path relative to CSM orbit.
Plotted as altitude vs. time or altitude vs. range, showing the catch-up geometry.
Terminal phase intercept (TPI) and braking gates marked.

**Left screens:** Rendezvous checklist, relative motion parameters.

**Right screens:** Television — docking camera views when available.

**Clocks:** GET, time to TPI, range to CSM, closing velocity.

### Mode 11: Trans-Earth Injection (TEI) / Trans-Earth Coast

**Center screen:** Departure trajectory from lunar orbit, transitioning to Earth-Moon
return path display (reverse of Mode 5). Midcourse correction opportunities marked.

**Left screens:** TEI burn parameters, entry corridor predictions.

**Right screens:** Television — onboard TV broadcasts.

**Clocks:** GET, time to entry interface, distance to Earth.

### Mode 12: Entry / Reentry

**Center screen:** Entry trajectory plot — altitude vs. range to landing point, or
ground track showing the entry corridor over the Pacific. Entry angle, g-loading,
and range to splashdown annotated. Skip-out boundaries shown.

**Left screens:** Entry parameters, recovery zone weather, landing point prediction.
**Right screens:** Television — recovery ship cameras, helicopter views.

**Clocks:** GET, time to entry interface, time to blackout, time to splashdown.

### Mode 13: Recovery

**Center screen:** Recovery zone map — splashdown point, recovery ship positions,
helicopter tracks. **[INFERRED]** May have been handled by ROCR (Recovery Operations
Control Room) displays rather than the MOCR screens at this phase.

**Left screens:** Post-landing checklist, crew status.

**Right screens:** Television — recovery helicopter and ship cameras (the iconic
footage of capsule floating under parachutes, frogmen attaching flotation collar).

**Clocks:** GET, time since splashdown.

---

## Display Modes Summary Table

| # | Phase | Center Screen | Update Rate | Confirmed? |
|---|-------|---------------|-------------|------------|
| 1 | Pre-Launch | Launch vehicle status | Static/manual | [INFERRED] |
| 2 | Ascent | Altitude vs. range trajectory | Real-time scribe | Confirmed |
| 3 | Earth Orbit | Mercator world map + ground track | Real-time scribe | Confirmed |
| 4 | TLI Burn | Burn trajectory plot | Real-time scribe | [INFERRED] |
| 5 | Translunar Coast | Earth-Moon transfer plot | Periodic update | [INFERRED] |
| 6 | LOI Burn | Approach/capture trajectory | Real-time scribe | [INFERRED] |
| 7 | Lunar Orbit | Lunar surface ground track | Real-time scribe | [INFERRED] || 8 | Powered Descent | Altitude vs. range descent plot | ~2 sec scribe | Confirmed |
| 9 | Lunar Surface/EVA | Surface map or timeline | Manual/periodic | [INFERRED] |
| 10 | Ascent/Rendezvous | Rendezvous trajectory plot | Real-time scribe | [INFERRED] |
| 11 | TEI / Trans-Earth | Return trajectory plot | Periodic update | [INFERRED] |
| 12 | Entry | Entry corridor / range plot | Real-time scribe | [INFERRED] |
| 13 | Recovery | Recovery zone map | Manual | [INFERRED] |

---

## KSA Implementation Plan

### What Maps to Real Solar System / KSA

The KSA-Bridge telemetry suite can support several of these display modes directly:

| MOCR Mode | KSA Equivalent | Data Source |
|-----------|---------------|-------------|
| Earth Orbit ground track | Orbital ground track over Earth | `ksa/telemetry/orbit` + `ksa/telemetry/vehicle` |
| Ascent trajectory | Altitude vs. downrange plot | `ksa/telemetry/altitude` + derived range |
| Powered descent | Altitude vs. range to target | `ksa/telemetry/altitude` + `ksa/telemetry/velocity` |
| Burn monitoring | Delta-V plot during maneuver | `ksa/telemetry/maneuver` + `ksa/telemetry/velocity` |
| Rendezvous | Relative motion plot | Would need new telemetry topics |
| Television | Camera view | Screenshot capture or IVA view |
### Proposed Implementation Screens

Each screen would be a standalone HTML page (consistent with VISION.md — no frameworks),
subscribing to MQTT telemetry and rendering via Canvas or SVG.

#### Screen A: Ground Track Map (Priority 1)

The signature MOCR display. Mercator projection of Earth with:
- Sine-wave orbital ground track (current orbit + 2 future)
- Spacecraft icon moving in real time
- Ground station markers (if KSA defines comm stations)
- AOS/LOS shading for communication coverage
- Orbital parameters overlay (Ap, Pe, Inc, Period)
- Day/night terminator line

**Data:** `ksa/telemetry/orbit`, `ksa/telemetry/vehicle`, `ksa/telemetry/altitude`
**Rendering:** HTML Canvas or SVG, Mercator projection math, real-time animation
**Reference:** This is the display seen in virtually every MOCR photograph

#### Screen B: Ascent/Descent Trajectory Plot (Priority 2)

Altitude vs. downrange distance plot with:
- Pre-plotted nominal trajectory (thin line)
- Actual trajectory traced in real time (bright line, simulating the scribe)
- Abort mode boundaries (ascent) or terrain profile (descent)
- Vehicle icon at current position
- Velocity and altitude annotations updating in real time
**Data:** `ksa/telemetry/altitude`, `ksa/telemetry/velocity`, derived downrange
**Rendering:** Canvas, scrolling plot, "scribe" animation effect (line drawn progressively)
**Dual use:** Works for both launch ascent and powered landing descent

#### Screen C: Transfer Trajectory Plot (Priority 3)

Earth-Moon transfer schematic:
- Earth at one side, Moon at the other
- Curved transfer arc with spacecraft icon
- Distance/velocity annotations
- Midcourse correction opportunity markers
- SOI boundary indicators

**Data:** `ksa/telemetry/orbit`, `ksa/telemetry/velocity`, `ksa/telemetry/altitude`
**Rendering:** Canvas, schematic (not to scale), icon animation

#### Screen D: Flight Plan / Telemetry Summary (Priority 4)

The "left screens" equivalent — a text-heavy display showing:
- Current flight plan step and next steps
- Command history log (recent MQTT messages)
- Key telemetry summary (selectable channel, mirroring any console's data)
- Maneuver planning parameters

**Data:** All `ksa/telemetry/#` topics, aggregated
**Rendering:** DOM text rendering (styled like CRT), scrolling log
#### Screen E: Television / Camera Feed (Priority 5)

The "right screen" equivalent — would display:
- Embedded video/image feed if screenshot capture is available
- Placeholder "NO SIGNAL" or "STANDBY" pattern when no feed
- Could potentially embed a simulator window capture via WebRTC or similar
- Mission event photo gallery as fallback

**Data:** External feed or static content
**Rendering:** Video element or image with periodic refresh

#### Screen F: Chronographic Clock Array (Priority 1)

The nine clocks above the main screens. Already sketched in index.html.
Would become a live, functional display:
- GMT (real wall clock time)
- GET / MET (from `ksa/telemetry/mission-time`)
- TIG (countdown to next maneuver from `ksa/telemetry/maneuver`)
- REV (orbit counter, derived from period and MET)
- AOS / LOS (derived from orbital position and ground station geometry)
- Event timers (configurable)

**Data:** `ksa/telemetry/mission-time`, `ksa/telemetry/maneuver`, `ksa/telemetry/orbit`
**Rendering:** Large seven-segment or fixed-width digit display, Apollo clock aesthetic

---

## Visual Design Notes
### Scribe Effect

The original displays drew trajectory lines by physically scratching metal off glass.
The digital equivalent should simulate this:
- Lines drawn progressively, not all at once
- Slight glow at the drawing point (the "stylus")
- Older portions of the trace slightly dimmer
- Occasional imperfection — the real scribes sometimes produced squiggly lines when
  malfunctioning (per Paul Dye's account)

### Color Palette

The original plotting displays used dichroic filters for color separation. Observed colors
in photographs and restoration references:
- **White/bright cyan** — primary trajectory traces and text
- **Green** — ground track lines, map grid
- **Yellow/amber** — spacecraft icon, target markers
- **Red** — abort boundaries, danger zones
- Background: deep black (projected onto dark screens)

These map well to the existing console palette (#00d4ff blue, #00ff88 green, #ffaa00 amber,
#ff4444 red on #000011 background).

### Screen Aspect Ratio

The center "ten by twenty" was approximately 1:2 (portrait-ish, 10 tall × 20 wide — actually
landscape 2:1). The side screens were closer to 4:3. For the web implementation, responsive
layouts should target these proportions but adapt to the user's actual screen.

---
## Open Research Questions

1. **Exact screen assignments per mission phase.** We know the center screen showed
   trajectory plots and the side screens showed TV and telemetry, but the specific
   assignment of screens 1-5 for each phase (launch, TLI, LOI, etc.) is not definitively
   documented in publicly available sources. The Hendrickson 1967 paper ("Real-Time
   Displays in Mission Control Center") may contain this detail but is not freely
   accessible online.

2. **Powered descent display layout.** The lunar landing trajectory display is the most
   iconic, but the exact graphical layout (altitude vs. range-rate? altitude vs. downrange?
   what abort boundaries were drawn?) varies across accounts. High-resolution photographs
   of the actual display during Apollo 11 would settle this.

3. **Earth orbit rendezvous plots.** During Gemini and early Apollo Earth orbit operations,
   the plotting displays showed rendezvous trajectories. The exact format (polar? Cartesian?
   relative motion?) is unclear from available sources.

4. **Eidophor content sources.** The Eidophor TV projectors could display any video signal.
   During Apollo, what specific camera feeds and data channels were routed to them? Was it
   always network TV pool feeds, or did MCC have dedicated camera angles?

5. **Color capabilities of the plotting system.** Sources confirm dichroic filters were used,
   but the exact number of simultaneous colors and whether colors were switchable per-display
   or fixed per-projector is unclear. The 4 scribing + 2 spotting + 1 background projector
   arrangement suggests up to 7 color layers, but practical usage may have been simpler.

6. **Clock display formats.** The nine chronographic clocks above the screens are visible in
   photographs, but the exact label and function of each clock position varied by mission
   phase. Some sources mention GMT, GET, TIG, and countdown clocks, but the full set of
   nine assignments is not confirmed.

7. **TLI and LOI trajectory plot formats.** These would have been the most complex 3D-to-2D
   projection problems for the plotting system. How were the translunar and transearth
   trajectories represented on a 2D display? Earth-Moon line profile view? Orbital plane
   projection?

---

## Sources

1. **Hackaday** — "The Projectors of Apollo Mission Control" (2019). Detailed breakdown of
   the 7-projector plotting display system, Xenon lamps, diamond-tipped styli, and metalized
   glass slide technology.

2. **Ironflight.com** — Eidophor memories from a former MCC display engineer. First-hand
   account of the Eidophor television projectors, maintenance challenges, and the "Bat Cave"
   rear-projection room (36 × 65 × 15 ft).

3. **Hendrickson, C.L. (1967)** — "Real-Time Displays in Mission Control Center." Technical
   paper describing the display system architecture. Referenced in multiple secondary sources
   but not freely available online. Likely contains definitive screen assignment tables.

4. **CollectSpace forums** — Multiple threads discussing MOCR display restoration, including
   photographs of the projection screens during various mission phases and discussion of
   display modes.

5. **Wikipedia** — "Christopher C. Kraft Jr. Mission Control Center" article. Overview of
   the facility including the five projection screens and their general purpose.

6. **Ars Technica** — Lee Hutchinson's extensive series on the restoration of the Apollo
   Mission Control Room (2019). Includes photographs and descriptions of the front wall
   displays during different mission phases.

7. **Paul Dye** — Former NASA Flight Director. Blog posts and public talks describing
   the display systems from an operator's perspective, including anecdotes about scribe
   malfunctions and display operator workflows.

8. **NASA History Division** — Various Apollo mission reports and press kits that reference
   the MOCR display configuration for specific missions.

---

*This document is a living reference for the KSA MOCR Console Replica Suite projection
screen implementation. It will be updated as new historical sources are discovered and
as implementation progresses.*

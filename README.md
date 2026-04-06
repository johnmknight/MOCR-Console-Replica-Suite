# MOCR Console Replica Suite

**Period-accurate, interactive recreations of Apollo Mission Operations Control Room
flight controller positions — driven by live telemetry from a spaceflight simulator.**

## What This Is

The MOCR Console Replica Suite is a collection of browser-based console displays that
recreate the individual flight controller workstations from NASA's Apollo-era Mission
Operations Control Room (MOCR) in Building 30 at the Johnson Space Center.

Each console is a standalone HTML page that subscribes to live telemetry over MQTT and
displays position-specific data in layouts inspired by the original Hazeltine and
Philco displays. No frameworks, no build tools — just vanilla HTML, CSS, and JavaScript.
Open a page in any browser and it connects.

The telemetry source is [KSA-Bridge](https://github.com/johnmknight/KSA-Bridge), a
companion mod for Kitten Space Agency (KSA) — the spiritual successor to Kerbal Space
Program. KSA-Bridge publishes 13 telemetry topics from the simulator to an MQTT broker.
These consoles subscribe to that data and render it in real time.

## Why This Exists

This project has two intersecting goals:

**Space history preservation.** Faithful recreation of the console layouts, display
conventions, and data responsibilities of each flight controller position — FIDO, GUIDO,
RETRO, EECOM, FLIGHT, CAPCOM, and the rest. The information architecture of Mission
Control was one of humanity's greatest engineering achievements. It deserves to be
understood, not just admired from behind a rope line.

**STEM education.** Students can sit at a virtual console, understand what each flight
controller was actually watching and why, and experience the collaborative decision-making
that got crews to the Moon and back. Because each console runs as a web page, any screen
with a browser becomes a workstation — a classroom of Chromebooks, a museum gallery of
repurposed laptops, or a game room mix of phones, tablets, and monitors. A single PC
running KSA drives all of them over a local network. Since KSA is free and this software
is open-source, the barrier to entry is zero.

## Console Positions — Planned

The full suite will cover all four rows of the MOCR, following the layout documented in
Lee Hutchinson's definitive reference, "Apollo Flight Controller 101: Every console
explained" (Ars Technica, December 24, 2019).

### Row 1 — The Trench (Trajectory & Dynamics)

| Position | Title | Status |
|----------|-------|--------|
| **BOOSTER** | Booster Systems Engineer | Planned |
| **RETRO** | Retrofire Officer | Planned |
| **FDO** | Flight Dynamics Officer | ✅ Working (Apollo + Hard Sci-Fi variants) |
| **GUIDO** | Guidance Officer | Planned |

### Row 2 — Spacecraft Systems

| Position | Title | Status |
|----------|-------|--------|
| **SURGEON** | Flight Surgeon | Planned |
| **CAPCOM** | Capsule Communicator | Planned |
| **EECOM** | Electrical, Environmental & Consumables | Planned |
| **GNC** | Guidance, Navigation & Control (CM) | Planned |
| **TELMU** | Telemetry, Electrical & EVA Mobility Unit | Planned |
| **CONTROL** | LM Guidance, Navigation & Control | Planned |

### Row 3 — Support & Command

| Position | Title | Status |
|----------|-------|--------|
| **INCO** | Instrumentation & Communications | Planned |
| **O&P** | Operations & Procedures | Planned |
| **FLIGHT** | Flight Director | Planned |
| **FAO** | Flight Activities Officer | Planned |
| **NETWORK** | Network Controller | Planned |

### Row 4 — Management & Public Relations

| Position | Title | Status |
|----------|-------|--------|
| **PAO** | Public Affairs Officer | Planned (see also: [KSA-PAO](https://github.com/johnmknight/KSA-PAO)) |

## Current Consoles

### Apollo FDO Console
A faithful recreation of the Flight Dynamics Officer display. Dense columnar data layout
with blue text on dark background, CRT scanline overlay, and responsive scaling from
mobile to 4K. Organized into ODO (orbital dynamics), VEL (velocity), ALT (altitude),
ATT (attitude), VEH (vehicle), RES (resources), MAN (maneuver), and MET (mission elapsed
time) sections.

### Hard Sci-Fi FDO Console
A modern variant featuring a full Three.js globe with real-time orbit rendering, orbital
element markers, trajectory sparklines, and comprehensive data panels. Supports light/dark
themes, event logging, and surface data for Earth, Moon, Mars, Mercury, Jupiter, Venus,
and Saturn.

## Running the Consoles

1. **Start an MQTT broker** (Mosquitto recommended):
   ```
   mosquitto -c mosquitto.conf
   ```

2. **Serve the console files**:
   ```
   cd consoles
   python -m http.server 8088
   ```

3. **Open a console in your browser**:
   - Apollo FDO: `http://127.0.0.1:8088/fdo/fdo-console.html`
   - Hard Sci-Fi FDO: `http://127.0.0.1:8088/fdo-hardscifi/hardscifi-fdo-console.html`

4. **Start KSA with KSA-Bridge** to stream live telemetry, or replay sample data files
   to the broker for development and demos.

## Project Structure

```
MOCR-Console-Replica-Suite/
├── README.md
├── consoles/
│   ├── fdo/                    # Apollo FDO console
│   │   ├── fdo-console.html
│   │   ├── apollo-fdo-console.html
│   │   └── lib/
│   └── fdo-hardscifi/          # Hard Sci-Fi FDO console
│       ├── hardscifi-fdo-console.html
│       ├── data/               # Celestial body surface data
│       └── lib/
├── docs/
│   ├── apollo-mission-control-reference.md
│   └── CONSOLES.md
├── lib/                        # Shared libraries (future)
└── scripts/                    # Dev tools (future)
```

## Data Source

All consoles receive telemetry via MQTT WebSocket (default: `127.0.0.1:9001`). The topic
structure follows:

```
ksa/telemetry/vehicle
ksa/telemetry/orbit
ksa/telemetry/velocity
ksa/telemetry/altitude
ksa/telemetry/attitude
ksa/telemetry/resources
ksa/telemetry/maneuver
ksa/telemetry/mission-time
ksa/bridge/status
```

See [KSA-Bridge](https://github.com/johnmknight/KSA-Bridge) for the full telemetry
specification and sample data files.

## Related Projects

- **[KSA-Bridge](https://github.com/johnmknight/KSA-Bridge)** — The MQTT telemetry
  bridge mod that feeds these consoles. Publishes 13 topics from KSA to Mosquitto.
- **KSA-PAO** — Public Affairs Officer commentary system. Subscribes to the same
  telemetry and generates NASA-style mission commentary with AI voice synthesis.
- **KittenRemoteControl** — RESTful API server mod for KSA. Enables external control
  of the game.

## Background & Advocacy

This project was cited in correspondence with the University of Houston-Clear Lake
Archives regarding access to the NASA JSC History Collection — original Apollo-era
console documentation, panel schematics, and position instrumentation records. That
collection is currently closed to the general public under an October 2024 NASA
headquarters directive. See [NASA-Policy-Work](https://github.com/johnmknight/NASA-Policy-Work)
for details on the access advocacy effort.

## License

MIT

## Author

John M. Knight — johnmknight@gmail.com

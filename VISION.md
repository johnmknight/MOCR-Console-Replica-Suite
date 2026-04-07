# MOCR Console Replica Suite
## Vision Document v0.1

John Knight | April 2026

License: MIT

---

## 1. What This Is

The MOCR Console Replica Suite is a collection of browser-based, period-accurate
recreations of the flight controller workstations from NASA's Apollo Mission Operations
Control Room — the room in Building 30 at the Johnson Space Center where every crewed
Apollo mission was flown from the ground.

Each console is a standalone HTML page. Each one subscribes to live telemetry over MQTT
and displays the data that the real controller at that position would have been watching.
FDO gets trajectory. EECOM gets power and life support. FLIGHT gets the go/no-go board.
The full suite covers all four rows — the trench, spacecraft systems, support and command,
and management — with individual pages for every named position.

There is no server-side rendering. No framework. No build step. Open a file in a browser,
point it at an MQTT broker, and it connects. That simplicity is the point.

## 2. Why It Exists

The Mission Operations Control Room was one of the most sophisticated information
environments ever built. Sixteen named console positions, each with a specific data
surface, specific authority, and a specific role in a decision-making structure that got
human beings to the Moon and brought them home. The controllers in the trench tracked
trajectory while the systems specialists in the second row watched power, life support,
and guidance hardware. The flight director in the third row held ultimate authority. The
information flowed up, the decisions flowed down, and the whole thing worked because
every position knew exactly what it was responsible for and exactly what it was seeing.

That architecture — who sees what, and why — is the real story of Mission Control. Not
the room. Not the consoles. The information design. And that story is almost never told
in a way you can experience firsthand.

Museums put you behind a rope. Documentaries show you the room from above. Books describe
what the controllers did. None of them let you sit down at EECOM and watch the fuel cells
while the flight director polls for go/no-go. None of them let a classroom of students
split into positions and fly a mission together, each one seeing only what their role
demands and learning why that constraint is what made the system work.

This project exists to make that experience possible — for free, on any hardware, for
anyone.

## 3. Design Principles

### 3.1 Any Screen Is a Workstation

Every console runs in a browser. A Chromebook, a phone, a tablet, a repurposed laptop,
a 4K monitor, a Raspberry Pi with a display — anything with a browser and a network
connection becomes a flight controller station. A classroom of 16 devices becomes a
full MOCR. A museum gallery of mismatched screens becomes an interactive exhibit. A
game room becomes mission control on launch night.

This is the most important design decision in the project. If a console requires
specific hardware, a specific OS, a specific screen size, or a specific browser, it
has failed. The whole point is that the barrier to entry is zero.

### 3.2 Position Accuracy Over Visual Spectacle

Each console should show the data that the real controller at that position was
responsible for — organized in a way that reflects the actual decision-making role.
FDO sees trajectory because FDO's job was to know where the spacecraft was going.
EECOM sees power and environmental systems because EECOM's job was to keep the crew
alive. FLIGHT sees the aggregate status of all positions because FLIGHT's job was to
make the call.

The temptation is to make every console show everything. Resist it. The power of the
MOCR was specialization. Each position saw a deliberately limited slice of reality. That
constraint is what made the system work, and it is what makes the experience educational.
A student sitting at RETRO who can only see abort trajectories will understand — viscerally
— what it meant to be the person whose entire job was getting the crew home if everything
went wrong.

### 3.3 No Frameworks, No Build Tools, No Dependencies

Each console is a single HTML file with embedded CSS and JavaScript, plus shared
libraries (MQTT client, Three.js where needed) loaded from local copies. There is no
npm install. There is no webpack. There is no transpilation. A teacher who has never
written code can open the file in a text editor, see what it does, and change a color.

This is a hard constraint, not a preference. The moment the project requires a build
pipeline, it becomes inaccessible to the people it is built for.

### 3.4 Live Data, Open Protocol

The consoles subscribe to MQTT — the same lightweight publish/subscribe protocol used
in real telemetry systems, IoT infrastructure, and industrial automation. The data
source is KSA-Bridge, which publishes 13 telemetry topics from the Kitten Space Agency
spaceflight simulator. KSA uses the real solar system (Earth, Moon, Mars, etc.), making
the telemetry directly analogous to real Apollo mission data. But the consoles do not know or care where the data comes from.
They subscribe to topics on a broker. Any system that publishes the right JSON to the
right topics will drive every console in the suite.

This means the consoles work with live gameplay, with recorded telemetry replayed to
the broker, with hand-crafted test data, or with a completely different data source
that happens to publish compatible messages. The protocol is the interface. Everything
else is decoupled.

### 3.5 The Broker Is the Integration Point

The MQTT broker is the only thing the consoles connect to. They do not connect to the
game. They do not connect to each other. They do not connect to a central server. Each
console is an independent subscriber that renders whatever telemetry arrives on its
topics. This means consoles can be added, removed, restarted, or replaced without
affecting anything else. A crashed browser tab does not take down the mission.

## 4. Who This Is For

### 4.1 Educators

A physics teacher can set up a live orbital mechanics demonstration where students sit
at different positions and watch the same trajectory from different perspectives — FDO
sees the flight path, GUIDO sees the guidance computer's state, RETRO sees the abort
options. A computer science class can examine how real-time data flows from a simulation
through a message broker to multiple independent displays. A history class can
recreate the Apollo 13 crisis with recorded telemetry and understand the decision-making
structure that saved the crew.

The barrier to entry is deliberately as low as it can be. MQTT client libraries exist
for every major language. A minimal subscriber that prints live altitude to the console
is five lines of Python. The consoles themselves are HTML files you open in a browser.
KSA is free. The software is open-source. The total cost to stand up a functioning
Mission Control in a classroom is zero dollars.

### 4.2 Museums and Science Centers

Space Center Houston welcomes 1.3 million visitors and 250,000 students annually.
Kennedy Space Center Visitor Complex, the Smithsonian Air and Space Museum, the
Cosmosphere, and dozens of smaller museums and science centers run space exhibits that
would benefit from an interactive Mission Control experience. Because the consoles run
on any screen with a browser, a museum can deploy them on whatever display hardware
they have — repurposed kiosks, donated laptops, commodity tablets — without specialized
equipment procurement.

### 4.3 Space Enthusiasts and Makers

The same architecture that serves classrooms serves a game room on launch night. Run
KSA on one screen, open console pages on every other screen in the house, and fly a
mission with friends where everyone has a real job. Or build a physical console desk,
mount a monitor, and run FDO full-time as an ambient display. Or wire up an ESP32 to
subscribe to telemetry topics and drive physical gauges. The data is on the broker. What
you build with it is up to you.

### 4.4 Open-Source Developers

Every console is a self-contained example of real-time data visualization driven by
MQTT. The codebase is deliberately readable — verbose comments, no abstractions, no
framework conventions to learn. A developer who wants to build their own telemetry
display can read an existing console, understand exactly how it works, and build from
there.

## 5. The Historical Record Problem

To build these consoles with full historical accuracy — the specific data each position
monitored, the display layouts, the instrumentation conventions, the alarm thresholds —
requires primary source documentation from the Apollo program. Console panel schematics,
Hazeltine display format specifications, position-specific instrumentation lists, and
mission operations procedures.

Much of this documentation exists in the NASA JSC History Collection, housed at the
University of Houston-Clear Lake Archives. As of October 2024, that collection is closed
to the general public under a NASA headquarters directive. Only badged NASA employees,
badged NASA contractors, and UHCL-affiliated researchers may access the materials.
Approved researchers may not photograph, copy, or reproduce anything.

This project was cited in a formal request to UHCL Archives for access to Apollo MOCR
documentation, and subsequently in advocacy correspondence with Florida's federal
congressional delegation regarding the access restrictions. The full advocacy effort
is documented in [NASA-Policy-Work](https://github.com/johnmknight/NASA-Policy-Work).

In the absence of primary source access, the project draws on publicly available
secondary sources — Lee Hutchinson's comprehensive Ars Technica reference, published
NASA technical reports, oral histories, photographs, and the accumulated knowledge of
the spaceflight history community. Where the historical record has gaps, the consoles
will document what is known, what is inferred, and what is invented, so that future
access to primary sources can improve accuracy without requiring a rewrite.

## 6. Relationship to KSA-Bridge

KSA-Bridge is the telemetry source. This project is the display layer.

KSA-Bridge is a C# mod for Kitten Space Agency that reads game state and publishes it
to an MQTT broker. Because KSA uses the real solar system, the telemetry represents
actual orbital mechanics around Earth, the Moon, and other real celestial bodies. It is a dumb pipe — it does not interpret, filter, or present data.
The MOCR Console Replica Suite subscribes to that telemetry and renders it in
historically-informed layouts.

The two projects are maintained separately because they serve different purposes and
have different audiences. KSA-Bridge is infrastructure for anyone building anything
that consumes spaceflight telemetry. The console suite is one specific consumer — the
one that recreates Mission Control.

They share a broker. They share a topic structure. They do not share code, dependencies,
or deployment.

## 7. What Success Looks Like

A teacher sets up 16 Chromebooks in a classroom. Each one opens a different console
page. One student runs KSA on the teacher's desktop. The class flies a mission to orbit.
The student at FDO calls out apoapsis. The student at EECOM watches the fuel cells. The
student at FLIGHT polls for go/no-go. Nobody had to install anything. Nobody had to buy
anything. Nobody had to know how to code. They just opened a browser and became flight
controllers.

That is what this project is for.

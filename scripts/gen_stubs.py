import os
B=r"C:\Users\john_\dev\MOCR-Console-Replica-Suite\consoles"
D=[
("booster","BOOSTER","Booster Systems Engineer","Row 1 - The Trench",[("S-IC","FIRST STAGE",[("THRUST","N"),("CHAMB P","PSI"),("LOX FLOW","KG/S"),("RP-1 FLOW","KG/S"),("BURN T","SEC")]),("S-II","SECOND STAGE",[("THRUST","N"),("CHAMB P","PSI"),("LH2 FLOW","KG/S"),("LOX FLOW","KG/S"),("BURN T","SEC")]),("S-IVB","THIRD STAGE",[("THRUST","N"),("CHAMB P","PSI"),("LH2 FLOW","KG/S"),("LOX FLOW","KG/S"),("BURN T","SEC")]),("SEQ","SEQUENCE EVENTS",[("STAGE",""),("SEP ARM",""),("IGN CMD","")])]),
("retro","RETRO","Retrofire Officer","Row 1 - The Trench",[("ABT","ABORT OPTIONS",[("MODE",""),("TIG","HH:MM:SS"),("DV REQ","M/S"),("IMPACT","LAT/LON")]),("TEI","TRANS-EARTH INJECTION",[("TIG","HH:MM:SS"),("DV REQ","M/S"),("BURN DUR","SEC"),("ENTRY ANG","DEG")]),("RET","REENTRY TRACKING",[("RANGE","KM"),("ENTRY I/F","KM"),("GAMMADOT","DEG/S"),("GLOAD","G")]),("RCV","RECOVERY ZONE",[("ZONE",""),("SPLASH","LAT/LON"),("WEATHER","")])]),
("guido","GUIDO","Guidance Officer","Row 1 - The Trench",[("CMC","CM COMPUTER (PGNCS)",[("PROG",""),("VERB",""),("NOUN",""),("R1",""),("R2",""),("R3","")]),("LGC","LM COMPUTER",[("PROG",""),("VERB",""),("NOUN",""),("R1",""),("R2",""),("R3","")]),("NAV","NAVIGATION STATE",[("POS ERR","M"),("VEL ERR","M/S"),("STATE","")]),("AGS","ABORT GUIDANCE",[("STATUS",""),("POS DEV","M"),("VEL DEV","M/S")])]),
("surgeon","SURGEON","Flight Surgeon","Row 2 - Spacecraft Systems",[("CDR","COMMANDER",[("HR","BPM"),("RESP","BPM"),("ECG",""),("TEMP","DEG F"),("BP","MMHG")]),("CMP","CM PILOT",[("HR","BPM"),("RESP","BPM"),("ECG",""),("TEMP","DEG F"),("BP","MMHG")]),("LMP","LM PILOT",[("HR","BPM"),("RESP","BPM"),("ECG",""),("TEMP","DEG F"),("BP","MMHG")]),("EVA","EVA BIOMEDICAL",[("SUIT P","PSI"),("O2 FLOW","LB/HR"),("METAB","BTU/HR")])]),
("capcom","CAPCOM","Capsule Communicator","Row 2 - Spacecraft Systems",[("COM","VOICE COMMUNICATIONS",[("UPLINK",""),("DOWNLINK",""),("QUALITY",""),("MODE","")]),("MSG","MESSAGE LOG",[("LAST TX",""),("LAST RX",""),("PENDING","")]),("PAD","VOICE PAD",[("READBACK",""),("CONFIRM","")]),("GNG","GO/NO-GO STATUS",[("POLL",""),("RESULT",""),("CREW ACK","")])]),
("eecom","EECOM","Electrical, Environmental & Consumables","Row 2 - Spacecraft Systems",[("EPS","ELECTRICAL POWER",[("FC1","AMPS"),("FC2","AMPS"),("FC3","AMPS"),("BUS A","VDC"),("BUS B","VDC"),("TOTAL W","WATTS")]),("CRY","CRYOGENICS",[("O2 TK1","PCT"),("O2 TK2","PCT"),("H2 TK1","PCT"),("H2 TK2","PCT"),("O2 FLOW","LB/HR"),("H2 FLOW","LB/HR")]),("ECS","ENVIRONMENTAL CONTROL",[("CABIN P","PSI"),("CABIN T","DEG F"),("PPO2","MMHG"),("CO2 PP","MMHG"),("HUMIDITY","PCT")]),("CON","CONSUMABLES",[("O2 RMNG","LBS"),("H2 RMNG","LBS"),("H2O RMNG","LBS"),("MARGIN","HRS")])]),
("gnc","GNC","Guidance, Navigation & Control (CM)","Row 2 - Spacecraft Systems",[("RCS","REACTION CONTROL",[("QUAD A","PCT"),("QUAD B","PCT"),("QUAD C","PCT"),("QUAD D","PCT"),("THRST","")]),("SPS","SERVICE PROPULSION",[("STATUS",""),("FUEL","PCT"),("OXID","PCT"),("CHAMB P","PSI"),("GIMBAL P","DEG"),("GIMBAL Y","DEG")]),("IMU","INERTIAL MEAS UNIT",[("STATUS",""),("DRIFT X","DEG/HR"),("DRIFT Y","DEG/HR"),("DRIFT Z","DEG/HR")]),("ATT","ATTITUDE",[("HDG","DEG"),("PITCH","DEG"),("ROLL","DEG"),("RATE P","DEG/S"),("RATE Y","DEG/S"),("RATE R","DEG/S")])]),
("telmu","TELMU","Telemetry, Electrical & EVA Mobility Unit","Row 2 - Spacecraft Systems",[("LPS","LM POWER SYSTEMS",[("BATT 1","VDC"),("BATT 2","VDC"),("BATT 3","VDC"),("BATT 4","VDC"),("ASC BATT","VDC"),("BUS V","VDC"),("AMPS","A")]),("LEC","LM ENVIRONMENTAL",[("CABIN P","PSI"),("CABIN T","DEG F"),("PPO2","MMHG"),("CO2 PP","MMHG"),("SUIT P","PSI")]),("EMU","EVA SUIT SYSTEMS",[("PLSS O2","PCT"),("PLSS BAT","PCT"),("SUIT P","PSI"),("COOL H2O","PCT"),("FEEDH2O","PCT")]),("LCN","LM CONSUMABLES",[("O2 ASC","LBS"),("O2 DES","LBS"),("H2O ASC","LBS"),("H2O DES","LBS"),("MARGIN","HRS")])]),
("control","CONTROL","LM Guidance, Navigation & Control","Row 2 - Spacecraft Systems",[("DPS","DESCENT PROPULSION",[("STATUS",""),("THRUST","PCT"),("FUEL","PCT"),("OXID","PCT"),("CHAMB P","PSI")]),("APS","ASCENT PROPULSION",[("STATUS",""),("FUEL","PCT"),("OXID","PCT"),("CHAMB P","PSI")]),("LRR","LANDING RADAR",[("ALT","FT"),("VEL X","FT/S"),("VEL Y","FT/S"),("VEL Z","FT/S"),("LOCK","")]),("RCS","LM REACTION CONTROL",[("SYS A","PCT"),("SYS B","PCT"),("THRST",""),("ATT HOLD","")])]),
("inco","INCO","Instrumentation & Communications","Row 3 - Support & Command",[("UPL","UPLINK",[("CMD RATE","BPS"),("SIGNAL","DBM"),("LOCK",""),("ERRORS","")]),("DNL","DOWNLINK",[("TLM RATE","KBPS"),("SIGNAL","DBM"),("BER",""),("FORMAT","")]),("VID","VIDEO",[("STATUS",""),("SOURCE",""),("QUALITY","")]),("ANT","ANTENNA / TRACKING",[("STATION",""),("AZ","DEG"),("EL","DEG"),("RANGE","KM"),("HANDOVER","")])]),
("op","O&P","Operations & Procedures","Row 3 - Support & Command",[("FLT","FLIGHT PLAN",[("STEP",""),("STATUS",""),("REF DOC","")]),("CHG","FLIGHT PLAN CHANGES",[("PENDING",""),("APPROVED",""),("REJECTED","")]),("LOG","OPERATIONS LOG",[("LAST ENTRY",""),("SHIFT",""),("GMT","HH:MM:SS")]),("REQ","DATA REQUESTS",[("PRINTOUT",""),("PLAYBACK",""),("STATUS","")])]),
("flight","FLIGHT","Flight Director","Row 3 - Support & Command",[("GNG","GO/NO-GO BOARD",[("BOOSTER",""),("RETRO",""),("FDO",""),("GUIDO",""),("SURGEON",""),("CAPCOM",""),("EECOM",""),("GNC",""),("TELMU",""),("CONTROL",""),("INCO",""),("FAO",""),("NETWORK","")]),("MIS","MISSION STATUS",[("PHASE",""),("RULE",""),("DECISION","")]),("ABT","ABORT STATUS",[("ARM",""),("MODE",""),("AUTHORITY","")]),("SHF","SHIFT MANAGEMENT",[("FLIGHT ID",""),("TEAM",""),("HANDOVER",""),("ON DUTY","HRS")])]),
("fao","FAO","Flight Activities Officer","Row 3 - Support & Command",[("TLN","MISSION TIMELINE",[("CURRENT",""),("NEXT",""),("T+","HH:MM:SS"),("DELTA","MIN")]),("EVT","UPCOMING EVENTS",[("EVENT 1",""),("T-","HH:MM:SS"),("EVENT 2",""),("T-","HH:MM:SS")]),("CKL","CHECKLISTS",[("ACTIVE",""),("STEP",""),("CREW ACK","")]),("SLP","CREW SCHEDULE",[("WAKE","HH:MM"),("SLEEP","HH:MM"),("MEAL","HH:MM"),("EVA WIN","HH:MM")])]),
("network","NETWORK","Network Controller","Row 3 - Support & Command",[("STA","TRACKING STATIONS",[("ACTIVE",""),("NEXT AOS","HH:MM:SS"),("LOS IN","MIN"),("COVERAGE","PCT")]),("LNK","DATA LINKS",[("UPLINK",""),("DOWNLINK",""),("BACKUP",""),("LATENCY","MS")]),("MCC","MCC SYSTEMS",[("MAINFRAME",""),("BACKUP",""),("DISPLAYS",""),("COMMS","")]),("ISS","ISSUES",[("OPEN",""),("PRIORITY",""),("LAST FIX","")])]),
("pao","PAO","Public Affairs Officer","Row 4 - Management",[("NAR","NARRATION",[("STATUS",""),("BROADCAST",""),("AUDIENCE","")]),("EVT","MISSION EVENTS",[("LAST",""),("CURRENT",""),("NEXT","")]),("MED","MEDIA",[("TV FEED",""),("RADIO",""),("PRESS","")]),("LOG","COMMENTARY LOG",[("ENTRIES",""),("LAST TX","HH:MM:SS")])]),
]

def sjs(secs):
    r=[]
    for i,(c,l,fs) in enumerate(secs):
        if i>0: r.append("            output += '\\n';")
        r.append(f"            output += '{c} - {l}\\n';")
        r.append(f"            output += '---------------------------------------------\\n';")
        for fn,u in fs:
            if u: r.append(f"            output += '{fn.ljust(8)} ' + formatNumber(null) + '  {u}\\n';")
            else: r.append(f"            output += '{fn.ljust(8)} ---\\n';")
    return "\n".join(r)

def html(cid,acr,ttl,row,secs):
    sj=sjs(secs)
    t = '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
    t += '    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    t += '    <title>Apollo Mission Control - '+ttl+'</title>\n'
    t += '    <script src="../fdo/lib/mqtt.min.js"></script>\n    <style>\n'
    t += '        :root {\n            --base-font-size: clamp(14px, 2vw, 24px);\n'
    t += '            --header-font-size: clamp(16px, 2.5vw, 28px);\n'
    t += '            --padding-base: clamp(8px, 2vw, 20px);\n            --border-width: 2px;\n        }\n'
    t += '        * { margin: 0; padding: 0; box-sizing: border-box; }\n        html { font-size: 16px; }\n'
    t += '        body {\n            background-color: #000011; color: #00d4ff;\n'
    t += '            font-family: \'Courier New\', \'Courier\', monospace;\n'
    t += '            font-size: var(--base-font-size); line-height: 1.3; overflow: hidden;\n        }\n'
    t += '        .container {\n            display: flex; flex-direction: column; height: 100vh;\n'
    t += '            border: var(--border-width) solid #00d4ff;\n'
    t += '            background: linear-gradient(135deg, #000011 0%, #001133 100%);\n        }\n'
    t += '        .header {\n            padding: var(--padding-base);\n'
    t += '            border-bottom: var(--border-width) solid #00d4ff;\n'
    t += '            background-color: rgba(0, 20, 51, 0.95);\n'
    t += '            text-align: center; font-weight: bold;\n'
    t += '            letter-spacing: clamp(1px, 0.2vw, 3px);\n'
    t += '            font-size: var(--header-font-size);\n            position: relative; flex-shrink: 0;\n        }\n'
    t += '        .header-right {\n            position: absolute; top: var(--padding-base); right: var(--padding-base);\n'
    t += '            display: flex; align-items: center; gap: clamp(4px, 1vw, 10px);\n'
    t += '            flex-wrap: wrap; justify-content: flex-end;\n        }\n'
    t += '        .status-indicator {\n            display: inline-block; width: clamp(8px, 1.2vw, 14px); height: clamp(8px, 1.2vw, 14px);\n'
    t += '            border-radius: 50%; animation: blink 1s infinite;\n        }\n'
    t += '        .status-connected { background-color: #00ff00; }\n        .status-disconnected { background-color: #ff0000; }\n'
    t += '        @keyframes blink {\n            0%, 49%, 100% { opacity: 1; }\n            50%, 99% { opacity: 0.3; }\n        }\n'
    t += '        .console-wrapper {\n            flex: 1; overflow-y: auto; overflow-x: hidden;\n'
    t += '            padding: var(--padding-base); white-space: pre-wrap; word-wrap: break-word;\n'
    t += '            font-family: \'Courier New\', \'Courier\', monospace;\n'
    t += '            line-height: clamp(1.3, 1.6vw, 1.8); font-size: var(--base-font-size);\n        }\n'
    t += '        .scanlines {\n            position: fixed; top: 0; left: 0; width: 100%; height: 100%;\n'
    t += '            background: repeating-linear-gradient(0deg, rgba(0,0,0,0.15), rgba(0,0,0,0.15) 1px, transparent 1px, transparent 2px);\n'
    t += '            pointer-events: none; z-index: 1000;\n        }\n'
    t += '        .console-wrapper::-webkit-scrollbar { width: clamp(6px, 1.2vw, 14px); }\n'
    t += '        .console-wrapper::-webkit-scrollbar-track { background: rgba(0, 212, 255, 0.1); }\n'
    t += '        .console-wrapper::-webkit-scrollbar-thumb { background: #00d4ff; border-radius: 2px; }\n'
    t += '        @media (max-width: 768px) {\n            :root {\n'
    t += '                --base-font-size: clamp(11px, 3vw, 16px);\n'
    t += '                --header-font-size: clamp(13px, 3.5vw, 18px);\n'
    t += '                --padding-base: clamp(6px, 2.5vw, 16px);\n            }\n'
    t += '            .header-right { position: static; justify-content: center; margin-top: clamp(4px, 1vw, 8px); width: 100%; }\n        }\n'
    t += '        @media (min-width: 1920px) { .console-wrapper { column-count: 2; column-gap: clamp(20px, 3vw, 40px); } }\n'
    t += '        @media (min-width: 2560px) { .console-wrapper { column-count: 3; column-gap: clamp(30px, 3vw, 50px); } }\n'
    t += '        @media (hover: none) and (pointer: coarse) {\n            :root { --padding-base: clamp(10px, 3vw, 24px); }\n'
    t += '            .header-right { gap: clamp(6px, 2vw, 16px); }\n        }\n    </style>\n</head>\n'
    t += '<body>\n    <div class="container">\n        <div class="header">\n'
    t += '            APOLLO MISSION CONTROL - '+acr+'\n'
    t += '            <div class="header-right">\n'
    t += '                <span class="status-indicator status-disconnected" id="statusIndicator"></span>\n'
    t += '                <span id="connectionStatus">DISCONNECTED</span>\n'
    t += '            </div>\n        </div>\n'
    t += '        <div class="console-wrapper" id="consoleOutput"></div>\n'
    t += '    </div>\n    <div class="scanlines"></div>\n    <script>\n'
    t += '        // =================================================================\n'
    t += '        // '+acr+' - '+ttl+'\n'
    t += '        // '+row+'\n'
    t += '        //\n'
    t += '        // STUB CONSOLE - Position-specific data sections are placeholders.\n'
    t += '        // MQTT subscription is active. Vehicle, status, and MET update live.\n'
    t += '        // All other fields display defaults until position-specific telemetry\n'
    t += '        // parsing is implemented.\n'
    t += '        // =================================================================\n'
    t += '        var client = null;\n        var telemetryData = {};\n'
    t += '        var RAD2DEG = 180 / Math.PI;\n'
    t += '        function formatNumber(num, width, decimals) {\n'
    t += '            width = width || 8; decimals = decimals || 2;\n'
    t += '            if (num === undefined || num === null) return \'---\'.padStart(width);\n'
    t += '            if (isNaN(num)) return \'---\'.padStart(width);\n'
    t += '            return num.toFixed(decimals).padStart(width);\n        }\n'
    t += '        function formatTime(seconds) {\n'
    t += '            if (!seconds || isNaN(seconds)) return \'--:--:--\';\n'
    t += '            var h = Math.floor(seconds / 3600);\n'
    t += '            var m = Math.floor((seconds % 3600) / 60);\n'
    t += '            var s = Math.floor(seconds % 60);\n'
    t += '            return String(h).padStart(2, \'0\') + \':\' + String(m).padStart(2, \'0\') + \':\' + String(s).padStart(2, \'0\');\n        }\n'
    t += '        function updateDisplay() {\n            var output = \'\';\n'
    t += '            output += \'VEH - VEHICLE\\n\';\n'
    t += '            output += \'---------------------------------------------\\n\';\n'
    t += '            output += \'NAME \' + (telemetryData.vehicleName || \'---\').padEnd(20) + \'\\n\';\n'
    t += '            output += \'STAT \' + (telemetryData.vehicleStatus || \'---\').padEnd(20) + \'\\n\';\n'
    t += '            output += \'MASS \' + formatNumber(telemetryData.vehicleMass) + \'  KG\\n\\n\';\n'
    t += '            output += \'MET - MISSION ELAPSED TIME\\n\';\n'
    t += '            output += \'---------------------------------------------\\n\';\n'
    t += '            output += \'TIME \' + formatTime(telemetryData.missionTime) + \'\\n\\n\';\n'
    t += sj + '\n'
    t += '            document.getElementById(\'consoleOutput\').textContent = output;\n        }\n'
    t += '        function connectMQTT() {\n'
    t += '            client = mqtt.connect(\'ws://127.0.0.1:9001\');\n'
    t += '            client.on(\'connect\', function() {\n'
    t += '                document.getElementById(\'statusIndicator\').className = \'status-indicator status-connected\';\n'
    t += '                document.getElementById(\'connectionStatus\').textContent = \'CONNECTED\';\n'
    t += '                client.subscribe(\'ksa/telemetry/#\');\n'
    t += '                client.subscribe(\'ksa/bridge/status\');\n            });\n'
    t += '            client.on(\'message\', function(topic, payload) {\n'
    t += '                try {\n                    var data = JSON.parse(payload.toString());\n'
    t += '                    if (topic.includes(\'vehicle\')) {\n'
    t += '                        telemetryData.vehicleName = data.name;\n'
    t += '                        telemetryData.vehicleStatus = data.status;\n'
    t += '                        telemetryData.vehicleMass = data.mass;\n                    }\n'
    t += '                    else if (topic.includes(\'mission-time\') || topic.includes(\'mission_time\')) {\n'
    t += '                        telemetryData.missionTime = data.value;\n                    }\n'
    t += '                    // TODO: Add position-specific telemetry parsing here.\n'
    t += '                    updateDisplay();\n'
    t += '                } catch (e) { console.error(\'Error:\', e); }\n            });\n'
    t += '            client.on(\'error\', function(err) {\n'
    t += '                document.getElementById(\'statusIndicator\').className = \'status-indicator status-disconnected\';\n'
    t += '                document.getElementById(\'connectionStatus\').textContent = \'ERROR\';\n            });\n'
    t += '            client.on(\'close\', function() {\n'
    t += '                document.getElementById(\'statusIndicator\').className = \'status-indicator status-disconnected\';\n'
    t += '                document.getElementById(\'connectionStatus\').textContent = \'DISCONNECTED\';\n            });\n        }\n'
    t += '        setTimeout(function() { connectMQTT(); updateDisplay(); }, 100);\n'
    t += '        window.addEventListener(\'beforeunload\', function() { if (client) client.end(); });\n'
    t += '    </script>\n</body>\n</html>'
    return t

for cid,acr,ttl,row,secs in D:
    d=os.path.join(B,cid)
    os.makedirs(d,exist_ok=True)
    p=os.path.join(d,cid+"-console.html")
    with open(p,"w",encoding="utf-8") as f: f.write(html(cid,acr,ttl,row,secs))
    print("  "+cid+"/"+cid+"-console.html")

print("\nDone: "+str(len(D))+" consoles.")

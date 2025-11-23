# Network Packet Visualizer & Basic Traffic Analyzer

**Overview**
A simple learning project that demonstrates core networking concepts by capturing (simulated) packets,
analyzing traffic, and providing a lightweight web dashboard to visualize results.

**Features**
- Packet capture (simulated)
- Traffic analysis and simple statistics
- Web dashboard (Flask) to view results and charts
- CLI utilities to run capture and analysis
- Unit tests for analyzer module

**Technologies**
- Python 3.9+
- Flask (for the web UI)
- SQLite (optional, for storing summaries)
- JavaScript + Chart.js (frontend charts)

**Run (development)**
1. Create virtualenv: `python -m venv venv && source venv/bin/activate`
2. Install: `pip install -r requirements.txt`
3. Start capture (simulated): `python -m capture.run_capture --outfile data/packets.json --count 200`
4. Analyze: `python -m analyzer.run_analysis --infile data/packets.json --outfile data/summary.json`
5. Start web UI: `python app.py`
6. Open http://127.0.0.1:5000

**Notes**
- This project provides simulated packet capture for ease of use (no root privileges required).
- For real capture (pcap/live), integrate `scapy` or `pyshark` and adjust `capture/` module.


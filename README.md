# 🌀 DemonLion Wave Lab – DL0V1

## Real-Time Mic • Camera Motion • RF (WiFi) Wave Visualiser

The **DemonLion Wave Lab** is a multi-sensor, real-time wave visualisation system that merges **audio**, **optical**, and **radio** signals into a unified oscilloscope-style interface.

It allows you to *see* how the world of waves behaves — sound waves, camera motion, and WiFi RF fields — forming the foundation of:

* WiFi radar
* Through-wall sensing
* RF motion detection
* Signal intelligence (SIGINT)
* AI-based sensor fusion
* Cyber-physical hacking tools

This is **DL0V1** — the first experimental build.

---

## 🚀 Features

### 🎤 Wave 1 — Microphone (Audio Energy)

* Captures audio input
* Converts amplitude into a smooth waveform

### 📸 Wave 2 — Camera Motion

* Detects motion by comparing brightness changes across video frames

### 🔮 Wave 3 — Synthetic Sine Wave

* Adjustable amplitude, frequency, and phase

### 📡 Wave 4 — WiFi RSSI (Radio Signal Strength)

* Python backend reads RSSI, Noise, SNR using macOS `airport -I`
* Frontend displays real-time RF fluctuations

### 🧬 Merged Wave

Combine waves using:

* Sum (1+2+3+4)
* Average
* Difference modes (1–2, 1–3, 1–4)

---

## 📁 Project Structure

```
WAVE_LAB_DL0V1/
│
├── demonlion_wave_lab_full.html     # Main frontend interface
├── wifi_wave_server.py              # Python backend for WiFi RSSI
├── camera_wave.html                 # Minimal camera motion test
├── README.md                        # Project documentation
└── .gitignore (optional)
```

---

## 🧠 How Each Wave Works

### Mic Wave

* Uses Web Audio API
* Computes RMS (energy)
* Normalized into visible waveform

### Camera Motion Wave

* Captures video frames
* Computes brightness differences
* Outputs motion intensity signal

### Synthetic Wave

* Pure sine generator
* Adjustable frequency, amplitude, phase

### WiFi RSSI Wave

* Python script parses macOS WiFi diagnostics
* Sends RSSI/Noise/SNR as JSON
* Delta-based algorithm visualizes subtle RF changes

---

## 🛠 How to Run Locally

### 1️⃣ Start WiFi Server (Terminal 1)

```bash
python3 wifi_wave_server.py
```

You should see:

```
[wifi_wave_server] Starting on http://localhost:5000/wifi
```

### 2️⃣ Start Local Web Server (Terminal 2)

```bash
python3 -m http.server 8000
```

### 3️⃣ Open the Wave Lab

Navigate to:

```
http://localhost:8000/demonlion_wave_lab_full.html
```

Allow **Camera** + **Microphone** permissions.

---

## ⚠ Notes & Limitations

* WiFi RSSI changes are small by nature
* Movement between router and laptop affects RF wave strongly
* Chrome recommended for full permissions
* GitHub Pages hosting works but with limited sensors

---

## 🔮 Future Versions (DL0V2 → DL0V3)

* Bluetooth RSSI Wave
* Ultrasound motion/sonar
* Magnetic-field readings
* WiFi CSI (advanced RF multipath data)
* AI interpretation of waves
* Through-wall motion classification
* RF environment mapping

---

## 👤 Author

**0xDL01 (DemonLion)**
AI • Cybersecurity • RF Sensing • Offensive Engineering
MSc Artificial Intelligence & Its Applications — University of Essex

GitHub: [https://github.com/0xDL01](https://github.com/0xDL01)
Project Page: [https://0xdl01.github.io/WAVE_LAB_DL0V1/](https://0xdl01.github.io/WAVE_LAB_DL0V1/)

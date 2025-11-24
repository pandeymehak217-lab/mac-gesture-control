# 🖐️ Mac Gesture Control

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Platform](https://img.shields.io/badge/Platform-macOS-black)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hands-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A lightweight, real-time gesture-based control system that lets you **control your entire Mac using hand gestures** — no mouse, no trackpad.

Built using **MediaPipe**, **OpenCV**, **cvzone**, and **PyAutoGUI**.


## 🚀 Features

- 🖱️ Move mouse with finger tracking  
- 👌 Pinch to Click  
- ✌️ Two-finger scroll  
- 🔊 Volume control using finger distance  
- 🎵 Palm → Fist = Play/Pause (YouTube, Spotify, VLC)  
- 👉👈 Swipe left/right = Next / Previous track  
- 🎥 Works in **real-time**, locally, with no cloud processing  
- 🧠 Easily customizable gesture rules (inside `gesture_control.py`)  

---

## ✋ Supported Gestures

| Gesture | Action |
|--------|--------|
| 👉 Index Finger | Move Cursor |
| 👌 Pinch | Click |
| ✌️ Two Fingers | Scroll |
| 🤏 Finger Distance | Volume Control |
| 🖐 → ✊ Palm to Fist | Play / Pause |
| 👈👉 Swipe | Next / Previous |

---

## ⚙️ Tech Stack

- Python 3.11  
- OpenCV 4.x  
- MediaPipe Hands  
- PyAutoGUI  
- NumPy  
- cvzone  

---

## 📦 Installation

### 1️⃣ Clone the repo  
```bash
git clone https://github.com/pandeymehak217-lab/mac-gesture-control.git
cd mac-gesture-control
```

### 2️⃣ Create virtual environment  
```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies  
```bash
pip install opencv-python mediapipe pyautogui numpy cvzone
```

⚠️ If `mediapipe` fails on M1/M2/M3:  
```bash
pip install mediapipe-silicon
```

---

## ▶️ Run the Program  
```bash
python gesture_control.py
```

### 📷 macOS Permissions
Make sure Python/Terminal has webcam permission:

**System Settings → Privacy & Security → Camera → Enable for Terminal**

---

## 📁 Project Structure
```
mac-gesture-control/
│── gesture_control.py
│── README.md
│── Screenshot-2025-11-24.png
│── assets/
│     └── logo.png
│── demo/
│     └── demo.gif
│── venv/
│── requirements.txt
```

---

## 🧩 Customizing Gestures  
Edit inside:

```
gesture_control.py
```

You can change:

- gesture → action mapping  
- volume sensitivity  
- scroll speed  
- swipe threshold  
- add custom hand shapes  

---

## 📝 Notes
- Works best on **Python 3.10–3.11**  
- macOS (Intel + M1/M2/M3) supported  
- MediaPipe runs ON-DEVICE → No internet needed  
- Tune gesture sensitivity inside code  

---

## 📄 License
MIT License  

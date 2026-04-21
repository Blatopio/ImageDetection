# 🧠 Image Detection System (Glass Defect & Plate Number)

This project is an AI-powered image detection system using **YOLO (Ultralytics)** to detect:

* 🔍 Glass defects (quality inspection)
* 🚗 Plate numbers (object detection & cropping)

The system is deployed using **Gradio** for an interactive web interface.

---

## 🚀 Features

### 🧪 Glass Defect Detection

* Detects defects on glass products
* Highlights defect areas with bounding boxes
* Provides:

  * Detection summary
  * Visual annotation
  * Status message (Defect / No Defect)

👉 Implemented in: 

---

### 🚗 Plate Number Detection

* Detects plate regions in images
* Crops detected plate area
* Outputs:

  * Annotated image
  * Cropped plate image
  * Detection summary

👉 Implemented in: 

---

## 🖥️ Demo Applications

### 1. Glass Detection App

👉 File: 

**Features:**

* Upload glass image
* Click **DETECT**
* View:

  * Annotated result
  * Summary
  * Status (HTML alert)

---

### 2. Plate Detection App

👉 File: 

**Features:**

* Upload image
* Detect plate number
* View:

  * Detection result
  * Cropped plate
  * Summary

---

## 🧠 Tech Stack

* **Python**
* **YOLO (Ultralytics)**
* **OpenCV**
* **NumPy**
* **PIL**
* **Gradio**

---

## 📦 Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Install Dependencies

```bash
pip install ultralytics opencv-python numpy pillow gradio
```

---

## ▶️ How to Run

### Run Glass Detection

```bash
python glass_main.py
```

### Run Plate Detection

```bash
python plate_main.py
```

Then open the local Gradio URL in your browser.

---

## 📁 Project Structure

```
├── detections.py        # Core detection logic
├── glass_main.py       # Glass defect UI (Gradio)
├── plate_main.py       # Plate detection UI (Gradio)
├── bestglass.pt        # YOLO model (glass)
├── bestplate.pt        # YOLO model (plate)
└── README.md
```

---

## ⚠️ Notes & Improvements

### Current Limitations:

* No handling if **no object detected (boxes = None)**
* Plate cropping assumes at least one detection
* Class mapping is static

### Suggested Improvements:

* Add safety check for `results.boxes`
* Support multiple detections
* Deploy as web app (Streamlit / FastAPI)
* Add real-time camera detection

---

## 🎯 Use Cases

* 🏭 Industrial quality control (glass inspection)
* 🚗 Smart parking / vehicle monitoring
* 🤖 AI-based automation systems

---

## 👨‍💻 Author : Alghi

Developed as part of AI Engineering learning journey.

---
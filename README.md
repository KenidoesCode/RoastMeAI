# RoastMe.AI 🔥

👉 A Streamlit-based AI app that analyzes your face and roasts you with zero mercy.  
Built by **Pranauv** as a fun way to learn Computer Vision, Feature Extraction, and AI pipelines.

---

## 🔗 Live Demo

**Use the app here:**  
https://roastmeai-keni.streamlit.app

⚠️*(Warning: This app does not care about your feelings.)*

---

## Overview

RoastMe.AI takes an uploaded image (or live camera feed), extracts emotions and simple visual cues, and then generates a structured roast using a custom “Inferno Roast Engine.”

This project was built to make Machine Learning **fun**, **practical**, and **painfully honest**.

---

## Features

- Image upload + live camera support  
- Emotion detection using DeepFace  
- Lightweight feature extraction  
- Custom dark-humor roast generator  
- Fully styled Streamlit UI  
- Warning popup (emotional damage disclaimer)

---

## Tech Stack

**Frontend / UI**  
- Streamlit  
- Custom CSS  
- Javascript alert injection  

**AI / CV**  
- OpenCV  
- DeepFace (emotion analysis)  
- Numpy  
- Pillow  

**Backend Logic**  
- Python  
- Custom feature extractor  
- “Inferno Roast Engine”

---

## What I Learned

### 1. Computer Vision Basics  
- Reading and preprocessing images  
- Converting RGB/BGR formats  
- Understanding how emotion models work

### 2. Feature Engineering  
- Turning raw image data into structured attributes  
- Designing roast conditions based on features

### 3. Streamlit App Development  
- Page routing with radio buttons  
- Handling file uploads  
- Live camera capture  
- Injecting HTML/JS for warnings  

### 4. Full AI Pipeline Design  
- Image → Features → Roast Engine → Output  
- Error handling (no face detected)  
- Maintaining a fast and lightweight workflow

### 5. Deployment  
- Fixing dependency conflicts  
- Working with Streamlit Cloud  
- Solving OpenCV + DeepFace + FER issues  

---

## Installation (Local)

```bash
pip install -r requirements.txt
streamlit run app.py

```
## Folder Structure
.
│── app.py
│── feature_extractor.py
│── roast_engine.py
│── requirements.txt
│── README.md

### Disclaimer

This project is meant for fun and learning.
Roasts are generated automatically and are not targeted personally.

If you get emotionally damaged, that is between you and your therapist.
pip install -r requirements.txt
streamlit run app.py

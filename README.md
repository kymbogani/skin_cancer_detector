# 🔬 DermaScan AI
### AI-Powered Skin Condition Detector

---

## 📌 What is this?

DermaScan AI is a web application that analyzes skin photos using AI and tells you the possible condition of your skin.

Simply upload or take a photo → the AI predicts the result instantly.

---

## 🎯 Skin Conditions It Can Detect

| Icon | Condition | Risk | What it means |
|------|-----------|------|---------------|
| 🔵 | Normal | No Risk | Your skin looks healthy |
| 🟢 | Benign | Low Risk | Non-cancerous, monitor it yearly |
| 🟡 | Premalignant | Medium Risk | See a doctor within 2-4 weeks |
| 🔴 | Malignant | High Risk | See a doctor immediately |

---

## ✅ What You Need Before Starting

### 1. Install Python 3.11
> ⚠️ Must be Python 3.11 — other versions will NOT work

Download here:
https://www.python.org/downloads/release/python-3119/

During installation → check ✅ **"Add Python to PATH"**

---

### 2. Install Git
Download here:
https://git-scm.com/downloads

---

### 3. Download the AI Model Files from Kaggle

> The model is too large for GitHub so you must download it manually.

Go to this link and download these 3 files:
https://www.kaggle.com/code/boganikymeddiebong/notebookf410c756f4/output

Files to download:
✅ skin_cancer_model.keras
✅ label_classes.pkl
✅ class_indices.pkl


---

## 🚀 How to Run the App

### Step 1 — Clone the project to your computer
Open terminal or command prompt and run:
```bash
git clone https://github.com/kymbogani/skin_cancer_detector.git
```

---

### Step 2 — Open the project folder
```bash
cd skin_cancer_detector
```

---

### Step 3 — Create a virtual environment
```bash
python -m venv venv
```

---

### Step 4 — Activate the virtual environment

**If you are on Windows:**
```bash
venv\Scripts\activate
```

**If you are on Mac or Linux:**
```bash
source venv/bin/activate
```

After activation you will see **(venv)** in your terminal like this:
(venv) C:\Users\yourname\skin_cancer_detector>

---

### Step 5 — Install required packages
```bash
pip install -r requirements.txt
```
Wait for it to finish installing. This may take a few minutes.

---

### Step 6 — Place the model files

Take the 3 files you downloaded from Kaggle and put them inside the **model** folder:
skin_cancer_detector/
└── model/
├── skin_cancer_model.keras   ← paste here
├── label_classes.pkl         ← paste here
└── class_indices.pkl         ← paste here

---

### Step 7 — Start the app
```bash
python app.py
```

You will see this message when it is ready:
Loading model...
Model loaded!
Classes: ['Benign', 'Malignant', 'Premalignant']

Running on http://localhost:5000

---

### Step 8 — Open in your browser

Type this in your browser address bar:

🎉 The app is now running and ready to use!

---

## 🛑 To Stop the App

Go back to terminal and press:

Ctrl + C
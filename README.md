# 📄 Text Extraction Model (OCR Pipeline)

An end-to-end **Optical Character Recognition (OCR) system** that extracts text from images using **advanced image preprocessing**, **deep-learning-based text detection**, and **OCR recognition**.

This project is structured using a **modular, production-style pipeline** with separate branches for preprocessing, recognition, and integration.

---

## 🚀 Features

- Robust image preprocessing (noise removal, thresholding, deskewing)
- Classical & deep-learning text detection (CRAFT)
- Accurate text recognition (Tesseract OCR)
- Modular architecture for easy extension
- Unit-tested preprocessing pipeline
- Jupyter notebook demos for visualization

---

## 🧠 OCR Pipeline Overview
Input Image
↓
Image Preprocessing
↓
Text Detection (CRAFT)
↓
Text Region Cropping
↓
Text Recognition (Tesseract)
↓
Extracted Text Output

---

## 🛠️ Tech Stack

### Core
- Python 3.10
- Conda + pip (environment management)
- Git (feature-branch workflow)

### Image Processing
- OpenCV
- NumPy

### Text Detection
- CRAFT (Character Region Awareness for Text Detection)
- PyTorch
- Torchvision

### Text Recognition
- Tesseract OCR
- pytesseract

### Testing & Experimentation
- PyTest
- Jupyter Notebook
- Matplotlib

---

## 📁 Project Structure

Text-Extraction-Model/
│
├── src/
│ ├── preprocessing.py # Image preprocessing & deskewing
│ ├── detection.py # Classical contour-based detection
│ ├── detection_craft.py # Deep-learning CRAFT detector
│ ├── recognition.py # OCR recognition (Tesseract)
│ └── run_text_extraction.py # End-to-end pipeline runner
│
├── tests/
│ └── test_preprocessing.py # Unit tests
│
├── notebooks/
│ └── craft_demo.ipynb # CRAFT visualization demo
│
├── images/ # Input images
├── data/ # Preprocessed outputs
└── README.md



---

## 🌿 Branching Strategy

| Branch | Purpose |
|------|--------|
| feature/preprocessing | Image preprocessing & enhancement |
| feature/recognition | OCR recognition logic |
| integration | Full pipeline integration |
| main | Stable release |

---

## 🧪 Preprocessing Techniques

- Grayscale conversion
- Median blur denoising
- Adaptive thresholding
- Morphological operations (open & close)
- Deskew correction using rotation estimation

---

## 🔍 Text Detection

### Classical Approach
- Contour detection
- Bounding box filtering
- Noise removal

### Deep Learning (Recommended)
- CRAFT text detector
- Handles rotated, curved, and dense text
- Uses pretrained PyTorch models

---

## 🔤 Text Recognition

- Tesseract OCR
- Extracts text from cropped regions
- Supports multiple languages (configurable)

---


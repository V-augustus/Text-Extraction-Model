import pytesseract
from PIL import Image
import cv2
import sys
import numpy as np

print("Python exe:", sys.executable)
print("NumPy version:", np.__version__)

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
img = cv2.imread("hinditest.jpg")

if img is None:
    print("Image NOT found!")
else:
    print("Image loaded.")

# Convert to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# OCR Hindi + English
text = pytesseract.image_to_string(img, lang="hin+eng")
print("Extracted Text:\n", text)


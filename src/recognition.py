import pytesseract
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(preprocessed_image, lang="eng", config="--oem 3 --psm 6"):
    if preprocessed_image is None:
        raise ValueError("Input image to OCR is None")
    text = pytesseract.image_to_string(preprocessed_image, lang=lang, config=config)
    return text.strip()

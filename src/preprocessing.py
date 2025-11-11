# src/preprocessing.py

import cv2
import numpy as np
import os

def deskew(image):
    """Detect and correct skew in a binary image."""
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h),
                             flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    print(f"🌀 Deskew angle: {angle:.2f} degrees")
    return rotated


def preprocess_image(image_path, show=False, save_output=False, output_path="data/image1.png"):
    """Full preprocessing pipeline for OCR optimization."""

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at: {image_path}")

    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Failed to read the image file: {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Denoise
    gray = cv2.medianBlur(gray, 3)

    # Thresholding
    th = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
        15, 10
    )

    # Morphological operations (noise cleanup + strengthen text)
    kernel = np.ones((2, 2), np.uint8)
    th = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
    th = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

    # Deskew correction
    th = deskew(th)

    if show:
        cv2.imshow("Preprocessed Image", th)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if save_output:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        cv2.imwrite(output_path, th)
        print(f"✅ Preprocessed image saved to: {output_path}")

    return th


if __name__ == "__main__":
    image_path = r"C:\Users\vjvan\OneDrive\Desktop\GitHub\Text-Extraction-Model\images\image1.png"
    output_path = r"C:\Users\vjvan\OneDrive\Desktop\GitHub\Text-Extraction-Model\data\sample_preprocessed.png"

    try:
        preprocessed_img = preprocess_image(image_path, show=False, save_output=True, output_path=output_path)
        print("✅ Image preprocessing completed successfully.")
    except Exception as e:
        print(f"❌ Error: {e}")

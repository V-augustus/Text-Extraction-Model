#to be added after thresholding but before returning the image
# src/morphologicaloperations.py
import cv2
import numpy as np 
def apply_morphological_operations(thresholded_image):
    """
    Apply morphological operations to clean up the thresholded image.
    
    Steps:
    1. Remove small noise using opening (erosion followed by dilation)
    2. Optionally thicken characters using closing (dilation followed by erosion)
    """
    kernel = np.ones((2, 2), np.uint8)  # Small square kernel

    # Remove small noise (opening = erosion + dilation)
    clean = cv2.morphologyEx(thresholded_image, cv2.MORPH_OPEN, kernel)

    # Optionally thicken characters (closing = dilation + erosion)
    clean = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, kernel)

    return clean

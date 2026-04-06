# tests/test_preprocessing.py

import os
import sys
import numpy as np
import pytest

# Ensure src folder is visible to Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.preprocessing import preprocess_image


@pytest.mark.preprocessing
def test_preprocess_image():
    """Basic test to verify preprocessing pipeline works."""
    test_img = r"C:\Users\vjvan\OneDrive\Desktop\GitHub\Text-Extraction-Model\images\image1.png"
    assert os.path.exists(test_img), "❌ Test image not found!"

    out = preprocess_image(test_img)
    assert out is not None, "❌ preprocess_image() returned None"
    assert isinstance(out, np.ndarray), "❌ Output is not a NumPy array"
    assert out.shape[0] > 0 and out.shape[1] > 0, "❌ Empty image output"
    print("✅ preprocess_image() passed all tests.")


#test script for craft
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.detection_craft import run_craft_detection

if __name__ == "__main__":
    image_path = r"C:\Users\vjvan\OneDrive\Desktop\GitHub\Text-Extraction-Model\images\image1.png"
    result = run_craft_detection(image_path)
    print("✅ Text detection complete.")
    print("Detected text boxes:", len(result["boxes"]))

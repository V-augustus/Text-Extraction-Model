import os
from src.detection_craft import run_craft_detection
from src.recognition import recognize_text
import cv2

def extract_text_from_image(image_path, output_dir="output"):
    # Step 1: Detect text regions using CRAFT
    print("[1/3] Running CRAFT text detection...")
    detection_result = run_craft_detection(image_path)
    
    os.makedirs(output_dir, exist_ok=True)
    detected_image_path = os.path.join(output_dir, "detected_text.png")

    # Step 2: Save the detection result if available
    if isinstance(detection_result, str) and os.path.exists(detection_result):
        detected_image_path = detection_result
    elif isinstance(detection_result, dict) and "image" in detection_result:
        cv2.imwrite(detected_image_path, detection_result["image"])

    print("[2/3] Running EasyOCR text recognition...")
    recognized_text = recognize_text(image_path)

    # Step 3: Save output to a text file
    output_text_path = os.path.join(output_dir, "recognized_text.txt")
    with open(output_text_path, "w", encoding="utf-8") as f:
        for item in recognized_text:
            f.write(f"{item['text']} (conf: {item['confidence']:.2f})\n")
    
    print(f"[3/3] Text extraction complete! Results saved to: {output_text_path}")

    return output_text_path

if __name__ == "__main__":
    test_image = "sample.jpg"  # path to your input image
    extract_text_from_image(test_image)

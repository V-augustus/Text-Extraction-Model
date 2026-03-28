# src/detection_craft.py
import cv2
import matplotlib.pyplot as plt
from craft_text_detector import Craft

def run_craft_detection(image_path, output_dir="outputs/craft"):
    """
    Runs CRAFT text detection on an input image.
    Returns bounding boxes and the visualization image.
    """
    craft = Craft(
        output_dir=output_dir,
        crop_type="poly",
        cuda=False  # use False for now since torch-directml is acting as CPU fallback
    )

    prediction_result = craft.detect_text(image_path)

    # Unload models after detection to free memory
    craft.unload_craftnet_model()
    craft.unload_refinenet_model()

    # Show result
    plt.imshow(cv2.cvtColor(cv2.imread(prediction_result["text_box_image"]), cv2.COLOR_BGR2RGB))
    plt.title("CRAFT Detected Text Regions")
    plt.axis("off")
    plt.show()

    return prediction_result

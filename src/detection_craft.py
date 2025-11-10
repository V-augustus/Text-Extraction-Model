# src/detection_craft.py
import os
from craft_text_detector import Craft

def detect_text_craft(image_path, output_dir="./outputs/craft", cuda=False):
    """
    Detect text regions using the pretrained CRAFT model.
    Args:
        image_path: path to input image
        output_dir: directory to store detection outputs
        cuda: use GPU if available
    Returns:
        prediction_result: dictionary containing detected boxes, heatmaps, etc.
    """
    # create output directory if missing
    os.makedirs(output_dir, exist_ok=True)

    craft = Craft(output_dir=output_dir, crop_type="poly", cuda=cuda)
    prediction_result = craft.detect_text(image_path)

    craft.unload_craftnet_model()
    craft.unload_refinenet_model()

    return prediction_result

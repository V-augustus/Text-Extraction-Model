# src/detection_craft.py
import os
from craft_text_detector import Craft

def detect_text_craft(image_path, output_dir="outputs/craft", cuda=False, text_threshold=0.7, link_threshold=0.4, low_text=0.4):
    """
    Run CRAFT detector and return polygons or boxes and cropped images list.
    Returns: dict with keys 'boxes' (list of (x,y,w,h)), 'cropped_images' (paths) and raw craft prediction.
    """
    os.makedirs(output_dir, exist_ok=True)
    craft = Craft(output_dir=output_dir, crop_type="poly", cuda=cuda)
    prediction_result = craft.detect_text(image_path, text_threshold=text_threshold, link_threshold=link_threshold, low_text=low_text)
    # prediction_result contains 'boxes' (list of arrays), 'polys', 'img' etc.
    craft.unload_craftnet_model()
    craft.unload_refinenet_model()
    # Convert polys to bounding rects (x,y,w,h)
    boxes = []
    if "polys" in prediction_result:
        for poly in prediction_result["polys"]:
            if poly is None or len(poly)==0:
                continue
            xs = [p[0] for p in poly]
            ys = [p[1] for p in poly]
            x, y = int(min(xs)), int(min(ys))
            w, h = int(max(xs)-x), int(max(ys)-y)
            boxes.append((x,y,w,h))
    return {"boxes": boxes, "prediction": prediction_result, "output_dir": output_dir}

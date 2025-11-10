import cv2
import numpy as np

def merge_overlapping_boxes(boxes, overlap_thresh=0.3):
    """Merge overlapping boxes using Intersection-over-Union."""
    if len(boxes) == 0:
        return []

    boxes = np.array(boxes)
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 0] + boxes[:, 2]
    y2 = boxes[:, 1] + boxes[:, 3]

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)

    pick = []
    while len(idxs) > 0:
        last = idxs[-1]
        pick.append(last)
        suppress = [last]

        for pos in range(len(idxs) - 1):
            i = idxs[pos]
            xx1 = max(x1[last], x1[i])
            yy1 = max(y1[last], y1[i])
            xx2 = min(x2[last], x2[i])
            yy2 = min(y2[last], y2[i])

            w = max(0, xx2 - xx1 + 1)
            h = max(0, yy2 - yy1 + 1)
            overlap = float(w * h) / areas[i]

            if overlap > overlap_thresh:
                suppress.append(i)

        idxs = np.delete(idxs, suppress)

    return boxes[pick].astype("int").tolist()


def detect_text_regions(preprocessed_image, min_area=200, max_area=20000):
    """
    Detect text regions using contours + heuristics.
    Args:
        preprocessed_image: binarized numpy image
        min_area: ignore smaller boxes (noise)
        max_area: ignore huge boxes (background)
    """
    contours, _ = cv2.findContours(preprocessed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes = []

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h

        # Filter boxes by size ratio
        aspect_ratio = w / float(h)
        if area < min_area or area > max_area:
            continue
        if aspect_ratio < 0.1 or aspect_ratio > 15:
            continue

        boxes.append((x, y, w, h))

    merged_boxes = merge_overlapping_boxes(boxes)
    merged_boxes.sort(key=lambda b: (b[1], b[0]))
    return merged_boxes

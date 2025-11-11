# src/detection.py
import cv2
import numpy as np

def non_max_suppression(boxes, scores=None, iou_threshold=0.3):
    """
    Basic NMS for axis-aligned boxes.
    boxes: list of (x,y,w,h)
    scores: optional confidence scores (same length as boxes)
    """
    if len(boxes) == 0:
        return []
    boxes_arr = np.array(boxes).astype(float)
    x1 = boxes_arr[:,0]
    y1 = boxes_arr[:,1]
    x2 = boxes_arr[:,0] + boxes_arr[:,2]
    y2 = boxes_arr[:,1] + boxes_arr[:,3]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)

    if scores is None:
        idxs = np.argsort(y2)  # fallback sort
    else:
        idxs = np.argsort(scores)

    pick = []
    while idxs.size > 0:
        last = idxs[-1]
        pick.append(last)
        idxs = idxs[:-1]

        if idxs.size == 0:
            break

        xx1 = np.maximum(x1[last], x1[idxs])
        yy1 = np.maximum(y1[last], y1[idxs])
        xx2 = np.minimum(x2[last], x2[idxs])
        yy2 = np.minimum(y2[last], y2[idxs])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        inter = w * h
        iou = inter / (areas[last] + areas[idxs] - inter)
        idxs = idxs[iou <= iou_threshold]
    return [tuple(map(int, boxes[i])) for i in pick]


def detect_text_regions(preprocessed_image, min_area=300, max_area=200000, iou_thresh=0.3):
    """
    Detect candidate text boxes from a binarized preprocessed image.
    Returns list of (x,y,w,h) sorted top-to-bottom.
    """
    # find contours
    contours, _ = cv2.findContours(preprocessed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes = []
    scores = []  # optional: small heuristic score (area)
    H, W = preprocessed_image.shape[:2]

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h
        aspect = w / float(h) if h>0 else 0

        # filter by size and aspect ratio
        if area < min_area or area > max_area:
            continue
        if aspect < 0.15 or aspect > 20:
            continue
        # filter by relative size to image - avoid entire background boxes
        if w > 0.95*W and h > 0.95*H:
            continue

        boxes.append((x, y, w, h))
        scores.append(area)

    # Merge overlapping boxes with NMS
    merged = non_max_suppression(boxes, scores=scores, iou_threshold=iou_thresh)
    merged.sort(key=lambda b: (b[1], b[0]))
    return merged

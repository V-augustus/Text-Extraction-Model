import easyocr

def recognize_text(image_path):
    """
    Performs text recognition on the given image using EasyOCR.
    Returns recognized text with bounding boxes and confidence scores.
    """
    reader = easyocr.Reader(['en'], gpu=False)  # use gpu=True if you have GPU acceleration working
    results = reader.readtext(image_path)
    
    text_output = []
    for (bbox, text, prob) in results:
        text_output.append({
            "bounding_box": bbox,
            "text": text,
            "confidence": float(prob)
        })
    return text_output


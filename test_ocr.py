import pytesseract
from PIL import Image

# Load the image
img = Image.open("ocr_test_image.png")

# Extract text
text = pytesseract.image_to_string(img)

print("Extracted Text:")
print(text)

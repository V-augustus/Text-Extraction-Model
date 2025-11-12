import pytesseract
from PIL import Image

# Load the image
img = Image.open("ocr_test_image.png")

# Use English language and LSTM neural engine
custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, lang='eng', config=custom_config)

print("Extracted Text:")
print(text)

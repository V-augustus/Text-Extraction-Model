from src.preprocessing import preprocess_image
from src.recognition import extract_text

if __name__ == "__main__":
    image_path = r"C:\Users\vjvan\OneDrive\Desktop\GitHub\Text-Extraction-Model\images\image1.png"

    preprocessed = preprocess_image(image_path, show=False, save_output=True)
    text = extract_text(preprocessed)

    print("\n📝 Extracted Text:")
    print("="*60)
    print(text)
    print("="*60)
    print("\n✅ Text extraction completed successfully.")
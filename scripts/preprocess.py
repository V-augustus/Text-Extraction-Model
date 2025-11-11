import cv2
import os
from albumentations import Compose, Resize, Normalize, RandomRotate90, GaussNoise

# Define augmentations
transform = Compose([
    Resize(224, 224),  # Standard size for models
    Normalize(mean=(0.4185, 0.456, 0.406), std=(0.229, 0.224, 0.225)),  # ImageNet normalization
    RandomRotate90(p=0.5),  # Augment for robustness
    GaussNoise(p=0.2)
])

def preprocess_image(image_path, output_path, label):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB
    augmented = transform(image=img)
    img_aug = augmented['image']
    # Save processed image
    cv2.imwrite(output_path, cv2.cvtColor(img_aug, cv2.COLOR_RGB2BGR))
    return label  # e.g., 0 for handwritten, 1 for typed

# Example: Process a folder
input_dir = 'data/raw/iam/'  # Or synth_typed
output_dir = 'data/processed/handwritten/'
os.makedirs(output_dir, exist_ok=True)
for file in os.listdir(input_dir)[:100]:  # Start small
    preprocess_image(os.path.join(input_dir, file), os.path.join(output_dir, file), 0)
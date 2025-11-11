from src.detection_craft import run_craft_detection

if __name__ == "__main__":
    image_path = r"images/image1.png"  # update this path to your image
    result = run_craft_detection(image_path)
    print("✅ Detection complete!")
    print(result)

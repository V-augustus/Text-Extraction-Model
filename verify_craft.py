import torch
import torch_directml
import cv2
import numpy as np
from craft_text_detector import Craft

print("Torch version:", torch.__version__)
print("DirectML device count:", torch_directml.device_count())
print("OpenCV version:", cv2.__version__)
print("NumPy version:", np.__version__)

craft = Craft(output_dir='output/', crop_type='poly', cuda=False)
print("CRAFT initialized successfully!")
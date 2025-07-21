from PIL import Image
import numpy as np
import os
import re
import matplotlib.pyplot as plt

# === Set path to your .coe file ===
coe_path = "E:/Unfinished Edits/basys3_image_8bit.coe"

# === SET IMAGE DIMENSIONS (MUST match original image) ===
width = 300   # 🔁 Change this to your image width
height = 225  # 🔁 Change this to your image height

# === Load COE content ===
with open(coe_path, "r") as f:
    coe_content = f.read()

# === Extract 2-digit hex values (grayscale pixels) ===
hex_values = re.findall(r'[0-9A-Fa-f]{2}', coe_content)
pixel_values = [int(h, 16) for h in hex_values]

# === Check for size mismatch ===
expected_pixels = width * height
if len(pixel_values) < expected_pixels:
    raise ValueError(f"❌ Not enough pixels: expected {expected_pixels}, got {len(pixel_values)}")
elif len(pixel_values) > expected_pixels:
    print("⚠️ Warning: More pixels than expected, cropping excess.")
    pixel_values = pixel_values[:expected_pixels]

# === Reconstruct grayscale image ===
gray_array = np.array(pixel_values, dtype=np.uint8).reshape((height, width))
image = Image.fromarray(gray_array)

# === Save image ===
output_image_path = os.path.splitext(coe_path)[0] + "_restored.png"
image.save(output_image_path)
print(f"✅ Image restored and saved at: {output_image_path}")

# === Show image ===
plt.imshow(gray_array, cmap='gray')
plt.title("Restored Grayscale Image")
plt.axis('off')
plt.show()

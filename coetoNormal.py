from PIL import Image
import numpy as np
import os
import re
import matplotlib.pyplot as plt

# === Set paths ===
coe_path = "E:/Unfinished Edits/minecraftpic_rgb.coe"              # Your COE file
reference_image_path = "E:/Unfinished Edits/minecraftpic.png"      # To get original dimensions

# === Step 1: Get original image dimensions ===
with Image.open(reference_image_path) as ref_img:
    width, height = ref_img.size
print(f"📐 Original image dimensions: {width}x{height}")

# === Step 2: Load and parse COE file ===
with open(coe_path, "r") as f:
    coe_content = f.read()

# Extract 6-digit hex color values (RRGGBB)
hex_values = re.findall(r'[0-9A-Fa-f]{6}', coe_content)
pixel_values = [(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)) for h in hex_values]

# === Step 3: Validate and reshape ===
expected_pixels = width * height
if len(pixel_values) != expected_pixels:
    raise ValueError(f"❌ Mismatch: Expected {expected_pixels} pixels, got {len(pixel_values)}")

rgb_array = np.array(pixel_values, dtype=np.uint8).reshape((height, width, 3))
image = Image.fromarray(rgb_array, mode="RGB")

# === Step 4: Save and show image ===
output_path = os.path.splitext(coe_path)[0] + "_restored.png"
image.save(output_path)
print(f"✅ Restored color image saved at: {output_path}")

plt.imshow(image)
plt.title("Restored RGB Image from COE")
plt.axis('off')
plt.show()

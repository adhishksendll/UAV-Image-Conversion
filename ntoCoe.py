from PIL import Image
import numpy as np
import os

# === Set image path ===
image_path = "E:/Unfinished Edits/minecraftpic.png"
image = Image.open(image_path).convert("RGB")  # Keep color

# Get RGB data and dimensions
rgb_array = np.array(image)
height, width = rgb_array.shape[:2]
print(f"📐 Color image loaded: {width}x{height}")

# Flatten and convert each pixel to 24-bit hex: RRGGBB
flat_pixels = rgb_array.reshape(-1, 3)
hex_values = [f"{r:02X}{g:02X}{b:02X}" for r, g, b in flat_pixels]

# Format COE content for 24-bit memory
coe_lines = [
    "memory_initialization_radix=16;",
    "memory_initialization_vector=",
    ',\n'.join(hex_values) + ";"
]

# === Save .coe file ===
output_path = os.path.splitext(image_path)[0] + "_rgb.coe"
with open(output_path, "w") as f:
    f.write('\n'.join(coe_lines))

print(f"✅ 24-bit color COE file saved at: {output_path}")

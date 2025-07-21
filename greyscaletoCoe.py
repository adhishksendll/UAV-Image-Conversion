from PIL import Image
import numpy as np
import os

# Set image directory and name
directory_path = "E:/Unfinished Edits"
image_name = "grayscale_minecraftpic.png"

# Build full image path
image_path = os.path.join(directory_path, image_name)

# Load and convert image to 8-bit grayscale
image = Image.open(image_path).convert("L")
gray_array = np.array(image).flatten()

# Convert each grayscale pixel (0–255) to 2-digit hex
hex_8bit = [f"{pixel:02X}" for pixel in gray_array]

# Format COE content for 8-bit memory
coe_lines = [
    "memory_initialization_radix=16;",
    "memory_initialization_vector=",
    ',\n'.join(hex_8bit) + ";"
]

# Output COE file path
coe_output_path = os.path.join(directory_path, "basys3_image_8bit.coe")

# Write COE file
with open(coe_output_path, "w") as f:
    f.write('\n'.join(coe_lines))

print(f"8-bit COE file successfully created at: {coe_output_path}")

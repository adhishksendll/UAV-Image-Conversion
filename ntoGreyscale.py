from PIL import Image
import os

# Set directory and image name
directory_path = "E:/Unfinished Edits"
image_name = "minecraftpic.png"

# Build full path to the image
image_path = os.path.join(directory_path, image_name)

# Open and convert image to grayscale
image = Image.open(image_path).convert("L")

# Save grayscale image
gray_image_path = os.path.join(directory_path, "grayscale_" + image_name)
image.save(gray_image_path)

print(f"Grayscale image saved at: {gray_image_path}")

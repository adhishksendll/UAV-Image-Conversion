from PIL import Image

image_path = "E:/Unfinished Edits/test1.webp"
with Image.open(image_path) as img:
    print("✅ Original image size:", img.size)

"""
Convert an image with a white background to the same image with a transparent background

Install Pillow:
python3 -m pip install pillow

Run as:
python3 main.py image_name.png

Image must have a white background and no '.' in the name prior to the extension
"""
from PIL import Image
import sys

img_name = sys.argv[1]
img = Image.open(img_name)
# Convert an RGB image to a Pillow image for processing
rgba = img.convert("RGBA")
# Get the pillow image data
data = rgba.getdata()

newData = []

for item in data:
    # finding color greater than threshold
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        # storing a transparent value when we find a white block
        newData.append((255, 255, 255, 0))
    else:
        # if not white, store original value
        newData.append(item)

# Create new image with the collected data
rgba.putdata(newData)

rgba.save(f"{img_name.split('.')[0]}_converted.png", "PNG")

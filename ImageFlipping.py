import os
from PIL import Image

input = ""
output = "" # only works if there is a pre-existing output directory

for images in os.listdir(input):
    if images.lower().endswith(('.jpg', '.png', '.jpeg')):
        image_location = os.path.join(input, images)
    with Image.open(image_location) as img:
        flipped_images = img.rotate(180)
        flipped_images.save(os.path.join(output,images))
    print ("done")

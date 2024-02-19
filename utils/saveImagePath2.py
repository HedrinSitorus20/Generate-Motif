import sys
from PIL import Image
import uuid
import os


image_fullpath=sys.argv[1]
folderUser=sys.argv[2]
image_fullpath = image_fullpath[1:]
img = Image.open(str(image_fullpath)) 

unique_file_name = uuid.uuid4().hex

img = img.save(f"media/Hasil/{unique_file_name}.png")

print(f"/media/Hasil/{unique_file_name}.png")

folder_path = (f'media/{folderUser}')
test = os.listdir(folder_path)
for images in test:
    if images.endswith(".png"):
        os.remove(os.path.join(folder_path, images))

for images in test:
    if images.endswith(".jpg"):
        os.remove(os.path.join(folder_path, images))
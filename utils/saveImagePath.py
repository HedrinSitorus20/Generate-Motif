import sys
from PIL import Image
import uuid
import os

image_fullpath=sys.argv[1]
image_fullpath = image_fullpath[1:]
img = Image.open(str(image_fullpath))
namaDirektori = f"media/Hasil"
Direktori = str(namaDirektori)

if(not os.path.exists(Direktori)):
    os.mkdir(Direktori)

unique_file_name = uuid.uuid4().hex

img = img.save(f"media/Hasil/{unique_file_name}.jpg")

os.remove(image_fullpath)
print(f"/media/Hasil/{unique_file_name}.jpg")
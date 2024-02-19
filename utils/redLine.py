from PIL import Image, ImageDraw
import os, sys


image_fullpath=sys.argv[1]

if os.path.exists(f"{image_fullpath[:-4]}_red.jpg"):
    print(f"{image_fullpath[:-4]}_red.jpg")

else:
    # membuka file gambar
    image = Image.open(image_fullpath)
    draw = ImageDraw.Draw(image)
    
    width, height = image.size
    
    x1, y1 = 0, height // 2
    x2, y2 = width, height // 2

    draw.line((x1, y1, x2, y2), fill='red', width=3)

    
    draw = ImageDraw.Draw(image)

    image.save(f"{image_fullpath[:-4]}_red.jpg")
    print(f"{image_fullpath[:-4]}_red.jpg")
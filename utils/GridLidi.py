import os, sys
from PIL import Image, ImageDraw

image_fullpath=sys.argv[1]
image_fullpath = image_fullpath[1:]
# Grid motif asal
if os.path.exists(f"{image_fullpath[:-4]}_grid.jpg"):
    print(f"{image_fullpath[:-4]}_grid.jpg")

else:
    image = Image.open(image_fullpath)

    width, height = image.size
    image = image.resize((width * 10, height * 10), Image.Resampling.NEAREST)

    draw = ImageDraw.Draw(image)

    width, height = image.size

    grid_size = 10

    for x in range(0, width, grid_size):
        draw.line((x, 0, x, height), fill=(127, 127, 127))

    for y in range(0, height, grid_size):
        draw.line((0, y, width, y), fill=(127, 127, 127))

    image.save(f"{image_fullpath[:-4]}_grid.jpg")
    print(f"{image_fullpath[:-4]}_grid.jpg")
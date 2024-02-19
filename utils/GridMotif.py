import os, sys
from PIL import Image, ImageDraw

image_fullpath=sys.argv[1]
image_fullpath = image_fullpath[1:]

# Grid motif asal
if os.path.exists(f"{image_fullpath[:-4]}_grid.png"):
    print(f"{image_fullpath[:-4]}_grid.png")

else:
    
    png_image = Image.open(image_fullpath)
    background = Image.new('RGB', png_image.size, (255, 255, 255))
    
    background.paste(png_image, mask=png_image.split()[3])
    
    image = background
    draw = ImageDraw.Draw(image)

    width, height = image.size

    grid_size = 10

    for x in range(0, width, grid_size):
        draw.line((x, 0, x, height), fill=(127, 127, 127))

    for y in range(0, height, grid_size):
        draw.line((0, y, width, y), fill=(127, 127, 127))

    image.save(f"{image_fullpath[:-4]}_grid.png")
    print(f"{image_fullpath[:-4]}_grid.png")
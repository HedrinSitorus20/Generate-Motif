from PIL import Image, ImageDraw
import sys, os
# Open the image file

image_fullpath=sys.argv[1]
image_fullpath = image_fullpath[1:]

if os.path.exists(f"{image_fullpath[:-4]}_grid_help.jpg"):
    print(f"{image_fullpath[:-4]}_grid_help.jpg")

else:
    image = Image.open(image_fullpath)

    width, height = image.size

    image = Image.new('RGB', (width, 1), color=(255, 255, 255))

    width, height = image.size
    image = image.resize((width * 10, height * 10))

    # Create a draw object
    draw = ImageDraw.Draw(image)

    width, height = image.size

    # Set the grid size
    grid_size = 10

    # Draw vertical gridlines
    for x in range(0, width, grid_size):
        draw.line((x, 0, x, height), fill=(0, 153, 153))


    # Save the image with gridlines
    image.save(f"{image_fullpath[:-4]}_grid_help.jpg")

    print(f"{image_fullpath[:-4]}_grid_help.jpg")

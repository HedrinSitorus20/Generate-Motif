import sys

image_fullpath=sys.argv[1]
status = 1

image_format = image_fullpath[-3:]

if(image_format == 'jpg'):
    status = 1
else:
    status = 0

print(f"{status}")
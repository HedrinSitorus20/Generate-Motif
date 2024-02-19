import sys
import cv2

image_fullpath=sys.argv[1]
status = 1

#Pemisahan Baris
img = cv2.imread(str(image_fullpath), 1)

height, width, channels = img.shape

if(6<=height <= 12):
    status = 1

else:
    status = 0

print(f"{status}{height}")
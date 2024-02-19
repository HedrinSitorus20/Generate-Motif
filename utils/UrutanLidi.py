import sys
import cv2

image_fullpath=sys.argv[1]
image_fullpath = image_fullpath[1:]

image = cv2.imread(image_fullpath)

h, w, c = image.shape
temp = []
for i in range(1, h+1):
    temp.append(i)

print(temp)
import cv2
from Function import SkorTotal
from ProcessImage import SeparateImage
from ProcessImage import ConvertRGB
from ProcessImage import ConvertArrayImage


arr = []
for i in range(1, 6):
    #Pemisahan Baris
    img = cv2.imread(f'Original/Data_{i}.jpg', 1)
    
    #Pemisahan Baris
    SeparateImage(img)

    height, width, channels = img.shape
    img = []
    Lidi = []

    # image to RGBA
    img, Lidi = ConvertRGB(img, Lidi, height)

    # convert binary
    Array_data = []

    Array_data = ConvertArrayImage(img, Array_data)

    SkorArray = []
    for i in range(0, int(len(Lidi))):
        for j in range(0, int(len(Lidi)-1)):
            temp1 = Array_data[i].copy()
            temp2 = Array_data[j].copy()

            SkorArray.append(SkorTotal(temp1, temp2))

    mean = sum(SkorArray)/int(len(SkorArray))

    arr.append(mean)

print(arr)
import cv2
import numpy as np
from PIL import Image
import os, sys

namaFile= sys.argv[1]
namaDirektori = f"{namaFile[:-4]}"
Direktori = f"{namaDirektori}"
temp = []
if(not os.path.exists(Direktori)):
    os.mkdir(Direktori)

    image = Image.open(namaFile)

    width, height = image.size

    #Pemisahan Baris
    img = cv2.imread(f"{namaFile}", 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for i in range(0,width, 10):
            try:
                na = np.array(img[i:i+10, : ], dtype=np.uint8)
                # membuat Numpy array menjadi PIL Image dan menyimpan menjadi bentuk jpg
                Image.fromarray(na).save(f"{namaDirektori}/Baris"+str(i)+".jpg")
                temp.append(f"{namaDirektori}/Baris"+str(i)+".jpg")
            except ValueError:
                break
    print(temp)
else:
    image = Image.open(namaFile)
    width, height = image.size

    for i in range(0, height, 10):
        try:
             temp.append(f"{namaDirektori}/Baris"+str(i)+".jpg")
        except ValueError:
             break
    print(temp)
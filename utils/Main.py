import numpy as np
import cv2
from PIL import Image
import os
import pants
from Function import TabuSearch
from Function import RandomSearch
from Function import GreedySearch
from Function import ACO
from Function import SkorTotal

def SkorACO(a, b):
    temp1 = Array_data[a[0]]
    temp2 = Array_data[a[1]]
    temp3 = Array_data[b[0]]
    temp4 = Array_data[b[1]]

    SkorArray1 = SkorTotal(temp1, temp2)
    SkorArray2 = SkorTotal(temp3, temp4)

    SkorArray = abs(1/(SkorArray1 + SkorArray2))
    return SkorArray


#inisialisasi nama direktori
namaDirektori = input("Nama Folder: ")
Direktori = f"{namaDirektori}"
namaFile = input("Nama File: ")

import time

timeout = 60   # [seconds]
timeout_start = time.time()
# namaDirektori = "Random Search Performance 5"
Direktori = f"{namaDirektori}"
# namaFile = "Data_5.jpg"
# ModeGenerate = 3
# jmlBaris = 10
# Baris = 2
namaGambar = 0

ModeGenerate = int(input("Pilih Mode Generate : "))
jmlBaris = int(input("jumlah baris yang digunakan: "))
Baris = int(input("inisiasi baris yang digunakan: "))

#Cek Path
if(not os.path.exists(Direktori)):
    os.mkdir(Direktori)


#Pemisahan Baris
img = cv2.imread(f'Original/{namaFile}', 1)
for i in range(0,72):
    try:
        na = np.array(img[i:i+1, : ], dtype=np.uint8)
        # membuat Numpy array menjadi PIL Image dan menyimpan menjadi bentuk jpg
        Image.fromarray(na).save(f"{namaDirektori}/Baris"+str(i)+".jpg")
        
    except ValueError:
        break
img = []
Lidi = []
# image to RGBA
for i in range(0,72):
    
    try:
        img_temp = Image.open(f'{namaDirektori}/Baris'+str(i)+'.jpg')
        img_temp.convert("RGBA")
        datas = img_temp.getdata()
        img.append(datas)
        Lidi.append(i)
    except FileNotFoundError:
        break

# Baca Motif keseluruhan
Array_data = []
Tabu_List = []
for i in range(0,72):
    try:
        Baca_data = []
        datas = img[i]
        for item in datas:
            if item[0] > 200 and item[1] > 200 and item[2] > 200:
                Baca_data.append(1)
            else:
                Baca_data.append(2)
        Array_data.append(Baca_data)
    except IndexError:
        break

# Bagaimana membandingkan semua kombinasi baris?
# Aturan tidak membandingkan baris yang sama
# Memakai operasi Permutasi

from itertools import permutations

comb = list(permutations(Lidi, 2))
# SkorArray = []
# for i in range(0, int(len(Lidi))):
#     for j in range(0, int(len(Lidi)-1)):
#         temp1 = Array_data[i].copy()
#         temp2 = Array_data[j].copy()

#         SkorArray.append(SkorTotal(temp1, temp2))

# print(SkorArray)

#World Ant
world = pants.World(comb, SkorACO)
solver = pants.Solver()

# print(comb)

# Bagaimana menyimpan perbandingan setiap baris?

comb = np.array_split(comb, 21)




# Main

PanjangLidi = int(len(Lidi))-1
# print("1 = Tabu Serach")
# print("2 = Greedy Search")
# print("3 = Random Search")
# print("4 = ACO Search")




#Inisialisasi Baris ke dalam Array

img = cv2.imread(f'Original/{namaFile}', 1)

height, width, channels = img.shape
img = []

for i in range(0,height):
    try:
        img.append(cv2.imread(f'{namaDirektori}/Baris'+str(i)+'.jpg', 1))
    except:
        break

# while time.time() < timeout_start + timeout:
for i in range(0,10):
        
    if(ModeGenerate == 1):
        print("Tabu Serach Result \n")
        Tabu_List,Best_Solution = TabuSearch(PanjangLidi, Array_data, Baris, jmlBaris, Tabu_List)
        a = Best_Solution[0]
        print(a)
    elif(ModeGenerate == 2):
        print("Greedy Serach Result \n")
        a = GreedySearch(PanjangLidi, comb,Baris, jmlBaris)
        print(a)
    elif(ModeGenerate == 3):
        print("Random Search Result \n")
        a = RandomSearch(PanjangLidi, jmlBaris)
        print(a)
    elif(ModeGenerate == 4):
        print("ACO Result \n")
        a = ACO(solver, world, jmlBaris)
        print(a)
    else:
        print("Format yang anda masukkan salah ex : 1")

    c = a.copy()
    c = c[::-1]
    mix =[]
    a.extend(c)
    print(a)

    while len(a) >=0:
        try:
            image1 = a.pop(0)
            # print(image1+1)
            # print(len(a))
            image2 = a.pop(0)
            # print(image2+1)
            # print(len(a))
            mix = np.vstack((img[image1], img[image2]))
            while len(a) >=0:
                image3 = a.pop(0)
                # print(image3+1)
                # print(len(a))
                mix = np.vstack((mix, img[image3]))
                # print("Berhasil")
        except Exception:
            break
    Image.fromarray(mix).save(f"{namaDirektori}/Hasil"+str(namaGambar)+".jpg")

    namaGambar +=1
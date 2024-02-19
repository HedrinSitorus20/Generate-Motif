from random import randint
temp = []
#pilih motif Random search
for i in range (1,6):
    #pilih motif
    for j in range(0, 3):
        j = randint(0, 20000)
        print(f"{i} , {j}")

#pilih motif Greedy search
for i in range (1,6):
    #pilih motif
    for j in range(0, 3):
        j = randint(0, 20000)
        print(f"{i} , {j}")

#pilih motif Tabu search
for i in range (1,6):
    #pilih motif
    for j in range(0, 3):
        j = randint(0, 10000)
        print(f"{i} , {j}")

#pilih motif dari ACO

for i in range (1,24):
    temp.append(i)

for i in range(0,8):
    n = randint(0,14)
    del temp[n]

print(temp)


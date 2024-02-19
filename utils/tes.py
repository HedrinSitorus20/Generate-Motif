import sys

modeGenerate=sys.argv[1]

modeGenerate = int(modeGenerate)

if modeGenerate == 1:
    modeGenerate = 1
elif modeGenerate == 2:
    modeGenerate = 2
elif modeGenerate == 3:
    modeGenerate = 3
else :
    modeGenerate = 4

print(f"{modeGenerate}")
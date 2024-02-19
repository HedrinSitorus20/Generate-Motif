import sys

jmlBaris =sys.argv[1]

jmlBaris = int(jmlBaris)

status = 1


if(1< jmlBaris <= 40):
    status = 1

else:
    status = 0

print(f"{status}")
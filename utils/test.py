import sys
import datetime

time = datetime.datetime.now()

output="HI %s current time is %s" %(sys.argv[1],time)

print(output)
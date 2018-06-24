import sys
import math

for line in sys.stdin:
    data = line.split()

    print int(math.ceil(int(data[0])/ math.sin(int(data[1])*2*math.pi/360.0)))
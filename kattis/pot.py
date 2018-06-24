import sys
import math

first = True

total = 0

for line in sys.stdin:
    if first:
        first = False
    else:
        data = line.split()[0]
        x = int(data[0:-1])
        y = int(data[-1])

        total += math.pow(x,y)

print int(total)
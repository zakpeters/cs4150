import sys
first = True
d = 0
p = 0
for line in sys.stdin:
    data = line.split()
    if first:
        first = False
    elif len(data) == 1:
        print str(d) + " miles"
        d = 0
        p = 0
    else:
        d += int(data[0]) * (int(data[1])-p)
        p = int(data[1])
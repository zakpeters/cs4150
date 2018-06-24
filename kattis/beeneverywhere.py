import sys

first = True
second = True
x = 0
cities = set()

for line in sys.stdin:
    if first:
        first = False
    elif x == 0:
        if second:
            second = False
        else:
            print len(cities)
        data = line.split()
        x = int(data[0])
        cities = set()
    else:
        data = line.split()
        cities.add(data[0])
        x -= 1

print len(cities)
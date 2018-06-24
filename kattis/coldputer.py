import sys

total = 0

first = True

for line in sys.stdin:
    if first:
        first = False
    else:
        data = line.split()
        for x in data:
            if int(x) < 0:
                total +=1

print total
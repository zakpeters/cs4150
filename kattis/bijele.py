import sys

l = [1,1,2,2,2,8]

for line in sys.stdin:
    data = line.split()
    for x in range(0,6):
        l[x] -= int(data[x])

for x in l:
    sys.stdout.write(str(x) + " ")
print ""
import sys


first = True

for line in sys.stdin:
    if(first):
        first = False
    data = line.split()
    x = int(data[0]) - int(data[1])
    if(x<0):
        print str(x*-1)
    else:
        print x
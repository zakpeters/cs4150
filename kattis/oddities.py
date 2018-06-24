import sys


first = True
for line in sys.stdin:
    if first:
        first = False
    else:
        x = int(line.split()[0])
        if x%2 == 0:
            print "%s is even" %x
        else:
            print "%s is odd" %x
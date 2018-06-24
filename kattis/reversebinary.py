import sys

for line in sys.stdin:
    data = int(line.split()[0])
    s = "{0:b}".format(data)
    print int(s[::-1], 2)
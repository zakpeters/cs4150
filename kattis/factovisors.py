import sys
import math

def factor(n, m):
    if m == 0:
        print "%d does not divide %d!" % (m, n)
        return
    if m == 1:
        print "%d divides %d!" % (m, n)
        return
    if(m <= n):
        print "%d divides %d!" % (m, n)
        return

    x = m #temp for m
    c = 0 #count of factors discovered

    for i in range(2, int(math.ceil(math.sqrt(m)))+1):
        #find factors largest factors of n
        while(x%i == 0):
            x /= i
            c += 1

        if c > 0:
            j = i
            while(n>=j):
                c -= n/j
                j *= i
            if c > 0:
                print "%d does not divide %d!" % (m, n)
                return
        c = 0

    if x<= n:
        print "%d divides %d!" % (m, n)
    else:
        print "%d does not divide %d!" % (m, n)

for line in sys.stdin:
    data = line.split()
    factor(int(data[0]),int(data[1]))
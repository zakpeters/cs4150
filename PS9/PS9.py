import sys

N = 0
L = []
cache = []

for line in sys.stdin:
    data = line.split()
    if N == 0:
        N = int(data[0])
    else:
        L.append(int(data[0]))
        cache.append(-1)

cache[N] = 0

def pen(i , k):
    return (400-L[k]+L[i])**2

def penalty(i):
    if cache[i] == -1:
        m = pen(i, i+1) + penalty(i+1)
        for k in xrange(i+2,N+1):
            tmp = pen(i, k) + penalty(k)
            if tmp < m:
                m = tmp
        cache[i] = m
    return cache[i]

print penalty(0)
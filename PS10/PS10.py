import sys

curr = 0
rows = 0
close = 0
cache = {}
L = []
tot = 0
N = 0

for line in sys.stdin:
    data = line.split()
    if curr == 0:
        rows = int(data[0])
        close = int(data[1])
    elif curr <= rows:
        L.append([int(data[0]), int(data[1])])
        tot += int(data[0]) + int(data[1])
        cache[curr - 1] = []
        for i in range(0, close+1):
            cache[curr - 1].append([-1, -1, -1])
        N += 1
    else:
        break
    curr += 1

def maxValue(r, u, k):
    if r == rows:
        return  0

    n = 0
    n0 = 0
    n1 = 0

    if k < N-r:
        if cache[r][k][-1] == -1:
            cache[r][k][-1] = L[r][0] + L[r][1] + maxValue(r+1, -1, k)
        n = cache[r][k][-1]
        if u != 0:
            if cache[r][k][1] == -1:
                cache[r][k][1] = L[r][1] + maxValue(r+1,1, k-1)
            n0 = cache[r][k][1]
        if u != 1:
            if cache[r][k][0] == -1:
                cache[r][k][0] = L[r][0] + maxValue(r+1,0, k-1)
            n1 = cache[r][k][0]
        return max([n,n0,n1])

    elif k == N-r:
        if u != 0:
            if cache[r][k][1] == -1:
                cache[r][k][1] = L[r][1] + maxValue(r+1,1, k-1)
            n0 = cache[r][k][1]
        if u != 1:
            if cache[r][k][0] == -1:
                cache[r][k][0] = L[r][0] + maxValue(r+1,0, k-1)
            n1 = cache[r][k][0]
        return max([n, n0, n1])

    else:
        return 0

print maxValue(0,-1,close)
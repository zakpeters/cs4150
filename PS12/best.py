import sys


N = 0
bound = 99999
matrix = []
cache = []

for line in sys.stdin:
    if N == 0:
        N = int(line)
    else:
        data = line.split()
        l = []
        for x in data:
            l.append(int(x))
        matrix.append(l)

#sort each row in ascending order
priority = []
l = []
for i in range(0, N):
    l.append(i)
for i in range(0, N):
    priority.append( sorted(l[:i]+l[i+1:], key=lambda x: matrix[i][x]) )

s = set()
d = [0]
l = [-1] * 2**(N)

#build cache
cache.append(l[:])
for i in range(1, N):
    s.add(i)
    cache.append(l[:])
    d.append(2**(i-1))

def travel(curr, remain, max):
    global bound
    if cache[curr][remain] == -1:
        if len(s) == 0:
            if (max + matrix[curr][0] < bound):
                bound = max + matrix[curr][0]
                print bound
            return matrix[curr][0]

        # if max > bound:
        #     cache[curr][remain] = -1

        if max < bound:
            min = 99999

            for x in priority[curr]:
                if x in s:
                    s.remove(x)
                    t = travel(x, remain + d[x], max+matrix[curr][x])

                    s.add(x)
                    if t != -1:
                        t += max+matrix[curr][x]
                        if t + max < min:
                            min = t
                            #idk bout this
                            newmax = t + max #+ matrix[curr][x] + t
                            if newmax < bound:
                                bound = newmax
                                print bound
            if min != 99999:
                cache[curr][remain] = min
    return cache[curr][remain]

print travel(0, 0, 0)

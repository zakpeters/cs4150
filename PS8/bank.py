import sys

N = 0
T = 0

L = []

for line in sys.stdin:
    data = line.split()
    if T == 0:
        T = int(data[1])
        N = int(data[0])
        L = [list() for _ in xrange(T )]
    else:
        L[int(data[1])].append(int(data[0]))

line = [0 for _ in xrange(T)]


for i in xrange(0, T):
    curr = T-1-i
    for val in L[curr]:
        if val >= line[curr]:
            if curr > 0:
                L[curr-1].append(line[curr])
            line[curr] = val
        elif curr > 0:
            L[curr - 1].append(val)

tot= 0
for i in line:
    tot += i

print tot
# print L
# print line
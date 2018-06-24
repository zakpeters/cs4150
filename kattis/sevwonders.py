import sys

t = 0
g = 0
c = 0

for line in sys.stdin:
    data = line.split()[0]
    for s in data:
        if s == "T":
            t += 1
        if s == "G":
            g += 1
        if s == "C":
            c += 1

s = t
if s > g:
    s = g
if s > c:
    s = c

total = t * t + g * g + c * c + s * 7

print total
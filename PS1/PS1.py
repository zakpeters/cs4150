import sys
d = set()
sol = set()
x = 0

for line in sys.stdin:
    
    s = ''.join(sorted(line))
    if (x==0):
        x = 1
    elif(s not in d):
        d.add(s)
        sol.add(s)
    elif(s in sol):
        sol.remove(s)
    

print len(sol)

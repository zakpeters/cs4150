import sys



res=1
for line in sys.stdin:
    s = line.split()[0]
    for x in s:
        if x == "A":
            if res == 1:
                res = 2
            elif res == 2:
                res = 1
        elif x == "B":
            if res == 2:
                res = 3
            elif res == 3:
                res = 2
        else:
            if res == 3:
                res = 1
            elif res == 1:
                res = 3
print res
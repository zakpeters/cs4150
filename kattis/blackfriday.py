import sys

first = True
l = [0,0,0,0,0,0]
for line in sys.stdin:
    if first == True:
        first = False
    else:
        data = line.split()

for r in data:
    l[int(r)-1] += 1

x = 5

while(x>=0):
    if(l[x] == 1):
        sys.stdout.write(str(data.index(str(x+1))+1)+"\n")
        break
    x -= 1
if x == -1:
    sys.stdout.write("none\n")
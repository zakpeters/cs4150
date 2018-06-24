import sys

x = 0

l1 = 0
l2 = 0
z = 0

for line in sys.stdin:
    if(x==0):
        z = int(line.split()[0])%2
    if(x==1):
        l1 = line.split()[0]
    if(x==2):
        l2 = line.split()[0]
    x+=1

if z == 0:
    if l1 == l2:
        print "Deletion succeeded"
    else:
        print "Deletion failed"
else:
    l1 = l1.replace("0", "2")
    l1 = l1.replace("1", "0")
    l1 = l1.replace("2", "1")

    if l2 == l1:
        print "Deletion succeeded"
    else:
        print "Deletion failed"
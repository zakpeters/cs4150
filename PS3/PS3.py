import sys

input = []

for line in sys.stdin:
    data = line.split()
    input.append((int(data[0]), int(data[1])))


#diameter squared
d = input[0][0]**2
#star count

k = input[0][1]/2
del input[0]


def isCluster(x1,y1,x2,y2):
    distance = (x1 - x2)**2 + (y1 - y2)**2
    # print distance
    if distance > d:
        return False
    else:
        return True

def majority(indata):
    output = []
    size = len(indata)
    if(size == 0):
        return "NO"
    elif(size == 1):
        return indata[0]
    else:
        for i in range(0,size/2):
            if(isCluster(indata[i*2][0],indata[i*2][1], indata[i*2+1][0], indata[i*2+1][1])):
                output.append(indata[i*2])
        # print output
        x = majority(output)
        # print x

        if x == "NO":
            if len(input)%2 == 1:
                for i in range(0,size-1):
                    if (isCluster(indata[i][0], indata[i][1], indata[size-1][0], indata[size-1][1])):
                        return indata[i]
                return "NO"
        else:
            for i in range(0,size-1):
                if (isCluster(indata[i][0], indata[i][1], x[0], x[1])):
                    return x
            return "NO"




x = majority(input)
count = 0
if(x == "NO" or x == None):
    print "NO"
else:
    for i in range(0,len(input)):
        if (isCluster(input[i][0], input[i][1], x[0], x[1])):
            count += 1
    if count > k:
        print count
    else:
        print "NO"
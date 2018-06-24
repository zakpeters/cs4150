import sys

class Tree:
    def __init__(self,value):
        self.backing = {}
        self.backing[1] = value
        self.maxindex = 1

    def addNode(self, newvalue):
        currindex = 1
        while(currindex in self.backing):
            if (newvalue > self.backing[currindex]):
                currindex = currindex * 2+1
            elif(newvalue < self.backing[currindex]):
                currindex = currindex * 2

        self.backing[currindex] = newvalue
        if currindex > self.maxindex:
            self.maxindex = currindex

    def getShape(self):
        s = "0"*(self.maxindex+1)
        result = list(s)
        for i in self.backing.keys():
            result[i] = "1"
        return "".join(result)



def treeTest(test):
    t = Tree(int(test[0]))
    for i in range(1,len(test)):
        t.addNode(int(test[i]))
    return t.getShape()


x = False

result = set()
data = []
for line in sys.stdin:
    if(x != True):
        x = True
    else:
        data.append(line.split())

for x in data:
    result.add(treeTest(x))
print len(result)

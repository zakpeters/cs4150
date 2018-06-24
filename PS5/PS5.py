import sys

x = 0
a = 0

names = set()
friends = {}
check = []

for line in sys.stdin:
    data = line.split()
    if a == 0:
        x = int(data[0])
        a += 1
    elif a == 1:
        names.add(data[0])
        friends[data[0]] = []
        x -= 1
        if x==0:
            a+=1
    elif a == 2:
        x = int(data[0])
        a+=1
    elif a  == 3:
        friends[data[0]].append(data[1])
        friends[data[1]].append(data[0])
        x -= 1
        if x==0:
            a+=1
    elif a == 4:
        x = int(data[0])
        a += 1
    elif a == 5:
        check.append(data[0])
        x -= 1
        if x==0:
            break


def visit(dist, vert):
    for x in friends[vert]:
        if x not in dist.keys() or dist[x]>=dist[vert] + 1:
            dist[x] = dist[vert] + 1
            if(dist[x]<2):
                visit(dist, x)

def BFS(source):
    dist = {}
    dist[source] = 0
    visit(dist, source)
    return dist

def sortNames(dist):
    day_0 = []
    day_1 = []
    day_2 = []
    day_3 = []
    names_copy = set(names)
    for name in names:
        if name not in dist.keys():
            day_3.append(name)
        elif dist[name] == 0:
            day_0.append(name)
            names_copy.remove(name)
        elif dist[name] == 1:
            day_1.append(name)
            names_copy.remove(name)
        elif dist[name] == 2:
            day_2.append(name)
            names_copy.remove(name)
    to_print = sorted(day_0) + sorted(day_1) + sorted(day_2) + sorted(day_3)
    print " ".join(to_print)


for t in check:
    sortNames(BFS(t))
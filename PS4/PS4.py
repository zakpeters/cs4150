import sys

# def rec_topo_sort(visited,stack,edge):
#     visited[edge] = True
#
#     for e in edges[edge]:
#         if visited[e] == False:
#             rec_topo_sort(visited,stack,e)
#
#     stack.append(edge)
#
# def topo_sort(edges):
#     visited = {}
#     for x in edges.keys():
#         visited[x] = False
#     stack = []
#     for e in edges.keys():
#         if visited[e] == False:
#             rec_topo_sort(visited,stack,e)
#
#     return stack

weight = {}
edges = {}
trips = []

a = 0
b = 0
c = 0
for line in sys.stdin:
    data = line.split()
    if a == 0:
        a = int(data[0])
    elif a > 0:
        weight[data[0]] = int(data[1])
        edges[data[0]] = []
        a -= 1
        if a == 0:
            a = -1
    elif b == 0:
        b = int(data[0])
        if b == 0:
            b = -1

    elif b > 0:
        edges[data[0]].append(data[1])
        b -= 1
        if b == 0:
            b = -1
    elif c == 0:
        c = int(data[0])
    elif c > 0:
        trips.append(data)
        c -= 1
        if c == 0:
            break;

topo = topo_sort(edges)
topo = topo[::-1]


def topo_calc(start):
    #used to have infinity but this works
    dist = [float('inf')] * len(topo)
    pred = [None] * len(topo)

    dist[start] = 0

    for x in range(start, len(topo)):

        for e in edges[topo[x]]:
            i = topo.index(e)
            w = weight[e]

            if (i < x):
                raise RuntimeError("should never hit this point if topo sort worked")

            if (dist[i] > dist[x] + w):
                dist[i] = dist[x] + w
                pred[i] = x

    return dist

#generate lists of distances for each starting point
topolist = []
for i in range(0, len(topo)):
    topolist.append(topo_calc(i))

for t in trips:
    d = topolist[topo.index(t[0])]
    x = d[topo.index(t[1])]
    if x >= float('inf'):
        print "NO"
    else:
        print x


def topo_sort(unsorted):
    sorted = []

    acyclic = False
    while len(unsorted) != 0:
        for node, edges in unsorted.items():
            for edge in edges:
                if edge in unsorted:
                    break
            acyclic = True
            del unsorted[node]
            sorted.append(node)
        if not acyclic:
            raise NotImplementedError("Something went wrong with topo sort")
    return sorted
def dist_calc(trip):

    index = topo.index(trip[0])
    dest = topo.index(trip[1])

    #simple cases
    if(index>dest):
        return float("inf")
    elif(index == dest):
        return 0

    dist = [float("inf")]* len(topo)
    pred = [None] * len(topo)

    dist[index] = 0

    for x in range(index,dest):

        for e in edges[topo[x]]:
            i = topo.index(e)
            w = weight[e]

            if(i < x):
                raise RuntimeError("should never hit this point if topo sort worked")

            if( dist[i] > dist[x] + w):
                dist[i] = dist[x] + w
                pred[i] = x

    return dist[dest]

for t in trips:
    d = dist_calc(t)
    if(d == float("inf")):
        print "NO"
    else:
        print int(d)


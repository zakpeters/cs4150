import sys
import Queue
import math

edges = {}

def BFS(source):
    q = Queue.Queue()
    q.put(source)

    dist = {}
    dist[source] = 1.0

    while not q.empty():
        vert = q.get()
        for x in edges[vert]:
            newdist = dist[vert] * x[1]
            if x[0] not in dist or newdist > dist[x[0]]:
                dist[x[0]] = newdist
                q.put(x[0])

    return (dist)

exit = 0
x = False

for line in sys.stdin:
    data = line.split()
    if len(data) == 2:
        if(x != False):
            print "%.4f"  %BFS(0)[exit]
        if int(data[0]) == 0:
            break

        x = True
        edges = {}
        exit = int(data[0]) - 1
        edges[exit] = []
    else:
        if int(data[0]) not in edges:
            edges[int(data[0])] = []
        if int(data[1]) not in edges:
            edges[int(data[1])] = []
        edges[int(data[0])].append( ( int(data[1]), float(data[2]) ) )
        edges[int(data[1])].append( ( int(data[0]), float(data[2]) ) )


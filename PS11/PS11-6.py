import sys

arr = []
cache = []
dir = []
mini = 1001

def spider():
    dir[0][arr[0]] = 1
    cache[0][arr[0]] = arr[0]

    for i in range(1, len(arr)):
        for h in range(0,mini):
            if cache[i-1][h] != 1001:
                down = h-arr[i]
                up = h+arr[i]

                if down >= 0:
                    if cache[i][down] > cache[i-1][h]:
                        dir[i][down] = -1
                        cache[i][down] = cache[i-1][h]

                tmp = max(cache[i-1][h], up)

                if cache[i][up] > tmp:
                    dir[i][up] = 1
                    cache[i][up] = tmp

    if cache[len(arr)-1][0] == 1001:
        print "IMPOSSIBLE"
    else:
        res = ""
        h = 0
        #reverse construct the solution
        for i in reversed(range(len(arr))):
            if dir[i][h] == 1:
                h -= arr[i]
                res = "U" + res
            else:
                h += arr[i]
                res = "D" + res
        print res


first = -1
for line in sys.stdin:
    data = line.split()
    if first == -1:
        first = 0
    elif first == 0:
        first = 1
    else:
        first = 0
        arr = []
        x = 0
        for i in data:
            arr.append(int(i))
            x += int(i)
        if x%2 != 0:
            print "IMPOSSIBLE"
        else:
            mini = min(x+1, 1001)
            cache = [[1001 for x in xrange(mini)]for y in xrange(len(arr))]
            dir = [[0 for x in xrange(mini)]for y in xrange(len(arr))]
            spider()
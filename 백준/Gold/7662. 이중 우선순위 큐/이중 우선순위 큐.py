import sys
from heapq import heapify, heappop, heappush

T = int(sys.stdin.readline())
for test in range(T):
    k = int(sys.stdin.readline())
    minheap = []
    maxheap = []
    visited = [0 for _ in range(k+1)]

    for i in range(k):
        order = sys.stdin.readline().split()
        if order[0] == 'I':
            num = int(order[1])
            heappush(minheap, (num, i))
            heappush(maxheap, (-num, i))
            visited[i] = 1
        elif order[0] == 'D':
            exist = False
            if order[1] == '1':
                while maxheap:
                    a = heappop(maxheap)
                    if visited[a[1]]:
                        exist = True
                        break
                # if maxheap:
                #     a = heappop(maxheap)
                if exist:
                    visited[a[1]] = 0
            else:
                while minheap:
                    a = heappop(minheap)
                    if visited[a[1]]:
                        exist = True
                        break
                # if minheap:
                #     a = heappop(minheap)
                if exist:
                    visited[a[1]] = 0
    res = False
    while maxheap:
        a = heappop(maxheap)
        if visited[a[1]]:
            maxvalue = -a[0]
            res = True
            break
    while minheap:
        a = heappop(minheap)
        if visited[a[1]]:
            minvalue = a[0]
            break
    if res:
        print(maxvalue, minvalue)
    else:
        print("EMPTY")
        
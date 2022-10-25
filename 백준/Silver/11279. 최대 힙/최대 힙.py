import sys
from heapq import heappush, heappop, heapify, nlargest

N = int(sys.stdin.readline())
maxheap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heappush(maxheap, -x)
    elif maxheap:
        print(-heappop(maxheap))
    else:
        print(0)

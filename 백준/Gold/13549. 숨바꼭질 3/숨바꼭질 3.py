import sys
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush

INF = float('inf')

N, K = map(int, sys.stdin.readline().split())

distance = [INF] * (100001)
n = N

def dijkstra():
    que = []
    heappush(que, (0, n))
    while que:
        t, pos = heappop(que)
        if pos == K:
            return t
        if pos * 2 < 100001 and  distance[pos*2] > t:
            distance[pos*2] = t
            heappush(que, (t, pos*2))
        if pos > 0 and distance[pos-1] > t+1:
            distance[pos-1] = t+1
            heappush(que, (t+1, pos-1))
        if pos < 100000 and distance[pos+1] > t+1:
            distance[pos+1] = t+1
            heappush(que, (t+1, pos+1))
print(dijkstra())

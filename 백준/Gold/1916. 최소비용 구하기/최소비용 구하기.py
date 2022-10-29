import sys
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush

INF = float('inf')

edges = defaultdict(dict)
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    if end in edges[start]:
        edges[start][end] = min(cost, edges[start][end])
    else:
        edges[start][end] = cost

A, B = map(int, sys.stdin.readline().split())

distance = [INF] * (N+1)
distance[A] = 0

def dijkstra():
    que = []
    heappush(que, (0,A))
    while que:
        dis, city = heappop(que)
        if dis > distance[city]:
            continue
        for next in edges[city]:
            if distance[next] > dis + edges[city][next]:
                distance[next] = dis + edges[city][next]
                heappush(que, (distance[next], next))

dijkstra()
print(distance[B])
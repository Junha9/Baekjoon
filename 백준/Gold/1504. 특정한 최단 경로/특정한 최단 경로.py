import sys
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush

INF = float('inf')

N, E = map(int, sys.stdin.readline().split())
edges = defaultdict(dict)
for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    edges[a][b] = c
    edges[b][a] = c
v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(first, last):
    visited = [INF] * (N+1)
    visited[first] = 0
    que = []
    heappush(que, (0, first))
    while que:
        dis, pos = heappop(que)
        if dis > visited[pos]:
            continue
        for next in edges[pos]:
            new = dis + edges[pos][next]
            if new < visited[next]:
                visited[next] = new
                heappush(que, (new, next))
    return visited[last]

a = dijkstra(1,v1)
b = dijkstra(v1,v2)
c = dijkstra(v2,N)
d = dijkstra(1,v2)
e = dijkstra(v2,v1)
f = dijkstra(v1,N)
if INF not in [a,b,c,d,e,f]:
    print(min(a+b+c, d+e+f))
else:
    print(-1)
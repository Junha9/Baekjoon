import sys
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush

INF = float('inf')

N, M, X = map(int, sys.stdin.readline().split())
edges = defaultdict(dict)
for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    edges[start][end] = time

def dijkstra(start,end):
    total = [INF] * (N+1)
    total[start] = 0
    que = []
    heappush(que, (0, start))
    while que:
        time, position = heappop(que)
        if time > total[position]:
            continue
        for next in edges[position]:
            if total[next] > time + edges[position][next]:
                total[next] = time + edges[position][next]
                heappush(que, (total[next], next))
    return total[end]
res = []
for i in range(1, N+1):
    res.append(dijkstra(i,X)+dijkstra(X,i))
print(max(res))
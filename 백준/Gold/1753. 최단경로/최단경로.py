import sys
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = defaultdict(list)
for i in range(E):
    info = list(map(int, sys.stdin.readline().split()))
    graph[info[0]].append((info[1],info[2]))

distance = [float('inf')] * (V+1)
def dijkstra():
    que = []
    heappush(que, (0, K))
    distance[K] = 0
    while que:
        dis, node = heappop(que)
        if distance[node] < dis:
            continue
        for next in graph[node]:
            weight = dis + next[1]
            if weight < distance[next[0]]:
                distance[next[0]] = weight
                heappush(que, (weight, next[0]))

dijkstra()

for i in range(1, V+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])

        
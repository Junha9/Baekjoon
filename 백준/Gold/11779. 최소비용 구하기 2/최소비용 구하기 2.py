import sys
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush

INF = float('inf')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edges = defaultdict(dict)
for _ in range(m):
    departure, arrive, cost = map(int, sys.stdin.readline().split())
    if arrive in edges[departure]:
        cost = min(cost, edges[departure][arrive])
    edges[departure][arrive] = cost
A, B = map(int, sys.stdin.readline().split())
total = [INF] * (n+1)
total[A] = 0
path = dict()
que = []
heappush(que, (0, A))
while que:
    cost, pos = heappop(que)
    if cost > total[pos]:
        continue
    for next in edges[pos]:
        new = cost + edges[pos][next]
        if total[next] > new:
            total[next] = new
            path[next] = pos
            heappush(que, (new, next))
print(total[B])
res = [B]
temp = B
while True:
    pre = path[temp]
    temp = pre
    res.append(temp)
    if pre == A:
        break
print(len(res))
print(*res[::-1])
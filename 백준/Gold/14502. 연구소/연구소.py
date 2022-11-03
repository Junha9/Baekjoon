import sys
sys.setrecursionlimit(10 ** 5)
from collections import deque, defaultdict
from heapq import heappush, heappop, heapify, nlargest
from itertools import combinations
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
virus = []
walls = []
cnt = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == 2:
            virus.append((i,j))
        if data[i][j] == 0:
            cnt += 1
            walls.append((i,j))

wallsets = combinations(walls, 3)


def BFS(v, lst, k):
    global ans
    que = deque()
    que.append(v)
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 0:
                lst[nx][ny] = 2
                k -= 1
                if k < ans:
                    return 0
                que.append((nx,ny))
    return k
    
ans = 0
for wallset in wallsets:
    lst = copy.deepcopy(data)
    res = cnt
    for wall in wallset:
        lst[wall[0]][wall[1]] = 1
    for v in virus:
        c = BFS(v, lst, res)
        if c:
            res = c
        else:
            break
    else:
        if res > ans:
            ans = res
print(ans-3)



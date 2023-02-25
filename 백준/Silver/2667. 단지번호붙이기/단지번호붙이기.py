import sys
sys.setrecursionlimit(10**5)
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def DFS(x, y):
    global n
    n += 1
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and data[nx][ny] and not visited[nx][ny]:
            DFS(nx,ny)


lst = []
for i in range(N):
    for j in range(N):
        if data[i][j] and not visited[i][j]: 
            n = 0
            DFS(i, j)
            lst.append(n)
        # visited[i][j] = 1

lst.sort()
print(len(lst))
for num in lst:
    print(num)
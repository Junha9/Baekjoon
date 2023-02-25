import sys
sys.setrecursionlimit(10**5)
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]


que = deque()
que.append((0,0))
visited = [[0] * M for _ in range(N)]
def BFS():
    while que:
        x, y = que.popleft()
        if x == N-1 and y == M-1:
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] and not visited[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = 1
                if data[nx][ny] <= data[x][y]:
                    data[nx][ny] = data[x][y] + 1

BFS()

print(data[N-1][M-1])


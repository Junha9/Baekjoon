import sys
from collections import deque, defaultdict

M, N = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
que = deque()
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            que.append((i,j))
res = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while que:
    pos = que.popleft()
    x, y = pos[0], pos[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 0:
            data[nx][ny] = data[x][y] + 1
            res = max(res, data[nx][ny])
            que.append((nx,ny))
for line in data:
    if 0 in line:
        res = -1
        break

if res > 0:
    res -= 1
print(res)

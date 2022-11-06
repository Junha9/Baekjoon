import sys
from collections import deque, defaultdict

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, sys.stdin.readline().split())
data = [list(sys.stdin.readline().rstrip()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
def find(c, i, j):
    cnt = 1
    visited[i][j] = 1
    que = deque()
    que.append((i,j))
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and data[nx][ny] == c:
                visited[nx][ny] = 1
                cnt += 1
                que.append((nx, ny))
    return cnt ** 2
s1, s2 = 0, 0
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            color = data[i][j]
            strength = find(color, i, j)
            if color == 'W':
                s1 += strength
            else:
                s2 += strength
print(s1, s2)
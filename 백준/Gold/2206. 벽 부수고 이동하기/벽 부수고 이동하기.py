import sys
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    que = deque()
    que.append((0,0,0))
    visited[0][0][0] = 1
    while que:
        x,y,smash = que.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][smash]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if smash:
                    if data[nx][ny] == 0 and not visited[nx][ny][1] and not visited[nx][ny][0]:
                        visited[nx][ny][1] = visited[x][y][1] + 1
                        que.append((nx,ny,1))
                    pass
                else:
                    if data[nx][ny] == 0 and not visited[nx][ny][0]:
                        visited[nx][ny][0] = visited[x][y][0] + 1
                        que.append((nx,ny,0))
                    if data[nx][ny] == 1:
                        visited[nx][ny][1] = visited[x][y][0] + 1
                        que.append((nx,ny,1))
    return -1
N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
print(BFS())



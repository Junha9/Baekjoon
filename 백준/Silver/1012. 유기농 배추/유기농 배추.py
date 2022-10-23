import sys
sys.setrecursionlimit(10**5)
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x,y):
    lst[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and  lst[nx][ny] == 1:
            DFS(nx,ny)


T = int(sys.stdin.readline())
for test in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    lst = [[0]*N for _ in range(M)]
    for _ in range(K):
        x,y = map(int, sys.stdin.readline().split())
        lst[x][y] = 1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if lst[i][j] == 1:
                cnt += 1
                DFS(i, j)
    print(cnt)
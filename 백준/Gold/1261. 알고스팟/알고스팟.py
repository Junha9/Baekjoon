import sys
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush

INF = float('inf')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, sys.stdin.readline().split())
data = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
breakwall = [[INF] * M for _ in range(N)]
breakwall[0][0] = 0
def dijkstra():
    que = []
    heappush(que, (0, 0,0))
    while que:
        cnt, posx, posy = heappop(que)
        if cnt > breakwall[posx][posy]:
            continue
        for i in range(4):
            nx, ny = posx + dx[i], posy + dy[i]
            if not 0 <= nx < N or not 0 <= ny < M:
                continue
            if data[nx][ny] == 0:
                if breakwall[nx][ny] > cnt:
                    breakwall[nx][ny] = cnt
                    heappush(que, (cnt, nx, ny))
            else:
                if breakwall[nx][ny] > cnt+1:
                    breakwall[nx][ny] = cnt + 1
                    heappush(que, (cnt+1, nx,ny))
dijkstra()
print(breakwall[-1][-1])
import sys
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush

INF = float('inf')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(sys.stdin.readline())

data = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

change = [[INF] * n for _ in range(n)]
change[0][0] = -(data[0][0]-1)
def dijkstra():
    que = []
    heappush(que, (change[0][0], 0, 0))
    while que:
        cnt, x, y = heappop(que)
        if cnt > change[x][y]:
            continue
        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] and change[nx][ny] > cnt:
                    change[nx][ny] = cnt
                    heappush(que, (cnt, nx, ny))
                elif data[nx][ny] == 0 and change[nx][ny] > cnt+1:
                    change[nx][ny] = cnt+1
                    heappush(que, (cnt+1, nx, ny))
dijkstra()
print(change[-1][-1])
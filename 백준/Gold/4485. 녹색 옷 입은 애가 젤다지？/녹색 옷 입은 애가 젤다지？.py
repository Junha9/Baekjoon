import sys
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush

INF = float('inf')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
i = 0

def dijkstra():
    rupee = [[INF] *  N for _ in range(N)]
    rupee[0][0] = data[0][0]
    que = []
    heappush(que, (rupee[0][0], 0, 0))
    while que:
        money, x, y = heappop(que)
        if money > rupee[x][y]:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and money + data[nx][ny] < rupee[nx][ny]:
                rupee[nx][ny] = money + data[nx][ny]
                heappush(que, (money+data[nx][ny], nx, ny))
    # for line in rupee:
    #     print(line)
    return rupee[-1][-1]

while True:
    i += 1
    N = int(sys.stdin.readline())
    if N == 0:
        break
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(f'Problem {i}:', dijkstra())
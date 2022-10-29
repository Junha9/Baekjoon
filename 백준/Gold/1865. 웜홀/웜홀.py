import sys
from collections import deque, defaultdict


INF = 555555


def bellman_ford(edges, start):
    distance = [INF] * (N+1)
    distance[start] = 0

    for i in range(N-1):
         for start in edges:
            for end in edges[start]:
                if distance[end] > distance[start] + edges[start][end]:
                    distance[end] = distance[start] + edges[start][end]

    for start in edges:
        for end in edges[start]:
            if distance[end] > distance[start] + edges[start][end]:
                return 'YES'
    return 'NO'


T = int(sys.stdin.readline())
for test in range(T):
    N, M, W = map(int, sys.stdin.readline().split())
    edges = defaultdict(dict)
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        if E in edges[S]:
            T = min(T, edges[S][E])
        edges[S][E] = T
        edges[E][S] = T
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        edges[S][E] = -T

    print(bellman_ford(edges, 1))
    
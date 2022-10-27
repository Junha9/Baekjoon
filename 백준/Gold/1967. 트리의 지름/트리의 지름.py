import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**5)

def DFS(pos, v):
    for a,b in graph[pos]:
        if not visited[a]:
            visited[a] = b+v
            DFS(a, b+v)

    return
n = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(n-1):
    info = list(map(int, sys.stdin.readline().split()))
    graph[info[0]].append((info[1], info[2]))
    graph[info[1]].append((info[0], info[2]))
visited = [0] * (n+1)
visited[1] = -1
DFS(1,0)
end = visited.index(max(visited))
start = end
visited = [0] * (n+1)
visited[start] = -1
DFS(start, 0)
print(max(visited))
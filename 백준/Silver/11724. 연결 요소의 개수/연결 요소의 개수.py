import sys
from collections import deque, defaultdict

def BFS(n):
    que = deque()
    que.append(n)
    while que:
        number = que.popleft()
        for nodes in dic[number]:
            if not visited[nodes]:
                visited[nodes] = 1
                que.append(nodes)

N, M = map(int, sys.stdin.readline().split())
visited = [0] * (N + 1)
setlist = []
dic = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    dic[u].append(v)
    dic[v].append(u)
cnt = 0 
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        BFS(i)
print(cnt)
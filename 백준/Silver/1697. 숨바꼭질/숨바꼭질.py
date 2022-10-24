import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())
que = deque()
que.append(N)
visited = [0] * (10**5 + 1)
while True:
    pos= que.popleft()
    if pos == K:
        res = visited[pos]
        break
    if 0 <= pos-1 <= 10**5 and not visited[pos-1]:
        visited[pos-1] = visited[pos]+1
        que.append(pos-1)
    if 0 <= pos+1 <= 10**5 and not visited[pos+1]:
        visited[pos+1] = visited[pos]+1
        que.append(pos+1)
    if 0 <= pos*2 <= 10**5 and not visited[pos*2]:
        visited[pos*2] = visited[pos] + 1
        que.append(pos*2)
print(res)
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
que = deque(range(1, n+1))
i = 0
res = []
while que:
    que.append(que.popleft())
    i += 1
    if i % k == 0:
        res.append(que.pop())
res = list(map(str, res))
res = ', '.join(res)

print(f'<{res}>')
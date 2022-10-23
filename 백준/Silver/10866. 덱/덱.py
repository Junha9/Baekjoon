import sys
from collections import deque
que = deque()
T = int(sys.stdin.readline())
for i in range(T):
    order = sys.stdin.readline().rstrip()
    if order == 'pop_front':
        print(que.popleft()) if len(que) else print(-1)
    elif order == 'pop_back':
        print(que.pop()) if len(que) else print(-1)
    elif order == 'size':
        print(len(que))
    elif order == 'empty':
        print(1) if len(que)== 0 else print(0)
    elif order == 'front':
        print(que[0]) if len(que) != 0 else print(-1)
    elif order == 'back':
        print(que[-1]) if len(que) != 0 else print(-1)
    elif 'push' in order:
        X = int(order.split()[-1])
        if 'front' in order:
            que.appendleft(X)
        else:
            que.append(X)
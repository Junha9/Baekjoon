import sys
from collections import deque, defaultdict


def BFS():
    que = deque()
    que.append(1)
    while que:
        n = que.popleft()
        infested[n] = 1
        for pc in dict[n]:
            if not infested[pc]:
                que.append(pc)


c = int(sys.stdin.readline())
net = int(sys.stdin.readline())
dict = defaultdict(list)
infested = [0] * (c+1)
for _ in range(net):
    line = list(map(int, sys.stdin.readline().split()))
    dict[line[0]].append(line[1])
    dict[line[1]].append(line[0])
BFS()
print(infested.count(1) - 1)
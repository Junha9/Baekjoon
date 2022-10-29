import sys

N, D = map(int, sys.stdin.readline().split())
dis = [i for i in range(D+1)]
shortcuts = []
for _ in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    shortcuts.append((start,end,length))

for position in range(D+1):
    dis[position] = min(dis[position], dis[position-1] + 1)

    for start,end,length in shortcuts:
        if start == position and end <= D and dis[end] > dis[start] + length:
            dis[end] = dis[start] + length

print(dis[-1])
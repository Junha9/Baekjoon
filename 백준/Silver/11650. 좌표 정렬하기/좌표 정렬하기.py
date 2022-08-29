import sys

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
data.sort(key=lambda x: x[1])
data.sort(key=lambda x: x[0])
for point in data:
    print(*point)
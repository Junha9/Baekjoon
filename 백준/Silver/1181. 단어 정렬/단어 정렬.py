import sys

N = int(sys.stdin.readline())
data = [sys.stdin.readline().rstrip() for _ in range(N)]
data = list(set(data))
data.sort()
data = sorted(data, key=lambda x: len(x))
for i in data:
    print(i)
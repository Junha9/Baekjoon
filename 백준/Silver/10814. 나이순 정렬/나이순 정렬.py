import sys

N = int(sys.stdin.readline())
data = [sys.stdin.readline().split() for _ in range(N)]
data.sort(key=lambda x: int((x[0])))
for person in data:
    print(*person)
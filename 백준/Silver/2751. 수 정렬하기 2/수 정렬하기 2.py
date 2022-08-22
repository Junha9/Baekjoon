import sys
N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(N)]
data.sort()
for num in data:
    print(num)
import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
res = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if data[i] + data[j] + data[k] > M:
                continue
            else:
                res = max(res, data[i] + data[j] + data[k])
print(res)
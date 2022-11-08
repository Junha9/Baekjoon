import sys

N, K, L = map(int, sys.stdin.readline().split())
n, k , l = N, K, L
i = 0
res = -1
while n > 1:
    i += 1
    n = (n+1) // 2
    k = (k+1) // 2
    l = (l+1) // 2
    if k == l:
        res = i
        break
print(res)
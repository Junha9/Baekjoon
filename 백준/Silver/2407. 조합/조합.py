import sys

n, m = map(int, sys.stdin.readline().split())

if m > n // 2:
    m = n-m
res = 1
for i in range(m):
    res *= (n-i)
    res = res//(i+1)
print(int(res))
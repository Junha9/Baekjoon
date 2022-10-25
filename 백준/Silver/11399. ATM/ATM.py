import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
lst = list(enumerate(data, start=1))
lst.sort(key=lambda x: x[1])
j = N
res = 0
for i, t in lst:
    res += t * j
    j -= 1
print(res)


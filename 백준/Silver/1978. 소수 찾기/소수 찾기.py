import sys

def prime(n):
    if n == 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    else:
        return 1

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
cnt = 0
for n in data:
    cnt += prime(n)
print(cnt)
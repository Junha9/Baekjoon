import sys


def female(n):
    data[n] = 0 if data[n] else 1
    i = 0
    while True:
        i += 1
        if n+i > S or n-i < 1:
            break
        if data[n-i] != data[n+i]:
            break
        else:
            data[n-i] = 0 if data[n-i] else 1
            data[n+i] = data[n-i]


S = int(sys.stdin.readline())
data = [0] + list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
for _ in range(N):
    gender, number = map(int, sys.stdin.readline().split())
    if gender == 1:
        for i in range(number, S+1, number):
            data[i] = 0 if data[i] else 1
    else:
        female(number)
for i in range(1, S+1, 20):
    print(*data[i:i+20])
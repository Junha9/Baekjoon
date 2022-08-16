import sys

def avg(lst):
    return sum(lst)/len(lst)

T = int(sys.stdin.readline())
for test in range(T):
    sys.stdin.readline()
    n, m = map(int, sys.stdin.readline().split())
    c = list(map(int, sys.stdin.readline().split()))
    e = list(map(int, sys.stdin.readline().split()))
    a, b = avg(c), avg(e)
    cnt = 0
    for i in range(n):
        if c[i] < a and c[i] > b:
            cnt += 1
    print(cnt)
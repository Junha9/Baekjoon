import sys


def backtrack(value):
    global cnt
    if value == n:
        cnt += 1
        return
    for i in range(1, 4):
        if value + i <= n:
            backtrack(value+i)



T = int(sys.stdin.readline())
for test in range(T):
    n = int(sys.stdin.readline())
    cnt = 0
    backtrack(0)
    print(cnt)
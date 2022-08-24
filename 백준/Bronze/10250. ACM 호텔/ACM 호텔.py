import sys

T = int(sys.stdin.readline())
for test in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    x, y = 1, 0
    for i in range(N):
        y += 1
        if y == H+1:
            x += 1
            y = 1
    xx = str(x)
    if x < 10:
        xx = '0'+xx
    yy = str(y)
    print(yy+xx)
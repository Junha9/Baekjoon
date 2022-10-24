import sys

def samecolor(x,y, N):
    global cnt1, cnt2
    divide = False
    if N == 1:
        if data[x][y] == 1:
            cnt2 += 1
        else:
            cnt1 += 1
        return
    init = data[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if data[i][j] != init:
                divide=True
                break
        else:
            continue
        break
    else:
        if init == 0:
            cnt1 += 1
        else:
            cnt2 += 1
        pass
    if divide:
        n = N // 2
        samecolor(x,y,n)
        samecolor(x+n,y, n)
        samecolor(x,y+n, n)
        samecolor(x+n,y+n,n)
    pass

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt1, cnt2 = 0, 0
samecolor(0,0, N)
print(cnt1, cnt2)
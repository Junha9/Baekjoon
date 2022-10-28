import sys


N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = data[0][0]
for i in range(N):
    for j in range(N):
        if i == 0 and j > 0:
            dp[i][j] = dp[i][j-1] + data[i][j]
        elif j == 0 and i > 0:
            dp[i][j] = dp[i-1][j] + data[i][j]
        elif i > 0 and j > 0:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + data[i][j]

for test in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    res = dp[x2][y2]
    if y1 > 0:
        res -= dp[x2][y1-1]
    if x1 > 0 :
        res -= dp[x1-1][y2]
    if x1 > 0 and y1 > 0:
        res += dp[x1-1][y1-1]

    print(res)
import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cost = [[0]* i for i in range(1, n+1)]
for i in range(n):
    if i == 0:
        cost[i][0] = data[i][0]
    else:
        for j in range(i+1):
            if j == 0:
                cost[i][j] = cost[i-1][j] + data[i][j]
            elif j == i:
                cost[i][j] = cost[i-1][j-1] + data[i][j]
            else:
                cost[i][j] = max(cost[i-1][j], cost[i-1][j-1]) + data[i][j]
print(max(cost[-1]))
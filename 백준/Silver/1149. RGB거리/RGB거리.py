import sys



N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
minimum = float('inf')
cost = []
cost.append(data[0][:])
for i in range(1, N):
    temp =[]
    r = min(cost[i-1][1], cost[i-1][2]) + data[i][0]
    g = min(cost[i-1][0], cost[i-1][2]) + data[i][1]
    b = min(cost[i-1][1], cost[i-1][0]) + data[i][2]
    temp.append(r)
    temp.append(g)
    temp.append(b)
    cost.append(temp)
print(min(cost[-1]))
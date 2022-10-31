import sys


N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [0] * 1001
temp, cnt = 0, 0
for i in range(N):
    num = data[i]
    dp[num] = max(dp[:num])+1
print(max(dp))
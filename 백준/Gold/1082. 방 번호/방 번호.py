import sys


N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
n = M // min(P)
dp = [-1] * (M+1)
for i in range(N):
    price = P[N-1-i]
    for j in range(price, M+1):
        dp[j] = max(dp[j], dp[j-price] * 10+N-1-i, N-1-i)
print(dp[M])
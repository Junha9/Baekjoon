N, M, K = list(map(int, input().split()))
n = K // M
m = K - n * M
print(n, m)

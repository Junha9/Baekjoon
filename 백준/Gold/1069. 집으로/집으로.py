import sys

X, Y, D, T = map(int, sys.stdin.readline().split())

distance = (X ** 2 + Y ** 2 ) ** 0.5
m, r = divmod(distance, D) 

if distance >= D:
    res = m * T + r
    res2 = (m+1) * T
else:
    res = (T+D-distance)
    res2 = 2 * T

res = min(res, res2, distance)
print(res)

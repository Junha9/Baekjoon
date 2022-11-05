import sys

X, Y = map(int, sys.stdin.readline().split())

Z, re= divmod(Y * 100, X)
Z = int(Z)
if Z >= 99:
    res = -1
else:
    i = (X * (Z+1) - 100 * Y ) / (99 - Z)
    if i == int(i):
        res = int(i)
    else:
        res = int(i) + 1
print(res)
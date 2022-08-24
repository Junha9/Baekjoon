import sys

while True:
    lengths = list(map(int, sys.stdin.readline().split()))
    if 0 in lengths:
        break
    lengths.sort()
    res = 'wrong'
    if lengths[0] ** 2 + lengths[1] ** 2 == lengths[2] ** 2:
        res = 'right'
    print(res)
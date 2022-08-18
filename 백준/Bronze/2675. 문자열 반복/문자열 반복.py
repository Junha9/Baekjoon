import sys
T = int(sys.stdin.readline())
for i in range(T):
    n, c = sys.stdin.readline().split()
    n = int(n)
    res = ''
    for l in c:
        res += l*n
    print(res)

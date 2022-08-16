import sys
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    a = int(n ** 0.5)
    i = 1
    t = n
    while i < t:
        i += 1
        if n % i == 0:
            print('NO')
            break
        if i > 10 ** 6:
            print('YES')
            break
        t = n / i
            
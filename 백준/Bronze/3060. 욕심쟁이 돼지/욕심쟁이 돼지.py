import sys
T = int(sys.stdin.readline())
for test in range(T):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    d = 0
    while True:
        d += 1
        if sum(data) > n:
            break
        temp = [0 for _ in range(6)]
        for i in range(6):
            temp[i] = data[i] + data[i-1] + data[i-3] + data[i-5]
        data = list(temp)
    print(d)
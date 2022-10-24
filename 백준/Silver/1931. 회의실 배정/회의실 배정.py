import sys


N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
data.sort(key=lambda x:(x[1], x[0]))
temp = 0
cnt = 0
for conf in data:
    if temp > conf[0]:
        pass
    else:
        temp = conf[1]
        cnt += 1
        pass
print(cnt)
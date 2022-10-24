import sys

N = int(sys.stdin.readline())
i = 0
lst = [0] * (N + 1)
lst[1] = 0
for i in range(2,N+1):
    temp = []
    if i % 2 == 0:
        temp.append((lst[i // 2]) + 1)
    if i % 3 == 0:
        temp.append((lst[i // 3]) + 1)
    temp.append(lst[i-1] + 1)
    lst[i] = min(temp)
print(lst[N])
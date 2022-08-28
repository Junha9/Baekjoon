import sys


N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
index = sorted(data, key=lambda x: x[1])[-1][0]
data.sort(key=lambda x: x[0])
max_index = data[-1][0]
lst = [0] * (max_index + 1)
for a in data:
    lst[a[0]] = a[1]
s, temp = 0, 0
for i in range(data[0][0], index):
    if lst[i] > temp:
        temp = lst[i]
    s += temp
temp = 0
for i in range(max_index, index, -1):
    if lst[i] > temp:
        temp = lst[i]
    s += temp
s += lst[index]
print(s)
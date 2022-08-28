import sys

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]
lst = [0] * 6
for i in range(1, 5):
    lst[i] = len(list(filter(lambda x: x[0] == i, data)))
main = []
for i in range(6):
    if lst[data[i][0]] == 1:
        main.append(data[i][1])
    elif data[i-2][0] == data[i][0]:
        if lst[data[i-3][0]] == 1:
            index = i
sub = data[index-1][1] * data[index][1]
a = (main[0] * main[1] - sub) * N
print(a)

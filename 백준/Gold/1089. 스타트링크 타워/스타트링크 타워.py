import sys
sys.setrecursionlimit(10 ** 5)

N = int(sys.stdin.readline())
data = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
def num(i, j):
    res = [0] * 10
    lst = []
    if data[i+1][j+1] == '#' or data[i+3][j+1] == '#':
        return lst
    if data[i][j] == '#':
        res[1] += 1
    if data[i][j+1] == '#':
        res[1] += 1
        res[4] += 1
    if data[i+1][j] == '#':
        res[1] += 1
        res[2] += 1
        res[3] += 1
        res[7] += 1
    if data[i+1][j+2] == '#':
        res[1] += 1
        res[5] += 1
        res[6] += 1
    if data[i+2][j] == '#':
        res[1] += 1
        res[7] += 1
    if data[i+2][j+1] == '#':
        res[1] += 1
        res[0] += 1
        res[7] += 1
    if data[i+3][j] == '#':
        res[1] += 1
        res[3] += 1
        res[4] += 1
        res[5] += 1
        res[7] += 1
        res[9] += 1
    if data[i+3][j+2] == '#':
        res[2] += 1
    if data[i+4][j] == '#' or data[i+4][j+1] == '#':
        res[1] += 1
        res[4] += 1
        res[7] += 1
    for k in range(10):
        if res[k] == 0:
            lst.append(k)
    return lst
tot = 1
sum = 0
res = []
for i in range(N):
    numbers = num(0, i*4)
    res.append(numbers)
    tot *= len(numbers)

for i in range(N):
    numbers = res[i]
    for number in numbers:
        sum += number * (10 ** (N-i-1)) * int(tot/len(numbers))

if tot == 0:
    print(-1)
else:
    print(sum/tot)
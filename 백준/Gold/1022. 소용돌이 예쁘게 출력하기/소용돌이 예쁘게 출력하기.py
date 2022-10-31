import sys

direction = [(0,1), (-1,0), (0, -1), (1,0)]

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

r = max(abs(r1), abs(r2))
c = max(abs(c1), abs(c2))
# print(r1,c1,r2,c2)
m = max(r,c)
lst = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
lstsize = len(lst) * len(lst[0])
i = 0
currentdirection = 0
x, y = 0, 0
size = 1
j = 0
cnt = 0
while True:
    i += 1
    j += 1
    if r1 <= x <= r2 and c1 <= y <= c2:
        cnt += 1
        lst[x-r1][y-c1] = i
        if cnt == lstsize:
            break
    if i == size ** 2:
        size += 1
    elif j == size:
        currentdirection = (currentdirection + 1) % 4
        j = 1
    x += direction[currentdirection][0]
    y += direction[currentdirection][1]

maxima = max(lst[0][0], lst[0][c2-c1], lst[r2-r1][0], lst[r2-r1][c2-c1])
length = len(str(maxima))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        val = str(lst[i][j])
        print(val.rjust(length,' '), end=' ')
    if i < r2-r1:
        print()
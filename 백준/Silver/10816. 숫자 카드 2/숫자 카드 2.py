import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
dic = dict()
for num in data:
    if dic.get(num):
        dic[num] += 1
    else:
        dic[num] = 1
for num in target:
    res = dic.get(num, 0)
    print(res, end=' ')
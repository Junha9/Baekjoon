import sys

N = int(sys.stdin.readline())
m = 0
for i in range(1, N+1):
    numbers = list(map(int, sys.stdin.readline().split()))
    subsets = [[]]
    for num in numbers:
        size = len(subsets)
        for y in range(size):
            subsets.append(subsets[y]+[num])
    len3 = list(filter(lambda x: len(x) == 3, subsets))
    localm = max(map(lambda x: sum(x) % 10, len3))
    if localm >= m:
        ind = i
        m = localm
print(ind)
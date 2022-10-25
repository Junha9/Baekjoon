import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
lst1 = list(enumerate(data, start=1))
lst1.sort(key=lambda x: x[1])
i = -1
temp = 'value'
lst2 = []
for index, num in lst1:
    if num != temp:
        i += 1
        lst2.append((index,i))
        temp = num
    else:
        lst2.append((index, i))
lst2.sort()
for i, num in lst2:
    print(num, end=' ')
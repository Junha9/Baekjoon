import sys

n = int(sys.stdin.readline())

lst = [0,1,2]
for i in range(3, n+1):
    lst.append(lst[-1]+lst[-2])
if n == 1:
    print(1)
else:
    print(lst[-1] % 10007)
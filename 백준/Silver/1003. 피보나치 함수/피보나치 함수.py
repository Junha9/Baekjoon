import sys
from collections import deque


T = int(sys.stdin.readline())
for test in range(T):
    lst1, lst2 = [1, 0], [0, 1]
    N = int(sys.stdin.readline())
    res = [0, 0]
    if N >=1 :
        for _ in range(N-1):
            lst1.append(lst1[-1]+lst1[-2])
            lst2.append(lst2[-1]+lst2[-2])
        print(lst1[-1], lst2[-1])  
    elif N == 0:
        print(1, 0)
   
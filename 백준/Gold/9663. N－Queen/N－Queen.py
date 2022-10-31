import sys
sys.setrecursionlimit(10 ** 5)
from collections import deque, defaultdict
from heapq import heappush, heappop, heapify, nlargest

N = int(sys.stdin.readline())
visited = [0] * N
cross1 = [0] * (2 * N)
cross2 = [0] * (2 * N)
res = 0
def backtrack(i):
    if i == N:
        global res
        res += 1
        return
    for j in range(N):
        if not visited[j] and not cross1[i+j] and not cross2[i-j]:
            visited[j] = cross1[i+j] = cross2[i-j] = 1
            backtrack(i+1)
            visited[j] = cross1[i+j] = cross2[i-j] = 0

backtrack(0)
print(res)
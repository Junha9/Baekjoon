import sys

from heapq import heappush, heappop, heapify, nlargest


N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    heappush(heap, int(sys.stdin.readline()))
res = 0
while len(heap) > 1:
    a, b = heappop(heap), heappop(heap)
    res += (a + b)
    heappush(heap, a+b)
print(res)
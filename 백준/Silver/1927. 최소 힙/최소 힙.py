import sys
from collections import deque
from heapq import heappush, heappop



N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    action = int(sys.stdin.readline())
    if action == 0:
        print(heappop(heap)) if heap else print(0)
    else:
        heappush(heap, action)

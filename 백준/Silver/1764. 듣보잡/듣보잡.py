import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
dudbo = set()
dudbojob = []
cnt = 0
for _ in range(N):
    dudbo.add(sys.stdin.readline().rstrip())

for i in range(M):
    person = sys.stdin.readline().rstrip()
    if person in dudbo:
        cnt += 1
        dudbojob.append(person)
dudbojob.sort()
print(cnt)
for person in dudbojob:
    print(person)
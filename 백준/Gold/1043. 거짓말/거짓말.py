import sys
sys.setrecursionlimit(10 ** 5)
from collections import deque, defaultdict

N, M = map(int, sys.stdin.readline().split())
knowtruth = list(map(int, sys.stdin.readline().split()))
index = set(knowtruth[1:])
parties = []
visited = [0] * (N+1)
graph = defaultdict(set)
res = 0
for i in range(M):
    party = list(map(int, sys.stdin.readline().split()))
    partypeople = party[1:]
    parties.append(partypeople)
    for person in partypeople:
        graph[person].update(set(partypeople))

que = deque(index)
while que:
    person = que.popleft()
    for friend in graph[person]:
        if not visited[friend]:
            visited[friend] = 1
            que.append(friend)
for party in parties:
    for person in party:
        if visited[person] == 1:
            break
    else:
        res += 1
print(res)
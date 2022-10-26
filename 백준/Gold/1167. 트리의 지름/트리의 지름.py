import sys
sys.setrecursionlimit(10**5)

def DFS(p,v):
    for a,b in data[p-1]:
        if visited[a] == -1:
            visited[a] = v + b
            DFS(a, v+b)
    
V = int(sys.stdin.readline())
data =[list() for _ in range(V)]
for _ in range(V):
    inputdata = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(inputdata)-2, 2):
        data[inputdata[0]-1].append((inputdata[j], inputdata[j+1]))
visited = [-1] * (V+1)
start = 1
visited[start] = 0
DFS(start, 0)
start = visited.index(max(visited))
visited = [-1] * (V+1)
visited[start] = 0
DFS(start, 0)
print(max(visited))
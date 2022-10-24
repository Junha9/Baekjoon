import sys

N, M = map(int, sys.stdin.readline().split())
dict = {}
revdict = {}
for j in range(1, N+1):
    temp = sys.stdin.readline().rstrip()
    dict[j] = temp
    revdict[temp] = j
for i in range(M):
    problem = sys.stdin.readline().rstrip()
    if problem.isdigit():
        print(dict[int(problem)])
    else:
        print(revdict[problem])

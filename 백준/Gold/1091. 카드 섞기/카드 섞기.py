import sys


N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
S = list(map(int, sys.stdin.readline().split()))

lst = list(range(N))
start = list(lst)
cnt = 0

def check(lstin):
    for j in range(N):
        if P[lstin[j]] != j % 3:
            return False
    return True

while True:
    if check(lst):
        break
    cnt += 1
    if cnt > 1 and lst == start:
        cnt = -1
        break
    new = [0] * N
    for i in range(N):
        new[S[i]]=lst[i]
    lst = list(new)
print(cnt)

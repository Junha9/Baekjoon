import sys

N, M = map(int, sys.stdin.readline().split())
def per(i, n, lst):
    if i > N + 1:
        return
    if n == M:
        print(*lst)
        return
    per(i+1,n+1, lst+[i])
    per(i+1,n, lst)

per(1, 0, [])
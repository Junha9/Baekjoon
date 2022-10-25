import sys

M = int(sys.stdin.readline())
S = set()
for i in range(M):
    order = sys.stdin.readline().split()
    if 'add' in order:
        S.add(int(order[-1]))
    elif 'remove' in order and int(order[-1]) in S:
        S.remove(int(order[-1]))
    elif 'check' in order:
        print(1) if int(order[-1]) in S else print(0)
    elif 'toggle' in order:
        S.remove(int(order[-1])) if int(order[-1]) in S else S.add(int(order[-1]))
    elif 'all' in order:
        S = set(range(1,21))
    elif 'empty':
        S = set()
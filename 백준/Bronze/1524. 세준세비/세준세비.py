import sys
T = int(sys.stdin.readline())

for test in range(T):
    sys.stdin.readline()
    n, m = list(map(int, sys.stdin.readline().split()))
    s = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    
    print('S') if max(s) >= max(b) else print('B')
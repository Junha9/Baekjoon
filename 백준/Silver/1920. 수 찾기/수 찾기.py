import sys

N = int(sys.stdin.readline())
A = set(sys.stdin.readline().split())
M = int(sys.stdin.readline())
X = sys.stdin.readline().split()


# s = set()
# a = set()
for n in X:
    if n in A:
        print(1)
#     elif n in a:
#         print(0)
#     elif n in A:
#         print(1)
#         s.add(n)
    else:
        print(0)
#         a.add(n)
import sys

N = int(sys.stdin.readline())
numbers = sys.stdin.readline().rstrip()
s = 0
for i in numbers:
    s += int(i)
print(s)
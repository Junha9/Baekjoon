import sys
from itertools import combinations

n, k = map(int, sys.stdin.readline().split())
a = list(combinations(range(n), k))
print(len(a))
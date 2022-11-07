import sys
sys.setrecursionlimit(10 ** 5)
from collections import deque, defaultdict

N = int(sys.stdin.readline())
data = [sys.stdin.readline().rstrip() for _ in range(N)]
alphabets = defaultdict(int)
for string in data:
    n = len(string)
    for i in range(n):
        alphabets[string[i]] += 10**(n-1-i)
dic = dict(alphabets)
dic = sorted(dic.values())
i = 9
res = 0
while dic:
    res += dic.pop() * i
    i -= 1
print(res)
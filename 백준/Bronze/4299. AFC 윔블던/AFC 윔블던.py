a, b = list(map(int, input().split()))
c = (a + b) / 2
d = (a - b) / 2
if d - int(d) == 0.5 or c - int(c) == 0.5 or a < b:
    print(-1)
else:
    print(int(c), int(d))

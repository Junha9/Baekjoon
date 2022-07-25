n, x = list(map(int,input().split()))
lst = list(map(int, input().split()))
s = []
for i in lst:
    if i < x:
        s.append(str(i))
print(' '.join(s))
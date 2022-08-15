n, p = map(int, input().split())
lst = []
o = n
while n not in lst:
    lst.append(n)
    n = (n * o) % p
i = lst.index(n)
print(len(lst[i:]))

x, y = list(map(int,input().split()))
def rev(a):
    s, r = str(a), ''
    for l in s:
        r = l + r
    return int(r)

print(rev(rev(x) + rev(y)))
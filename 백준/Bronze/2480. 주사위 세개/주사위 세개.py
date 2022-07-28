a, b, c = list(map(int, input().split()))
if a == b and b == c:
    print(10000 + 1000 * a)
elif a == b or b == c or a == c:
    lst = [a,b,c]
    for x in list({a,b,c}):
        lst.remove(x)
    print(1000 + lst[0] * 100)
else:
    print(max(a,b,c) * 100)
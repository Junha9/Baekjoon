h, m, s = list(map(int, input().split()))
t = int(input())
m += (s + t) // 60
s = (s + t) % 60
h += m // 60
m = m % 60
h = h % 24
print(h, m, s)
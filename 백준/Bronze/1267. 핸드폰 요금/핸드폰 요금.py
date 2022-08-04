n = int(input())
lst = list(map(int, input().split()))
m, y = 0, 0
for t in lst:
    y += ((t // 30) + 1) * 10
    m += ((t // 60) + 1) * 15
if y > m:
    print('M', m)
elif y == m:
    print('Y M', y)
else:
    print('Y', y)
    

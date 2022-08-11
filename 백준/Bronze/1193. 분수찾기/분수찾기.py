x = int(input())
n, i = 0, 0
while n < x :
    i += 1
    n += i
n -= i
k = x-n
if i % 2 ==0:
    a, b = k, i+1-k
else:
    a, b = i+1-k, k
print(f'{a}/{b}')

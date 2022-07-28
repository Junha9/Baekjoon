n, c = list(map(int,input().split()))
total_area, bedroom_area, temp = 0, 0, 0
for i in range(n):
    a, t = input().split()
    total_area += int(a)
    if t == 'bedroom':
        bedroom_area += int(a)
    if t == 'balcony':
        temp += int(a)
total_price = (total_area - temp * 0.5) * c
print(total_area)
print(bedroom_area)
print(total_price)

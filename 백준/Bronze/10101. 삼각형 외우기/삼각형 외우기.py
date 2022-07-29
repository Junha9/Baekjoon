a,b,c = [int(input()) for _ in range(3)]

if a + b + c != 180:
    print('Error')
elif a == b == 60:
    print('Equilateral')
elif len(set([a,b,c])) == 2:
    print('Isosceles')
elif len(set([a,b,c])) == 3:
    print('Scalene')
def prime(n):
    lst = []
    i = 2
    while i <= n:
        if n % i == 0:
            for j in range(2, i):
                if i % j == 0 :
                    break
            else:
                lst.append(i)
                n = int(n/i)
                continue
        i += 1
    return lst
a, b = map(int, input().split())
lsta, lstb = prime(a), prime(b)

primes = [1]
for num in lsta:
    if num in lstb:
        lstb.remove(num)
        primes.append(num)
res = 1
for nums in primes:
    res *= nums
print(res)
print(int(a*b/res))


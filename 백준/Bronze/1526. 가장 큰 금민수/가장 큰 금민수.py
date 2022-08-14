i = input()

n = int(i)
while True:
    for k in str(n):
        if not(k == '4' or k == '7'):
            break
    else:
        print(n)
        break
    n -= 1

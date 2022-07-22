while True:
    a, b = list(map(int, input().split()))
    if not a and not b:
        break
    else:
        pass
    if a > b:
        print('Yes')
    else:
        print('No')
import sys
case = 0
while True:
    n, p = map(int, sys.stdin.readline().split())
    if n == 0 or p == 0:
        break
    if case > 0:
        print()
    case += 1
    requirements = [sys.stdin.readline().rstrip() for _ in range(n)]
    vendors = []
    tempmax = 0
    for i in range(p):
        vendors.append(sys.stdin.readline().rstrip())
        data = sys.stdin.readline().split()
        price = float(data[0])
        n_items = int(data[1])
        items = []
        for j in range(n_items):
            items.append(sys.stdin.readline().rstrip())
        if n_items/p > tempmax:
            tempmax = n_items/p
            tempprice = price
            index = i
        elif n_items/p == tempmax:
            if price < tempprice:
                tempprice = price
                index = i
    print(f'RFP #{case}')
    print(vendors[index])
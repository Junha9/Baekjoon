while True:
    try:
        n, s = list(map(int, input().split()))
        print(s // (n + 1))
    except EOFError:
        break
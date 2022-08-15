m, n = map(int, input().split())

def cnt(m, n):
    if m == 0:
        return -2
    elif n == 0:
        return -1
    elif m == 1:
        return 0
    elif n == 1:
        return 1
    return cnt(m-2, n-2) + 4

print(cnt(m,n))
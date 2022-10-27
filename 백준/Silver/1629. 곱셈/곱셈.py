import sys

def divide(k):
    if k == 1:
        return A % C
    if k % 2 == 0:
        return (divide(k//2) **2 ) % C
    else:
        return (divide(k//2) ** 2 * divide(1)) % C 
A, B, C = map(int, sys.stdin.readline().split())
print(divide(B))
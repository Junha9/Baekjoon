import sys

def cnt(data,R,C,i,j):
    cnt = 0
    for a in range(max(0,i-1), min(R,i+2)):
        for b in range(max(0, j-1), min(C, j+2)):
            if data[a][b] == '*' and not(a == i and b == j):
                cnt += 1
    return cnt

while True:
    R, C = map(int, sys.stdin.readline().split())
    if R == 0 or C == 0:
        break
    data = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
    explosive =[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if data[i][j] == '*':
                explosive[i][j] = '*'
            else:
                explosive[i][j] = str(cnt(data,R,C,i,j))
    for row in explosive:
        print(''.join(row))
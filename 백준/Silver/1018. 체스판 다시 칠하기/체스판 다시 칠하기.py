import sys
def chess(lst):
    cnt1, cnt2 = 0, 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if lst[i][j] == 'W':
                    cnt1 += 1
                else:
                    cnt2 += 1
            else:
                if lst[i][j] == 'B':
                    cnt1 += 1
                else:
                    cnt2 += 1
    return min(cnt1,cnt2)


N, M = map(int, input().split())
data = [sys.stdin.readline() for _ in range(N)]
boards = []
for i in range(N-8+1):
    for j in range(M-8+1):
        lst = [[0] * 8 for _ in range(8)]
        for l in range(8):
            for k in range(8):
                lst[l][k] = data[i+l][j+k]
        boards.append(chess(lst))
print(min(boards))

import sys
data = list(map(int, sys.stdin.readline().split()))
res = ''
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        if res == 'descending':
            res = 'mixed'
            break
        res = 'ascending'
    elif data[i] < data[i-1]:
        if res == 'ascending':
            res = 'mixed'
            break
        res = 'descending'
print(res)
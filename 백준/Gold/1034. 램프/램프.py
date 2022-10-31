import sys

N, M = map(int, sys.stdin.readline().split())

data = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
K = int(sys.stdin.readline())
result = []
resset = []
for i in range(N):
    line = data[i]
    # if line in resset:
    #     continue
    zerocount = line.count(0)
    if zerocount > K or zerocount % 2 != K % 2:
        continue
    else:
        resset.append(line)
        cnt = 0
        for j in range(N):
            if data[j] == line:
                cnt += 1
        result.append(cnt)
if result:
    print(max(result))
else:
    print(0)
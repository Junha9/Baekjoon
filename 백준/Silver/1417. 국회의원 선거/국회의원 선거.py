import sys
N = int(sys.stdin.readline())
votes = [int(sys.stdin.readline()) for _ in range(N)]
i = 0
while True:
    if len(votes) == 1:
        break
    maxx = max(votes[1:])
    ind = votes[1:].index(max(votes[1:])) + 1
    if votes[0] > maxx:
        break
    votes[0] += 1
    votes[ind] -= 1
    i += 1
print(i)
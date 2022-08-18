import sys

T = int(sys.stdin.readline())
for test in range(1, T+1):
    line = list(sys.stdin.readline().rstrip())
    score, temp = 0, 0
    for i, l in enumerate(line):
        if l == 'O':
            temp += 1
        elif l == 'X':
            temp = 0
        score += temp
    print(score)
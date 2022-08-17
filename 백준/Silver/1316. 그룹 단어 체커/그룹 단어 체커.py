import sys
T = int(sys.stdin.readline())
cnt = 0
for test in range(1, T+1):
    word = sys.stdin.readline()
    lst = []
    for i, letter in enumerate(word):
        # lst.append(letter)
        if letter in lst and word[i-1] != letter:
            break
        lst.append(letter)
    else:
        cnt += 1
print(cnt)


import sys
T = int(sys.stdin.readline())
for i in range(T):
    data = sys.stdin.readline().rstrip('\n')
    stack = []
    res = 'YES'
    for letter in data:
        if letter == '(':
            stack.append(letter)
        elif letter == ')':
            if not stack:
                res = 'NO'
            elif stack[-1] == '(':
                stack.pop()
            else:
                res = 'NO'
        else:
            res = 'NO'
    if stack:
        res = 'NO'

    print(res)
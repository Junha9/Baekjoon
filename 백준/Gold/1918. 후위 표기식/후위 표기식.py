import sys

stack = []
res = []
operators = ['*' , '+', '-' , '/']
weight = {
    '*' : 1,
    '/' : 1,
    '+' : 0,
    '-' : 0,
    '(' : -1,
    ')' : 0,
}
equation = sys.stdin.readline().rstrip()
for elem in equation:
    if elem in operators:
        while stack and weight[elem] <= weight[stack[-1]]:
                res.append(stack.pop())
        stack.append(elem)
    elif elem == '(':
        stack.append(elem)
    elif elem == ')':
        while stack[-1] != '(':
            res.append(stack.pop())
        stack.pop()
        pass
    else:
        res.append(elem)
while stack:
    res.append(stack.pop())
print(''.join(res))
import sys
stack = []
N = int(sys.stdin.readline())
for line in range(N):
    command = sys.stdin.readline().rstrip()
    if command == 'pop':
        print(stack.pop()) if stack else print(-1)
    elif command == 'top':
        print(stack[-1]) if stack else print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        res = 0 if stack else 1
        print(res)
    else:
        stack.append(int(command.split()[1]))
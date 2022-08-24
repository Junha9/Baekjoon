import sys

que = []
N = int(sys.stdin.readline())
for line in range(N):
    command = sys.stdin.readline().rstrip()
    if command == 'pop':
        print(que.pop(0)) if que else print(-1)
    elif command == 'size':
        print(len(que))
    elif command == 'empty':
        print(1) if not que else print(0)
    elif command == 'front':
        print(que[0]) if que else print(-1)
    elif command == 'back':
        print(que[-1]) if que else print(-1)
    else:
        que.append(int(command.split()[1]))

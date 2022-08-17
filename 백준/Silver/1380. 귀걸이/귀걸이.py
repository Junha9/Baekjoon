import sys
t = 0
while True:
    t += 1
    n = int(sys.stdin.readline())
    if n == 0:
        break
    names = [sys.stdin.readline().rstrip() for _ in range(n)]
    dic = dict(zip(range(1, n+1), [[] for _ in range(n)]))
    for _ in range(2 * n - 1):
        student, c = sys.stdin.readline().rstrip().split()
        i = int(student)
        dic[i].append(c)
    a = dict(filter(lambda x: len(x[1]) == 1, dic.items()))
    index = list(a.keys())[0]
    print(f'{t} {names[index-1]}')
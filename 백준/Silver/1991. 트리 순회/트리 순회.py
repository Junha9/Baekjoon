import sys

def front(k):
    if k == '.':
        return
    frontres.append(k)
    front(nodes[k][0])
    front(nodes[k][1])
    return

def middle(k):
    if k == '.':
        return
    middle(nodes[k][0])
    middleres.append(k)
    middle(nodes[k][1])

def back(k):
    if k == '.':
        return
    back(nodes[k][0])
    back(nodes[k][1])
    backres.append(k)


N = int(sys.stdin.readline())
nodes = dict()
frontres = []
middleres = []
backres = []
for _ in range(N):
    info = sys.stdin.readline().split()
    nodes[info[0]] = info[1:]
# print(data)

front('A')
middle('A')
back('A')
print(''.join(frontres))
print(''.join(middleres))
print(''.join(backres))
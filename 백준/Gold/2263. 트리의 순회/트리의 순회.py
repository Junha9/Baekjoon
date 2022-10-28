import sys
sys.setrecursionlimit(10 ** 7)

def divide(a,b,c,d):
    if a > b or c > d:
        return
    root = postorder[d]
    print(root, end=' ')
    j = indexlist[root]
    l = j-a
    r = b-j
    divide(a, a+l-1, c, c+l-1)
    divide(b-r+1, b, d-r, d-1)


n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
indexlist = [0] * (n+1)
for i in range(n):
    indexlist[inorder[i]] = i
res = []
divide(0,n-1,0,n-1)
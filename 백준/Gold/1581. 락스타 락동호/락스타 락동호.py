import sys

FF, FS, SF, SS = map(int, sys.stdin.readline().split())
# 0 => Fast end, 1 => slow end
res = 0
if FF == FS == 0:
    res = SS+(min(SF,1))
elif FS == 0:
    res = FF
else:
    res = FF + SS + min(SF,FS) * 2
    if SF < FS:
        res += 1

print(res)

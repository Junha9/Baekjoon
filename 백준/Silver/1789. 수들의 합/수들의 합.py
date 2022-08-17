import sys
s = int(sys.stdin.readline())
su, i = 0, 0
while su <= s:
    i += 1
    su += i
print(i-1)

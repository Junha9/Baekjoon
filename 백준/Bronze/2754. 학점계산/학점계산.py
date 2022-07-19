s = input()
if 'A' in s:
    t = 4
if 'B' in s:
    t = 3
if 'C' in s:
    t = 2
if 'D' in s:
    t = 1
if 'F' in s:
    t = 0
if '+' in s:
    t += 0.3
if '-' in s:
    t -= 0.3
print(float(t))
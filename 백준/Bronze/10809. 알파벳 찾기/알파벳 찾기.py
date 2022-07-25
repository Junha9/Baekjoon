a = input()
out = ' '
for i in range(97, 123):
    out += str(a.find(chr(i))) + ' '
print(out.strip())
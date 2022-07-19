n = input()
letter = ''
for i in n:
    if i.isupper():
        letter += i.lower()
    else:
        letter += i.upper()
print(letter)
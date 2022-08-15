p, w = map(int, input().split())
s = input()
t = 0
def typing(l):
    global t
    if l == 'A' or l == 'D' or l == 'G' or l == 'J' or l == 'M' or l == 'P' or l == 'T' or l == 'W':
        t += p
    elif l == 'B' or l == 'E' or l == 'H' or l == 'K' or l == 'N' or l == 'Q' or l == 'U' or l == 'X':
        t += 2 * p
    elif l == ' ':
        t += p
    elif l == 'S' or l == 'Z':
        t += 4 * p
    else:
        t += 3 * p

def find(l):
    for i, g in enumerate(lst):
        if l in g:
            return i

lst = [['A', 'B' , 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z'], [0, ' ']]

temp = -1
for l in s:
    if l in lst[temp] and l != ' ':
        t += w
    typing(l)
    temp = find(l)
print(t)
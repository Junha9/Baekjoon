import sys

length = int(sys.stdin.readline())
lst = [64]
if sum(lst) > length:
    i = 0
    while True:
        ind = lst.index(min(lst))
        stick = lst[ind]
        del lst[ind]
        lst.append(stick/2)
        if sum(lst) < length:
            lst.append(stick/2)
        if sum(lst) == length:
            break
print(len(lst))
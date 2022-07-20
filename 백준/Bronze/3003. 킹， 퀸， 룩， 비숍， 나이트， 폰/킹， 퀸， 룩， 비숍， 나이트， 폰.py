lst = list(map(int, input().strip().split()))
lst_need = [1-lst[0], 1-lst[1], 2-lst[2], 2-lst[3], 2-lst[4], 8-lst[5]]
a = ' '.join(list(map(str, lst_need)))
print(a)
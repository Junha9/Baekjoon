import sys
N = int(sys.stdin.readline())
lst = list(range(1, N+1))
j = 0
def func(lst):
    global j
    if len(lst) == 1:
        return lst[0]
    elif len(lst) % 2 == 0:
        new = []
        for i in range(len(lst)):
            if i % 2 == 1:
                new.append(lst[i])
        return func(new)
    else:
        new = []
        for i in range(len(lst)):
                if i % 2 == 1:
                    new.append(lst[i])
        new.append(new.pop(0))
        return func(new)
        # if j % 2 == 0:
        #     for i in range(len(lst)):
        #         if i % 2 == 1:
        #             new.append(lst[i])
        #     j += 1
        #     return func(new)
        # else:
        #     for i in range(len(lst)):
        #         if i % 2 == 1:
        #             new.append(lst[i])
        #     new.append(new.pop(0))
        #     return func(new)
print(func(lst))
x = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]


def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(0)
    return lst


print(move_zeros(x))

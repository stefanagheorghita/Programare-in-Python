def find_tuple(ls):
    unique = set(ls)
    a = len(unique)
    b = len(ls) - a
    return a, b


def find_tuple2(ls):
    unique = set()
    duplicate = set()
    for el in ls:
        count = ls.count(el)
        if count == 1:
            unique.add(el)
        else:
            duplicate.add(el)
    return len(unique), len(duplicate)


list = [1, 2, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7]
print(find_tuple(list))
print(find_tuple2(list))

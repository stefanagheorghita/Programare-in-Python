def find_tuple(ls):
    unique = set(ls)
    a = len(unique)
    b = len(ls) - a
    return a, b


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 2, 2]
print(find_tuple(list))


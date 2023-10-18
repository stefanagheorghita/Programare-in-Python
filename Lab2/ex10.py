def tuples(*lis):
    max_length = max(len(ls) for ls in lis)
    res = []
    for i in range(max_length):
        pair = tuple(ls[i] if i < len(ls) else None for ls in lis)
        res.append(pair)
    return res


l1 = [1, 2, 3]
l2 = [5, 6, 7]
l3 = ["a", "b"]
print(tuples(l1, l2, l3))

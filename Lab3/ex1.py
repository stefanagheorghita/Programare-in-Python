def calculate(a, b):
    union = set(a) | set(b)
    intersect = set(a) & set(b)
    a_b = set(a) - set(b)
    b_a = set(b) - set(a)
    final = [union, intersect, a_b, b_a]
    return final


a = [1, 2, 3, 4, 5, 6]
b = [2, 3, 23, 5, 46]
result = calculate(a, b)
print("Union: " + str(result[0]) + "\nIntersection: " + str(result[1]) + "\nA/B: " + str(result[2]) + "\nB/A: " + str(
    result[3]))

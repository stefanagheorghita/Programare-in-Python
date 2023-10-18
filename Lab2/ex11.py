def keys(e):
    return e[1]


def sort(lis):
    list_to_ord = [0] * len(lis)
    pos = 0
    new_list = []
    for tup in lis:
        if len(tup) < 2:
            list_to_ord[pos] = ord('a') - 1
        else:
            if len(tup[1]) < 3:
                list_to_ord[pos] = ord('a') - 1
            else:
                list_to_ord[pos] = ord(tup[1][2])
        new_list.append((tup, list_to_ord[pos]))
        pos = pos + 1
    # for i in range(len(new_list) - 1):
    #     for j in range(i + 1, len(new_list)):
    #         if new_list[i][1] > new_list[j][1]:
    #             aux = new_list[i]
    #             new_list[i] = new_list[j]
    #             new_list[j] = aux
    new_list.sort(key=keys)
    final_list = []
    for tup in new_list:
        final_list.append(tup[0])
    return final_list


input_list = [('abc', 'bcd'), ('abc', 'zza'), ('add', 'bbb')]
print(sort(input_list))

def filtering(x=1, strings=[], flag=True):
    lis = []
    for string in strings:
        chars = []
        for char in string:
            if flag:
                if ord(char) % x == 0:
                    chars.append(char)
            else:
                if ord(char) % x != 0:
                    chars.append(char)
        lis.append(chars)
    return lis


x = 2
strings = ["test", "hello", "lab002"]
flag = False

res = filtering(x, strings, flag)
print(res)

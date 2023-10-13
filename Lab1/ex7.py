def find(string):
    number_as_string = ""
    found = 0
    for ch in string:
        if ch.isdigit():
            number_as_string = number_as_string + ch;
            found = 1
        else:
            if found == 1:
                break
    return int(number_as_string)


print(find("abcd123avd"))
print(find("abcd 112 a745 avd23455ddff"))

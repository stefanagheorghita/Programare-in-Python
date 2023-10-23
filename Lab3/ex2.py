def count_characters(str):
    char_count = {}
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


string = "Ana has apples."
result = count_characters(string)
print(result)

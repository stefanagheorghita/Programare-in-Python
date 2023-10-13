def count_letters(string):
    numbers = [0] * 26
    for ch in string:
        if ch.isalpha():
            numbers[ord(ch.lower()) - ord('a')] = numbers[ord(ch.lower()) - ord('a')] + 1
    max = 0
    pos = 0
    for i in range(26):
        if numbers[i] > max:
            max = numbers[i]
            pos = i
    print(chr(pos + ord('a')) + " with " + str(max) + " occurrences")


count_letters("an apple is not a tomato")

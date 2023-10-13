def count_bits(number):
    count = 0
    while number:
        count = count + number % 2;
        number = int(number / 2)
    return count


print(count_bits(24))

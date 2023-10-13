# print("Hello World!")

def gcd(a, b):
    while a != b:
        if b > a:
            b = b - a
        else:
            a = a - b
    return a


value = input("Choose a number or press any letter to exit: ")
n = 0
numbers = [0]
while 1:
    try:
        num = int(value)
        numbers.append(0)
        numbers[n] = num
        n = n + 1
        value = input("Choose a number or press any letter to exit: ")
    except ValueError:
        if not isinstance(value, int):
            print("A character value was introduced.")
            break
    # else:

if len(numbers) < 2:
    print("You introduced to few numbers.")
else:
    res = numbers[0]
    for numb in numbers[1:len(numbers) - 1]:
        res = gcd(res, numb)
    print("The greatest common divisor is: " + str(res))

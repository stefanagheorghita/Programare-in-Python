def my_function(*args, **kwargs):
    number = 0
    for arg in args:
        if arg in kwargs.values():
            number += 1
    return number


print(my_function(1, 2, 3, 4, 5, a=1, b=2, c=3, d=5))

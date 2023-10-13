def palindrome(number):
    reverse = int(str(number)[::-1])
    if reverse == number:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")


palindrome(1222332221)
palindrome(12223322214)

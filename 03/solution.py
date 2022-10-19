import math

def is_palindrome(string):
    for index in range(math.floor(len(string) / 2)):
        if string[index] != string[len(string) - 1 - index]:
            return False

    return True


print(is_palindrome("amanaplanacanalpanama"))
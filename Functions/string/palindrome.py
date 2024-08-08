def is_palindrome(string):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return "Not Palindrome"
    return "Palindrome"

string = input()
print(is_palindrome(string))
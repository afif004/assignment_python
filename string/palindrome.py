str = input()

is_palindrome = True
length = len(str)

for i in range(length // 2):
    if str[i] != str[length - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")
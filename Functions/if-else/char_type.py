def char_type(C):
    if C.isdigit():
        return "Digit"
    elif C == ' ':
        return "Space"
    elif C.isalpha():
        return "Alphabet"
    else:
        return "Punctuation"

C = input()
print(char_type(C))
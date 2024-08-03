def char_type_vowel(C):
    vowel = "AEIOUaeiou"
    if C.isdigit():
        return "Digit"
    elif C.isalpha():
        if C in vowel:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Other"

C = input()
print(char_type_vowel(C))

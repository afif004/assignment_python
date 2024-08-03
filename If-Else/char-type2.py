C = input()
vowel = ['A','E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
if C>='0' and C<='9':
    print("Digit")
elif ((C>='A' and C<='Z') or (C>='a' and C<='z')):
    if C in vowel:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Other")
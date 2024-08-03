str = input()

vowel = 0
consonant = 0
digit = 0
other = 0
vowels = "aeiouAEIOU"
digits = "0123456789"

for char in str:
    if char in vowels:
        vowel += 1
    elif char.isalpha():
        consonant += 1
    elif char in digits:
        digit += 1
    else:
        other += 1

print("Vowels:", vowel)
print("Consonants:", consonant)
print("Digits:", digit)
print("Others:", other)
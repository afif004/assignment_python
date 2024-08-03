C = input()
if C>='0' and C<='9':
    print("Digit")
elif C==' ':
    print("Space")
elif ((C>='A' and C<='Z') or (C>='a' and C<='z')):
    print("Albhabet")
else:
    print("Punctuation")
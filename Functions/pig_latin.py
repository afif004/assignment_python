def pig_latin(string):
    return string[1:] + string[0] + 'a'
string = input()
print(pig_latin(string))
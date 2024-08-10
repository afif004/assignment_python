filename = 'file_handling\\example.txt'

with open(filename, 'r') as file:
    text = file.read()
    words = text.split()
    c = len(words)
print(c)
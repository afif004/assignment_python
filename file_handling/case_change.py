filename = "file_handling\\example.txt"

with open(filename, 'r') as file:
    text = file.read()
with open (filename, 'w') as file:
    file.write(text.lower())
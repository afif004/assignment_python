file_name = "file_handling\\example.txt"
with open(file_name, 'rt') as file:
    content = file.read()
    print(content)
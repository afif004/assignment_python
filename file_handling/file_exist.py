import os

path = 'file_handling/example.txt'

if os.path.exists(path):
    print(f"The file or directory '{path}' exists.")
else:
    print(f"The file or directory '{path}' does not exist.")
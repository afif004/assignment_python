filename = 'file_handling\\file1.txt'
search_word = input("Enter the word to find: ")

with open(filename, 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        words = line.split()
        if search_word in words:
            print(f"The word '{search_word}' was found in line {i + 1}")

filename = 'file_handling\\example.txt'
search_word = input("Enter the word to count: ")

with open(filename, 'r') as file:
    text = file.read()
    words = text.split()
    c = words.count(search_word)
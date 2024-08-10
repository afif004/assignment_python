filename = 'file_handling\\file1.txt'
search_word = input("Enter the word to find: ")
replacing_word = input("Enter the word to be replaced with: ")

with open(filename, 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        words = line.split()
        word_len = len(words)
        for j in range(word_len):
            if words[j]==search_word:
                words[j] = replacing_word
        lines[i] = ' '.join(words) + '\n'
with open(filename, 'w') as file:
    file.writelines(lines)
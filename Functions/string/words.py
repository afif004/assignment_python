def word(string):
    words = string.split()
    word_count = len(words)
    return word_count
sentence = input()
print(word(sentence))
def rev(string):
    words = sentence.split()
    reverse = ' '.join(word[::-1] for word in words)
    return reverse

sentence = input()
print(rev(sentence))
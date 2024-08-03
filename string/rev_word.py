sentence = input()

words = sentence.split()
reversed_sentence = ' '.join(word[::-1] for word in words)

print(reversed_sentence)
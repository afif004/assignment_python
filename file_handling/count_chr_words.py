file_name = "file_handling\example.txt"
with open (file_name, "rt") as f:
    text = f.read()
    char_count = len(text)
    words = text.split()
    word_count = len(words)
    line_count = text.count('\n') + 1
print(f"Characters: {char_count}")
print(f"Words: {word_count}")
print(f"Lines: {line_count}")
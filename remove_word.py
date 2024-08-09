file_name = "file_handling\\example.txt"
word_to_remove = input("Word to remove: ")
with open (file_name, "rt") as f:
    lines = f.readlines()
with open (file_name, "w") as f:
    for line in lines:
        modified_line = line.replace(word_to_remove, "")
        f.write(modified_line)
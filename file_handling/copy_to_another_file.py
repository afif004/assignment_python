main_file = "file_handling\\main_file.txt"
copy_file = "file_handling\\copy_file.txt"
with  open (main_file, "rt") as f:
    contents = f.read().strip()
with open(copy_file, "w") as f:
    f.write(contents)
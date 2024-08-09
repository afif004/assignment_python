file1 = "file_handling\\file1.txt"
file2 = "file_handling\\file2.txt"
merge_file = "file_handling\\merge_file.txt"
with  open (file1, "rt") as f:
    contents1 = f.read().strip()
with  open (file2, "rt") as f:
    contents2 = f.read().strip()

with  open (merge_file, "w") as f:
    f.write(contents1 + "\n" + contents2)
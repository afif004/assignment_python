file_name = "file_handling\\file1.txt"
line_num = int(input("Line to remove: "))

with open (file_name, "rt") as f:
    lines = f.readlines()
with open (file_name, "w") as f:
    for i, line in enumerate(lines):
        if i != line_num-1:
             f.write(line)
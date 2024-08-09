file1 = "file_handling\\file1.txt"
file2 = "file_handling\\file2.txt"

with open(file1, "rt") as f1:
    lines1 = f1.readlines()
with open(file2, "rt") as f2:
    lines2 = f2.readlines()
    
max_len = max(len(lines1), len(lines2))
for i in range(max_len):
    f1line = lines1[i].strip() if i < len(lines1) else "No Line"
    f2line = lines2[i].strip() if i < len(lines2) else "No Line"

    if f1line == f2line:
        print(f"Line {i+1}: IDENTICAL")
    else:
        print(f"Line {i+1}: DIFFERENT")
        print(f"File 1: {f1line}")
        print(f"File 2: {f2line}")
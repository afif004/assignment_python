filename = 'file_handling\\file1.txt'
n = int(input("Enter the line number to find: "))
replacing_line = input("Enter the line to be replaced with: ")

with open(filename, 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if i==n-1:
            lines[i] = replacing_line + '\n'
with open(filename, "w") as file:
    file.writelines(lines)
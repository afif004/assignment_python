filename = 'line_extra.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    non_empty_lines = [line for line in lines if line.strip()]

with open(filename, 'w') as file:
    file.writelines(non_empty_lines)
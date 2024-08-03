rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

A = [[0 for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        A[i][j] = int(input(f"A[{i}][{j}]: "))

zero_count = 0
non_zero_count = 0

for i in range(rows):
    for j in range(cols):
        if A[i][j] == 0:
            zero_count += 1
        else:
            non_zero_count += 1

if zero_count > non_zero_count:
    print("The matrix is sparse.")
else:
    print("The matrix is not sparse.")

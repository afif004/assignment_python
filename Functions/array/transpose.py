def transpose(matrices,row,col):
    transpose = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            transpose[j][i] = A[i][j]
    return transpose
row = int(input("Row: "))
col = int(input("Column: "))
A = [[0 for _ in range(col)] for _ in range(row)]
for i in range(row):
    for j in range(col):
        A[i][j] = int(input(f"A[{i}][{j}]: "))
T = transpose(A,row,col)
print("Transpose of the matrix:")
for row in T:
    print(row)
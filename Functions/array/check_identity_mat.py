def input_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(int(input(f"A[{i}][{j}]: ")))
        matrix.append(row)
    return matrix

def is_identity_matrix(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if (i == j and matrix[i][j] != 1) or (i != j and matrix[i][j] != 0):
                return 0
    return 1

size = int(input("Size of matrix: "))
A = input_matrix(size)
if is_identity_matrix(A):
    print("Identity Matrix")  
else:
    print("Not Identity Matrix")
def read_matrix(size, name):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(int(input(f"{name}[{i}][{j}]: ")))
        matrix.append(row)
    return matrix

def multiply_matrices(A, B, size):
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = 0
            for k in range(size):
                C[i][j] += A[i][k] * B[k][j]
    return C

size = int(input("Size of matrix: "))
A = read_matrix(size, 'A')
B = read_matrix(size, 'B')
C = multiply_matrices(A, B, size)
print("Matrix:")
for row in C:
    print(row)
size = int(input("Size of matrix: "))
A = [[0 for _ in range(size)] for _ in range(size)]
for i in range(size):
    for j in range(size):
        A[i][j] = int(input(f"A[{i}][{j}]: "))
B = [[0 for _ in range(size)] for _ in range(size)]
for i in range(size):
    for j in range(size):
        B[i][j] = int(input(f"B[{i}][{j}]: "))
C = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):
    for j in range(size):
        C[i][j] = A[i][j] - B[i][j]

print("Matrix C:")
for row in C:
    print(row)
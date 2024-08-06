def is_symmetric(matrices, size):
    for i in range(size):
        for j in range(size):
            if A[i][j] != A[j][i]:
                return 0
    return 1
size = int(input("Size of matrix: "))
A = [[0 for _ in range(size)] for _ in range(size)]
for i in range(size):
    for j in range(size):
        A[i][j] = int(input(f"A[{i}][{j}]: "))

if is_symmetric(A,size):
    print("Symmetric")
else:
    print("Not Symmetric")
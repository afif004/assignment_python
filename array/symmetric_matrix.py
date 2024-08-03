size = int(input("Size of matrix: "))
flag = int(1)
A = [[0 for _ in range(size)] for _ in range(size)]
for i in range(size):
    for j in range(size):
        A[i][j] = int(input(f"A[{i}][{j}]: "))

symmetric = True

for i in range(size):
    for j in range(size):
        if A[i][j] != A[j][i]:
            symmetric = False
            break
    if not symmetric:
        break

if symmetric:
    print("Symmetric")
else:
    print("Not Symmetric")
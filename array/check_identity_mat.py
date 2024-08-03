size = int(input("Size of matrix: "))
flag = int(1)
A = [[0 for _ in range(size)] for _ in range(size)]
for i in range(size):
    for j in range(size):
        A[i][j] = int(input(f"A[{i}][{j}]: "))
        if (i == j and A[i][j] != 1) or (i != j and A[i][j] != 0):
            flag = 0
if flag:
    print("Identity Matrix")  
else:
    print("Not Identity Matrix")
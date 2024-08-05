def check_sparse(A, r, c):
    zero_count = 0
    for i in range(r):
        for j in range(c):
            if A[i][j] == 0:
                zero_count +=1
    if zero_count <= ( (r*c)//2):
        return "The matrix is not sparse."
    else:
       return "The matrix is sparse."
       
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
A = [[0 for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        A[i][j] = int(input(f"A[{i}][{j}]: "))
print(check_sparse(A,rows,cols))
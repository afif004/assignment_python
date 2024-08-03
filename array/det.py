import numpy as np 
size = int(input("Size of matrix: "))
A = np.array([[0 for _ in range(size)] for _ in range(size)])
for i in range(size):
    for j in range(size):
        A[i][j] = int(input(f"A[{i+1}][{j+1}]: "))

print("Numpy Matrix is:") 
print(A) 

det = np.linalg.det(A) 

print("\nDeterminant: ") 
print(int(det)) 
class MatrixOperations:
    def getCofactor(self, matrix, temp, p, q, n):
        i, j = 0, 0
        for row in range(n):
            for col in range(n):
                if row != p and col != q:
                    temp[i][j] = matrix[row][col]
                    j += 1
                    if j == n - 1:
                        j = 0
                        i += 1
    
    def determinant(self, matrix, n):
        d = 0
        if n == 1:
            return matrix[0][0]
        
        temp = [[0 for _ in range(n)] for _ in range(n)]
        sign = 1
        
        for i in range(n):
            self.getCofactor(matrix, temp, 0, i, n)
            d += sign * matrix[0][i] * self.determinant(temp, n - 1)
            sign = -sign
        
        return d

n = int(input("Size of matrix: "))
A = [[int(input(f"A[{i+1}][{j+1}]: ")) for j in range(n)] for i in range(n)]

matrix_ops = MatrixOperations()
print(f"Determinant: {matrix_ops.determinant(A, n)}")

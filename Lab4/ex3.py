class Matrix:

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.matrix = [[0 for x in range(M)] for y in range(N)]

    def set(self, row, col, value):
        self.matrix[row][col] = value

    def get(self, row, col):
        return self.matrix[row][col]

    def transpose(self):
        new_matrix = Matrix(self.M, self.N)
        for i in range(self.N):
            for j in range(self.M):
                new_matrix.set(j, i, self.matrix[i][j])
        # self.N = new_matrix.N
        # self.M = new_matrix.M
        # self.matrix = new_matrix.matrix
        return new_matrix

    def mul(self, other):
        if self.M != other.N:
            return None
        product = Matrix(self.N, other.M)
        for i in range(self.N):
            for j in range(other.M):
                for k in range(self.M):
                    product.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return product

    def transform(self, func):
        for i in range(self.N):
            for j in range(self.M):
                self.matrix[i][j] = func(self.matrix[i][j])
        return self

    def __str__(self):
        print("Matrix:")
        for i in range(self.N):
            for j in range(self.M):
                print(self.matrix[i][j], end=" ")
            print()
        return ""


matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 2)
matrix.set(1, 2, 1)
print(matrix)
print("Element 0 0:", matrix.get(0, 0))
print("Element 1 2:", matrix.get(1, 2))
matrix2 = matrix.transpose()
print(matrix2)
multiplied = matrix.mul(matrix2)
print(multiplied)
modified = matrix.transform(lambda x: x * 2)
print(modified)
modified2 = matrix.transform(lambda x: x * x)
print(modified2)

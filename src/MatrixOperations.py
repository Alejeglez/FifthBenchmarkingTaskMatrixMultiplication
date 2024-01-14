class MatrixOperations:
    def multiply_matrices(self, matrix_a, matrix_b):
        matrix_result = []

        for i in range(len(matrix_a)):
            matrix_result.append([])
            for j in range(len(matrix_b)):
                matrix_result[i].append(0)
                for k in range(len(matrix_a)):
                    matrix_result[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return matrix_result
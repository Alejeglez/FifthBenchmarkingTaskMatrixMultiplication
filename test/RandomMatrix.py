import random
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.MatrixSerializer import MatrixSerializer
class RandomMatrix:


    def generate_random_matrix(self, size, id, serialize = False):
        matrix = []
        for i in range(size):
            matrix.append([])
            for j in range(size):
                matrix[i].append(random.randint(0, 10))
        if serialize:
            matrix_serializer = MatrixSerializer()
            matrix_serializer.serialize(matrix, id, size)
        else:
            return matrix
    
    def generate_two_random_matrices(self, size: int):
        self.generate_random_matrix(size, "A", True)
        self.generate_random_matrix(size, "B", True)

if __name__ == "__main__":
    random_matrix = RandomMatrix()
    sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512]
    for size in sizes:
        random_matrix.generate_two_random_matrices(size)
    
import subprocess
import sys
import os
from glob import glob  # Add this line
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MatrixSerializer import MatrixSerializer
from CoordinateMatrix import CoordinateMatrix
from MatrixBuilder import CoordinateMatrixBuilder
from src.MatrixOperations import MatrixOperations
import random

resource_files = glob(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources', 'matrix_*.txt')))


MatrixSerializer = MatrixSerializer()
MatrixOperations = MatrixOperations()
for resource_file in resource_files:
    #identificar  el numero tras _ y antes de .txt
    size = int(resource_file.split('_')[1].split('.')[0])
    if size == 2:
        matrix_a, matrix_b = MatrixSerializer.deserialize(resource_file, size)
        print(f"Matriz A:")
        MatrixOperations.print_matrix(matrix_a)
        print(f"Matriz B:")
        MatrixOperations.print_matrix(matrix_b)
        initial_time = time.time()
        matrix_c = MatrixOperations.multiply_matrices(matrix_a, matrix_b)
        end_time = time.time()
        elapsed_time = end_time - initial_time
        print(f"Tiempo de ejecución: {elapsed_time} segundos para el archivo {resource_file}")        







import pytest
import sys
import os
from glob import glob

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.MatrixOperations import MatrixOperations
from src.MatrixSerializer import MatrixSerializer

resource_files = glob(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources', 'matrix_*.txt')))
MatrixSerializer = MatrixSerializer()
MatrixOperations = MatrixOperations()


def matrix_multiplication(matrix_a, matrix_b):
    MatrixOperations.multiply_matrices(matrix_a, matrix_b)

def deserialize_matrix(resource_file):
    size = int(resource_file.split('_')[1].split('.')[0])
    matrix_a, matrix_b = MatrixSerializer.deserialize(resource_file, size)
    return matrix_a, matrix_b
    
@pytest.mark.benchmark(group="throughput", warmup=True, warmup_iterations=5, max_time=1)
@pytest.mark.parametrize("matrix_a, matrix_b", [(deserialize_matrix(resource_file)[0], deserialize_matrix(resource_file)[1])  for resource_file in resource_files])
def test_matrix_multiplication_with_setup(benchmark, matrix_a, matrix_b):
    benchmark.pedantic(matrix_multiplication, args=(matrix_a, matrix_b), iterations=5, rounds=4)
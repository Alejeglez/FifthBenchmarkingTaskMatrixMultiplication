import sys
import os
from glob import glob
import time
import subprocess

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.MatrixOperations import MatrixOperations
from src.MatrixSerializer import MatrixSerializer
def run_map_reduce(input_file):
    command = ["python", "src/MapReduce.py", input_file, "--output", "output/{input_file}"]
    with open(os.devnull, "w") as null_file:
        subprocess.run(command, shell=True, stdout=null_file, stderr=null_file)

resource_files = glob(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources', 'matrix_*.txt')))

times_map_reduce = {}
for resource_file in resource_files:
    size = int(resource_file.split('_')[1].split('.')[0])
    initial_time  = time.time()
    run_map_reduce(resource_file)
    final_time = time.time()
    print("Time for size " + str(size) + " is " + str(final_time - initial_time) + " using MapReduce")

times_dense = {}
MatrixSerializer = MatrixSerializer()
MatrixOperations = MatrixOperations()
for resource_file in resource_files:
    size = int(resource_file.split('_')[1].split('.')[0])
    matrix_a, matrix_b = MatrixSerializer.deserialize(resource_file, size)
    initial_time  = time.time()
    matrix_result = MatrixOperations.multiply_matrices(matrix_a, matrix_b)
    final_time = time.time()
    print("Time for size " + str(size) + " is " + str(final_time - initial_time) + " using Dense")


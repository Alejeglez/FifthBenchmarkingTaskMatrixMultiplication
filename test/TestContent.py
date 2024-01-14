import unittest
import sys
import os
from glob import glob
import time
import subprocess

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.MatrixOperations import MatrixOperations
from src.MatrixSerializer import MatrixSerializer

def run_map_reduce(input_file, size):
    command = ["python", "src/MapReduce.py", input_file, "--output","output/{}".format(size)]
    with open(os.devnull, "w") as null_file:
        subprocess.run(command, shell=True, stdout=null_file, stderr=null_file)

resource_files = glob(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources', 'matrix_*.txt')))

MatrixSerializer = MatrixSerializer()
MatrixOperations = MatrixOperations()

if os.path.exists("output"):
    for filename in os.listdir("output"):
        os.remove(os.path.join("output", filename))

for resource_file in resource_files:
    
    size = int(resource_file.split('_')[1].split('.')[0])
    print("Running test for size {}".format(size))
    run_map_reduce(resource_file, size)
    matrix_a, matrix_b = MatrixSerializer.deserialize(resource_file, size)
    matrix_result = MatrixOperations.multiply_matrices(matrix_a, matrix_b)
    hadoop_output_dir = "output/{}".format(size)

    matrix_result_hadoop = []
    for i in range(size):
        matrix_result_hadoop.append([])
        for j in range(size):
            matrix_result_hadoop[i].append(0)

    for filename in os.listdir(hadoop_output_dir):
        hadoop_result_file = os.path.join(hadoop_output_dir, filename)
    
        if os.path.isfile(hadoop_result_file):
            with open(hadoop_result_file, 'r') as reader:
                for line in reader.readlines():
                    line = line.split()
                    matrix_result_hadoop[int(line[0][1:-1])][int(line[1][:-1])] = int(line[2])

    all_comparisons_pass = all(matrix_result[i][j] == matrix_result_hadoop[i][j] for i in range(size) for j in range(size))

    if all_comparisons_pass:
        print(f"The comparison for size {size} passed successfully")
    else:
        for i in range(size):
            for j in range(size):
                assert matrix_result[i][j] == matrix_result_hadoop[i][j], f"Error in {resource_file} in position {i} {j}"
    


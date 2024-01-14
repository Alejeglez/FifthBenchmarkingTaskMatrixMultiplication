import subprocess
import pytest
import sys
import os
from glob import glob

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def run_map_reduce(input_file):
    command = ["python", "src/MapReduce.py", input_file, "--output", "output/{input_file}"]
    process = subprocess.run(command, shell=True)
    assert process.returncode == 0

resource_files = glob(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources', 'matrix_*.txt')))


@pytest.mark.benchmark(group="throughput", warmup=True, warmup_iterations=5, max_time=1)
@pytest.mark.parametrize("output_file", [(resource_file)  for resource_file in resource_files])
def test_matrix_multiplication_with_setup(benchmark, output_file):
    benchmark.pedantic(run_map_reduce, args=(output_file,), iterations=5, rounds=4)




from src.CoordinateMatrix import CoordinateMatrix
import os

class MatrixSerializer():
    def serialize(self, matrix, id, size):
        resources_path = os.path.join(os.path.dirname(__file__), '..', 'Resources')
        if not os.path.exists(resources_path):
            os.mkdir(resources_path)


        output_file_path = os.path.join(resources_path, f"matrix_{size}.txt")

        if os.path.exists(output_file_path) and id == "A":
            os.remove(output_file_path)
        

        with open(output_file_path, 'a') as writer:
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j] == 0:
                        continue
                    else:
                        line = f"{id} {i} {j} {matrix[i][j]}"
                        writer.write(line + '\n')

    def deserialize(self, path, size):
        matrix_a = []
        matrix_b = []
        for i in range(size):
            matrix_a.append([])
            matrix_b.append([])
            for j in range(size):
                    matrix_a[i].append(0)
                    matrix_b[i].append(0)
        with open(path, 'r') as reader:
            lines = reader.readlines()

            for line in lines:
                line = line.split()
                if line[0] == "A":
                    matrix_a[int(line[1])][int(line[2])] = int(line[3])
                elif line[0] == "B":
                    matrix_b[int(line[1])][int(line[2])] = int(line[3])
        return matrix_a, matrix_b

    

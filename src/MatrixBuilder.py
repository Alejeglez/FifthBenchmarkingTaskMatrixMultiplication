import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.CoordinateMatrix import CoordinateMatrix, Coordinate

class CoordinateMatrixBuilder:
    def __init__(self, size: int, coordinates):
        self.size = size
        self.coordinates = coordinates

    def get_coordinates(self):
        return self.coordinates

    def set(self, i, j, value):
        coordinate = Coordinate(i, j, value)
        # Buscar si ya existe una coordenada con las mismas i y j
        existing_coord = next((c for c in self.coordinates if c.i == coordinate.i and c.j == coordinate.j), None)

        if existing_coord:
            # Si existe, sumar el valor
            existing_coord.value += coordinate.value
        else:
            # Si no existe, añadir la nueva coordenada
            self.coordinates.append(coordinate)

    def set_coordinate(self, coordinate):
        self.coordinates.append(coordinate)

    def get(self):
        return CoordinateMatrix(self.size, self.coordinates)
    
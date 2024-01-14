from typing import List, Optional

class CoordinateMatrix:
    def __init__(self, size, coordinates):
        self._size = size
        self._coordinates = coordinates

    def get_coordinates(self):
        return self._coordinates

    def get_size(self):
        return int(self._size)

    def get(self, i, j):
        return next((c.value() for c in self.get_coordinates() if c.i() == i and c.j() == j), 0)


class Coordinate:
    def __init__(self, i: int, j: int, value):
        self._i = i
        self._j = j
        self._value = value

    def i(self):
        return self._i

    def j(self):
        return self._j

    def value(self):
        return self._value
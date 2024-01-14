from mrjob.job import MRJob
from mrjob.step import MRStep
import os

class MatrixMultiply(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapperRead,
                   reducer=self.reducerProduct),
            MRStep(mapper=self.mapperProduct,
                   reducer=self.reducerSum)]

    def mapperRead(self, _, line):
        elements = line.split(' ')
        if len(elements) == 4:
            key, row, column, value = line.split(' ')
            key = str(key)
            row = int(row)
            column = int(column)
            value = int(value)

            if key == "A":
                yield column,(key,row,value)
            elif key == "B":
                 yield row,(key,column,value)

    def reducerProduct(self, key, values):
        values_list = list(values)

        values_matrix_a = []
        values_matrix_b = []

        for value in values_list:
            if value[0] == "A":
                values_matrix_a.append(value[1:])
            elif value[0] == "B":
                values_matrix_b.append(value[1:])
        
        result = []
        for value_a in values_matrix_a:
            for value_b in values_matrix_b:
                coordinate = (value_a[0], value_b[0])
                product = value_a[1] * value_b[1]
                result.append((coordinate, product))
        for coordinate, value in result:
            yield coordinate, value
        
    def mapperProduct(self, coordinates, products):
        yield coordinates, products

    def reducerSum(self, coordinates, products):
        yield coordinates, sum(products)

if __name__ == '__main__':
    MatrixMultiply.run()
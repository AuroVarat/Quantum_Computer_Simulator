
import numpy as np


class SparseMatrix:
    def __init__(self, dimension: int):
        self.Dimension = dimension
        self.Columns = [ [] for _ in range(dimension) ]

    def __iter__(self):
        for col in range(self.Dimension):
            for column in self.Columns[col]:
                yield (column.Row, col, column.Value)

    def Multiply(self, m):
        assert self.Dimension == m.Dimension, "Incompatible Dimensions"
        p = SparseMatrix(self.Dimension)
        for me in m:
            column = self.Columns[me.Row]
            for ce in column:
                p[ce.Row, me.Col] += ce.Value * me.Value
        return p

    def __getitem__(self, index):
        return self.Columns[index]

    def __setitem__(self, index, value):
        self.Columns[index] = value

import numpy as np
class SparseMatrix:
    def __init__(self, rows, cols,data=None):
        self.rows = rows
        self.cols = cols
       
        self.data = []
        self.indices = []
        self.indptr = [0]

    def add_element(self, i, j, value):
        self.data.append(value)
        self.indices.append(j)
        if i > self.indptr[-1]:
            self.indptr.append(len(self.data))
        elif i < self.indptr[-1]:
            raise ValueError("Row index must be non-decreasing.")
        self.indptr[-1] += 1

    def to_array(self):
        arr = np.zeros((self.rows, self.cols))
        for i in range(self.rows):
            for j in range(self.indptr[i], self.indptr[i+1]):
                arr[i, self.indices[j]] = self.data[j]
        return arr

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication.")

        result = SparseMatrix(self.rows, other.cols)

        for i in range(self.rows):
            row_data = {}
            for j in range(self.indptr[i], self.indptr[i+1]):
                k = self.indices[j]
                row_data[k] = self.data[j]

            for j in range(other.indptr[0], other.indptr[-1]):
                col_data = {}
                for k in range(other.indptr[j], other.indptr[j+1]):
                    col_data[other.indices[k]] = other.data[k]

                dot_product = sum(row_data.get(k, 0) * col_data.get(k, 0) for k in set(row_data) & set(col_data))
                if dot_product != 0:
                    result.add_element(i, j, dot_product)

        return result
    
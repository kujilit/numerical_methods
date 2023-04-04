import numpy as np
import pylatex


class Solution:
    def __init__(self, dim: int, eps: float):
        self.eps = eps
        self.dim = dim
        self.arr_a = np.add(-np.triu(np.ones((dim, dim), dtype=int), 1), np.identity(dim, dtype=int))

        self.vector_b = -np.ones(dim, dtype=int)
        self.vector_b[dim - 1] = 1

        self.vector_x = np.zeros(dim, dtype=int)
        self.vector_x[dim - 1] = 1

        self.arr_n = np.add(np.triu(-np.ones((dim, dim), dtype=int), 1), np.tri(dim, dtype=int))

        self.solution = np.linalg.tensorsolve(np.add(self.arr_a, eps * self.arr_n), self.vector_b)

    def display(self, doc):
        with doc.create(pylatex.Section(f'Dimension: {self.dim}')):
            with doc.create(pylatex.Section(f'Epsilon:{self.eps}')):
                doc.append(pylatex.Math(data=['(', pylatex.Matrix(self.arr_a), '+', '(', self.eps, ')',
                                              pylatex.Matrix(self.arr_n), ')x =',
                                              pylatex.Matrix(np.array([self.vector_b]).T)
                                              ]))
                doc.append(pylatex.LargeText(data=['Condition number:',
                                                   np.linalg.cond(np.add(self.arr_a, self.eps * self.arr_n))]))


if __name__ == "__main__":
    doc = pylatex.Document()
    Solution(3, 1e-6).display(doc)
    Solution(3, 1e-5).display(doc)
    Solution(3, 1e-4).display(doc)
    Solution(3, 1e-3).display(doc)

    Solution(6, 1e-6).display(doc)
    Solution(6, 1e-5).display(doc)
    Solution(6, 1e-4).display(doc)
    Solution(6, 1e-3).display(doc)
    doc.generate_pdf('solution', clean_tex=False)

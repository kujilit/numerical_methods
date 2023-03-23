import numpy as np
import pylatex
import array_to_latex


class Solution:
    def __init__(self, dim: int, eps: float):
        self.eps = eps
        self.arr_a = np.add(-np.triu(np.ones((dim, dim), dtype=int), 1), np.identity(dim, dtype=int))

        self.vector_b = -np.ones(dim, dtype=int)
        self.vector_b[dim - 1] = 1
        # self.ltx_vector_b = "\begin{bmatrix}" + array_to_latex.to_ltx(self.vector_b) + "\end{bmatrix}"

        self.vector_x = np.zeros(dim, dtype=int)
        self.vector_x[dim - 1] = 1

        self.arr_n = np.add(np.triu(-np.ones((dim, dim), dtype=int), 1), np.tri(dim, dtype=int))

        self.solution = np.linalg.tensorsolve(np.add(self.arr_a, eps * self.arr_n), self.vector_b)

    def display(self):
        # doc = pylatex.Document()
        # with doc.create(pylatex.Section('Lab 1')):
        #     with doc.create(pylatex.Section('Matrix')):
        #         doc.append(pylatex.Math(data=[pylatex.Matrix(self.arr_a), self.eps,
        #                                       pylatex.Matrix(self.arr_n),
        #                                       self.vector_b
        #                                       ]))
        # doc.generate_pdf('full', clean_tex=False)
        # print(f"A = \n{self.arr_a}\n N = \n{self.arr_n}\n b = {self.vector_b}\n x = {self.solution}\n")
        print(f"x = {self.solution}")
        print(f"Число обусловленности: {np.linalg.cond(np.add(self.arr_a, self.eps * self.arr_n))}\n")


if __name__ == "__main__":
    print("Матрица размерности 3")
    Solution(3, 1e-6).display()
    Solution(3, 1e-5).display()
    Solution(3, 1e-4).display()
    Solution(3, 1e-3).display()

    print("Матрица размерности 10")
    Solution(10, 1e-6).display()
    Solution(10, 1e-5).display()
    Solution(10, 1e-4).display()
    Solution(10, 1e-3).display()

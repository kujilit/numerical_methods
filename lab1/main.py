import numpy as np


class Solution:
    def __init__(self, dim: int, eps: float):
        self.arr_a = np.add(-np.triu(np.ones((dim, dim), dtype=int), 1), np.identity(dim, dtype=int))

        self.vector_b = -np.ones(dim, dtype=int)
        self.vector_b[dim - 1] = 1

        self.vector_x = np.zeros(dim, dtype=int)
        self.vector_x[dim - 1] = 1

        self.arr_n = np.add(np.triu(-np.ones((dim, dim), dtype=int), 1), np.tri(dim, dtype=int))

        self.solution = np.linalg.tensorsolve(np.add(self.arr_a, eps * self.arr_n), self.vector_b)

    def display(self):
        print(f"A = \n{self.arr_a}\n N = \n{self.arr_n}\n b = {self.vector_b}\n x = {self.solution}\n")


if __name__ == "__main__":
    Solution(5, 1e-3).display()



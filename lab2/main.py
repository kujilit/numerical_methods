import numpy
import numpy as np


def is_invertible(a: np.array):
    return np.linalg.det(a) != 0 and np.shape(a)[0] == np.shape(a)[1]


class Solution:
    def __init__(self, matrix: np.array):
        self.dim = matrix.shape[0]

        self.l_matrix = np.zeros((self.dim, self.dim))
        self.u_matrix = np.zeros((self.dim, self.dim))
        self.l_matrix += np.identity(self.dim, dtype=int)

        self.sum = 0

        for i in range(self.dim):
            for j in range(self.dim):
                if i <= j:
                    self.sum = 0
                    for k in range(i):
                        self.sum = self.l_matrix[i][k] * self.u_matrix[k][j]
                    self.u_matrix[i][j] = matrix[i][j] - self.sum
                if i > j:
                    self.sum = 0
                    for k in range(j):
                        self.sum = self.l_matrix[i][k] * self.u_matrix[k][j]
                    self.l_matrix[i][j] = (matrix[i][j] - self.sum) / self.u_matrix[j][j]

        print(self.u_matrix)
        print(self.l_matrix)
        print(np.matmul(self.l_matrix, self.u_matrix))


if __name__ == "__main__":
    a1 = np.array([
        [13.14, -2.12, 1.17],
        [-2.12, 6.3, -2.45],
        [1.17, -2.45, 4.6]
    ])

    Solution(a1)

    a2 = np.array([
        [4.31, 0.26, 0.61, 0.27],
        [0.26, 2.32, 0.18, 0.34],
        [0.61, 0.18, 3.20, 0.31],
        [0.27, 0.34, 0.31, 5.17]
    ])


import numpy as np


def is_invertible(a: np.array):
    return np.linalg.det(a) != 0 and np.shape(a)[0] == np.shape(a)[1]


class Solution:
    def __init__(self, matrix: np.array):
        self.dim = matrix.shape[0]

        self.x = np.zeros(self.dim)
        self.y = np.zeros(self.dim)

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

    def display(self):
        print(self.l_matrix)
        print(self.u_matrix)

    def get_system_solution(self, b: np.array):
        self.y = np.linalg.tensorsolve(self.l_matrix, b)
        self.x = np.linalg.tensorsolve(self.u_matrix, self.y)

        print(self.x)


if __name__ == "__main__":
    a1 = np.array([
        [13.14, -2.12, 1.17],
        [-2.12, 6.3, -2.45],
        [1.17, -2.45, 4.6]
    ])

    b1 = np.array([1.27, 2.13, 3.14])

    Solution(a1).display()
    Solution(a1).get_system_solution(b1)

    a2 = np.array([
        [4.31, 0.26, 0.61, 0.27],
        [0.26, 2.32, 0.18, 0.34],
        [0.61, 0.18, 3.20, 0.31],
        [0.27, 0.34, 0.31, 5.17]
    ])

    b2 = np.array([1.02, 1.00, 1.34, 1.27])

    Solution(a2).display()
    Solution(a2).get_system_solution(b2)


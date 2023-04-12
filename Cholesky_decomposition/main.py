import numpy as np


class Solution:
    def __init__(self, matrix: np.array, b: np.array):
        self.dim = np.shape(matrix)[0]
        self.s_matrix = np.zeros((self.dim, self.dim))

        self.s_matrix[0][0] = np.sqrt(matrix[0][0])

        self.sum = 0
        self.y = np.zeros((self.dim))
        self.b = b

        for i in range(self.dim):
            for j in range(i + 1):
                self.sum = 0
                for k in range(j):
                    self.sum += self.s_matrix[i][k] * self.s_matrix[j][k]
                if i == j:
                    self.s_matrix[i][j] = np.sqrt(matrix[i][i] - self.sum)
                else:
                    self.s_matrix[i][j] = (1. / self.s_matrix[j][j] * (matrix[i][j] - self.sum))

    def get_solution(self):
        self.y = np.linalg.tensorsolve(self.s_matrix.T, self.b)
        return np.linalg.tensorsolve(self.s_matrix, self.y)

    def display(self):
        print(self.s_matrix)
        print(np.matmul(self.s_matrix, self.s_matrix.transpose()))


if __name__ == "__main__":
    a = np.array([
        [5.8, 0.3, -0.2],
        [0.3, 4, -0.7],
        [-0.2, -0.7, -6.7]
    ])

    b = np.array([3.1, -1.7, 1.1])

    Solution(a, b).display()

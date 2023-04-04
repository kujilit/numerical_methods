import numpy as np


class Solution:
    def __init__(self, matrix: np.array):
        self.dim = np.shape(matrix)[0]
        self.s_matrix = np.zeros((self.dim, self.dim))

        self.s_matrix[0][0] = np.sqrt(matrix[0][0])

        self.sum = 0

        for i in range(self.dim):
            for j in range(i + 1):
                self.sum = 0
                for k in range(j):
                    self.sum += self.s_matrix[i][k] * self.s_matrix[j][k]
                if i == j:
                    self.s_matrix[i][j] = np.sqrt(matrix[i][i] - self.sum)
                else:
                    self.s_matrix[i][j] = (1. / self.s_matrix[j][j] * (matrix[i][j] - self.sum))

    def display(self):
        print(self.s_matrix)
        print(np.matmul(self.s_matrix, self.s_matrix.transpose()))


if __name__ == "__main__":
    a = np.array([
        [4, 12, -16],
        [12, 37, -43],
        [-16, -43, 98]
    ])

    Solution(a).display()

import numpy as np


class Solution:
    def __init__(self, a: np.array, b: np.array):
        self.dim = a.shape[0]

        self.u = np.zeros(a.shape, dtype=float)

        self.u[0][0] = np.sqrt(a[0][0])

        for i in range(0, self.dim):
            for j in range(i):
                if j > 0:
                    self.u[0][j] = a[0][j] / self.u[0][0]
                sum = 0
                for k in range(i - 1):
                    sum += pow(self.u[k][i], 2)

                self.u[i][i] = np.sqrt(a[i][i] - sum)
            for j in range(i + 1, self.dim):
                if i < j:
                    sum = 0
                    for k in range(i - 1):
                        sum += self.u[k][i] * self.u[k][j]

                    self.u[i][j] = (a[i][j] - sum) / self.u[i][i]

    def display_eigvals(self):
        print(f"{np.linalg.eigvals(a)} <-- eigvals\n")

    def display_u_matrix(self):
        print(f"{self.u} <-- U matrix\n")

    def get_solution(self):
        self.y = np.linalg.tensorsolve(self.u.T, b)
        return np.linalg.tensorsolve(self.u, self.y)

    def display_solution(self):
        print(f"{self.get_solution()} <-- Solution\n")


if __name__ == "__main__":
    a = np.array([
        [5.8, 0.3, 0.2],
        [0.3, 4, 0.7],
        [0.2, 0.7, 6.7]
    ])

    b = np.array([3.1, 1.7, 1.1])

    Solution(a, b).display_solution()
    Solution(a, b).display_u_matrix()

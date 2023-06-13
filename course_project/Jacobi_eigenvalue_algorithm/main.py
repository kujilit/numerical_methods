import numpy as np
import sys


def trace(a: np.array) -> float:
    dim = a.shape
    sum = 0
    if dim[0] == dim[1]:
        for i in range(dim[0]):
            sum += a[i][i]
        return sum
    else:
        raise TypeError("Функция trace определена только для квадратных матриц.")


def frobenius_norm(a: np.array) -> float:
    return np.sqrt(trace(a.transpose() @ a))


class Jacobi:
    def __init__(self, a):
        self.a = a
        self.phi, self.i, self.j = 0, 0, 0

    def __get_phi(self):
        matrix = np.triu(self.a, 1)
        max_elem = matrix[0][1]
        index_i = 0
        index_j = 1
        for i in range(1, self.a.shape[0]):
            for j in range(i + 1, self.a.shape[0]):
                # print(matrix[i][j])
                if abs(max_elem) < abs(matrix[i][j]):
                    max_elem = matrix[i][j]
                    index_i = i
                    index_j = j
        if self.a[index_i][index_i] == self.a[index_j][index_j]:
            return np.pi/4, index_i, index_j
        else:
            return 0.5 * np.arctan(2 * max_elem / (self.a[index_i][index_i] - self.a[index_j][index_j])), index_i, index_j

    def __generate_rotation_matrix(self):
        self.phi, self.i, self.j = self.__get_phi()
        mat_T = np.eye(self.a.shape[0], dtype=float)
        mat_T[self.i][self.i] = np.cos(self.phi)
        mat_T[self.j][self.j] = np.cos(self.phi)
        mat_T[self.i][self.j] = np.sin(self.phi)
        mat_T[self.j][self.i] = -np.sin(self.phi)

        print(mat_T)

        return mat_T

    def next_iteration(self):
        mat_T = self.__generate_rotation_matrix()
        mat_a = mat_T.transpose() @ self.a @ mat_T
        return mat_a

    def diagonalize(self):
        while abs(self.a[self.i][self.j]) > 1e-5:
            print(self.i, self.j)
            self.a = self.next_iteration()
        return self.a


if __name__ == "__main__":
    a = np.array([
        [4.22, -0.03, 0.02, 0.05],
        [-0.03, 0.3, -0.06, 0.04],
        [0.02, -0.06, 1.6, -0.01],
        [0.05, 0.04, -0.01, 1.71]
    ])

    # a = np.array([[1, 2, 4],
    #               [2, 3, 5],
    #               [4, 5, 6]])

    # a = np.array([[1, 2],
    #               [2, 3]])

    print(Jacobi(a).diagonalize())
    print(np.linalg.eigvals(a))


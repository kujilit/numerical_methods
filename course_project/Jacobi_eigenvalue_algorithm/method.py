import numpy as np
from stuff import frobenius_norm


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

        return mat_T

    def __next_iteration(self):
        mat_T = self.__generate_rotation_matrix()
        mat_a = mat_T.transpose() @ self.a @ mat_T
        # print(mat_a)
        return mat_a

    def __diagonalize(self):
        while abs(self.a[self.i][self.j]) > 1e-4:
            self.a = self.__next_iteration()
            # print(self.a)
        return self.a

    def display_eigvals(self):
        eigvals = []
        print(f"{frobenius_norm(self.a)} <– Фробениусова норма A до преобразований\n")
        self.a = self.__diagonalize()
        print(f"{self.a} <– Матрица A после всех преобразований")
        print(f"{frobenius_norm(self.a)} <– Фробениусова норма A после преобразований\n")
        for i in range(self.a.shape[0]):
            eigvals.append(self.a[i][i])
        print(f"{eigvals} <– Элементы главной диагонали матрицы A")





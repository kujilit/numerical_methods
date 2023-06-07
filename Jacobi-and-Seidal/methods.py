import numpy as np


def define_alpha_and_beta(dim, a, b):
    alpha = np.zeros(dim)
    beta = np.zeros(dim[0])

    for i in range(dim[0]):
        for j in range(dim[0]):
            if i != j:
                alpha[i][j] = - a[i][j] / a[i][i]
            if i == j:
                beta[i] = b[i] / a[i][i]
    return alpha, beta


def error(x):
    vect_sum = 0
    for elem in x:
        vect_sum += np.power(elem, 2)

    return np.sqrt(vect_sum)


class Jacobi:
    def __init__(self, a: np.array, b: np.array, eps: float):
        self.a = a
        self.b = b

        self.dim = a.shape
        self.eps = eps

        self.alpha , self.beta = define_alpha_and_beta(self.dim, self.a, self.b)

    def get_solution(self):
        x_current = self.b
        x_next = self.alpha.dot(x_current) + self.beta
        # x_next = np.zeros(self.dim[0])
        iterator = 1

        while error(x_next - x_current) >= self.eps:
            print(f"iteration: {iterator}, x_cur: {x_current}, x_next: {x_next}")
            x_current = x_next
            x_next = self.alpha.dot(x_current) + self.beta
            iterator += 1

        return x_next, iterator


class Seidal:
    def __init__(self, a: np.array, b: np.array, eps:float):
        self.a = a
        self.b = b

        self.dim = a.shape
        self.eps = eps

        self.alpha, self.beta = define_alpha_and_beta(self.dim, self.a, self.b)

    def get_solution(self):
        x_current = self.b
        x_next = np.zeros(self.dim[0])

        iterator = 1

        while error(x_next - x_current) >= self.eps:
            sum_dim = 0
            sum_iter = 0
            # print(f"iteration: {iterator}, x_cur: {x_current}, x_next: {x_next}")
            x_current = x_next
            for i in range(self.dim[0]):
                sum_dim = 0
                sum_iter = 0
                for j in range(i, self.dim[0]):
                    sum_dim += self.alpha[i][j] * x_current[j]
                for j in range(i):
                    sum_iter += self.alpha[i][j] * x_next[j]
                x_next[i] = (sum_iter + sum_dim) + self.beta[i]
            iterator += 1

        return x_next, iterator


A = np.array([
    [10, -1, 1],
    [1, 10, -1],
    [1, -2, 10]
])
b = np.array([10, 8, 9])

print(np.linalg.tensorsolve(A, b))
print(Jacobi(A, b, 1e-3).get_solution()[0])
print(Seidal(A, b, 1e-5).get_solution()[0])

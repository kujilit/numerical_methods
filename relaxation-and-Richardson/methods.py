import numpy as np


def get_alpha_and_beta(a: np.array, b: np.array):
    alpha = np.zeros(a.shape)
    beta = np.zeros(a.shape[0])
    for i in range(a.shape[0]):
        beta[i] = b[i] / a[i][i]
        for j in range(a.shape[1]):
            if i != j:
                alpha = -a[i][j]/a[i][i]
    return alpha, beta


class Relaxation:
    def __init__(self, a: np.array, b: np.array, x_0: np.array):
        self.a = a
        self.b = b
        self.x = x_0
        self.alpha, self.beta = get_alpha_and_beta(a, b)

    def solution(self, eps: float):
        x_next = np.zeros(self.x.shape)
        while np.linalg.norm(self.x - x_next) > eps:
            for i in range(self.x_next.shape[0]):
                for j in range


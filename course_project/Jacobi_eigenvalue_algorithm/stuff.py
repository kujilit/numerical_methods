import numpy as np


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


data = [np.array([
    [4.22, -0.003, 0.002, 0.005],
    [-0.003, 0.3, -0.006, 0.004],
    [0.002, -0.006, 1.6, -0.001],
    [0.005, 0.004, -0.001, 1.71]]),
    np.array([
    [4.22, -0.003, 0.002],
    [-0.003, 0.3, -0.006],
    [0.002, -0.006, 1.6]]),
    np.array([
    [4.22, -0.003],
    [-0.003, 0.3]]),
]

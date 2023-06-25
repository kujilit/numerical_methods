import numpy as np
from matrix_generator import generate_matrix


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


data = []
for i in range(3, 10):
    data.append(generate_matrix(i))

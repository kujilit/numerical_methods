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


if __name__ == "__main__":
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

print(frobenius_norm(a))


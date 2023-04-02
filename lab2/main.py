import numpy
import numpy as np


def is_invertible(a: np.array):
    return np.linalg.det(a) > 0 and np.shape(a)[0] == np.shape(a)[1]


class Solution:
    def __int__(self, dim: int):
        self.A = np.array()


if __name__ == "__main__":
    a1 = np.array([
        [13.14, -2.12, 1.17],
        [-2.12, 6.3, -2.45],
        [1.17, -2.45, 4.6]
    ])

    print(is_invertible(a1))

    a2 = np.array([
        [4.31, 0.26, 0.61, 0.27],
        [0.26, 2.32, 0.18, 0.34],
        [0.61, 0.18, 3.20, 0.31],
        [0.27, 0.34, 0.31, 5.17]
    ])

from methods import Relaxation
import numpy as np

if __name__ == "__main__":
    a = np.array([
        [4, -1, -6, 0],
        [-5, -4, 10, 8],
        [0, 9, 4, -2],
        [1, 0, -7, 5]
    ])
    b = np.array([2, 21, -12, -6])
    x_0 = np.array([1, 1, 1, 1])
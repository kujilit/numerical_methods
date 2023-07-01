import numpy as np

np.random.seed(1)


def generate_matrix(dim: int):
    rng = np.random.default_rng()
    matrix = 1 * rng.random((dim, dim)) - 1
    matrix = np.triu(matrix)
    matrix = matrix + matrix.T
    return matrix


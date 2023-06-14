import numpy as np
from method import Jacobi
from stuff import data


if __name__ == "__main__":
    for a in data:
        print(f"============ Размерность: {a.shape[0]} ============")
        print(f"{a} <– Матрица A")

        Jacobi(a, 1e-6).display_eigvals()

        print(f"{np.linalg.eigvals(a)} <– Ожидаемые собственные значения")
import numpy as np

np.set_printoptions(linewidth=1000, suppress=True, precision=9)

np.random.seed(1)


def generate_matrix(dim: int):
    rng = np.random.default_rng()
    matrix = 1 * rng.random((dim, dim)) - 1
    matrix = np.triu(matrix)
    matrix = matrix + matrix.T
    return matrix

def iterations_method(A: np.array, x_0: np.array, accuracy: float):
    x_new = A.dot(x_0)

    eigval_new = np.inf
    steps_num = 0
    while True:
        steps_num += 1
        x_old = x_new / np.linalg.norm(x_new)
        x_new = A.dot(x_old)

        eigval_old = eigval_new
        eigval_new = max(x_new / x_old)

        if abs(eigval_new - eigval_old) < accuracy:
            break

    return eigval_new, x_new, steps_num


if __name__ == "__main__":

    A1 = generate_matrix(3)
    A2 = generate_matrix(5)
    A3 = generate_matrix(7)

    A_list = [A1, A2, A3]
    acc_list = [1e-1, 1e-3, 1e-6, 1e-9]

    for A in A_list:
        print("================\n")
        print(f"{A} <– matrix\n")

        for accuracy in acc_list:
            print(f"{accuracy} <– accuracy\n")
            n = A.shape[0]

            eigval, eigvect, steps_num = iterations_method(A, np.zeros(n) + 1, accuracy)

            print(f"{eigval} <– eigval\n")
            print(f"{eigvect} <– found eigvector\n")
            print(f"iterations: {steps_num}\n")
            print("================\n")

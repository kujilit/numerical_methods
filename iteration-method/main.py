import numpy as np
import warnings


warnings.simplefilter(action="ignore", category=RuntimeWarning)
np.set_printoptions(precision=9)


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
    A1 = np.array([
            [5, 2, 1],
            [2, 4, 2],
            [1, 2, 9]
    ])
    A2 = np.array([
            [10, 1, 2, 3, 1],
            [1, 2, -3, 1, 3],
            [2, -3, 5, 7, 2],
            [3, 1, 7, 9, 1],
            [1, 3, 2, 1, 10]
    ])
    A3 = np.array([
            [10, 1, 2, 3, 2, 1, 1],
            [1, 4, -3, 1, 1, 1, 1],
            [2, -3, 3, 2, 1, 1, 2],
            [3, 1, 2, 10, 1, 1, 3],
            [2, 1, 1, 1, 5, 1, 2],
            [1, 1, 1, 1, 1, 4, 1],
            [1, 1, 2, 3, 2, 1, 10]
    ])

    A_list = [A1, A2, A3]
    acc_list = [1e-1, 1e-3, 1e-6, 1e-9]

    for A in A_list:
        print("========Матрица========: \n{}\n\n".format(A))
        print(f"Ожидаемые данные:{np.linalg.eigvals(A)}\n\n")

        for accuracy in acc_list:
            print("accuracy: {}\n".format(accuracy))
            n = A.shape[0]
            eigval, eigvect, steps_num = iterations_method(A, np.zeros(n) + 1, accuracy)
            print("Найденное собственное значение: " + str(eigval))
            print("Собственный вектор: " + str(eigvect))
            print("Номер шага: " + str(steps_num) + "\n")
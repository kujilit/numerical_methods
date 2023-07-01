import math
import numpy as np

np.set_printoptions(linewidth=1000, suppress=True)

def nu(k, n):
    return math.cos((2 * k - 1) * math.pi / (2 * n))

def error(x):
    vect_sum = 0
    for elem in x:
        vect_sum += np.power(elem, 2)

    return np.sqrt(vect_sum)


def relax(_a, _b, _x_start):
    omega = 0.7
    _x_next = np.copy(_x_start)
    for i in range(len(_a)):
        _x_next[i] = (1 - omega) * _x_start[i] +\
                     omega * (- sum((_a[i][j] * _x_start[j]) for j in range(i + 1, len(_a)))
                              - sum((_a[i][j] * _x_next[j]) for j in range(0, i)) + _b[i]) / _a[i][i]
    iterator = 1
    while error(_x_next - _x_start) >= 10e-10:
        _x_start = np.copy(_x_next)
        for i in range(len(_a)):
            _x_next[i] = (1 - omega) * _x_start[i] \
                      + omega * (- sum((_a[i][j] * _x_start[j]) for j in range(i + 1, len(_a)))
                                 - sum((_a[i][j] * _x_next[j]) for j in range(0, i)) + _b[i]) / _a[i][i]
        iterator += 1
    return _x_next, iterator


def richardson(_a, _b, _x_start):
    lambda_max = max(np.linalg.eigvals(_a))
    lambda_min = min(np.linalg.eigvals(_a))

    eta = lambda_min / lambda_max
    ro0 = (1 - eta) / (1 + eta)
    tau0 = 2 / (lambda_max + lambda_min)
    n = 7

    _x_next = _x_start + (tau0 / (1 + ro0 * nu(1, n))) * (- _a.dot(_x_start) + _b)
    iterator = 2
    while iterator < n and error(_x_next - _x_start) >= 10e-10:
        _x_start = np.copy(_x_next)
        _x_next = _x_start + (tau0 / (1 + ro0 * nu(iterator, n))) * (- _a.dot(_x_start) + _b)
        iterator += 1

    return _x_next, iterator


if __name__ == "__main__":
    a = np.array( [[2, -4, 1, 3],
                  [4, 15, -1, 2],
                  [1, -1, 11, 1],
                  [3, 2, 1, 5]])

    b = np.array([13, 1, 4, 2])

    x_start = np.array([0., 0., 0., 0.])

    x1, iterator_1 = relax(a, b, x_start)
    print(f"{x1}<– relaxation method\n{iterator_1} <– iterations\n")
    x2, iterator_2 = richardson(a, b, x_start)
    print(f"{x2}<– Richardson method\n{iterator_2} <– iterations\n")


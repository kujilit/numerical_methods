import numpy as np

A = np.array([
    [2, 8, 16],
    [13, 82, 34],
    [10, 8, 44]
])

print(np.linalg.cond(A, np.inf) / np.linalg.cond(A, 2))
print(1/3 <= np.linalg.cond(A, np.inf) / np.linalg.cond(A, 2) <= 3)


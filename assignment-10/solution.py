import numpy as np

A = np.array([[2, 1, 5],
              [2, -3, 1],
              [1, 5, 7]])

B = np.array([10, 13, 8])

X = np.linalg.solve(A, B)

print("Solution:")
print("x1 =", X[0])
print("x2 =", X[1])
print("x3 =", X[2])

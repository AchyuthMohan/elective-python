import numpy as np
A = np.array([[3, 2, 4], [4, 6, 2], [2, 7, 6]])
B = np.array([6, 3, 4])
X = np.linalg.solve(A, B)
print("Solution: ")
print(X)
print("Inverse of A: ")
a_inverse=np.linalg.inv(A)
print(a_inverse)

print("Determinant pf A: ")
det=np.linalg.det(A)
print(det)
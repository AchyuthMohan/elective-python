import numpy as np

print("Enter a 3x3 matrix:")
matrix = np.zeros((3, 3))
for i in range(3):
    row = input(f"Enter values for row {i+1} (space-separated): ").split()
    matrix[i] = row

trace = np.trace(matrix)
print("Trace:", trace)

determinant = np.linalg.det(matrix)
print("Determinant:", determinant)
transpose = np.transpose(matrix)
print("Transpose:")
print(transpose)
try:
    inverse = np.linalg.inv(matrix)
    print("Inverse:")
    print(inverse)
except np.linalg.LinAlgError:
    print("The matrix is singular, inverse does not exist.")
rank = np.linalg.matrix_rank(matrix)
print("Rank:", rank)

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

vector = np.array([1, 2, 3]).reshape(-1, 1)
result = np.dot(matrix, vector)
print("Matrix-vector multiplication:")
print(result)

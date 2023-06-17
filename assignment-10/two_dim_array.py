import numpy as np

A = np.array([[3, 4, 5, 2],
              [5, 6, 7, 4],
              [7, 8, 9, 5]])
A = np.vstack((A, [1, 1, 1, 1]))

A = np.hstack((A, np.array([[2], [2], [2], [2]])))
A = np.delete(A, 1, axis=0)

print("Shape of A:", A.shape)
smallest_per_column = np.min(A, axis=0)
print("Smallest element in each column:", smallest_per_column)
largest_per_row = np.max(A, axis=1)
print("Largest element in each row:", largest_per_row)
average_per_column = np.mean(A, axis=0)
print("Average of elements in each column:", average_per_column)
sorted_rows = np.sort(A, axis=1)
print("Sorted elements in each row:\n", sorted_rows)

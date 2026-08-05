import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix Multiplication")
print(A @ B)

print()

print("Transpose")
print(A.T)

print()

print("Determinant")
print(np.linalg.det(A))

print()

print("Inverse")
print(np.linalg.inv(A))
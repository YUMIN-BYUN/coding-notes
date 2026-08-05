import numpy as np

#1
v = np.array([10, 20, 30, 40, 50])
print(v)
print(type(v))

#2
print(np.zeros(4))
print(np.ones(6))
print(np.arange(2,12,2))
print(np.linspace(0,100,5))

#3
numbers = np.array([5, 10, 15, 20 ,25])

print(numbers[0])
print(numbers[-1])
print(numbers[2])
print(numbers[:3])
print(numbers[-2:])
print(numbers[1:4])

#4
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a + 10)
print(b * 2)

#5
matrix = np.array([
    [1,2,3],
    [4,5,6]
])

vector = np.array([10,20,30])

print(matrix+vector)

#6
A = np.array([
    [2, 1],
    [5, 3]
])

B = np.array([
    [1, 2],
    [3, 4]
])

print(A @ B)
print(A.T)
print(np.linalg.det(A))
print(np.linalg.inv(A))
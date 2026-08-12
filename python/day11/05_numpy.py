import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 6, 8, 10])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

#1
print(a[0])
print(a[-1])
print(a[2])
print()

#2
print(a[1:4])
print()

#3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print()

#4
print(a+5)
print()

#5
print(b*3)
print()

#6
print(matrix[1,1])
print()

#7
print(matrix[1,:])
print()

#8
print(matrix * 2)
print(matrix + 10)
print()

#9
print(np.zeros(5))
print(np.ones(5))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))
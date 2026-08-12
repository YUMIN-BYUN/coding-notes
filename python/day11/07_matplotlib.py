import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])

physics = np.array([70, 75, 83, 88, 95])
math = np.array([65, 72, 80, 85, 90])

#1
plt.plot(x,physics)
plt.title("Physics Scores")
plt.xlabel("Test")
plt.ylabel("Score")
plt.show()

#2
plt.plot(x,physics,label = "Physics")
plt.plot(x,math,label = "Math")
plt.title("Physics vs Math")
plt.xlabel("Test")
plt.ylabel("Score")
plt.grid(True)
plt.legend()
plt.show()

#3
plt.scatter(physics,math)
plt.title("Physics vs Math Scores")
plt.xlabel("Physics scores")
plt.ylabel("Math scores")
plt.show()

#4
students = ["Alice", "Bob", "Charlie", "David", "Emma"]
plt.bar(students,physics)
plt.title("Physics Scores by Student")
plt.show()

#5
x = np.linspace(0,10,100)
y = x**2
plt.plot(x,y)
plt.title("y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 1
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Line")

# 2
plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Bar")

# 3
plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Scatter")

# 4
plt.subplot(2, 2, 4)
plt.hist(y)
plt.title("Histogram")

plt.tight_layout()

plt.show()
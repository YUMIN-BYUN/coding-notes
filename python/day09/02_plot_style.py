import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 5, 4, 7, 6]

plt.plot(
    x,
    y,
    color="red",
    linestyle="--",
    marker="o",
    label="Data"
)

plt.title("Styled Line Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)
plt.legend()

plt.show()
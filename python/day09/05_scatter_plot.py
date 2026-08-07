import matplotlib.pyplot as plt

height = [160, 165, 170, 175, 180]
score = [70, 75, 82, 88, 95]

plt.scatter(
    height,
    score,
    color="blue",
    s=80,
    marker="o"
)

plt.title("Height vs Score")
plt.xlabel("Height (cm)")
plt.ylabel("Score")

plt.grid(True)

plt.show()
import matplotlib.pyplot as plt

scores = [
    72, 75, 81, 83, 84,
    85, 86, 87, 88, 90,
    91, 92, 95, 96, 98
]

plt.hist(
    scores,
    bins=5,
    color="skyblue",
    edgecolor="black"
)

plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.grid(axis="y")

plt.show()
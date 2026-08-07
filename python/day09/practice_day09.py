import matplotlib.pyplot as plt

students = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Ivy", "Jack"
]

scores = [72, 75, 81, 83, 84, 85, 86, 87, 88, 90]
study_hours = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8]

subjects = ["Math", "English", "Physics", "Chemistry"]
averages = [82, 76, 91, 85]


# 1. Line plot
plt.subplot(2, 2, 1)

plt.plot(
    students,
    scores,
    marker="o"
)

plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.grid(True)


# 2. Bar chart
plt.subplot(2, 2, 2)

plt.bar(
    subjects,
    averages,
    color="skyblue"
)

plt.title("Subject Averages")
plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.grid(axis="y")


# 3. Scatter plot
plt.subplot(2, 2, 3)

plt.scatter(
    study_hours,
    scores,
    marker="*",
    s=80
)

plt.title("Study Hours vs Scores")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.grid(True)


# 4. Histogram
plt.subplot(2, 2, 4)

plt.hist(
    scores,
    bins=5,
    color="green",
    edgecolor="black"
)

plt.title("Score Distribution")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.grid(axis="y")


plt.tight_layout()
plt.show()
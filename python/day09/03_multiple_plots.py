import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

student_a = [70, 75, 80, 90, 95]
student_b = [65, 72, 78, 85, 90]

plt.plot(
    x,
    student_a,
    marker="o",
    label="Student A"
)

plt.plot(
    x,
    student_b,
    marker="s",
    label="Student B"
)

plt.title("Student Scores")
plt.xlabel("Exam")
plt.ylabel("Score")

plt.grid(True)
plt.legend()

plt.show()
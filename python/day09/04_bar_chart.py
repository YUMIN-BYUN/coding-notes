import matplotlib.pyplot as plt

fruits = ["Apple", "Banana", "Orange", "Grape"]
sales = [15, 23, 18, 30]

plt.bar(
    fruits,
    sales,
    color="skyblue",
    width=0.6
)

plt.title("Fruit Sales")
plt.xlabel("Fruit")
plt.ylabel("Sales")

plt.grid(axis="y")

plt.show()
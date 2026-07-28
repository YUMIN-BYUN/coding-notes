import random

# randint()
print("=== randint() ===")
number = random.randint(1, 10)
print(number)

print()

# choice()
print("=== choice() ===")
fruits = ["apple", "banana", "orange", "grape"]
print(random.choice(fruits))

word = "PYTHON"
print(random.choice(word))

print()

# shuffle()
print("=== shuffle() ===")
cards = ["A", "K", "Q", "J", "10"]
print("Before:", cards)

random.shuffle(cards)

print("After :", cards)

print()

# sample()
print("=== sample() ===")
numbers = [1, 2, 3, 4, 5]
print(random.sample(numbers, 3))

students = ["Kim", "Lee", "Park", "Choi", "Jung", "Han"]
print(random.sample(students, 2))
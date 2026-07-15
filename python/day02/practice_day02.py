# ==========================
# Python Day 2 Practice
# Loops and Functions
# ==========================

SEPARATOR = "=" * 20


# Problem 1
for number in range(1, 101):
    print(number)

print(SEPARATOR)


# Problem 2
sum_1_to_100 = 0

for number in range(1, 101):
    sum_1_to_100 += number

print(sum_1_to_100)
print(SEPARATOR)


# Problem 3
for number in range(1, 10):
    print(f"7 x {number} = {7 * number}")

print(SEPARATOR)


# Problem 4
for number in range(1, 6):
    print("*" * number)

print(SEPARATOR)


# Problem 5
for number in range(1, 21):
    if number % 3 == 0:
        continue

    print(number)

print(SEPARATOR)


# Problem 6
def square(number):
    return number * number


print(square(8))
print(SEPARATOR)


# Problem 7
def average(number1, number2, number3):
    return (number1 + number2 + number3) / 3


print(average(90, 80, 100))
print(SEPARATOR)


# Problem 8
def sum_to_n(n):
    result = 0

    for number in range(1, n + 1):
        result += number

    return result


print(sum_to_n(10))
print(SEPARATOR)


# Problem 9
def add(x, y):
    return x + y


a = int(input("number 1: "))
b = int(input("number 2: "))

print("sum:", add(a, b))
print(SEPARATOR)


# Additional Problem
for number in range(1, 6):
    print(str(number) * number)
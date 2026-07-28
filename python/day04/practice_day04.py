import random
import my_math

name = input("Student name: ")
try:
    subject_count = int(input("Number of subjects: "))

    if subject_count <= 0:
        raise ValueError

    

except ValueError:
    print("Pleas enter a positive integer")

else:
    scores = []

    for _ in range(subject_count):
            scores.append(random.randint(60,100))

    average = my_math.average(scores)

    print(scores)
    print(average)

    with open("scores.txt", "w") as file:
        file.write(f"Student: {name}\n")
        file.write(f"Scores: {scores}\n")
        file.write(f"Average: {average:.2f}\n")

    print("\n===== Saved Data =====")

    with open("scores.txt", "r") as file:
        for line in file:
            print(line.strip())
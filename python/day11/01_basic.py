students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 93},
    {"name": "David", "score": 68},
    {"name": "Emma", "score": 88}
]

#1
total = 0
for i in range(0,len(students)):
    print(f"{students[i]["name"]}: {students[i]["score"]}")
    total += students[i]["score"]
print()

#2
average = total / len(students)
print(f"Total: {total}")
print(f"Average: {average}")
print()

#3
print("Student with score >= 80")
for i in range(0,len(students)):
    if students[i]["score"] >= 80:
        print(f"{students[i]["name"]}: {students[i]["score"]}")
print()


#4
for i in range(0,len(students)):
    count = 0
    for j in range(0,len(students)):
        if students[i]["score"] >= students[j]["score"]:
            count += 1
        else:
            break

    if count == len(students):
        top_index = i
        break

print(f"Top Student: {students[top_index]["name"]}")
print(f"Score: {students[top_index]["score"]}")
print()

#5
for i in range(0,len(students)):
    if students[i]["score"] >= 90:
        grade = "A"
    elif students[i]["score"] >= 80:
        grade = "B"
    elif students[i]["score"] >= 70:
        grade = "C"
    elif students[i]["score"] >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{students[i]["name"]}: {grade}")
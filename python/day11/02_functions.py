students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 93},
    {"name": "David", "score": 68},
    {"name": "Emma", "score": 88}
]

#1
def calculate_total(students):
    total = 0
    for student in students:
        total += student["score"]
    return total

#2 
def calculate_average(students):
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)

#3
def get_high_scorers(students, cutoff):
    temp = []
    for student in students:
        if student["score"] >= cutoff:
            temp.append(student)
    return temp

#4
def get_top_students(students):
    top_index = 0
    for i in range(1,len(students)):
        if students[i]["score"] > students[top_index]["score"]:
            top_index = i
    return students[top_index]

#5
def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade ="B"
    elif score >= 70:
        grade ="C"
    elif score >= 60:
        grade ="D"
    else:
        grade ="F"

    return grade

print(f"Total: {calculate_total(students)}")
print(f"Average: {calculate_average(students)}\n")
print("Students with score >= 80")
for student in get_high_scorers(students,80):
    print(f"{student["name"]}: {student["score"]}")
print()
print(f"Top student: {get_top_students(students)["name"]}")
print(f"Score: {get_top_students(students)["score"]}\n")
print("Grade")
for student in students:
    print(f"{student['name']}: {get_grade(student['score'])}")


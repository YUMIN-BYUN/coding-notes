#given data
students = [
    {
        "name": "Alice",
        "major": "Physics",
        "courses": ["Python", "Math"],
        "scores": {"Python": 88, "Math": 92}
    },
    {
        "name": "Bob",
        "major": "Engineering",
        "courses": ["Python", "C++"],
        "scores": {"Python": 76, "C++": 85}
    },
    {
        "name": "Charlie",
        "major": "Physics",
        "courses": ["Math", "C++"],
        "scores": {"Math": 95, "C++": 91}
    },
    {
        "name": "David",
        "major": "Engineering",
        "courses": ["Python", "Math", "C++"],
        "scores": {"Python": 82, "Math": 79, "C++": 88}
    }
]

#1
print("Physics Students")
for student in students:
    if student["major"] == "Physics":
        print(f"{student["name"]}: {student['courses']}")
print()

#2
print("Python Students")
for student in students:
    for course in student["courses"]:
        if course == "Python":
            print(f"{student['name']}: {student['scores']['Python']}")
print()

#3
for student in students:
    if student["name"] == "Bob":
        student["courses"].append("Math")
        student["scores"]["Math"] = 84
        print(f"{student}")
print()

#4
new_student = {
        "name": "Emma",
        "major": "Physics",
        "courses": ["Python", "C++", "Math"],
        "scores": {"Python": 94, "C++": 90, "Math": 89}
    }
students.append(new_student)
for student in students:
    print(f"{student['name']}")
print()

#5
cpp_list = []
for student in students:
    for course in student["courses"]:
        if course == "C++":
            cpp_list.append(
                {"name": student["name"],
                 "score": student["scores"]["C++"]}
                )
top_index = 0
for i in range(1,len(cpp_list)):
    if cpp_list[i]['score'] > cpp_list[top_index]['score']:
        top_index = i
print(f"Top C++ Students: {cpp_list[i]['name']}")
print(f"Score: {cpp_list[top_index]['score']}")
print()

#6
course_students = {}
py_group = []
cpp_group = []
math_group = []
for student in students:
    for course in student["courses"]:
        if course == "Python":
            py_group.append(student['name'])
        elif course == "C++":
            cpp_group.append(student["name"])
        elif course == "Math":
            math_group.append(student["name"])
course_students["Python"] = py_group
course_students["Math"] = math_group
course_students["C++"] = cpp_group
print(course_students)
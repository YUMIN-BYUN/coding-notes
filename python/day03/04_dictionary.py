student = {
    "name": "Lee",
    "age": 22,
    "major": "Electrical Engineering"
}

print(student["name"])
student["age"] = 23
student["gpa"] = 4.3
del student["major"]
for key, value in student.items():
    print(key, value)
print(student.get("major"))
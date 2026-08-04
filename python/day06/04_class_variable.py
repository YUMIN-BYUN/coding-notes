class Student:
    school = "Korea University"

    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name   : {self.name}")
        print(f"School : {Student.school}")


student1 = Student("Alice")
student2 = Student("Bob")

student1.show_info()
print()

student2.show_info()
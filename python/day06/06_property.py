class Student:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative.")
        else:
            self._age = value


student = Student(20)

print(student.age)

student.age = 25
print(student.age)

student.age = -10
print(student.age)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")


student = Student("Kim", 20)

student.introduce()
student.birthday()
student.introduce()
class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Invalid age.")

    def introduce(self):
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Species : {Person.species}")

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        super().introduce()
        print(f"Major   : {self.major}")

class MathTool:
    @staticmethod
    def square(x):
        return x**2

    @staticmethod
    def cube(x):
        return x**3

student = Student("Alice", 20, "Physics")

student.introduce()

print()

print(MathTool.square(5))
print(MathTool.cube(3))

print()

student.age = -10
print(student.age)
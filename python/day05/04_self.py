class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


student1 = Student("Kim")
student2 = Student("Lee")

student1.introduce()
student2.introduce()
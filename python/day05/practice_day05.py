class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}!")

    def change_major(self,major):
        self.major = major
        print(f"Major changed to {self.major}")

st1 = Student("Kim",20,"Chemistry")
st2 = Student("Lee",21,"Mathematics")
st3 = Student("Park",22,"Education")

st1.introduce()
st2.introduce()
st3.introduce()

print()
st1.birthday()
st1.change_major("Business")
print()

st1.introduce()
st2.introduce()
st3.introduce()
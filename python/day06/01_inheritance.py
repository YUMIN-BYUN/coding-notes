class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog("Buddy")
cat = Cat("Nabi")

dog.speak()
cat.speak()

print(dog.name)
print(cat.name)
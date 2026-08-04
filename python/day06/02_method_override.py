class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof.")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow.")


animal = Animal("Animal")
dog = Dog("Buddy")
cat = Cat("Nabi")

animal.speak()
dog.speak()
cat.speak()
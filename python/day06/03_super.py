class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print("Dog constructor")

    def show_info(self):
        print(f"Name : {self.name}")
        print(f"Breed: {self.breed}")


dog = Dog("Buddy", "Golden Retriever")
dog.show_info()
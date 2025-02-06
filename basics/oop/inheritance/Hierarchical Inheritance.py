# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} meows")

# Creating instances of Dog and Cat classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

dog.speak()
cat.speak()

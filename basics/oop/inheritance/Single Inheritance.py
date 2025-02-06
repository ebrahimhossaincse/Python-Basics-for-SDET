# Single Inheritance: A child class inherits from a single parent class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

# Creating instance of Dog class
dog = Dog("Buddy", "Golden Retriever")
dog.speak()

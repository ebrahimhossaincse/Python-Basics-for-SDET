# Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age

# Creating instance of Puppy class
puppy = Puppy("Max", "Labrador", 1)
puppy.speak()
# Run-Time Polymorphism (Method Overriding)
class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

class Cat(Animal):
    def speak(self):
        print("The cat meows")

# Creating instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the speak method on different objects
animal.speak()  # The animal makes a sound
dog.speak()     # The dog barks
cat.speak()     # The cat meows

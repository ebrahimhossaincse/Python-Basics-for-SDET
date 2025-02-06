# Hybrid Inheritance: A combination of two or more types of inheritance.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Bird:
    def __init__(self, species):
        self.species = species

    def fly(self):
        print(f"{self.species} flies in the sky")

class Parrot(Animal, Bird):
    def __init__(self, name, species):
        Animal.__init__(self, name)
        Bird.__init__(self, species)

    def speak(self):
        print(f"{self.name} says hello!")

# Creating instance of Parrot class
parrot = Parrot("Polly", "Macaw")
parrot.speak()
parrot.fly()

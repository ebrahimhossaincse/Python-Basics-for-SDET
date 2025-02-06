# Multiple Inheritance: A child class inherits from more than one parent class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I am {self.age} years old.")

class Employee:
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

    def work(self):
        print(f"Working as a {self.position}, earning {self.salary}")

class Manager(Person, Employee):
    def __init__(self, name, age, position, salary):
        Person.__init__(self, name, age)
        Employee.__init__(self, position, salary)

# Creating instance of Manager class
manager = Manager("Alice", 35, "Manager", 80000)
manager.introduce()
manager.work()

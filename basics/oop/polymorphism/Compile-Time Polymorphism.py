# Compile-Time Polymorphism (Method Overloading Simulation)
class Calculator:
    # Method to add two numbers (or more if needed)
    def add(self, a, b=0, c=0):  # Default arguments simulate overloading
        return a + b + c

# Creating an instance of Calculator
calc = Calculator()

# Calling the add method with different numbers of arguments
print(calc.add(5))       # Outputs 5 (5 + 0 + 0)
print(calc.add(5, 10))    # Outputs 15 (5 + 10 + 0)
print(calc.add(5, 10, 15)) # Outputs 30 (5 + 10 + 15)
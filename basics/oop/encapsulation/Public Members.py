# Example: Public Members
class Car:
    def __init__(self, make, model):
        self.make = make  # Public attribute
        self.model = model  # Public attribute

    def start(self):
        print(f"The {self.make} {self.model} is starting.")  # Public method

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla")

# Accessing public members outside the class
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Corolla

# Calling the public method
my_car.start()  # Output: The Toyota Corolla is starting.
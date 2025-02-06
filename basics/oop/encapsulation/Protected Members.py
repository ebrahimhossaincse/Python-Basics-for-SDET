# Example: Protected Members
class Vehicle:
    def __init__(self, brand, speed):
        self._brand = brand  # Protected attribute
        self._speed = speed  # Protected attribute

    def drive(self):
        print(f"The {self._brand} vehicle is driving at {self._speed} km/h.")

class Car(Vehicle):
    def __init__(self, brand, speed, model):
        super().__init__(brand, speed)
        self._model = model  # Protected attribute

    def display_info(self):
        print(f"Car: {self._brand}, Model: {self._model}, Speed: {self._speed} km/h")

# Creating an instance of the Car class
car = Car("Honda", 120, "Civic")

# Accessing protected members within the subclass
car.display_info()  # Output: Car: Honda, Model: Civic, Speed: 120 km/h

# Accessing protected members directly (outside class)
# While possible, it's not recommended
print(car._brand)  # Output: Honda
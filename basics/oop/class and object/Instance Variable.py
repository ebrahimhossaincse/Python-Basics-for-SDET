class Car:
    def __init__(self, make, model, year):
        self.make = make    # Instance variable
        self.model = model  # Instance variable
        self.year = year    # Instance variable

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

# Creating instances of Car
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Accessing instance variables
car1.display_info()  # Output: Car Info: 2020 Toyota Corolla
car2.display_info()  # Output: Car Info: 2022 Honda Civic

# Accessing individual instance variables
print(f"Car 1 Make: {car1.make}, Model: {car1.model}, Year: {car1.year}")
print(f"Car 2 Make: {car2.make}, Model: {car2.model}, Year: {car2.year}")
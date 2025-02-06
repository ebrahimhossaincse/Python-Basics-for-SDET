class TechDevice:
    category = "Electronics"  # Class attribute

    def __init__(self, brand, model, year):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute
        self.year = year  # Instance attribute

# Create instances of TechDevice
device1 = TechDevice("Apple", "iPhone 14", 2022)
device2 = TechDevice("Samsung", "Galaxy S23", 2023)

# Access instance and class attributes
print(device1.brand, device1.model, device1.year, device1.category)  # Instance and class attributes
print(device2.brand, device2.model, device2.year, device2.category)  # Instance and class attributes
print(TechDevice.category)  # Access class attribute directly
class Employee:
    company_name = "Tech Corp"  # Class variable (shared by all instances)

    def __init__(self, name, position):
        self.name = name  # Instance variable
        self.position = position  # Instance variable

    def display_info(self):
        print(f"Employee: {self.name}, Position: {self.position}, Company: {Employee.company_name}")

# Creating instances of Employee
employee1 = Employee("Alice", "Developer")
employee2 = Employee("Bob", "Manager")

# Displaying employee information
employee1.display_info()
employee2.display_info()

# Accessing class variable directly from the class
print(f"Company Name: {Employee.company_name}")
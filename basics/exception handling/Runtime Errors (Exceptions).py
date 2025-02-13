# Runtime Errors (Exceptions) Examples

# 1. ZeroDivisionError: Division by zero
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result of {a} / {b} = {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# 2. TypeError: Incompatible types
def add_numbers(a, b):
    try:
        result = a + b
        print(f"Result of {a} + {b} = {result}")
    except TypeError:
        print("Error: Incompatible types for addition!")

# 3. IndexError: Accessing an out-of-range index
def access_list_element(my_list, index):
    try:
        value = my_list[index]
        print(f"Value at index {index}: {value}")
    except IndexError:
        print(f"Error: Index {index} is out of range for the list!")

# 4. KeyError: Accessing a non-existent dictionary key
def access_dict_value(my_dict, key):
    try:
        value = my_dict[key]
        print(f"Value for key '{key}': {value}")
    except KeyError:
        print(f"Error: Key '{key}' does not exist in the dictionary!")

# 5. FileNotFoundError: Trying to open a non-existent file
def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"File content: {content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")

# 6. ValueError: Invalid value for an operation
def convert_to_int(value):
    try:
        number = int(value)
        print(f"Converted value: {number}")
    except ValueError:
        print(f"Error: Cannot convert '{value}' to an integer!")

# 7. AttributeError: Accessing a non-existent attribute
def access_attribute(obj, attr):
    try:
        value = getattr(obj, attr)
        print(f"Value of attribute '{attr}': {value}")
    except AttributeError:
        print(f"Error: Object has no attribute '{attr}'!")

# 8. NameError: Accessing an undefined variable
def print_variable():
    try:
        print(undefined_variable)
    except NameError:
        print("Error: Variable 'undefined_variable' is not defined!")

# 9. ModuleNotFoundError: Importing a non-existent module
def import_module(module_name):
    try:
        __import__(module_name)
        print(f"Module '{module_name}' imported successfully!")
    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found!")

# 10. KeyboardInterrupt: User interrupts the program
def handle_keyboard_interrupt():
    try:
        print("Press Ctrl+C to interrupt...")
        while True:
            pass
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user!")

# Main function to demonstrate all exceptions
def main():
    print("=== Runtime Errors (Exceptions) Examples ===")

    # 1. ZeroDivisionError
    print("\n1. ZeroDivisionError Example:")
    divide_numbers(10, 0)

    # 2. TypeError
    print("\n2. TypeError Example:")
    add_numbers(10, "5")

    # 3. IndexError
    print("\n3. IndexError Example:")
    access_list_element([1, 2, 3], 5)

    # 4. KeyError
    print("\n4. KeyError Example:")
    access_dict_value({"name": "Alice"}, "age")

    # 5. FileNotFoundError
    print("\n5. FileNotFoundError Example:")
    read_file("nonexistent_file.txt")

    # 6. ValueError
    print("\n6. ValueError Example:")
    convert_to_int("abc")

    # 7. AttributeError
    print("\n7. AttributeError Example:")
    access_attribute("hello", "length")

    # 8. NameError
    print("\n8. NameError Example:")
    print_variable()

    # 9. ModuleNotFoundError
    print("\n9. ModuleNotFoundError Example:")
    import_module("nonexistent_module")

    # 10. KeyboardInterrupt (Uncomment to test)
    # print("\n10. KeyboardInterrupt Example:")
    # handle_keyboard_interrupt()

if __name__ == "__main__":
    main()
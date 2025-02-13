def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid operand type!")
    else:
        print("Result:", result)
    finally:
        print("Division operation attempted.")

divide(10, 2)  # Output: Result: 5.0, Division operation attempted.
divide(10, 0)  # Output: Error: Cannot divide by zero!, Division operation attempted.
divide(10, "2")  # Output: Error: Invalid operand type!, Division operation attempted.
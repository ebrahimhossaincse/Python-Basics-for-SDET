# Basic Shorthand `if-else`
x = int(input("Enter a number: "))
result = "Positive" if x > 0 else "Non-positive"
print(f"Basic Shorthand: {result}")  # Output: Positive

# Shorthand `if-else` with Multiple Conditions
x = int(input("Enter a number: "))
result = "Even" if x % 2 == 0 else "Odd"
print(f"Multiple Conditions: {result}")  # Output: Odd

# Shorthand `if-else` with Nested Conditions
x = int(input("Enter a number: "))
result = "Large" if x > 10 else "Small" if x < 5 else "Medium"
print(f"Nested Conditions: {result}")  # Output: Large

# Shorthand `if-else` with Lists
x = int(input("Enter a number: "))
result = [x * 2 if x > 5 else x + 3 for x in [4, 6, 8]]
print(f"List Comprehension: {result}")  # Output: [7, 12, 16]

# Assigning a Value Based on a Condition
age = int(input("Enter your age: "))
is_adult = "Adult" if age >= 18 else "Minor"
print(f"Age Check: {is_adult}")  # Output: Adult

# Shorthand `if-else` with Functions
x = int(input("Enter a number: "))
def check_sign(x):
    return "Positive" if x > 0 else "Zero or Negative"

print(f"Check Sign (3): {check_sign(3)}")    # Output: Positive
print(f"Check Sign (0): {check_sign(0)}")    # Output: Zero or Negative
print(f"Check Sign (-1): {check_sign(-1)}")  # Output: Zero or Negative

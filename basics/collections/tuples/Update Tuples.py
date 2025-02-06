# Define the tuple
thisTuple = ("Python", "Java", "JavaScript", "C++", "Swift", "Ruby", "Go")

# Change Tuple Values
y = list(thisTuple)  # Convert tuple to list
y[1] = "C"  # Modify the value
thisTuple = tuple(y)  # Convert back to tuple
print(thisTuple)

# Add Items: Convert to list, append new item, then convert back to tuple
newTuple = list(thisTuple)  # Convert tuple to list
newTuple.append("JS")  # Append a new item
thisTuple = tuple(newTuple)  # Convert back to tuple
print(thisTuple)

# Remove an Item
y = list(thisTuple)  # Convert tuple to list
y.remove("Python")  # Remove an item
thisTuple = tuple(y)  # Convert back to tuple
print(thisTuple)

# Delete the Tuple
del thisTuple  # Deletes the tuple completely

# Trying to print it now will cause an error since it's deleted
try:
    print(thisTuple)  # This will cause a NameError
except NameError:
    print("The tuple has been deleted and no longer exists.")

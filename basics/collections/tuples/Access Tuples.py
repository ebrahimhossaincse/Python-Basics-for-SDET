thisTuple = ("Python", "Java", "JavaScript", "C++", "Swift", "Ruby", "Go")

# Access Tuple Items
print(thisTuple[1])  # Output: Java

# Negative Indexing
print(thisTuple[-1])  # Output: Go

# Range of Indexes
print(thisTuple[2:5])  # Output: ('JavaScript', 'C++', 'Swift')

# Check if Item Exists
if "Python" in thisTuple:
  print("Yes, 'Python' is in the programming languages tuple")
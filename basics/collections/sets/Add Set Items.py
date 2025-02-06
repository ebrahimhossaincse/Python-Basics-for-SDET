# Define a set
thisSet = {"Python", "Java", "JavaScript", "C++", "Swift", "Ruby", "Go"}

# Add a single item to the set
thisSet.add("Kotlin")
print(thisSet)

# Add multiple items to the set
thisSet.update(["PHP", "TypeScript", "Rust"])
print(thisSet)

# Attempting to add a duplicate item (sets do not allow duplicates)
thisSet.add("Python")
print(thisSet)
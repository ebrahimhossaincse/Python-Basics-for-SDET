# Define a set
thisSet = {"Python", "Java", "JavaScript", "C++", "Swift", "Ruby", "Go"}

# Remove an item using remove() (raises an error if the item does not exist)
thisSet.remove("Java")
print(thisSet)

# Remove an item using discard() (does NOT raise an error if the item does not exist)
thisSet.discard("Swift")
print(thisSet)

# Attempting to remove a non-existent item using remove() (causes an error)

# Attempting to remove a non-existent item using discard() (no error)
thisSet.discard("Kotlin")  # No error, set remains unchanged

# Remove and return a random item using pop()
removed_item = thisSet.pop()
print(f"Removed: {removed_item}")
print(thisSet)

# Clear all items in the set
thisSet.clear()
print(thisSet)

# Delete the set completely
del thisSet
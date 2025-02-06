# Define a dictionary
tech_dict = {
    "language": "Python",
    "version": 3.11,
    "framework": "Django",
    "database": "PostgreSQL",
    "IDE": "VS Code"
}

# Remove a specific key using pop() (returns the removed value)
removed_value = tech_dict.pop("framework")
print("Removed framework:", removed_value)
print("After pop:", tech_dict)

# Remove the last inserted key-value pair using popitem() (returns a tuple)
removed_item = tech_dict.popitem()
print("Removed item:", removed_item)
print("After popitem:", tech_dict)

# Remove a key using del
del tech_dict["database"]
print("After del:", tech_dict)

# Delete all key-value pairs using clear()
tech_dict.clear()
print("After clear:", tech_dict)

# Delete the dictionary completely
del tech_dict

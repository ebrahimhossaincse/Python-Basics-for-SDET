# Define a dictionary
tech_dict = {
    "language": "Python",
    "version": 3.11,
    "framework": "Django"
}

# Add a new key-value pair directly
tech_dict["database"] = "PostgreSQL"
print("After adding database:", tech_dict)

# Add multiple key-value pairs using update()
tech_dict.update({"IDE": "VS Code", "OS": "Windows"})
print("After adding multiple items:", tech_dict)

# Adding a key with an empty value
tech_dict["license"] = None
print("After adding a key with None:", tech_dict)

# Using setdefault() to add a key if it doesn’t exist
tech_dict.setdefault("editor", "PyCharm")
print("After setdefault:", tech_dict)

# Attempting to add a key that already exists using setdefault() (won't change the value)
tech_dict.setdefault("language", "Java")
print("After setdefault with existing key:", tech_dict)
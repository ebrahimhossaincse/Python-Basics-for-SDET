# Define a dictionary
tech_dict = {
    "language": "Python",
    "version": 3.11,
    "framework": "Django",
    "database": "PostgreSQL"
}

# Change the value of an existing key
tech_dict["version"] = 3.12
print("Updated version:", tech_dict)

# Using update() method to change multiple values
tech_dict.update({"framework": "Flask", "database": "MongoDB"})
print("Updated dictionary:", tech_dict)

# Adding a new key-value pair using update()
tech_dict.update({"IDE": "VS Code"})
print("Added IDE:", tech_dict)

# Adding a new key-value pair directly
tech_dict["platform"] = "Windows"
print("Added platform:", tech_dict)
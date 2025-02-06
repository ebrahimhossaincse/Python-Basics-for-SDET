# Define a dictionary
tech_dict = {
    "language": "Python",
    "version": 3.11,
    "framework": "Django",
    "database": "PostgreSQL"
}

# Loop through keys
print("Looping through keys:")
for key in tech_dict:
    print(key)

# Loop through values
print("\nLooping through values:")
for value in tech_dict.values():
    print(value)

# Loop through keys and values
print("\nLooping through key-value pairs:")
for key, value in tech_dict.items():
    print(f"{key}: {value}")


# Looping using dictionary comprehension (creating a new dictionary with modified values)
uppercase_dict = {key: str(value).upper() for key, value in tech_dict.items()}
print("\nDictionary with uppercase values:", uppercase_dict)

# Looping with index using enumerate()
print("\nLooping with index:")
for index, (key, value) in enumerate(tech_dict.items()):
    print(f"{index}: {key} -> {value}")

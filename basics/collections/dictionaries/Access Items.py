# Define a dictionary
tech_dict = {
    "language": "Python",
    "version": 3.11,
    "framework": "Django",
    "database": "PostgreSQL"
}

# Access a specific value using the key
print("Language:", tech_dict["language"])

# Using get() method (avoids KeyError if the key does not exist)
print("Framework:", tech_dict.get("framework"))

# Access all keys
print("Keys:", tech_dict.keys())

# Access all values
print("Values:", tech_dict.values())

# Access all key-value pairs (items)
print("Items:", tech_dict.items())

# Loop through keys
print("\nLooping through keys:")
for key in tech_dict:
    print(key)

# Loop through values
print("\nLooping through values:")
for value in tech_dict.values():
    print(value)

# Loop through key-value pairs
print("\nLooping through key-value pairs:")
for key, value in tech_dict.items():
    print(f"{key}: {value}")
# Nested Dictionary Examples

# 1. Creating a Nested Dictionary
tech_dict = {
    "Python": {
        "creator": "Guido van Rossum",
        "year": 1991,
        "type": "Programming Language"
    },
    "JavaScript": {
        "creator": "Brendan Eich",
        "year": 1995,
        "type": "Scripting Language"
    },
    "Database": {
        "SQL": {
            "popular": "PostgreSQL",
            "alternative": "MySQL"
        },
        "NoSQL": {
            "popular": "MongoDB",
            "alternative": "Cassandra"
        }
    }
}
print("Nested Dictionary:", tech_dict)

# 2. Accessing Items in a Nested Dictionary
print("Python Creator:", tech_dict["Python"]["creator"])
print("JavaScript Year:", tech_dict["JavaScript"]["year"])
print("Popular NoSQL Database:", tech_dict["Database"]["NoSQL"]["popular"])

# 3. Adding Items to a Nested Dictionary
tech_dict["C++"] = {"creator": "Bjarne Stroustrup", "year": 1983, "type": "Programming Language"}
print("After Adding C++:", tech_dict)

tech_dict["Python"]["latest_version"] = 3.11
print("After Adding Python's Latest Version:", tech_dict)

# 4. Removing Items from a Nested Dictionary
removed_item = tech_dict["JavaScript"].pop("year")
print("Removed Year from JavaScript:", removed_item)
print("After Removing JavaScript Year:", tech_dict)

del tech_dict["Database"]["SQL"]
print("After Deleting SQL from Database:", tech_dict)

# 5. Looping Through a Nested Dictionary
print("\nLooping through main keys:")
for key in tech_dict:
    print(key)

print("\nLooping through nested dictionaries:")
for lang, details in tech_dict.items():
    print(f"{lang} Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

# 6. Copying a Nested Dictionary (Deep Copy)
import copy
tech_dict_copy = copy.deepcopy(tech_dict)
print("\nDeep Copied Dictionary:", tech_dict_copy)

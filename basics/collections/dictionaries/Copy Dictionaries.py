# Define an original dictionary
tech_dict = {
    "language": "Python",
    "version": 3.11,
    "framework": "Django",
    "database": "PostgreSQL"
}

# Method 1: Using copy() method (Shallow Copy)
copied_dict1 = tech_dict.copy()
print("Copied Dictionary (copy() method):", copied_dict1)

# Method 2: Using dict() constructor
copied_dict2 = dict(tech_dict)
print("Copied Dictionary (dict() constructor):", copied_dict2)

# Method 3: Using dictionary comprehension (Alternative shallow copy)
copied_dict3 = {key: value for key, value in tech_dict.items()}
print("Copied Dictionary (dict comprehension):", copied_dict3)

# Method 4: Deep Copy (for nested dictionaries)
import copy

nested_dict = {
    "language": "Python",
    "details": {
        "creator": "Guido van Rossum",
        "year": 1991
    }
}

deep_copied_dict = copy.deepcopy(nested_dict)
print("Deep Copied Dictionary:", deep_copied_dict)

# Verifying deep copy (modifying original doesn't affect deep copy)
nested_dict["details"]["year"] = 2000
print("Modified Original Dictionary:", nested_dict)
print("Deep Copied Dictionary After Modification:", deep_copied_dict)

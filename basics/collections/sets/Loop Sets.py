# Define a set
thisSet = {"Python", "Java", "JavaScript", "C++", "Swift", "Ruby", "Go"}

# Loop through a set using a for loop
print("Looping through set items:")
for lang in thisSet:
    print(lang)

# Loop and check for a specific item
print("\nChecking if 'Python' is in the set:")
for lang in thisSet:
    if lang == "Python":
        print("Yes, 'Python' is in the set")

# Loop through a set and modify it (must first convert to a list)
print("\nAdding 'TypeScript' while looping:")
for lang in list(thisSet):  # Convert to a list to avoid runtime errors
    if lang == "JavaScript":
        thisSet.add("TypeScript")  # Adding new item
print(thisSet)

# Loop through a set using comprehension
uppercase_set = {lang.upper() for lang in thisSet}
print("\nSet with uppercase values:")
print(uppercase_set)
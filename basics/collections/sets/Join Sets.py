# Define two sets
set1 = {"Python", "Java", "JavaScript"}
set2 = {"C++", "Swift", "Ruby", "Go"}

# Using union() (creates a new set with all unique items)
joined_set = set1.union(set2)
print("Union:", joined_set)

# Using update() (adds items from one set to another)
set1.update(set2)
print("Updated set1:", set1)

# Using intersection() (returns only common items)
set3 = {"Python", "Java", "C"}
common_set = set1.intersection(set3)
print("Intersection:", common_set)

# Using intersection_update() (keeps only common items in the original set)
set1.intersection_update(set3)
print("After intersection_update:", set1)

# Using difference() (returns items only in the first set)
setA = {"Python", "Java", "C++"}
setB = {"Java", "Swift"}
diff_set = setA.difference(setB)
print("Difference:", diff_set)

# Using difference_update() (removes common items from the first set)
setA.difference_update(setB)
print("After difference_update:", setA)

# Using symmetric_difference() (returns items not in both sets)
sym_diff_set = setA.symmetric_difference(setB)
print("Symmetric Difference:", sym_diff_set)

# Using symmetric_difference_update() (modifies the original set)
setA.symmetric_difference_update(setB)
print("After symmetric_difference_update:", setA)
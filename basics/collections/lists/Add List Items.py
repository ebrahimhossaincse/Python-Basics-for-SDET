thislist = ["Python", "Java", "JavaScript", "C++", "Swift", "Ruby", "Go"]

# Append Items: To add an item to the end of the list, use the append() method
thislist.append("C")
print(thislist)

# Insert Items: To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist.insert(2, "React")
print(thislist)

# Extend List: To append elements from another list to the current list, use the extend() method.
newlist = ["PHP", "Kotlin"]
thislist.extend(newlist)
print(thislist)
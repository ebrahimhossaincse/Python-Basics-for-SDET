thislist = ["Python", "Java", "JavaScript", "C++", "Swift", "Ruby", "Go"]

# Join Two Lists
list1 = ["Python", "Java", "JavaScript"]
list2 = ["C++", "Swift", "Ruby", "Go"]
list3 = list1 + list2
print(list3)

# Append list2 into list1
for x in list2:
  list1.append(x)
print(list1)
thislist = ["Python", "Java", "JavaScript", "C++", "Swift", "Ruby", "Go"]

# Remove Specified Item: The remove() method removes the specified item.
thislist.remove("Go")
print(thislist)

#Remove Specified Index: The pop() method removes the specified index.
thislist.pop(1)
print(thislist)

# Remove the last item:
thislist.pop()
print(thislist)

# Delete Specified Index: The del keyword removes the specified index.
del thislist[0]
print(thislist)

# Clear the list
thislist.clear()
print(thislist)
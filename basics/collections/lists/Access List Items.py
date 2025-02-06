thislist = ["Python", "Java", "JavaScript", "C++", "Swift", "Ruby", "Go"]

# Access List Items
print(thislist[1])  # Output: Java

# Negative Indexing
print(thislist[-1])  # Output: Go

# Range of Indexes
print(thislist[2:5])  # Output: ['JavaScript', 'C++', 'Swift']

# Check if Item Exists
if "Python" in thislist:
  print("Yes, 'Python' is in the programming languages list")
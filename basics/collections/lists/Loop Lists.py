thislist = ["Python", "Java", "JavaScript", "C++", "Swift", "Ruby", "Go"]

# Loop Through a List
for x in thislist:
  print(x)

# Loop Through the Index Numbers: Use the range() and len() functions to create a suitable iterable.
for i in range(len(thislist)):
  print(f'Index{i}: {thislist[i]}')

# Using a While Loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension
[print(x) for x in thislist]
print('The break Statement: Exit the loop when x is "banana", but this time the break comes before the print')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

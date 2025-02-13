# Reading the entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('sample.txt', 'r') as file:
    for line in file:
        print(line.strip())
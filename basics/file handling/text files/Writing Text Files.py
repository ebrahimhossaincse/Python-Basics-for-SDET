# Writing to a file (overwrites existing content)

text_example = "RN Entrance Exam Before you can get admitted to an accredited nursing school, you will be required to pass one of the RN Entrance Exams (TEAS, HESI, PAX, KAPLAN). Let’s see what type of support you may need…"

with open('example.txt', 'w') as file:
    file.write(text_example)

text_sample = "Each nursing college sets their own requirements on how many times you can take an RN Entrance Exam, with additional restrictions on how long you have to wait in between each attempt. How would you like to avoid delays and pass on the first attempt?"
# Appending to a file
with open('sample.txt', 'a') as file:
    file.write(text_sample)

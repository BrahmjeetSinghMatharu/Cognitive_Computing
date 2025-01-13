# 7.1 Write a program to create a text file, write some text into it, and then read and print the content.

file_name = "python1.txt"

with open(file_name, "w") as file:
    file.write("My name is Brahmjeet Singh.\n")
    file.write("I am currently learning Python.\n")

with open(file_name, "r") as file:
    text = file.read()

print("Content of the file :- ")
print(text)


# 7.2 Write a program to append text to an existing file and print the updated content.

with open(file_name, "a") as file:
    file.write("I currently in 2nd year.\n")

with open(file_name, "r") as file:
    text = file.read()

print("Updated content of the file :- ")
print(text)

# 7.3 Write a program to count the number of lines in a text file.

with open(file_name, "r") as file:
    line_count = sum(1 for line in file)

print(f"The file '{file_name}' contains {line_count} lines.")
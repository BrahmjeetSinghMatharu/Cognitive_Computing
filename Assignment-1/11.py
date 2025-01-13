# 11.1 Write a program to use the math library to calculate the square root of a given number.

import math
number = float(input("Enter a number : "))
root = math.sqrt(number)

print(f"The square root of {number} is : {root}")

# 11.2 Write a program to use the datetime library to print the current date and time.

import datetime
dateTime = datetime.datetime.now()
print("Date and time : ", dateTime)

# 11.3 Write a program to use the os library to list all files in the current directory.

import os
files = os.listdir()

print("Files in the current directory:")
for file1 in files:
    if os.path.isfile(file1):
        print(file1)
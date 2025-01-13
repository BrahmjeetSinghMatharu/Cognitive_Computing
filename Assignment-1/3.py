# 3.1 Write a Python program to check if a number is positive, negative, or zero using an if-else statement.

no = int(input("Enter a no : "))

if (no>0):
    print("Positive Number")
elif (no==0):
    print("Zero")
else:
    print("Enter a valid number")
    

# 3.2 Write a program to check if a given number is odd or even.

number = int(input("Enter a number : "))

if (number%2 == 1):
    print("Odd number")
else:
    print("Even number")
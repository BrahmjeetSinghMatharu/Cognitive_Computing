# 8.1 Write a program to handle division by zero using a try-except block.

try:
    num = int(input("Enter the numerator: "))
    deno = int(input("Enter the denominator: "))
    result = num / deno
    print(f"The result is : {result}")
    
except ZeroDivisionError:
    print("Division by zero is not allowed.")
    
except ValueError:
    print("Please enter valid numbers.")


    
# 8.2 Write a program to handle invalid input (e.g., when the user enters a string instead of a number).
    
try:
    number = int(input("Enter a number: "))
    print(f"You entered the number: {number}")
except ValueError:
    print("Invalid input. Enter a valid integer.")
    

# 8.3 Write a program to demonstrate the use of finally in exception handling.
    

try:
    num1 = int(input("Enter the numerator: "))
    deno1 = int(input("Enter the denominator: "))
    
    result = num1 / deno1
    print(f"The result is : {result}")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter valid numbers.")
finally:
    print("Execution completed.")
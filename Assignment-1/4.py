# 4.1 Write a program to print numbers from 1 to 10 using a for loop.
num = 11

for i in range(1,num):
    print(i)
    
# 4.2 Write a program to print numbers from 1 to 10 using a while loop.

i = 1

while i<=10:
    print(i)
    i = i+1
    
# 4.3 Write a program to calculate the sum of numbers from 1 to 100 using a loop.

sum = 0

for i in range(1,101):
    sum = sum + i

print(f"Sum of numbers from 1 to 100 is : {sum}")
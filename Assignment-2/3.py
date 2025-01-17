# 3. WAP to create a list of 100 random numbers between 100 and 900. Count and print the :
import random
list = []

for i in range(100):
    list.append(random.randint(100,900))
    
print(list)

# i. All odd numbers

print("Printing Odd Numbers :- ")

for i in list:
    if((i%2) != 0):
        print(i, end = " ")
        
# ii. All even numbers

print("\nPrinting Even Numbers :- ")
for i in list:
  if((i%2) == 0):
    print(i,end = " ")
    
# iii. All prime numbers
    
print("\nPrinting Prime Numbers :- ")
for i in list:
  flag = True
  for j in range(2,i):
    if(i%j==0):
        flag=False
        break
  if(flag):
    print(i,end = " ")
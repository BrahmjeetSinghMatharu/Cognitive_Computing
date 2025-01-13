# 9.1 Write a program to generate 5 random numbers between 1 and 100 and print them.

import random

for i in range(5):
    no = random.randint(1, 100)
    print(no)
    
# 9.2 Write a program to generate a random number and check if it is prime.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

rand = random.randint(1, 100)

if is_prime(rand):
    print(f"The number is prime.")
else:
    print(f"The number is not prime.")
    
# 9.3 Write a program to simulate rolling a six-sided die.

die = random.randint(1, 6)
print(f"The number on the die is : {die}")

# 9.4 Write a program to shuffle a list of numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)

print(f"Shuffled list : {numbers}")

# 9.5 Write a program to randomly select an item from a list.

items = ["a1", "b2", "c3", "d4", "e5"]
sitem = random.choice(items)

print(f"The randomly selected item is : {sitem}")

# 9.6 Write a program to generate a random password of given length.

password = ''
passw = int(input("Enter length of password : "))

for i in range(passw):
  password = password + str(random.randint(0,9))

print(password)

# 9.7 Write a program to pick a random card from a standard deck of 52 cards.

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
rand = random.choice(deck)

print(f"The randomly selected card is: {rand}")
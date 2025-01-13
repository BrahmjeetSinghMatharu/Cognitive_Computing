# 6.1 Write a program to count the number of vowels in a given string.

str = input("Enter a string : ")
vowel_count = 0

for i in str:
    if i in "aeiouAEIOU":
        vowel_count = vowel_count+1

print(vowel_count)

# 6.2 Write a program to reverse a string and print it.

str1 = input("Enter a string : ")
rstr2 = ''

for i in str1:
  rstr2 = i+rstr2

print(rstr2)

# 6.3 Write a program to check if a string is a palindrome.

str3 = input("Enter a string : ")
rstr4 = ''

for i in str3:
  rstr4 = i+rstr4

print(rstr4)

if (str3 == rstr4):
    print("Palindrome")
else:
    print("Not a Palindrome")
# 5.1 Create a list of 5 numbers. Write a program to find the largest and smallest numbers in the list.

list = [2,4,6,8,10]

print(list)

maxi = max(list)
mini = min(list)

print(f"Largest : {maxi}")
print(f"Smallest : {mini}")

print('\n')

# 5.2 Create a dictionary with at least 3 key-value pairs. Write a program to retrieve the value of a given key.

dictionary = {
    "Name":"Brahmjeet Singh",
    "Age":19,
    "Hostel":"B"
}

print(dictionary)
print(dictionary["Age"])

print('\n')

# 5.3 Write a program to sort a list of numbers in ascending and descending order.

list01 = [-3,9,-10,3,6,19]
print(list01)

list01.sort(reverse=False)
print(f"Ascending Order : {list01}")

list01.sort(reverse=True)
print(f"Descending Order: {list01}")

print('\n')

#  5.4 Write a program to merge two dictionaries into one.

dict1={
    "a":1,
    "b":2
}
print(dict1)

dict2={
    "c":3,
    "d":4
}
print(dict2)

dict1.update(dict2)
print(dict1)
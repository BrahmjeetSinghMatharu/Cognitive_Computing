# 2. Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and perform the following operations using tuple functions:

scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

# i. Identify the highest score and its index in the tuple.

print(f"Highest Score : {max(scores)}")
print(f"Index of Highest Score : {scores.index(max(scores))}")

# ii. Find the lowest score and count how many times it appears.

print(f"Lowest Score : {min(scores)}")

cnt = 0

for i in scores:
  if(i == min(scores)):
    cnt = cnt + 1
    
print(f"Occurence of Minimum Score is : {cnt}")

# iii. Reverse the tuple and return it as a list.

L = list(reversed(scores))
print(f"Reverse : {L}")

# iv. Check if a specific score ‘76’ (input by the user) is present in the tuple and print its first occurrence index, or a message saying it’s not present.

score = int(input("Enter a score : "))

if score in scores:
    print(f"{score} is at present at index {scores.index(score)}")
else:
    print(f"{score} is not present")
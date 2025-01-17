# 4. Consider the following two sets, A and B, representing scores of two teams in multiple matches. A = {34, 56, 78, 90} and B = {78, 45, 90, 23} WAP to perform the following operations using set functions:

A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# i. Find the unique scores achieved by both teams (union of sets).

unique_scores = A | B
print("Unique scores:", unique_scores)

# ii. Identify the scores that are common to both teams (intersection of sets).

common_scores = A & B
print("Common scores:", common_scores)

# iii. Find the scores that are exclusive to each team (symmetric diﬀerence).

exclusive = A ^ B
print("Exclusive scores:", exclusive)

# iv. Check if the scores of team A are a subset of team B, and if team B's scores are a superset of team A.

subset = A.issubset(B)
print("Is A a subset of B ? : ", subset)

superset = B.issuperset(A)
print("Is B a superset of A ? : ", superset)

#  v. Remove a specific score 𝑋 (input by the user) from set A if it exists. If not, print a message saying it is not present.

X = int(input("Enter the score to remove from set A : "))

if X in A:
    A.remove(X)
    print(f"Set after removal: {A}")
else:
    print(f"Score {X} is not present in set A.")
     
# Find common elements
list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6]
list_3 = [4, 5, 7, 8]

s1, s2, s3 = set(list_1), set(list_2), set(list_3)
print("Common in all:", s1 & s2 & s3)
print("Common in first two:", s1 & s2)

at_least_two = (s1 & s2) | (s2 & s3) | (s1 & s3)
print("Present in at least two lists:", at_least_two)

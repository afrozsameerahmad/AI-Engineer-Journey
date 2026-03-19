# Tuple methods and common operations
numbers = (1, 2, 2, 3, 4, 2, 5)
print("Tuple:", numbers)
print("count(2):", numbers.count(2))
print("index(4):", numbers.index(4))

tuple_a = (1, 2)
tuple_b = (3, 4)
print("Concatenate:", tuple_a + tuple_b)
print("Repeat:", tuple_a * 3)

scores = (85, 90, 78, 92)
print("min/max/sum:", min(scores), max(scores), sum(scores))

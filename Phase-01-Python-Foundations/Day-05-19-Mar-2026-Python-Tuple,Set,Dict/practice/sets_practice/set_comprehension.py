# Set comprehension examples
squares = {x * x for x in range(1, 6)}
print("Squares:", squares)

even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print("Even numbers:", even_numbers)

word = "programming"
unique_letters = {ch for ch in word}
print("Unique letters:", unique_letters)

common = {x for x in [1, 2, 3, 4] if x in [3, 4, 5, 6]}
print("Common values:", common)

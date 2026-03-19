# Remove duplicates using sets
numbers = [1, 2, 2, 3, 4, 4, 5]
print("Original:", numbers)
print("Unique as set:", set(numbers))

# Preserve original order while removing duplicates
ordered_unique = list(dict.fromkeys(numbers))
print("Unique with order:", ordered_unique)

words = ["apple", "banana", "apple", "cherry"]
print("Unique words:", set(words))

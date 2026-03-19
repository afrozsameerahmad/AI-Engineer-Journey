# Iterate keys, values, and items
person = {"name": "Samee", "age": 21, "city": "Delhi"}

print("Keys:")
for key in person:
    print(key)

print("\nValues:")
for value in person.values():
    print(value)

print("\nItems:")
for key, value in person.items():
    print(f"{key}: {value}")

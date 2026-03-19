# Dictionary comprehension examples
squares = {x: x * x for x in range(1, 6)}
print("Squares:", squares)

even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print("Even squares:", even_squares)

keys = ["name", "age", "city"]
values = ["Samee", 21, "Delhi"]
profile = {k: v for k, v in zip(keys, values)}
print("Profile:", profile)

inverted = {v: k for k, v in {"a": 1, "b": 2}.items()}
print("Inverted:", inverted)

# Merge dictionaries in simple ways
defaults = {"theme": "light", "language": "en", "timeout": 30}
user_settings = {"theme": "dark", "timeout": 60}

merged = {**defaults, **user_settings}
print("Merged with unpacking:", merged)

base = {"a": 1, "b": 2}
extra = {"b": 20, "c": 3}
base.update(extra)
print("Merged with update:", base)

many = [{"x": 1}, {"y": 2}, {"x": 9, "z": 3}]
combined = {}
for item in many:
    combined.update(item)
print("Merged list of dicts:", combined)

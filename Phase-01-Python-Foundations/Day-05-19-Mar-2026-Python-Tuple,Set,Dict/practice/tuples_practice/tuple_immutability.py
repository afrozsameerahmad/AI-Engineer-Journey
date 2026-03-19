# Tuples are immutable
colors = ("red", "green", "blue")
print("Original tuple:", colors)

try:
    colors[0] = "black"
except TypeError as err:
    print("Error:", err)

# Mutable object inside tuple can still change
mixed = ("python", [1, 2, 3])
mixed[1].append(4)
print("Tuple with list after append:", mixed)

# Tuple can be dictionary key
locations = {
    (28.61, 77.20): "Delhi",
    (19.07, 72.87): "Mumbai",
}
print("City at (28.61, 77.20):", locations[(28.61, 77.20)])

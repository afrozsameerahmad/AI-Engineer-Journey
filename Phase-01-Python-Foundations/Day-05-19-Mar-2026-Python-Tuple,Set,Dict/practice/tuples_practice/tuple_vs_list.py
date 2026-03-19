# Quick tuple vs list comparison
import sys

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print("List size:", sys.getsizeof(my_list))
print("Tuple size:", sys.getsizeof(my_tuple))

my_list[0] = 99
print("List after change:", my_list)

try:
    my_tuple[0] = 99
except TypeError as err:
    print("Tuple change error:", err)

points = {(1, 2): "Point A"}
print("Tuple as dictionary key:", points)

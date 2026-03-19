# Add, update, remove, discard, pop, clear
fruits = {"apple", "banana"}
print("Start:", fruits)

fruits.add("cherry")
fruits.update(["mango", "orange"])
print("After add/update:", fruits)

fruits.remove("banana")
fruits.discard("grape")  # no error if missing
print("After remove/discard:", fruits)

removed = fruits.pop()
print("Popped item:", removed)
print("After pop:", fruits)

fruits.clear()
print("After clear:", fruits)

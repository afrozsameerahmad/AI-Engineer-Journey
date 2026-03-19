# Tuple unpacking examples
point = (10, 20, 30)
x, y, z = point
print("x, y, z:", x, y, z)

data = (1, 2, 3, 4, 5)
first, *middle, last = data
print("first, middle, last:", first, middle, last)

name, age, role = ("Samee", 21, "Learner")
print(f"{name} is {age} and is a {role}")

names = ("A", "B", "C")
marks = (90, 85, 88)
paired = tuple(zip(names, marks))
print("Zipped:", paired)

unzipped_names, unzipped_marks = zip(*paired)
print("Unzipped names:", unzipped_names)
print("Unzipped marks:", unzipped_marks)

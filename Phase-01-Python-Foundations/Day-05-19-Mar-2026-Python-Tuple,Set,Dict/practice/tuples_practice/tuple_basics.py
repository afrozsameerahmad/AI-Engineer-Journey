# Tuple basics: create, access, slice, membership
empty_tuple = ()
single_item = (42,)
student = ("Samee", 21, "Python")

print("Empty:", empty_tuple)
print("Single item:", single_item)
print("Student:", student)

print("First item:", student[0])
print("Last item:", student[-1])

numbers = (0, 1, 2, 3, 4, 5)
print("Slice [1:4]:", numbers[1:4])
print("Every second item:", numbers[::2])

print("'Python' in student?", "Python" in student)

# Dictionary create, access, update, delete
student = {"name": "Samee", "age": 21, "course": "Python"}
print("Start:", student)

print("Name:", student["name"])
print("Phone with get():", student.get("phone", "Not available"))

student["age"] = 22
student["city"] = "Delhi"
student.update({"course": "AI", "active": True})
print("After updates:", student)

removed = student.pop("city")
print("Popped city:", removed)
del student["active"]
print("Final:", student)

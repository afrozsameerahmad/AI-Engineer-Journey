'''Question:
Create a student result program using **kwargs.
Subject names are not fixed, so we pass them dynamically.
'''


def get_grade(avg):
    """Return grade from average marks."""
    if avg >= 90:
        return "A+"
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    return "D"


def print_result(name, **subjects):
    """Print a simple result card using dynamic subject marks."""
    total = sum(subjects.values())
    count = len(subjects)
    average = total / count if count else 0
    grade = get_grade(average)
    status = "Pass" if average >= 40 else "Fail"

    print(f"\nResult card of {name}")
    print("Subject marks:", subjects)
    print("Total        :", total)
    print("Average      :", round(average, 2))
    print("Grade        :", grade)
    print("Status       :", status)


print_result("Sameer", python=92, sql=84, statistics=76, communication=88)
print_result("Kaif", python=55, sql=49, statistics=61, communication=58)

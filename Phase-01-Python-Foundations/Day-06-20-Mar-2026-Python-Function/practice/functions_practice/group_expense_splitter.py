'''Question:
Friends went out and spent money on multiple items.
Use *args and default arguments to find final bill and split amount per person.
'''


def split_expense(*expenses, people=1, tax_percent=5):
    """Return final total and per person share."""
    if people <= 0:
        return 0, 0

    subtotal = sum(expenses)
    tax = subtotal * tax_percent / 100
    final_total = subtotal + tax
    per_person = final_total / people
    return round(final_total, 2), round(per_person, 2)


def show_split_report(title, *expenses, people=1, tax_percent=5):
    total, per_person = split_expense(*expenses, people=people, tax_percent=tax_percent)
    print(f"\n{title}")
    print("Expenses list :", expenses)
    print("People count  :", people)
    print("Final total   :", total)
    print("Per person    :", per_person)


show_split_report("Trip Expense", 450, 820, 230, 1200, 600, people=4, tax_percent=5)
show_split_report("Office Lunch", 320, 540, 260, people=3)

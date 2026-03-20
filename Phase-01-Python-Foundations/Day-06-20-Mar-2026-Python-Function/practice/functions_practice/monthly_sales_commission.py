'''Question:
A sales employee has monthly sales values.
Use functions and *args to calculate total sales and commission.

Rule:
1) Base commission = 5%
2) If total >= target, extra 2% bonus commission
'''


def calculate_total_sales(*sales):
    """Return total sales using *args."""
    return sum(sales)


def calculate_commission(total, target=50000):
    """Return commission amount based on target rule."""
    commission = total * 0.05
    if total >= target:
        commission += total * 0.02
    return commission


def show_sales_report(name, *sales, target=50000):
    total = calculate_total_sales(*sales)
    commission = calculate_commission(total, target)

    print(f"\nEmployee name : {name}")
    print("Monthly sales :", sales)
    print("Total sales   :", total)
    print("Target        :", target)
    print("Commission    :", round(commission, 2))


show_sales_report("Ravi", 12000, 15000, 9800, 13000, 14500, target=60000)
show_sales_report("Anita", 7000, 8500, 9000, 7600, 8100)

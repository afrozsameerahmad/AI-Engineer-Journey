'''Question:
Given a mixed list of values, separate valid integers into even and odd.
Put all non-integer values in invalid and print a report.
'''


def is_even(num):
    """Return True if even, False if odd, and None if input is not int."""
    if type(num) is int:
        return num % 2 == 0
    return None


def analyze_numbers(values):
    even_numbers = []
    odd_numbers = []
    invalid_values = []

    for value in values:
        check = is_even(value)
        if check is True:
            even_numbers.append(value)
        elif check is False:
            odd_numbers.append(value)
        else:
            invalid_values.append(value)

    return even_numbers, odd_numbers, invalid_values


def print_report(even_numbers, odd_numbers, invalid_values):
    print("Even numbers   :", even_numbers)
    print("Odd numbers    :", odd_numbers)
    print("Invalid values :", invalid_values)
    print("Total valid    :", len(even_numbers) + len(odd_numbers))


data = [10, 13, 18, -5, 0, "python", 7.2, True, 22]
even_list, odd_list, invalid_list = analyze_numbers(data)
print_report(even_list, odd_list, invalid_list)

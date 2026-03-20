'''Question:
Create a power function and practice default, positional, and keyword arguments.
Then print powers for a list of base-exponent pairs.
'''


def power(a=2, b=2):
    """Return a raised to the power b."""
    return a**b


def print_power_table(pairs):
    """Print power results for (base, exponent) pairs."""
    for base, exponent in pairs:
        result = power(base, exponent)
        print(f"{base}^{exponent} = {result}")


print("Default call          :", power())
print("Positional call       :", power(3, 4))
print("Keyword argument call :", power(b=3, a=5))

print("\nPower table:")
power_pairs = [(2, 5), (3, 3), (4, 2), (7, 2)]
print_power_table(power_pairs)

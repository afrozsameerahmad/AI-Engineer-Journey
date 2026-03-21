def is_perfect(n):
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
perfect_numbers = list(filter(is_perfect, range(1, 10000)))
print(perfect_numbers)
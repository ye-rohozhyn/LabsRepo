def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def print_prime_numbers(a, b):
    for num in range(a, b + 1):
        if is_prime(num):
            print(num)

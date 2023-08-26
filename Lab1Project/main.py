from prime_numbers import *

a = int(input("Task 1\nEnter first number: "))
b = int(input("Enter second number: "))

if a > b:
    a, b = b, a

print_prime_numbers(a, b)
